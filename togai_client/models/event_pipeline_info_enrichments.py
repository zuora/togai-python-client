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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from togai_client.models.enriched_field import EnrichedField
from togai_client.models.enrichment_dependency import EnrichmentDependency
from typing import Optional, Set
from typing_extensions import Self

class EventPipelineInfoEnrichments(BaseModel):
    """
    EventPipelineInfoEnrichments
    """ # noqa: E501
    attributes: Optional[List[EnrichedField]] = None
    dimensions: Optional[List[EnrichedField]] = None
    dependencies: Optional[List[EnrichmentDependency]] = None
    __properties: ClassVar[List[str]] = ["attributes", "dimensions", "dependencies"]

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
        """Create an instance of EventPipelineInfoEnrichments from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in dependencies (list)
        _items = []
        if self.dependencies:
            for _item_dependencies in self.dependencies:
                if _item_dependencies:
                    _items.append(_item_dependencies.to_dict())
            _dict['dependencies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventPipelineInfoEnrichments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attributes": [EnrichedField.from_dict(_item) for _item in obj["attributes"]] if obj.get("attributes") is not None else None,
            "dimensions": [EnrichedField.from_dict(_item) for _item in obj["dimensions"]] if obj.get("dimensions") is not None else None,
            "dependencies": [EnrichmentDependency.from_dict(_item) for _item in obj["dependencies"]] if obj.get("dependencies") is not None else None
        })
        return _obj


