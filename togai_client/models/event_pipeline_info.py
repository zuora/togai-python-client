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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from togai_client.models.event_pipeline_info_account import EventPipelineInfoAccount
from togai_client.models.event_pipeline_info_customer import EventPipelineInfoCustomer
from togai_client.models.event_pipeline_info_enrichments import EventPipelineInfoEnrichments
from togai_client.models.event_pipeline_info_event_schema import EventPipelineInfoEventSchema
from togai_client.models.event_pipeline_info_feature_details import EventPipelineInfoFeatureDetails
from togai_client.models.event_pipeline_info_price_plans import EventPipelineInfoPricePlans
from togai_client.models.event_pipeline_info_revenue_details import EventPipelineInfoRevenueDetails
from togai_client.models.event_pipeline_info_usage_meters import EventPipelineInfoUsageMeters
from typing import Optional, Set
from typing_extensions import Self

class EventPipelineInfo(BaseModel):
    """
    Information related to ingestion of an event
    """ # noqa: E501
    event_schema: Optional[EventPipelineInfoEventSchema] = Field(default=None, alias="eventSchema")
    usage_meters: Optional[List[EventPipelineInfoUsageMeters]] = Field(default=None, alias="usageMeters")
    price_plans: Optional[List[EventPipelineInfoPricePlans]] = Field(default=None, alias="pricePlans")
    account: Optional[EventPipelineInfoAccount] = None
    customer: Optional[EventPipelineInfoCustomer] = None
    feature_details: Optional[EventPipelineInfoFeatureDetails] = Field(default=None, alias="featureDetails")
    enrichments: Optional[EventPipelineInfoEnrichments] = None
    revenue_details: Optional[List[EventPipelineInfoRevenueDetails]] = Field(default=None, alias="revenueDetails")
    status_before_reverting: Optional[StrictStr] = Field(default=None, alias="statusBeforeReverting")
    base_currency: Optional[StrictStr] = Field(default=None, alias="baseCurrency")
    invoice_currency: Optional[StrictStr] = Field(default=None, alias="invoiceCurrency")
    __properties: ClassVar[List[str]] = ["eventSchema", "usageMeters", "pricePlans", "account", "customer", "featureDetails", "enrichments", "revenueDetails", "statusBeforeReverting", "baseCurrency", "invoiceCurrency"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EventPipelineInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of event_schema
        if self.event_schema:
            _dict['eventSchema'] = self.event_schema.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in usage_meters (list)
        _items = []
        if self.usage_meters:
            for _item_usage_meters in self.usage_meters:
                if _item_usage_meters:
                    _items.append(_item_usage_meters.to_dict())
            _dict['usageMeters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in price_plans (list)
        _items = []
        if self.price_plans:
            for _item_price_plans in self.price_plans:
                if _item_price_plans:
                    _items.append(_item_price_plans.to_dict())
            _dict['pricePlans'] = _items
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of feature_details
        if self.feature_details:
            _dict['featureDetails'] = self.feature_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enrichments
        if self.enrichments:
            _dict['enrichments'] = self.enrichments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in revenue_details (list)
        _items = []
        if self.revenue_details:
            for _item_revenue_details in self.revenue_details:
                if _item_revenue_details:
                    _items.append(_item_revenue_details.to_dict())
            _dict['revenueDetails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventPipelineInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventSchema": EventPipelineInfoEventSchema.from_dict(obj["eventSchema"]) if obj.get("eventSchema") is not None else None,
            "usageMeters": [EventPipelineInfoUsageMeters.from_dict(_item) for _item in obj["usageMeters"]] if obj.get("usageMeters") is not None else None,
            "pricePlans": [EventPipelineInfoPricePlans.from_dict(_item) for _item in obj["pricePlans"]] if obj.get("pricePlans") is not None else None,
            "account": EventPipelineInfoAccount.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "customer": EventPipelineInfoCustomer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "featureDetails": EventPipelineInfoFeatureDetails.from_dict(obj["featureDetails"]) if obj.get("featureDetails") is not None else None,
            "enrichments": EventPipelineInfoEnrichments.from_dict(obj["enrichments"]) if obj.get("enrichments") is not None else None,
            "revenueDetails": [EventPipelineInfoRevenueDetails.from_dict(_item) for _item in obj["revenueDetails"]] if obj.get("revenueDetails") is not None else None,
            "statusBeforeReverting": obj.get("statusBeforeReverting"),
            "baseCurrency": obj.get("baseCurrency"),
            "invoiceCurrency": obj.get("invoiceCurrency")
        })
        return _obj

