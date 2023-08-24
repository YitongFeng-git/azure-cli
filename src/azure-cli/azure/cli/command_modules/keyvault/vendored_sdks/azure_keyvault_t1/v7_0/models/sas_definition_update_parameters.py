# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: skip-file
# flake8: noqa
from msrest.serialization import Model


class SasDefinitionUpdateParameters(Model):
    """The SAS definition update parameters.

    :param template_uri: The SAS definition token template signed with an
     arbitrary key.  Tokens created according to the SAS definition will have
     the same properties as the template.
    :type template_uri: str
    :param sas_type: The type of SAS token the SAS definition will create.
     Possible values include: 'account', 'service'
    :type sas_type: str or ~azure.keyvault.v7_0.models.SasTokenType
    :param validity_period: The validity period of SAS tokens created
     according to the SAS definition.
    :type validity_period: str
    :param sas_definition_attributes: The attributes of the SAS definition.
    :type sas_definition_attributes:
     ~azure.keyvault.v7_0.models.SasDefinitionAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'template_uri': {'key': 'templateUri', 'type': 'str'},
        'sas_type': {'key': 'sasType', 'type': 'str'},
        'validity_period': {'key': 'validityPeriod', 'type': 'str'},
        'sas_definition_attributes': {'key': 'attributes', 'type': 'SasDefinitionAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(SasDefinitionUpdateParameters, self).__init__(**kwargs)
        self.template_uri = kwargs.get('template_uri', None)
        self.sas_type = kwargs.get('sas_type', None)
        self.validity_period = kwargs.get('validity_period', None)
        self.sas_definition_attributes = kwargs.get('sas_definition_attributes', None)
        self.tags = kwargs.get('tags', None)
