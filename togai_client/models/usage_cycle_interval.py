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


class UsageCycleInterval(str, Enum):
    """
    UsageCycleInterval field allows you to treat the billing interval as many smaller windows. Revenue is calculated for each of the windows (usage cycles) and their sum is considered as the billing interval revenue. Example: 1 Named License being used across entire billing interval. Rate Value: $1/license CASE 1: Without usage cycle. $1 is charged for the entire billing cycle. CASE 2: Usage cycle is configure to be WEEKLY and the billing interval has 4 weeks. In this case $1 is charged  for each week totalling to $4 across for the billing interval 
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
        """Create an instance of UsageCycleInterval from a JSON string"""
        return cls(json.loads(json_str))


