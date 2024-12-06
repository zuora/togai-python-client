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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from togai_client.models.alert_status import AlertStatus
from typing import Optional, Set
from typing_extensions import Self

class Alert(BaseModel):
    """
    Alert
    """ # noqa: E501
    id: StrictStr = Field(description="Alert ID")
    version: StrictInt = Field(description="Alert Version")
    description: Optional[StrictStr] = Field(default=None, description="Alert Description")
    status: AlertStatus
    validity: Optional[StrictInt] = Field(default=None, description="Validity of the alert in minutes, if null then alert will be valid forever")
    alert_template_id: StrictStr = Field(description="Alert Template Id", alias="alertTemplateId")
    interval: StrictInt = Field(description="Interval")
    entity_details: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="entityDetails")
    owner_details: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, alias="ownerDetails")
    parameters: Optional[Dict[str, Dict[str, Any]]] = None
    created_at: datetime = Field(description="Created At", alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, description="Updated At", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "version", "description", "status", "validity", "alertTemplateId", "interval", "entityDetails", "ownerDetails", "parameters", "createdAt", "updatedAt"]

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
        """Create an instance of Alert from a JSON string"""
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
        """Create an instance of Alert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "version": obj.get("version"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "validity": obj.get("validity"),
            "alertTemplateId": obj.get("alertTemplateId"),
            "interval": obj.get("interval"),
            "entityDetails": obj.get("entityDetails"),
            "ownerDetails": obj.get("ownerDetails"),
            "parameters": obj.get("parameters"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


