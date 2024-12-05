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


class PriceType(str, Enum):
    """
    PriceType
    """

    """
    allowed enum values
    """
    FLAT = 'FLAT'
    PER_UNIT = 'PER_UNIT'
    PACKAGE = 'PACKAGE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PriceType from a JSON string"""
        return cls(json.loads(json_str))

