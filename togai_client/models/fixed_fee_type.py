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


class FixedFeeType(str, Enum):
    """
    Fixed fee applies either for a one-time occurrence or for each cycle.
    """

    """
    allowed enum values
    """
    ONE_TIME = 'ONE_TIME'
    RECURRING = 'RECURRING'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FixedFeeType from a JSON string"""
        return cls(json.loads(json_str))

