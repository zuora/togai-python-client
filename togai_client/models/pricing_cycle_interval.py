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


class PricingCycleInterval(str, Enum):
    """
    Interval field allow you to define the billing interval you would like to set
    """

    """
    allowed enum values
    """
    WEEKLY = 'WEEKLY'
    MONTHLY = 'MONTHLY'
    QUARTERLY = 'QUARTERLY'
    HALF_YEARLY = 'HALF_YEARLY'
    ANNUALLY = 'ANNUALLY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PricingCycleInterval from a JSON string"""
        return cls(json.loads(json_str))


