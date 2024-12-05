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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class LicenseUpdateRequest(BaseModel):
    """
    License update request
    """ # noqa: E501
    license_id: Annotated[str, Field(strict=True, max_length=50)] = Field(description="The license id for which the update is requested", alias="licenseId")
    account_id: Annotated[str, Field(strict=True, max_length=50)] = Field(description="The account id for which the license is being updated", alias="accountId")
    update_type: StrictStr = Field(description="The type of update to be performed", alias="updateType")
    quantity: Union[StrictFloat, StrictInt] = Field(description="The quantity to be updated")
    effective_from: Optional[datetime] = Field(default=None, description="The effective from date for the update", alias="effectiveFrom")
    idempotency_key: Optional[StrictStr] = Field(default=None, description="The idempotency key for uniqueness of the license update request", alias="idempotencyKey")
    metadata: Optional[Dict[str, StrictStr]] = None
    __properties: ClassVar[List[str]] = ["licenseId", "accountId", "updateType", "quantity", "effectiveFrom", "idempotencyKey", "metadata"]

    @field_validator('update_type')
    def update_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RELATIVE', 'ABSOLUTE']):
            raise ValueError("must be one of enum values ('RELATIVE', 'ABSOLUTE')")
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
        """Create an instance of LicenseUpdateRequest from a JSON string"""
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
        """Create an instance of LicenseUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "licenseId": obj.get("licenseId"),
            "accountId": obj.get("accountId"),
            "updateType": obj.get("updateType"),
            "quantity": obj.get("quantity"),
            "effectiveFrom": obj.get("effectiveFrom"),
            "idempotencyKey": obj.get("idempotencyKey"),
            "metadata": obj.get("metadata")
        })
        return _obj

