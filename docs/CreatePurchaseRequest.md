# CreatePurchaseRequest

Create a purchase for an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_plan_id** | **str** | Id of the price plan, Required for ENTITLEMENT_GRANT, ASSOCIATION purchase | [optional] 
**quantity** | **int** |  | [optional] 
**rate_card_quantities** | **Dict[str, float]** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**purchase_plan_override** | [**PurchasePlanOverride**](PurchasePlanOverride.md) |  | [optional] 
**association_override** | [**CreatePricePlanDetailsOverride**](CreatePricePlanDetailsOverride.md) |  | [optional] 
**wallet_topup_details** | [**WalletTopupDetails**](WalletTopupDetails.md) |  | [optional] 
**effective_from** | **date** |  | [optional] 
**effective_until** | **date** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**type** | [**PurchaseType**](PurchaseType.md) |  | [optional] 

## Example

```python
from togai_client.models.create_purchase_request import CreatePurchaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePurchaseRequest from a JSON string
create_purchase_request_instance = CreatePurchaseRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePurchaseRequest.to_json())

# convert the object into a dict
create_purchase_request_dict = create_purchase_request_instance.to_dict()
# create an instance of CreatePurchaseRequest from a dict
create_purchase_request_from_dict = CreatePurchaseRequest.from_dict(create_purchase_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


