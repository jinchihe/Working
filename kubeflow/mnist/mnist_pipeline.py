#!/usr/bin/env python3

import kfp.dsl as dsl
from kubernetes import client as k8s_client


def mnist_train_op(data_dir: str, model_dir: str,
                   export_dir: str, train_steps: int, batch_size: int,
                   learning_rate: float, step_name='Training'):
    return dsl.ContainerOp(
        name=step_name,
        image='mnist_hjc:1.8',
        arguments=[
            '/opt/model.py',
            '--tf-data-dir', data_dir,
            '--tf-model-dir', model_dir,
            '--tf-export-dir', export_dir,
            '--tf-train-steps', train_steps,
            '--tf-batch-size', batch_size,
            '--tf-learning-rate', learning_rate,
        ],
        file_outputs={'train': '/output.txt'}
    )


def kubeflow_deploy_op(model: 'TensorFlow model', tf_server_name, pvc_name, step_name='deploy_serving'):
    return dsl.ContainerOp(
        name=step_name,
        image='pipeline-deployment-test1:last',
        arguments=[
            '--cluster-name', 'mnist-pipeline',
            '--model-path', model,
            '--namespace', 'mnist'
            '--server-name', tf_server_name,
            '--pvc-name', pvc_name,
        ]
    )


@dsl.pipeline(
    name='Mnist Pipelines',
    description='Mnist Pipelines'
)
def mnist_pipeline(
        pvc_name='mnist-pvc',
        model='mnist',
        tf_data_dir='data',
        tf_model_dir='model',
        tf_export_dir='model/export/export',
        batch_size=100,
        training_steps=200,
        learning_rate=0.01):
    mnist_training = mnist_train_op('/mnt/%s' % tf_data_dir, '/mnt/%s' % tf_model_dir, '/mnt/%s' % tf_export_dir,
                              training_steps, batch_size, learning_rate).add_volume(
        k8s_client.V1Volume(name='mnist-nfs', persistent_volume_claim=k8s_client.V1PersistentVolumeClaimVolumeSource(
            claim_name='mnist-pvc'))).add_volume_mount(k8s_client.V1VolumeMount(mount_path='/mnt', name='mnist-nfs'))
    deploy_serving = kubeflow_deploy_op(mnist_training.output, model, pvc_name).add_volume_mount(
        k8s_client.V1VolumeMount(mount_path='/mnt', name='mnist-nfs'))


if __name__ == '__main__':
    import kfp.compiler as compiler
    compiler.Compiler().compile(mnist_pipeline, __file__ + '.tar.gz')
