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


class SasDefinitionBundle(Model):
    """A SAS definition bundle consists of key vault SAS definition details plus
    its attributes.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The SAS definition id.
    :vartype id: str
    :ivar secret_id: Storage account SAS definition secret id.
    :vartype secret_id: str
    :ivar template_uri: The SAS definition token template signed with an
     arbitrary key.  Tokens created according to the SAS definition will have
     the same properties as the template.
    :vartype template_uri: str
    :ivar sas_type: The type of SAS token the SAS definition will create.
     Possible values include: 'account', 'service'
    :vartype sas_type: str or ~azure.keyvault.v7_0.models.SasTokenType
    :ivar validity_period: The validity period of SAS tokens created according
     to the SAS definition.
    :vartype validity_period: str
    :ivar attributes: The SAS definition attributes.
    :vartype attributes: ~azure.keyvault.v7_0.models.SasDefinitionAttributes
    :ivar tags: Application specific metadata in the form of key-value pairs
    :vartype tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'secret_id': {'readonly': True},
        'template_uri': {'readonly': True},
        'sas_type': {'readonly': True},
        'validity_period': {'readonly': True},
        'attributes': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'secret_id': {'key': 'sid', 'type': 'str'},
        'template_uri': {'key': 'templateUri', 'type': 'str'},
        'sas_type': {'key': 'sasType', 'type': 'str'},
        'validity_period': {'key': 'validityPeriod', 'type': 'str'},
        'attributes': {'key': 'attributes', 'type': 'SasDefinitionAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(SasDefinitionBundle, self).__init__(**kwargs)
        self.id = None
        self.secret_id = None
        self.template_uri = None
        self.sas_type = None
        self.validity_period = None
        self.attributes = None
        self.tags = None
