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


class Action(Model):
    """The action that will be executed.

    :param action_type: The type of the action. Possible values include:
     'EmailContacts', 'AutoRenew'
    :type action_type: str or ~azure.keyvault.v7_0.models.ActionType
    """

    _attribute_map = {
        'action_type': {'key': 'action_type', 'type': 'ActionType'},
    }

    def __init__(self, *, action_type=None, **kwargs) -> None:
        super(Action, self).__init__(**kwargs)
        self.action_type = action_type
