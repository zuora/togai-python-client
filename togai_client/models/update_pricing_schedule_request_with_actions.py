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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from togai_client.models.create_price_plan_details_override import CreatePricePlanDetailsOverride
from togai_client.models.create_pricing_rule import CreatePricingRule
from togai_client.models.pre_action import PreAction
from typing import Optional, Set
from typing_extensions import Self

class UpdatePricingScheduleRequestWithActions(BaseModel):
    """
    Request to associate or disassociate a price plan to an account with actions
    """ # noqa: E501
    mode: Optional[StrictStr] = Field(default=None, description="Mode of request to create dis/association")
    price_plan_id: Optional[StrictStr] = Field(default=None, description="Id of the price plan if association request", alias="pricePlanId")
    effective_from: date = Field(description="Date of effectiveness of the association. The date is expected in YYYY-MM-DD format - Editing of a BILLING plan with deferredRevenue can be achieved with    effectiveFrom as start date of current cycle or using `retainStartOffset` option. ", alias="effectiveFrom")
    effective_until: date = Field(description="Date until which the association must be effective. The date is expected in YYYY-MM-DD format ", alias="effectiveUntil")
    price_plan_details_override: Optional[CreatePricePlanDetailsOverride] = Field(default=None, alias="pricePlanDetailsOverride")
    pricing_rules_override: Optional[List[CreatePricingRule]] = Field(default=None, alias="pricingRulesOverride")
    retain_start_offsets: Optional[StrictBool] = Field(default=None, description="If this flag is true, current pricing cycle of the account on the date of association will continue rather  than the configurations of the newly associated price plan. Pricing cycle overrides specified  using  `pricePlanDetailsOverride` will take precedence over the pricing cycle configurations of  the new price plan that the account needs to migrate to. PricingCycleInterval of the existing plan and  the new plan must be same for this to work. We'll return a `400 BadRequest` otherwise. Examples:   - Ongoing plan (1st Oct to 30th Oct) - {dayOffset: 1, monthOffset: NIL}     New association (15th Oct to 15th Nov) of different price plan with retainStartOffsets option true      will use the same pricing cycle configuration {dayOffset: 1, monthOffset: NIL} rather than using the     pricing cycle configuration of the new price plan that the account needs to migrate to.   - Ongoing plan (1st Oct to 30th Oct) - {dayOffset: 1, monthOffset: NIL}     New association (1st Nov to 30th Nov) of different price plan with retainStartOffsets option true will     throw a `400 BadRequest` as no existing price plan configuration found on date of association ", alias="retainStartOffsets")
    pre_actions: Optional[List[PreAction]] = Field(default=None, description="Pre actions to be performed before association or disassociation", alias="preActions")
    __properties: ClassVar[List[str]] = ["mode", "pricePlanId", "effectiveFrom", "effectiveUntil", "pricePlanDetailsOverride", "pricingRulesOverride", "retainStartOffsets", "preActions"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ASSOCIATE', 'DISASSOCIATE']):
            raise ValueError("must be one of enum values ('ASSOCIATE', 'DISASSOCIATE')")
        return value

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
        """Create an instance of UpdatePricingScheduleRequestWithActions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price_plan_details_override
        if self.price_plan_details_override:
            _dict['pricePlanDetailsOverride'] = self.price_plan_details_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_rules_override (list)
        _items = []
        if self.pricing_rules_override:
            for _item_pricing_rules_override in self.pricing_rules_override:
                if _item_pricing_rules_override:
                    _items.append(_item_pricing_rules_override.to_dict())
            _dict['pricingRulesOverride'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pre_actions (list)
        _items = []
        if self.pre_actions:
            for _item_pre_actions in self.pre_actions:
                if _item_pre_actions:
                    _items.append(_item_pre_actions.to_dict())
            _dict['preActions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdatePricingScheduleRequestWithActions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mode": obj.get("mode"),
            "pricePlanId": obj.get("pricePlanId"),
            "effectiveFrom": obj.get("effectiveFrom"),
            "effectiveUntil": obj.get("effectiveUntil"),
            "pricePlanDetailsOverride": CreatePricePlanDetailsOverride.from_dict(obj["pricePlanDetailsOverride"]) if obj.get("pricePlanDetailsOverride") is not None else None,
            "pricingRulesOverride": [CreatePricingRule.from_dict(_item) for _item in obj["pricingRulesOverride"]] if obj.get("pricingRulesOverride") is not None else None,
            "retainStartOffsets": obj.get("retainStartOffsets"),
            "preActions": [PreAction.from_dict(_item) for _item in obj["preActions"]] if obj.get("preActions") is not None else None
        })
        return _obj


