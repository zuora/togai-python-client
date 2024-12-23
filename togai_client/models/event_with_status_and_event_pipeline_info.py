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
from typing_extensions import Annotated
from togai_client.models.event import Event
from togai_client.models.event_pipeline_info import EventPipelineInfo
from togai_client.models.event_source import EventSource
from togai_client.models.ingestion_status import IngestionStatus
from typing import Optional, Set
from typing_extensions import Self

class EventWithStatusAndEventPipelineInfo(BaseModel):
    """
    EventWithStatusAndEventPipelineInfo
    """ # noqa: E501
    reference_id: StrictStr = Field(description="Unique id generated by Togai to identify an event uniquely", alias="referenceId")
    event_payload: Event = Field(alias="eventPayload")
    ingestion_status: IngestionStatus = Field(alias="ingestionStatus")
    customer_id: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The associated account belongs to this customer", alias="customerId")
    source: Optional[EventSource] = None
    created_at: datetime = Field(description="Created time stamp of the event. This timestamp must be in ISO 8601 format.", alias="createdAt")
    event_pipeline_info: EventPipelineInfo = Field(alias="eventPipelineInfo")
    __properties: ClassVar[List[str]] = ["referenceId", "eventPayload", "ingestionStatus", "customerId", "source", "createdAt", "eventPipelineInfo"]

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
        """Create an instance of EventWithStatusAndEventPipelineInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of event_payload
        if self.event_payload:
            _dict['eventPayload'] = self.event_payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ingestion_status
        if self.ingestion_status:
            _dict['ingestionStatus'] = self.ingestion_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event_pipeline_info
        if self.event_pipeline_info:
            _dict['eventPipelineInfo'] = self.event_pipeline_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EventWithStatusAndEventPipelineInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "referenceId": obj.get("referenceId"),
            "eventPayload": Event.from_dict(obj["eventPayload"]) if obj.get("eventPayload") is not None else None,
            "ingestionStatus": IngestionStatus.from_dict(obj["ingestionStatus"]) if obj.get("ingestionStatus") is not None else None,
            "customerId": obj.get("customerId"),
            "source": EventSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "createdAt": obj.get("createdAt"),
            "eventPipelineInfo": EventPipelineInfo.from_dict(obj["eventPipelineInfo"]) if obj.get("eventPipelineInfo") is not None else None
        })
        return _obj


