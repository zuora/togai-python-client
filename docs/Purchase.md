# Purchase

Represents a Purchase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**account_id** | **str** |  | 
**price_plan_id** | **str** | Id of the price plan, Required for ENTITLEMENT_GRANT, ASSOCIATION purchase | [optional] 
**quantity** | **int** |  | [optional] 
**rate_card_quantities** | **Dict[str, float]** |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**price_plan_version** | **int** |  | [optional] 
**purchase_plan_override** | [**PricePlanDetailsOverride**](PricePlanDetailsOverride.md) |  | [optional] 
**association_override** | [**CreatePricePlanDetailsOverride**](CreatePricePlanDetailsOverride.md) |  | [optional] 
**wallet_topup_details** | [**WalletTopupDetails**](WalletTopupDetails.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | [optional] 
**effective_from** | **date** |  | [optional] 
**effective_until** | **date** |  | [optional] 
**expiry_date** | **datetime** |  | [optional] 
**price** | **float** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_currency** | **str** |  | [optional] 
**status** | [**PurchaseStatus**](PurchaseStatus.md) |  | 
**type** | [**PurchaseType**](PurchaseType.md) |  | 
**comment** | **str** |  | [optional] 

## Example

```python
from togai_client.models.purchase import Purchase

# TODO update the JSON string below
json = "{}"
# create an instance of Purchase from a JSON string
purchase_instance = Purchase.from_json(json)
# print the JSON string representation of the object
print(Purchase.to_json())

# convert the object into a dict
purchase_dict = purchase_instance.to_dict()
# create an instance of Purchase from a dict
purchase_from_dict = Purchase.from_dict(purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


