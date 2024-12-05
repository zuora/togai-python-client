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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from togai_client.models.add_on_type import AddOnType
from togai_client.models.invoice_timing import InvoiceTiming
from togai_client.models.license_rate_card_config import LicenseRateCardConfig
from togai_client.models.prorated_refund_mode import ProratedRefundMode
from togai_client.models.rate_plan import RatePlan
from togai_client.models.rate_value import RateValue
from togai_client.models.usage_cycle_interval import UsageCycleInterval
from typing import Optional, Set
from typing_extensions import Self

class LicenseRateCard(BaseModel):
    """
    LicenseRateCard
    """ # noqa: E501
    id: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Unique Identifier of the attached AddOn")
    type: Optional[AddOnType] = None
    display_name: Optional[StrictStr] = Field(default=None, description="Name of the attached AddOn", alias="displayName")
    name: Optional[StrictStr] = Field(default=None, description="Unique identifier for the rate card in a price plan. If left null it is auto-generated.")
    tag: Optional[StrictStr] = Field(default=None, description="A tag string to group licenseRateCards")
    invoice_timing: Optional[InvoiceTiming] = Field(default=None, alias="invoiceTiming")
    usage_cycle: Optional[UsageCycleInterval] = Field(default=None, alias="usageCycle")
    enable_proration: StrictBool = Field(alias="enableProration")
    config: Optional[LicenseRateCardConfig] = None
    rate_plan: RatePlan = Field(alias="ratePlan")
    rate_values: List[RateValue] = Field(alias="rateValues")
    prorated_refund_mode: Optional[ProratedRefundMode] = Field(default=None, alias="proratedRefundMode")
    __properties: ClassVar[List[str]] = ["id", "type", "displayName", "name", "tag", "invoiceTiming", "usageCycle", "enableProration", "config", "ratePlan", "rateValues", "proratedRefundMode"]

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
        """Create an instance of LicenseRateCard from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rate_plan
        if self.rate_plan:
            _dict['ratePlan'] = self.rate_plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rate_values (list)
        _items = []
        if self.rate_values:
            for _item_rate_values in self.rate_values:
                if _item_rate_values:
                    _items.append(_item_rate_values.to_dict())
            _dict['rateValues'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LicenseRateCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "displayName": obj.get("displayName"),
            "name": obj.get("name"),
            "tag": obj.get("tag"),
            "invoiceTiming": obj.get("invoiceTiming"),
            "usageCycle": obj.get("usageCycle"),
            "enableProration": obj.get("enableProration"),
            "config": LicenseRateCardConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "ratePlan": RatePlan.from_dict(obj["ratePlan"]) if obj.get("ratePlan") is not None else None,
            "rateValues": [RateValue.from_dict(_item) for _item in obj["rateValues"]] if obj.get("rateValues") is not None else None,
            "proratedRefundMode": obj.get("proratedRefundMode")
        })
        return _obj

