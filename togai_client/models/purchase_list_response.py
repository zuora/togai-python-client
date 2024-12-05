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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from togai_client.models.price_plan_details import PricePlanDetails
from togai_client.models.purchase_status import PurchaseStatus
from togai_client.models.purchase_type import PurchaseType
from togai_client.models.wallet_topup_details import WalletTopupDetails
from typing import Optional, Set
from typing_extensions import Self

class PurchaseListResponse(BaseModel):
    """
    Represents a Purchase for List Response
    """ # noqa: E501
    id: StrictStr
    price_plan_id: Optional[StrictStr] = Field(default=None, alias="pricePlanId")
    price_plan_name: Optional[StrictStr] = Field(default=None, alias="pricePlanName")
    quantity: Optional[StrictInt] = None
    rate_card_quantities: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, alias="rateCardQuantities")
    price_plan_version: Optional[StrictInt] = Field(default=None, alias="pricePlanVersion")
    status: PurchaseStatus
    idempotency_key: Optional[StrictStr] = Field(default=None, alias="idempotencyKey")
    purchase_plan: Optional[PricePlanDetails] = Field(default=None, alias="purchasePlan")
    wallet_topup_details: Optional[WalletTopupDetails] = Field(default=None, alias="walletTopupDetails")
    price: Optional[Union[StrictFloat, StrictInt]] = None
    invoice_currency: Optional[StrictStr] = Field(default=None, alias="invoiceCurrency")
    created_at: datetime = Field(alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    type: PurchaseType
    __properties: ClassVar[List[str]] = ["id", "pricePlanId", "pricePlanName", "quantity", "rateCardQuantities", "pricePlanVersion", "status", "idempotencyKey", "purchasePlan", "walletTopupDetails", "price", "invoiceCurrency", "createdAt", "updatedAt", "type"]

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
        """Create an instance of PurchaseListResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of purchase_plan
        if self.purchase_plan:
            _dict['purchasePlan'] = self.purchase_plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wallet_topup_details
        if self.wallet_topup_details:
            _dict['walletTopupDetails'] = self.wallet_topup_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PurchaseListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "pricePlanId": obj.get("pricePlanId"),
            "pricePlanName": obj.get("pricePlanName"),
            "quantity": obj.get("quantity"),
            "rateCardQuantities": obj.get("rateCardQuantities"),
            "pricePlanVersion": obj.get("pricePlanVersion"),
            "status": obj.get("status"),
            "idempotencyKey": obj.get("idempotencyKey"),
            "purchasePlan": PricePlanDetails.from_dict(obj["purchasePlan"]) if obj.get("purchasePlan") is not None else None,
            "walletTopupDetails": WalletTopupDetails.from_dict(obj["walletTopupDetails"]) if obj.get("walletTopupDetails") is not None else None,
            "price": obj.get("price"),
            "invoiceCurrency": obj.get("invoiceCurrency"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "type": obj.get("type")
        })
        return _obj

