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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from togai_client.models.create_pricing_rule import CreatePricingRule
from typing import Optional, Set
from typing_extensions import Self

class UpdatePricingRulesRequest(BaseModel):
    """
    UpdatePricingRulesRequest
    """ # noqa: E501
    pricing_rules: Optional[List[CreatePricingRule]] = Field(default=None, alias="pricingRules")
    __properties: ClassVar[List[str]] = ["pricingRules"]

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
        """Create an instance of UpdatePricingRulesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_rules (list)
        _items = []
        if self.pricing_rules:
            for _item_pricing_rules in self.pricing_rules:
                if _item_pricing_rules:
                    _items.append(_item_pricing_rules.to_dict())
            _dict['pricingRules'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdatePricingRulesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pricingRules": [CreatePricingRule.from_dict(_item) for _item in obj["pricingRules"]] if obj.get("pricingRules") is not None else None
        })
        return _obj

