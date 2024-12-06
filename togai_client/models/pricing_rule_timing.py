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


class PricingRuleTiming(str, Enum):
    """
    If IN_ADVANCE, the rule will be applied on rate cards with invoice timing IN_ADVANCE . If IN_ARREARS, the rule will be applied on rate cards with invoice timing IN_ARREARS . 
    """

    """
    allowed enum values
    """
    IN_ADVANCE = 'IN_ADVANCE'
    IN_ARREARS = 'IN_ARREARS'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PricingRuleTiming from a JSON string"""
        return cls(json.loads(json_str))


