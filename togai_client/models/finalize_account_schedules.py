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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from togai_client.models.pre_action import PreAction
from typing import Optional, Set
from typing_extensions import Self

class FinalizeAccountSchedules(BaseModel):
    """
    Request to finalize account schedules
    """ # noqa: E501
    merge_schedules: Optional[StrictBool] = Field(default=None, description="If this flag is true, the schedules will be merged with the existing schedules of the account if possible. If this flag is false, the existing schedules will be replaced with the new schedules. Default value is false ", alias="mergeSchedules")
    pre_actions: Optional[List[PreAction]] = Field(default=None, description="Pre actions to be performed before association or disassociation", alias="preActions")
    __properties: ClassVar[List[str]] = ["mergeSchedules", "preActions"]

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
        """Create an instance of FinalizeAccountSchedules from a JSON string"""
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
        """Create an instance of FinalizeAccountSchedules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mergeSchedules": obj.get("mergeSchedules"),
            "preActions": [PreAction.from_dict(_item) for _item in obj["preActions"]] if obj.get("preActions") is not None else None
        })
        return _obj


