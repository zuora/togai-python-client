# coding: utf-8

"""
    Togai Apis

    APIs for Togai App

    The version of the OpenAPI document: 1.0
    Contact: engg@togai.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from togai_client.models.pricing_rules_paginated_response import PricingRulesPaginatedResponse

from togai_client.api_client import ApiClient, RequestSerialized
from togai_client.api_response import ApiResponse
from togai_client.rest import RESTResponseType


class PricingRulesApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def list_pricing_rules_by_schedule_id(
        self,
        price_plan_id: Annotated[str, Field(strict=True, max_length=50)],
        pricing_schedule_id: Annotated[str, Field(strict=True, max_length=50)],
        invoice_timing: Annotated[Optional[StrictStr], Field(description="Optional field to filter pricing rules based on invoice timing")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> PricingRulesPaginatedResponse:
        """(DEPRECATED) List pricing rules by price plan id and pricing schedule id

        Get a list of pricing rules using price plan id and pricing schedule id

        :param price_plan_id: (required)
        :type price_plan_id: str
        :param pricing_schedule_id: (required)
        :type pricing_schedule_id: str
        :param invoice_timing: Optional field to filter pricing rules based on invoice timing
        :type invoice_timing: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_pricing_rules_by_schedule_id_serialize(
            price_plan_id=price_plan_id,
            pricing_schedule_id=pricing_schedule_id,
            invoice_timing=invoice_timing,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PricingRulesPaginatedResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_pricing_rules_by_schedule_id_with_http_info(
        self,
        price_plan_id: Annotated[str, Field(strict=True, max_length=50)],
        pricing_schedule_id: Annotated[str, Field(strict=True, max_length=50)],
        invoice_timing: Annotated[Optional[StrictStr], Field(description="Optional field to filter pricing rules based on invoice timing")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[PricingRulesPaginatedResponse]:
        """(DEPRECATED) List pricing rules by price plan id and pricing schedule id

        Get a list of pricing rules using price plan id and pricing schedule id

        :param price_plan_id: (required)
        :type price_plan_id: str
        :param pricing_schedule_id: (required)
        :type pricing_schedule_id: str
        :param invoice_timing: Optional field to filter pricing rules based on invoice timing
        :type invoice_timing: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_pricing_rules_by_schedule_id_serialize(
            price_plan_id=price_plan_id,
            pricing_schedule_id=pricing_schedule_id,
            invoice_timing=invoice_timing,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PricingRulesPaginatedResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_pricing_rules_by_schedule_id_without_preload_content(
        self,
        price_plan_id: Annotated[str, Field(strict=True, max_length=50)],
        pricing_schedule_id: Annotated[str, Field(strict=True, max_length=50)],
        invoice_timing: Annotated[Optional[StrictStr], Field(description="Optional field to filter pricing rules based on invoice timing")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """(DEPRECATED) List pricing rules by price plan id and pricing schedule id

        Get a list of pricing rules using price plan id and pricing schedule id

        :param price_plan_id: (required)
        :type price_plan_id: str
        :param pricing_schedule_id: (required)
        :type pricing_schedule_id: str
        :param invoice_timing: Optional field to filter pricing rules based on invoice timing
        :type invoice_timing: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_pricing_rules_by_schedule_id_serialize(
            price_plan_id=price_plan_id,
            pricing_schedule_id=pricing_schedule_id,
            invoice_timing=invoice_timing,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "PricingRulesPaginatedResponse",
            '400': "ErrorResponse",
            '401': "ErrorResponse",
            '403': "ErrorResponse",
            '404': "ErrorResponse",
            '429': "ErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_pricing_rules_by_schedule_id_serialize(
        self,
        price_plan_id,
        pricing_schedule_id,
        invoice_timing,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if price_plan_id is not None:
            _path_params['price_plan_id'] = price_plan_id
        if pricing_schedule_id is not None:
            _path_params['pricing_schedule_id'] = pricing_schedule_id
        # process the query parameters
        if invoice_timing is not None:
            
            _query_params.append(('invoice_timing', invoice_timing))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'bearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/price_plans/{price_plan_id}/pricing_schedules/{pricing_schedule_id}/pricing_rules',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


