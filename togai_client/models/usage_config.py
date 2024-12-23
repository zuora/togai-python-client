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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from togai_client.models.usage_config_lookup_cycle import UsageConfigLookupCycle
from togai_client.models.usage_config_lookup_range import UsageConfigLookupRange
from typing import Optional, Set
from typing_extensions import Self

class UsageConfig(BaseModel):
    """
    Configuration for getting the usage
    """ # noqa: E501
    mode: StrictStr = Field(description="Mode to get the usage for the usage meters - CUSTOM: Use the usages provided in the request - LOOKUP_RANGE: Use the usage of a given account for the specified range - LOOKUP_CYCLE: Use the usage of a given account for the specified cycle ")
    usage_map: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="Map of usage meter id and usage, this will be considered if mode is CUSTOM", alias="usageMap")
    lookup_range: Optional[UsageConfigLookupRange] = Field(default=None, alias="lookupRange")
    lookup_cycle: Optional[UsageConfigLookupCycle] = Field(default=None, alias="lookupCycle")
    __properties: ClassVar[List[str]] = ["mode", "usageMap", "lookupRange", "lookupCycle"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CUSTOM', 'LOOKUP_RANGE', 'LOOKUP_CYCLE']):
            raise ValueError("must be one of enum values ('CUSTOM', 'LOOKUP_RANGE', 'LOOKUP_CYCLE')")
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
        """Create an instance of UsageConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of lookup_range
        if self.lookup_range:
            _dict['lookupRange'] = self.lookup_range.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lookup_cycle
        if self.lookup_cycle:
            _dict['lookupCycle'] = self.lookup_cycle.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mode": obj.get("mode"),
            "usageMap": obj.get("usageMap"),
            "lookupRange": UsageConfigLookupRange.from_dict(obj["lookupRange"]) if obj.get("lookupRange") is not None else None,
            "lookupCycle": UsageConfigLookupCycle.from_dict(obj["lookupCycle"]) if obj.get("lookupCycle") is not None else None
        })
        return _obj


