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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from togai_client.models.billing_entitlement_rate_card import BillingEntitlementRateCard
from togai_client.models.credit_grant_rate_card import CreditGrantRateCard
from togai_client.models.entitlement_overage_rate_card import EntitlementOverageRateCard
from togai_client.models.fixed_fee_rate_card import FixedFeeRateCard
from togai_client.models.license_rate_card import LicenseRateCard
from togai_client.models.minimum_commitment import MinimumCommitment
from togai_client.models.pricing_cycle_config import PricingCycleConfig
from togai_client.models.usage_rate_card import UsageRateCard
from typing import Optional, Set
from typing_extensions import Self

class CreatePricePlanDetailsOverride(BaseModel):
    """
    CreatePricePlanDetailsOverride
    """ # noqa: E501
    pricing_cycle_config: Optional[PricingCycleConfig] = Field(default=None, alias="pricingCycleConfig")
    supported_currencies: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, alias="supportedCurrencies")
    usage_rate_cards: Optional[List[UsageRateCard]] = Field(default=None, alias="usageRateCards")
    billing_entitlement_rate_cards: Optional[List[BillingEntitlementRateCard]] = Field(default=None, alias="billingEntitlementRateCards")
    entitlement_overage_rate_cards: Optional[List[EntitlementOverageRateCard]] = Field(default=None, alias="entitlementOverageRateCards")
    fixed_fee_rate_cards: Optional[List[FixedFeeRateCard]] = Field(default=None, alias="fixedFeeRateCards")
    license_rate_cards: Optional[List[LicenseRateCard]] = Field(default=None, alias="licenseRateCards")
    minimum_commitment: Optional[MinimumCommitment] = Field(default=None, alias="minimumCommitment")
    credit_grant_rate_cards: Optional[List[CreditGrantRateCard]] = Field(default=None, alias="creditGrantRateCards")
    __properties: ClassVar[List[str]] = ["pricingCycleConfig", "supportedCurrencies", "usageRateCards", "billingEntitlementRateCards", "entitlementOverageRateCards", "fixedFeeRateCards", "licenseRateCards", "minimumCommitment", "creditGrantRateCards"]

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
        """Create an instance of CreatePricePlanDetailsOverride from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pricing_cycle_config
        if self.pricing_cycle_config:
            _dict['pricingCycleConfig'] = self.pricing_cycle_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in usage_rate_cards (list)
        _items = []
        if self.usage_rate_cards:
            for _item_usage_rate_cards in self.usage_rate_cards:
                if _item_usage_rate_cards:
                    _items.append(_item_usage_rate_cards.to_dict())
            _dict['usageRateCards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in billing_entitlement_rate_cards (list)
        _items = []
        if self.billing_entitlement_rate_cards:
            for _item_billing_entitlement_rate_cards in self.billing_entitlement_rate_cards:
                if _item_billing_entitlement_rate_cards:
                    _items.append(_item_billing_entitlement_rate_cards.to_dict())
            _dict['billingEntitlementRateCards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in entitlement_overage_rate_cards (list)
        _items = []
        if self.entitlement_overage_rate_cards:
            for _item_entitlement_overage_rate_cards in self.entitlement_overage_rate_cards:
                if _item_entitlement_overage_rate_cards:
                    _items.append(_item_entitlement_overage_rate_cards.to_dict())
            _dict['entitlementOverageRateCards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fixed_fee_rate_cards (list)
        _items = []
        if self.fixed_fee_rate_cards:
            for _item_fixed_fee_rate_cards in self.fixed_fee_rate_cards:
                if _item_fixed_fee_rate_cards:
                    _items.append(_item_fixed_fee_rate_cards.to_dict())
            _dict['fixedFeeRateCards'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in license_rate_cards (list)
        _items = []
        if self.license_rate_cards:
            for _item_license_rate_cards in self.license_rate_cards:
                if _item_license_rate_cards:
                    _items.append(_item_license_rate_cards.to_dict())
            _dict['licenseRateCards'] = _items
        # override the default output from pydantic by calling `to_dict()` of minimum_commitment
        if self.minimum_commitment:
            _dict['minimumCommitment'] = self.minimum_commitment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in credit_grant_rate_cards (list)
        _items = []
        if self.credit_grant_rate_cards:
            for _item_credit_grant_rate_cards in self.credit_grant_rate_cards:
                if _item_credit_grant_rate_cards:
                    _items.append(_item_credit_grant_rate_cards.to_dict())
            _dict['creditGrantRateCards'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreatePricePlanDetailsOverride from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pricingCycleConfig": PricingCycleConfig.from_dict(obj["pricingCycleConfig"]) if obj.get("pricingCycleConfig") is not None else None,
            "supportedCurrencies": obj.get("supportedCurrencies"),
            "usageRateCards": [UsageRateCard.from_dict(_item) for _item in obj["usageRateCards"]] if obj.get("usageRateCards") is not None else None,
            "billingEntitlementRateCards": [BillingEntitlementRateCard.from_dict(_item) for _item in obj["billingEntitlementRateCards"]] if obj.get("billingEntitlementRateCards") is not None else None,
            "entitlementOverageRateCards": [EntitlementOverageRateCard.from_dict(_item) for _item in obj["entitlementOverageRateCards"]] if obj.get("entitlementOverageRateCards") is not None else None,
            "fixedFeeRateCards": [FixedFeeRateCard.from_dict(_item) for _item in obj["fixedFeeRateCards"]] if obj.get("fixedFeeRateCards") is not None else None,
            "licenseRateCards": [LicenseRateCard.from_dict(_item) for _item in obj["licenseRateCards"]] if obj.get("licenseRateCards") is not None else None,
            "minimumCommitment": MinimumCommitment.from_dict(obj["minimumCommitment"]) if obj.get("minimumCommitment") is not None else None,
            "creditGrantRateCards": [CreditGrantRateCard.from_dict(_item) for _item in obj["creditGrantRateCards"]] if obj.get("creditGrantRateCards") is not None else None
        })
        return _obj


