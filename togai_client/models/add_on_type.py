# coding: utf-8

"""
    Togai Apis

    APIs for Togai App

    The version of the OpenAPI document: 1.0
    Contact: engg@togai.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AddOnType(str, Enum):
    """
    LICENSE: Addon can be used in license rate cards FIXED_FEE: Addon can be used in fixed fee rate cards CREDIT_GRANT: Addon can be used in credit grant rate cards NAMED_LICENSE: Addon can be used in license rate cards 
    """

    """
    allowed enum values
    """
    LICENSE = 'LICENSE'
    FIXED_FEE = 'FIXED_FEE'
    CREDIT_GRANT = 'CREDIT_GRANT'
    NAMED_LICENSE = 'NAMED_LICENSE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AddOnType from a JSON string"""
        return cls(json.loads(json_str))

