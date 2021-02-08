# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class AccountingAppSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "app_id": "int",
        "urls": "AccountingAppUrls",
        "features": "AccountingFeatures",
    }

    attribute_map = {"app_id": "appId", "urls": "urls", "features": "features"}

    def __init__(
        self, app_id=None, urls=None, features=None, local_vars_configuration=None
    ):  # noqa: E501
        """AccountingAppSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._app_id = None
        self._urls = None
        self._features = None
        self.discriminator = None

        self.app_id = app_id
        self.urls = urls
        if features is not None:
            self.features = features

    @property
    def app_id(self):
        """Gets the app_id of this AccountingAppSettings.  # noqa: E501

        The ID of the accounting app. This is the identifier of the application created in your HubSpot developer portal.  # noqa: E501

        :return: The app_id of this AccountingAppSettings.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AccountingAppSettings.

        The ID of the accounting app. This is the identifier of the application created in your HubSpot developer portal.  # noqa: E501

        :param app_id: The app_id of this AccountingAppSettings.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and app_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `app_id`, must not be `None`"
            )  # noqa: E501

        self._app_id = app_id

    @property
    def urls(self):
        """Gets the urls of this AccountingAppSettings.  # noqa: E501


        :return: The urls of this AccountingAppSettings.  # noqa: E501
        :rtype: AccountingAppUrls
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this AccountingAppSettings.


        :param urls: The urls of this AccountingAppSettings.  # noqa: E501
        :type: AccountingAppUrls
        """
        if (
            self.local_vars_configuration.client_side_validation and urls is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `urls`, must not be `None`"
            )  # noqa: E501

        self._urls = urls

    @property
    def features(self):
        """Gets the features of this AccountingAppSettings.  # noqa: E501


        :return: The features of this AccountingAppSettings.  # noqa: E501
        :rtype: AccountingFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this AccountingAppSettings.


        :param features: The features of this AccountingAppSettings.  # noqa: E501
        :type: AccountingFeatures
        """

        self._features = features

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountingAppSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountingAppSettings):
            return True

        return self.to_dict() != other.to_dict()