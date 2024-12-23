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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from togai_client.models.dimensions_schema import DimensionsSchema
from togai_client.models.enrichments import Enrichments
from togai_client.models.event_attribute_schema import EventAttributeSchema
from togai_client.models.feature_details import FeatureDetails
from typing import Optional, Set
from typing_extensions import Self

class EventSchemaListData(BaseModel):
    """
    EventSchemaListData
    """ # noqa: E501
    name: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Name of the event. Must be unique for an organization.")
    description: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, description="Description of the event")
    version: Annotated[int, Field(strict=True, ge=1)] = Field(description="Version of event schema")
    status: Optional[StrictStr] = Field(default=None, description="Status of event schema * DRAFT - Schema is in draft state  * ACTIVE - Schema is currently active  * INACTIVE - Schema is currently inactive * ARCHIVED - Older version of event schema ")
    attributes: Optional[Annotated[List[EventAttributeSchema], Field(max_length=50)]] = None
    dimensions: Optional[Annotated[List[DimensionsSchema], Field(max_length=50)]] = None
    filter_fields: Optional[List[StrictStr]] = Field(default=None, alias="filterFields")
    feature_details: Optional[FeatureDetails] = Field(default=None, alias="featureDetails")
    enrichments: Optional[Enrichments] = None
    event_id_template: Optional[StrictStr] = Field(default=None, description="Template used to generate event id based on event payload", alias="eventIdTemplate")
    event_level_revenue: Optional[StrictBool] = Field(default=None, alias="eventLevelRevenue")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    usage_meters_count: Optional[StrictInt] = Field(default=None, alias="usageMetersCount")
    __properties: ClassVar[List[str]] = ["name", "description", "version", "status", "attributes", "dimensions", "filterFields", "featureDetails", "enrichments", "eventIdTemplate", "eventLevelRevenue", "createdAt", "updatedAt", "usageMetersCount"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[\sa-zA-Z0-9_-]*$", value):
            raise ValueError(r"must validate the regular expression /^[\sa-zA-Z0-9_-]*$/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DRAFT', 'ACTIVE', 'INACTIVE', 'ARCHIVED']):
            raise ValueError("must be one of enum values ('DRAFT', 'ACTIVE', 'INACTIVE', 'ARCHIVED')")
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
        """Create an instance of EventSchemaListData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item_attributes in self.attributes:
                if _item_attributes:
                    _items.append(_item_attributes.to_dict())
            _dict['attributes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dimensions (list)
        _items = []
        if self.dimensions:
            for _item_dimensions in self.dimensions:
                if _item_dimensions:
                    _items.append(_item_dimensions.to_dict())
            _dict['dimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of feature_details
        if self.feature_details:
            _dict['featureDetails'] = self.feature_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enrichments
        if self.enrichments:
            _dict['enrichments'] = self.enrichments.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventSchemaListData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "version": obj.get("version"),
            "status": obj.get("status"),
            "attributes": [EventAttributeSchema.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "dimensions": [DimensionsSchema.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "filterFields": obj.get("filterFields"),
            "featureDetails": FeatureDetails.from_dict(obj["featureDetails"]) if obj.get("featureDetails") is not None else None,
            "enrichments": Enrichments.from_dict(obj["enrichments"]) if obj.get("enrichments") is not None else None,
            "eventIdTemplate": obj.get("eventIdTemplate"),
            "eventLevelRevenue": obj.get("eventLevelRevenue"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "usageMetersCount": obj.get("usageMetersCount")
        })
        return _obj


