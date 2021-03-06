# coding: utf-8

"""
    KFServing

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IoK8sApimachineryPkgApisMetaV1ListOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'api_version': 'str',
        '_continue': 'str',
        'field_selector': 'str',
        'include_uninitialized': 'bool',
        'kind': 'str',
        'label_selector': 'str',
        'limit': 'int',
        'resource_version': 'str',
        'timeout_seconds': 'int',
        'watch': 'bool'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        '_continue': 'continue',
        'field_selector': 'fieldSelector',
        'include_uninitialized': 'includeUninitialized',
        'kind': 'kind',
        'label_selector': 'labelSelector',
        'limit': 'limit',
        'resource_version': 'resourceVersion',
        'timeout_seconds': 'timeoutSeconds',
        'watch': 'watch'
    }

    def __init__(self, api_version=None, _continue=None, field_selector=None, include_uninitialized=None, kind=None, label_selector=None, limit=None, resource_version=None, timeout_seconds=None, watch=None):  # noqa: E501
        """IoK8sApimachineryPkgApisMetaV1ListOptions - a model defined in Swagger"""  # noqa: E501

        self._api_version = None
        self.__continue = None
        self._field_selector = None
        self._include_uninitialized = None
        self._kind = None
        self._label_selector = None
        self._limit = None
        self._resource_version = None
        self._timeout_seconds = None
        self._watch = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if _continue is not None:
            self._continue = _continue
        if field_selector is not None:
            self.field_selector = field_selector
        if include_uninitialized is not None:
            self.include_uninitialized = include_uninitialized
        if kind is not None:
            self.kind = kind
        if label_selector is not None:
            self.label_selector = label_selector
        if limit is not None:
            self.limit = limit
        if resource_version is not None:
            self.resource_version = resource_version
        if timeout_seconds is not None:
            self.timeout_seconds = timeout_seconds
        if watch is not None:
            self.watch = watch

    @property
    def api_version(self):
        """Gets the api_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def _continue(self):
        """Gets the _continue of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.  # noqa: E501

        :return: The _continue of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        """Sets the _continue of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the \"next key\".  This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.  # noqa: E501

        :param _continue: The _continue of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: str
        """

        self.__continue = _continue

    @property
    def field_selector(self):
        """Gets the field_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        A selector to restrict the list of returned objects by their fields. Defaults to everything.  # noqa: E501

        :return: The field_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._field_selector

    @field_selector.setter
    def field_selector(self, field_selector):
        """Sets the field_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        A selector to restrict the list of returned objects by their fields. Defaults to everything.  # noqa: E501

        :param field_selector: The field_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: str
        """

        self._field_selector = field_selector

    @property
    def include_uninitialized(self):
        """Gets the include_uninitialized of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        If true, partially initialized resources are included in the response.  # noqa: E501

        :return: The include_uninitialized of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: bool
        """
        return self._include_uninitialized

    @include_uninitialized.setter
    def include_uninitialized(self, include_uninitialized):
        """Sets the include_uninitialized of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        If true, partially initialized resources are included in the response.  # noqa: E501

        :param include_uninitialized: The include_uninitialized of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: bool
        """

        self._include_uninitialized = include_uninitialized

    @property
    def kind(self):
        """Gets the kind of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def label_selector(self):
        """Gets the label_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        A selector to restrict the list of returned objects by their labels. Defaults to everything.  # noqa: E501

        :return: The label_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._label_selector

    @label_selector.setter
    def label_selector(self, label_selector):
        """Sets the label_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        A selector to restrict the list of returned objects by their labels. Defaults to everything.  # noqa: E501

        :param label_selector: The label_selector of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: str
        """

        self._label_selector = label_selector

    @property
    def limit(self):
        """Gets the limit of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.  # noqa: E501

        :return: The limit of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        limit is a maximum number of responses to return for a list call. If more items exist, the server will set the `continue` field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.  The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.  # noqa: E501

        :param limit: The limit of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def resource_version(self):
        """Gets the resource_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.  # noqa: E501

        :return: The resource_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: str
        """
        return self._resource_version

    @resource_version.setter
    def resource_version(self, resource_version):
        """Sets the resource_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv.  # noqa: E501

        :param resource_version: The resource_version of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: str
        """

        self._resource_version = resource_version

    @property
    def timeout_seconds(self):
        """Gets the timeout_seconds of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.  # noqa: E501

        :return: The timeout_seconds of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: int
        """
        return self._timeout_seconds

    @timeout_seconds.setter
    def timeout_seconds(self, timeout_seconds):
        """Sets the timeout_seconds of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.  # noqa: E501

        :param timeout_seconds: The timeout_seconds of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: int
        """

        self._timeout_seconds = timeout_seconds

    @property
    def watch(self):
        """Gets the watch of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501

        Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.  # noqa: E501

        :return: The watch of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :rtype: bool
        """
        return self._watch

    @watch.setter
    def watch(self, watch):
        """Sets the watch of this IoK8sApimachineryPkgApisMetaV1ListOptions.

        Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.  # noqa: E501

        :param watch: The watch of this IoK8sApimachineryPkgApisMetaV1ListOptions.  # noqa: E501
        :type: bool
        """

        self._watch = watch

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IoK8sApimachineryPkgApisMetaV1ListOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IoK8sApimachineryPkgApisMetaV1ListOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
