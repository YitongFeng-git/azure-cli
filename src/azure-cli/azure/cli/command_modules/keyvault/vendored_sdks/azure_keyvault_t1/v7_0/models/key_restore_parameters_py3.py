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


class KeyRestoreParameters(Model):
    """The key restore parameters.

    All required parameters must be populated in order to send to Azure.

    :param key_bundle_backup: Required. The backup blob associated with a key
     bundle.
    :type key_bundle_backup: bytes
    """

    _validation = {
        'key_bundle_backup': {'required': True},
    }

    _attribute_map = {
        'key_bundle_backup': {'key': 'value', 'type': 'base64'},
    }

    def __init__(self, *, key_bundle_backup: bytes, **kwargs) -> None:
        super(KeyRestoreParameters, self).__init__(**kwargs)
        self.key_bundle_backup = key_bundle_backup
