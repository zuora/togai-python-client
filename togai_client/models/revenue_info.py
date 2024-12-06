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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from togai_client.models.billing_entitlement_rate_card import BillingEntitlementRateCard
from togai_client.models.billing_entitlement_revenue_summary import BillingEntitlementRevenueSummary
from togai_client.models.credit_grant_rate_card import CreditGrantRateCard
from togai_client.models.credit_grant_revenue_summary import CreditGrantRevenueSummary
from togai_client.models.entitlement_overage_rate_card import EntitlementOverageRateCard
from togai_client.models.entitlement_overage_revenue_summary import EntitlementOverageRevenueSummary
from togai_client.models.fixed_fee_rate_card import FixedFeeRateCard
from togai_client.models.fixed_fee_revenue_summary import FixedFeeRevenueSummary
from togai_client.models.license_rate_card import LicenseRateCard
from togai_client.models.slab_revenue_summary import SlabRevenueSummary
from togai_client.models.usage_rate_card import UsageRateCard
from typing import Optional, Set
from typing_extensions import Self

class RevenueInfo(BaseModel):
    """
    RevenueInfo
    """ # noqa: E501
    usage_rate_card: Optional[UsageRateCard] = Field(default=None, alias="usageRateCard")
    fixed_fee_rate_card: Optional[FixedFeeRateCard] = Field(default=None, alias="fixedFeeRateCard")
    license_rate_card: Optional[LicenseRateCard] = Field(default=None, alias="licenseRateCard")
    billing_entitlement_rate_card: Optional[BillingEntitlementRateCard] = Field(default=None, alias="billingEntitlementRateCard")
    credit_grant_rate_card: Optional[CreditGrantRateCard] = Field(default=None, alias="creditGrantRateCard")
    entitlement_overage_rate_card: Optional[EntitlementOverageRateCard] = Field(default=None, alias="entitlementOverageRateCard")
    usages: Dict[str, Union[StrictFloat, StrictInt]]
    fixed_fee_revenue_summary: Optional[FixedFeeRevenueSummary] = Field(default=None, alias="fixedFeeRevenueSummary")
    license_revenue_summary: Optional[List[SlabRevenueSummary]] = Field(default=None, alias="licenseRevenueSummary")
    billing_entitlement_revenue_summary: Optional[BillingEntitlementRevenueSummary] = Field(default=None, alias="billingEntitlementRevenueSummary")
    credit_grant_revenue_summary: Optional[CreditGrantRevenueSummary] = Field(default=None, alias="creditGrantRevenueSummary")
    entitlement_overage_revenue_summary: Optional[EntitlementOverageRevenueSummary] = Field(default=None, alias="entitlementOverageRevenueSummary")
    slab_revenue_summaries: Optional[List[SlabRevenueSummary]] = Field(default=None, alias="slabRevenueSummaries")
    __properties: ClassVar[List[str]] = ["usageRateCard", "fixedFeeRateCard", "licenseRateCard", "billingEntitlementRateCard", "creditGrantRateCard", "entitlementOverageRateCard", "usages", "fixedFeeRevenueSummary", "licenseRevenueSummary", "billingEntitlementRevenueSummary", "creditGrantRevenueSummary", "entitlementOverageRevenueSummary", "slabRevenueSummaries"]

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
        """Create an instance of RevenueInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of usage_rate_card
        if self.usage_rate_card:
            _dict['usageRateCard'] = self.usage_rate_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_fee_rate_card
        if self.fixed_fee_rate_card:
            _dict['fixedFeeRateCard'] = self.fixed_fee_rate_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of license_rate_card
        if self.license_rate_card:
            _dict['licenseRateCard'] = self.license_rate_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_entitlement_rate_card
        if self.billing_entitlement_rate_card:
            _dict['billingEntitlementRateCard'] = self.billing_entitlement_rate_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_grant_rate_card
        if self.credit_grant_rate_card:
            _dict['creditGrantRateCard'] = self.credit_grant_rate_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entitlement_overage_rate_card
        if self.entitlement_overage_rate_card:
            _dict['entitlementOverageRateCard'] = self.entitlement_overage_rate_card.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_fee_revenue_summary
        if self.fixed_fee_revenue_summary:
            _dict['fixedFeeRevenueSummary'] = self.fixed_fee_revenue_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in license_revenue_summary (list)
        _items = []
        if self.license_revenue_summary:
            for _item_license_revenue_summary in self.license_revenue_summary:
                if _item_license_revenue_summary:
                    _items.append(_item_license_revenue_summary.to_dict())
            _dict['licenseRevenueSummary'] = _items
        # override the default output from pydantic by calling `to_dict()` of billing_entitlement_revenue_summary
        if self.billing_entitlement_revenue_summary:
            _dict['billingEntitlementRevenueSummary'] = self.billing_entitlement_revenue_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of credit_grant_revenue_summary
        if self.credit_grant_revenue_summary:
            _dict['creditGrantRevenueSummary'] = self.credit_grant_revenue_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of entitlement_overage_revenue_summary
        if self.entitlement_overage_revenue_summary:
            _dict['entitlementOverageRevenueSummary'] = self.entitlement_overage_revenue_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in slab_revenue_summaries (list)
        _items = []
        if self.slab_revenue_summaries:
            for _item_slab_revenue_summaries in self.slab_revenue_summaries:
                if _item_slab_revenue_summaries:
                    _items.append(_item_slab_revenue_summaries.to_dict())
            _dict['slabRevenueSummaries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RevenueInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "usageRateCard": UsageRateCard.from_dict(obj["usageRateCard"]) if obj.get("usageRateCard") is not None else None,
            "fixedFeeRateCard": FixedFeeRateCard.from_dict(obj["fixedFeeRateCard"]) if obj.get("fixedFeeRateCard") is not None else None,
            "licenseRateCard": LicenseRateCard.from_dict(obj["licenseRateCard"]) if obj.get("licenseRateCard") is not None else None,
            "billingEntitlementRateCard": BillingEntitlementRateCard.from_dict(obj["billingEntitlementRateCard"]) if obj.get("billingEntitlementRateCard") is not None else None,
            "creditGrantRateCard": CreditGrantRateCard.from_dict(obj["creditGrantRateCard"]) if obj.get("creditGrantRateCard") is not None else None,
            "entitlementOverageRateCard": EntitlementOverageRateCard.from_dict(obj["entitlementOverageRateCard"]) if obj.get("entitlementOverageRateCard") is not None else None,
            "usages": obj.get("usages"),
            "fixedFeeRevenueSummary": FixedFeeRevenueSummary.from_dict(obj["fixedFeeRevenueSummary"]) if obj.get("fixedFeeRevenueSummary") is not None else None,
            "licenseRevenueSummary": [SlabRevenueSummary.from_dict(_item) for _item in obj["licenseRevenueSummary"]] if obj.get("licenseRevenueSummary") is not None else None,
            "billingEntitlementRevenueSummary": BillingEntitlementRevenueSummary.from_dict(obj["billingEntitlementRevenueSummary"]) if obj.get("billingEntitlementRevenueSummary") is not None else None,
            "creditGrantRevenueSummary": CreditGrantRevenueSummary.from_dict(obj["creditGrantRevenueSummary"]) if obj.get("creditGrantRevenueSummary") is not None else None,
            "entitlementOverageRevenueSummary": EntitlementOverageRevenueSummary.from_dict(obj["entitlementOverageRevenueSummary"]) if obj.get("entitlementOverageRevenueSummary") is not None else None,
            "slabRevenueSummaries": [SlabRevenueSummary.from_dict(_item) for _item in obj["slabRevenueSummaries"]] if obj.get("slabRevenueSummaries") is not None else None
        })
        return _obj


