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

class CreditTransaction(BaseModel):
    """
    CreditTransaction
    """ # noqa: E501
    id: Annotated[str, Field(strict=True, max_length=50)] = Field(description="Identifier of credit transactions")
    credit_id: StrictStr = Field(alias="creditId")
    transaction_type: StrictStr = Field(alias="transactionType")
    invoice_id: Optional[StrictStr] = Field(default=None, alias="invoiceId")
    entity_id: Optional[StrictStr] = Field(default=None, alias="entityId")
    amount: Union[StrictFloat, StrictInt]
    created_at: datetime = Field(alias="createdAt")
    __properties: ClassVar[List[str]] = ["id", "creditId", "transactionType", "invoiceId", "entityId", "amount", "createdAt"]

    @field_validator('transaction_type')
    def transaction_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CREDITED', 'DEBITED', 'EXPIRED', 'VOIDED']):
            raise ValueError("must be one of enum values ('CREDITED', 'DEBITED', 'EXPIRED', 'VOIDED')")
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
        """Create an instance of CreditTransaction from a JSON string"""
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
        """Create an instance of CreditTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "creditId": obj.get("creditId"),
            "transactionType": obj.get("transactionType"),
            "invoiceId": obj.get("invoiceId"),
            "entityId": obj.get("entityId"),
            "amount": obj.get("amount"),
            "createdAt": obj.get("createdAt")
        })
        return _obj


