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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from togai_client.models.address import Address
from typing import Optional, Set
from typing_extensions import Self

class InvoiceGroups(BaseModel):
    """
    InvoiceGroups
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    email: Annotated[str, Field(strict=True, max_length=320)]
    daily_invoice_consolidation: StrictBool = Field(alias="dailyInvoiceConsolidation")
    net_term_days: Optional[StrictInt] = Field(default=None, alias="netTermDays")
    invoice_currency: StrictStr = Field(alias="invoiceCurrency")
    billing_address: Address = Field(alias="billingAddress")
    accounts_count: Annotated[int, Field(strict=True, ge=0)] = Field(alias="accountsCount")
    created_at: datetime = Field(alias="createdAt")
    updated_at: datetime = Field(alias="updatedAt")
    __properties: ClassVar[List[str]] = ["id", "name", "email", "dailyInvoiceConsolidation", "netTermDays", "invoiceCurrency", "billingAddress", "accountsCount", "createdAt", "updatedAt"]

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
        """Create an instance of InvoiceGroups from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceGroups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "dailyInvoiceConsolidation": obj.get("dailyInvoiceConsolidation"),
            "netTermDays": obj.get("netTermDays"),
            "invoiceCurrency": obj.get("invoiceCurrency"),
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "accountsCount": obj.get("accountsCount"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


