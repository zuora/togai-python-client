# PurchaseListResponse

Represents a Purchase for List Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**price_plan_id** | **str** |  | [optional] 
**price_plan_name** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**rate_card_quantities** | **Dict[str, float]** |  | [optional] 
**price_plan_version** | **int** |  | [optional] 
**status** | [**PurchaseStatus**](PurchaseStatus.md) |  | 
**idempotency_key** | **str** |  | [optional] 
**purchase_plan** | [**PricePlanDetails**](PricePlanDetails.md) |  | [optional] 
**wallet_topup_details** | [**WalletTopupDetails**](WalletTopupDetails.md) |  | [optional] 
**price** | **float** |  | [optional] 
**invoice_currency** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**type** | [**PurchaseType**](PurchaseType.md) |  | 

## Example

```python
from togai_client.models.purchase_list_response import PurchaseListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseListResponse from a JSON string
purchase_list_response_instance = PurchaseListResponse.from_json(json)
# print the JSON string representation of the object
print(PurchaseListResponse.to_json())

# convert the object into a dict
purchase_list_response_dict = purchase_list_response_instance.to_dict()
# create an instance of PurchaseListResponse from a dict
purchase_list_response_from_dict = PurchaseListResponse.from_dict(purchase_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


