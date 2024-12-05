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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from togai_client.models.create_account_alias_request import CreateAccountAliasRequest
from typing import Optional, Set
from typing_extensions import Self

class AddAccountAliasesRequest(BaseModel):
    """
    Payload to add aliases from account
    """ # noqa: E501
    aliases: Optional[Annotated[List[Annotated[str, Field(min_length=3, strict=True, max_length=50)]], Field(min_length=1, max_length=10)]] = Field(default=None, description="List of aliases to add")
    account_aliases: Optional[Annotated[List[CreateAccountAliasRequest], Field(min_length=1, max_length=10)]] = Field(default=None, description="List of account aliases to add", alias="accountAliases")
    __properties: ClassVar[List[str]] = ["aliases", "accountAliases"]

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
        """Create an instance of AddAccountAliasesRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in account_aliases (list)
        _items = []
        if self.account_aliases:
            for _item_account_aliases in self.account_aliases:
                if _item_account_aliases:
                    _items.append(_item_account_aliases.to_dict())
            _dict['accountAliases'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddAccountAliasesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aliases": obj.get("aliases"),
            "accountAliases": [CreateAccountAliasRequest.from_dict(_item) for _item in obj["accountAliases"]] if obj.get("accountAliases") is not None else None
        })
        return _obj

