#!/usr/bin/env python3

import kfp.dsl as dsl
from kubernetes import client as k8s_client


def mnist_train_op(data_dir: str, model_dir: str,
                   export_dir: str, train_steps: int, batch_size: int,
                   learning_rate: float, step_name='Training'):
    return dsl.ContainerOp(
        name=step_name,
        image='mnist_hjc:1.9',
        arguments=[
            '/opt/model.py',
            '--tf-data-dir', data_dir,
            '--tf-model-dir', model_dir,
            '--tf-export-dir', export_dir,
            '--tf-train-steps', train_steps,
            '--tf-batch-size', batch_size,
            '--tf-learning-rate', learning_rate,
        ],
        file_outputs={
            'export': '/export.txt',
            'model': '/model.txt',
        }
    )


def kubeflow_tensorboard(model_dir: str, step_name='Tensorboard'):
    return dsl.ContainerOp(
        name=step_name,
        image='tensorflow/tensorflow:1.7.0',
        arguments=[
            '/usr/local/bin/tensorboard',
            '--logdir=%s' % model_dir,
        ]
    )


def kubeflow_deploy_op(model: 'TensorFlow model', tf_model_name, tf_model_port: int, step_name='Deploy_serving'):
    return dsl.ContainerOp(
        name=step_name,
        image='tensorflow/serving:1.11.1',
        arguments=[
            '--model_base_path=%s' % model,
            '--model_name=%s' % tf_model_name,
            '--port=%s' % tf_model_port,
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
        tf_export_dir='model/export',
        batch_size=100,
        training_steps=200,
        learning_rate=0.01,
        tf_model_port=9000):
    mnist_training = mnist_train_op('/mnt/%s' % tf_data_dir, '/mnt/%s' % tf_model_dir, '/mnt/%s' % tf_export_dir,
                                    training_steps, batch_size, learning_rate).add_volume(
        k8s_client.V1Volume(name='mnist-nfs', persistent_volume_claim=k8s_client.V1PersistentVolumeClaimVolumeSource(
            claim_name='mnist-pvc'))).add_volume_mount(k8s_client.V1VolumeMount(mount_path='/mnt', name='mnist-nfs'))
    tensorboard = kubeflow_tensorboard(mnist_training.outputs['model'])
    deploy_serving = kubeflow_deploy_op(mnist_training.outputs['export'], model, tf_model_port).add_volume_mount(
        k8s_client.V1VolumeMount(mount_path='/mnt', name='mnist-nfs'))


if __name__ == '__main__':
    import kfp.compiler as compiler

    compiler.Compiler().compile(mnist_pipeline, __file__ + '.tar.gz')
