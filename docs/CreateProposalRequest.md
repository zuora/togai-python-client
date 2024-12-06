# CreateProposalRequest


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
**type** | [**PurchaseType**](PurchaseType.md) |  | 
**payment_mode** | **str** |  | 

## Example

```python
from togai_client.models.create_proposal_request import CreateProposalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProposalRequest from a JSON string
create_proposal_request_instance = CreateProposalRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProposalRequest.to_json())

# convert the object into a dict
create_proposal_request_dict = create_proposal_request_instance.to_dict()
# create an instance of CreateProposalRequest from a dict
create_proposal_request_from_dict = CreateProposalRequest.from_dict(create_proposal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


