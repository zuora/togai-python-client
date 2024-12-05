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
from typing_extensions import Annotated
from togai_client.models.pricing_rule_action import PricingRuleAction
from togai_client.models.pricing_rule_timing import PricingRuleTiming
from typing import Optional, Set
from typing_extensions import Self

class PricingRule(BaseModel):
    """
    Represents pricing rules of a price plan. i.e, price plan bound by time.
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    version: Annotated[int, Field(strict=True, ge=1)]
    invoice_timing: Optional[PricingRuleTiming] = Field(default=None, alias="invoiceTiming")
    order: Annotated[int, Field(strict=True, ge=1)]
    condition: Optional[StrictStr] = Field(default=None, description="JSON logic condition deciding whether to compute this pricing rule or not")
    computation: StrictStr = Field(description="JSON logic to be computed")
    action: PricingRuleAction
    __properties: ClassVar[List[str]] = ["id", "name", "version", "invoiceTiming", "order", "condition", "computation", "action"]

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
        """Create an instance of PricingRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict['action'] = self.action.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PricingRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "version": obj.get("version"),
            "invoiceTiming": obj.get("invoiceTiming"),
            "order": obj.get("order"),
            "condition": obj.get("condition"),
            "computation": obj.get("computation"),
            "action": PricingRuleAction.from_dict(obj["action"]) if obj.get("action") is not None else None
        })
        return _obj


