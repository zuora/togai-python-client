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
from togai_client.models.computation import Computation
from togai_client.models.usage_meter_aggregation import UsageMeterAggregation
from togai_client.models.usage_meter_filter_entry import UsageMeterFilterEntry
from typing import Optional, Set
from typing_extensions import Self

class UpdateUsageMeterRequest(BaseModel):
    """
    Request to update usage meter
    """ # noqa: E501
    name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Name of usage meter.")
    billable_name: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Billable name of usage meter. Billable name takes precedence over name to display in invoice.", alias="billableName")
    description: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Description of the usage meter")
    event_schema_name: Optional[StrictStr] = Field(default=None, description="Event Schema Identifier", alias="eventSchemaName")
    type: Optional[StrictStr] = Field(default=None, description="Type of usage meter * COUNTER - Count usage ")
    aggregation: Optional[UsageMeterAggregation] = None
    computations: Optional[List[Computation]] = None
    filters: Optional[List[UsageMeterFilterEntry]] = None
    __properties: ClassVar[List[str]] = ["name", "billableName", "description", "eventSchemaName", "type", "aggregation", "computations", "filters"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['COUNTER']):
            raise ValueError("must be one of enum values ('COUNTER')")
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
        """Create an instance of UpdateUsageMeterRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in computations (list)
        _items = []
        if self.computations:
            for _item_computations in self.computations:
                if _item_computations:
                    _items.append(_item_computations.to_dict())
            _dict['computations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in filters (list)
        _items = []
        if self.filters:
            for _item_filters in self.filters:
                if _item_filters:
                    _items.append(_item_filters.to_dict())
            _dict['filters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateUsageMeterRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "billableName": obj.get("billableName"),
            "description": obj.get("description"),
            "eventSchemaName": obj.get("eventSchemaName"),
            "type": obj.get("type"),
            "aggregation": obj.get("aggregation"),
            "computations": [Computation.from_dict(_item) for _item in obj["computations"]] if obj.get("computations") is not None else None,
            "filters": [UsageMeterFilterEntry.from_dict(_item) for _item in obj["filters"]] if obj.get("filters") is not None else None
        })
        return _obj


