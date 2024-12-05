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


class MetricName(str, Enum):
    """
    Define the metric you would like to get - allowed options are EVENTS - Aggregation of raw events, USAGE - Default to METER_USAGE. To be deprecated soon, METER_USAGE - Aggregated usage value from Usage meters, NAMED_LICENSE_USAGE - Aggregated usage value from Named Licenses, REVENUE - Aggregated revenue value from Pricing Plans USAGE_FOR_CYCLE - Usage in pricing cycle REVENUE_FOR_CYCLE - Revenue in pricing cycle 
    """

    """
    allowed enum values
    """
    EVENTS = 'EVENTS'
    USAGE = 'USAGE'
    METER_USAGE = 'METER_USAGE'
    NAMED_LICENSE_USAGE = 'NAMED_LICENSE_USAGE'
    REVENUE = 'REVENUE'
    USAGE_FOR_CYCLE = 'USAGE_FOR_CYCLE'
    REVENUE_FOR_CYCLE = 'REVENUE_FOR_CYCLE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MetricName from a JSON string"""
        return cls(json.loads(json_str))

