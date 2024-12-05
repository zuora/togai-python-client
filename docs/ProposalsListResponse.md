# ProposalsListResponse

Represents a Proposal for List Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**price_plan_id** | **str** |  | [optional] 
**price_plan_name** | **str** |  | [optional] 
**price_plan_version** | **int** |  | [optional] 
**status** | [**PurchaseStatus**](PurchaseStatus.md) |  | 
**wallet_topup_details** | [**WalletTopupDetails**](WalletTopupDetails.md) |  | [optional] 
**idempotency_key** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**expiry_date** | **datetime** |  | [optional] 
**payment_mode** | **str** |  | 
**type** | [**PurchaseType**](PurchaseType.md) |  | 

## Example

```python
from togai_client.models.proposals_list_response import ProposalsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProposalsListResponse from a JSON string
proposals_list_response_instance = ProposalsListResponse.from_json(json)
# print the JSON string representation of the object
print(ProposalsListResponse.to_json())

# convert the object into a dict
proposals_list_response_dict = proposals_list_response_instance.to_dict()
# create an instance of ProposalsListResponse from a dict
proposals_list_response_from_dict = ProposalsListResponse.from_dict(proposals_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


