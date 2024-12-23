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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from togai_client.models.query_input import QueryInput
from togai_client.models.report_status import ReportStatus
from togai_client.models.report_type import ReportType
from typing import Optional, Set
from typing_extensions import Self

class Report(BaseModel):
    """
    Represents a Report
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    account_id: Optional[StrictStr] = None
    status: ReportStatus
    file_id: Optional[StrictStr] = Field(default=None, alias="fileId")
    query_input: Optional[QueryInput] = Field(default=None, alias="queryInput")
    report_template_id: Optional[StrictStr] = Field(default=None, alias="reportTemplateId")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    pre_signed_url: Optional[StrictStr] = Field(default=None, alias="preSignedUrl")
    type: Optional[ReportType] = None
    __properties: ClassVar[List[str]] = ["id", "name", "account_id", "status", "fileId", "queryInput", "reportTemplateId", "createdAt", "updatedAt", "preSignedUrl", "type"]

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
        """Create an instance of Report from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of query_input
        if self.query_input:
            _dict['queryInput'] = self.query_input.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Report from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "account_id": obj.get("account_id"),
            "status": obj.get("status"),
            "fileId": obj.get("fileId"),
            "queryInput": QueryInput.from_dict(obj["queryInput"]) if obj.get("queryInput") is not None else None,
            "reportTemplateId": obj.get("reportTemplateId"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "preSignedUrl": obj.get("preSignedUrl"),
            "type": obj.get("type")
        })
        return _obj


