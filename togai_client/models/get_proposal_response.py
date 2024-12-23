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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from togai_client.models.create_price_plan_details_override import CreatePricePlanDetailsOverride
from togai_client.models.price_plan_details_override import PricePlanDetailsOverride
from togai_client.models.purchase_status import PurchaseStatus
from togai_client.models.purchase_type import PurchaseType
from togai_client.models.wallet_topup_details import WalletTopupDetails
from typing import Optional, Set
from typing_extensions import Self

class GetProposalResponse(BaseModel):
    """
    GetProposalResponse
    """ # noqa: E501
    id: StrictStr
    account_id: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="accountId")
    price_plan_id: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Id of the price plan, Required for ENTITLEMENT_GRANT, ASSOCIATION purchase", alias="pricePlanId")
    quantity: Optional[StrictInt] = None
    rate_card_quantities: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, alias="rateCardQuantities")
    idempotency_key: Optional[StrictStr] = Field(default=None, alias="idempotencyKey")
    price_plan_version: Optional[StrictInt] = Field(default=None, alias="pricePlanVersion")
    purchase_plan_override: Optional[PricePlanDetailsOverride] = Field(default=None, alias="purchasePlanOverride")
    association_override: Optional[CreatePricePlanDetailsOverride] = Field(default=None, alias="associationOverride")
    wallet_topup_details: Optional[WalletTopupDetails] = Field(default=None, alias="walletTopupDetails")
    created_at: datetime = Field(alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    effective_from: Optional[date] = Field(default=None, alias="effectiveFrom")
    effective_until: Optional[date] = Field(default=None, alias="effectiveUntil")
    expiry_date: Optional[datetime] = Field(default=None, alias="expiryDate")
    price: Optional[Union[StrictFloat, StrictInt]] = None
    invoice_id: Optional[StrictStr] = Field(default=None, alias="invoiceId")
    invoice_currency: Optional[StrictStr] = Field(default=None, alias="invoiceCurrency")
    status: PurchaseStatus
    type: PurchaseType
    comment: Optional[StrictStr] = None
    payment_mode: StrictStr = Field(alias="paymentMode")
    proposal_response_date: Optional[datetime] = Field(default=None, alias="proposalResponseDate")
    __properties: ClassVar[List[str]] = ["id", "accountId", "pricePlanId", "quantity", "rateCardQuantities", "idempotencyKey", "pricePlanVersion", "purchasePlanOverride", "associationOverride", "walletTopupDetails", "createdAt", "updatedAt", "effectiveFrom", "effectiveUntil", "expiryDate", "price", "invoiceId", "invoiceCurrency", "status", "type", "comment", "paymentMode", "proposalResponseDate"]

    @field_validator('payment_mode')
    def payment_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PREPAID', 'POSTPAID']):
            raise ValueError("must be one of enum values ('PREPAID', 'POSTPAID')")
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
        """Create an instance of GetProposalResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of purchase_plan_override
        if self.purchase_plan_override:
            _dict['purchasePlanOverride'] = self.purchase_plan_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of association_override
        if self.association_override:
            _dict['associationOverride'] = self.association_override.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wallet_topup_details
        if self.wallet_topup_details:
            _dict['walletTopupDetails'] = self.wallet_topup_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetProposalResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "accountId": obj.get("accountId"),
            "pricePlanId": obj.get("pricePlanId"),
            "quantity": obj.get("quantity"),
            "rateCardQuantities": obj.get("rateCardQuantities"),
            "idempotencyKey": obj.get("idempotencyKey"),
            "pricePlanVersion": obj.get("pricePlanVersion"),
            "purchasePlanOverride": PricePlanDetailsOverride.from_dict(obj["purchasePlanOverride"]) if obj.get("purchasePlanOverride") is not None else None,
            "associationOverride": CreatePricePlanDetailsOverride.from_dict(obj["associationOverride"]) if obj.get("associationOverride") is not None else None,
            "walletTopupDetails": WalletTopupDetails.from_dict(obj["walletTopupDetails"]) if obj.get("walletTopupDetails") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "effectiveFrom": obj.get("effectiveFrom"),
            "effectiveUntil": obj.get("effectiveUntil"),
            "expiryDate": obj.get("expiryDate"),
            "price": obj.get("price"),
            "invoiceId": obj.get("invoiceId"),
            "invoiceCurrency": obj.get("invoiceCurrency"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "comment": obj.get("comment"),
            "paymentMode": obj.get("paymentMode"),
            "proposalResponseDate": obj.get("proposalResponseDate")
        })
        return _obj


