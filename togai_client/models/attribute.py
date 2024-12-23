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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Attribute(BaseModel):
    """
    Metric to be recorded
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="Name of the event attribute")
    value: Annotated[str, Field(strict=True)] = Field(description="Value of the event attribute")
    unit: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=50)]] = Field(default=None, description="Unit with which the attribute value was measured. Natively supported units - \"Meters, Miles, Kilometers, Grams, Kilograms, ounces, Pounds, Minutes, Hours, Seconds, Milliseconds, Microseconds, None\". Clients are free to add any other custom units.")
    __properties: ClassVar[List[str]] = ["name", "value", "unit"]

    @field_validator('value')
    def value_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^-?\d{1,512}(\.\d+)?$", value):
            raise ValueError(r"must validate the regular expression /^-?\d{1,512}(\.\d+)?$/")
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
        """Create an instance of Attribute from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Attribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "value": obj.get("value"),
            "unit": obj.get("unit")
        })
        return _obj


