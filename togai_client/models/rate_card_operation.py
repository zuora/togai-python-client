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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from togai_client.models.rate_card_data import RateCardData
from typing import Optional, Set
from typing_extensions import Self

class RateCardOperation(BaseModel):
    """
    Rate card operation
    """ # noqa: E501
    action_type: StrictStr = Field(description="Operation type", alias="actionType")
    rate_card_name: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Required for UPDATE and DELETE operations", alias="rateCardName")
    rate_card: Optional[RateCardData] = Field(default=None, alias="rateCard")
    __properties: ClassVar[List[str]] = ["actionType", "rateCardName", "rateCard"]

    @field_validator('action_type')
    def action_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CREATE', 'UPDATE', 'DELETE']):
            raise ValueError("must be one of enum values ('CREATE', 'UPDATE', 'DELETE')")
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
        """Create an instance of RateCardOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rate_card
        if self.rate_card:
            _dict['rateCard'] = self.rate_card.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RateCardOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actionType": obj.get("actionType"),
            "rateCardName": obj.get("rateCardName"),
            "rateCard": RateCardData.from_dict(obj["rateCard"]) if obj.get("rateCard") is not None else None
        })
        return _obj

