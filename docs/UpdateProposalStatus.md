# UpdateProposalStatus

Approve or decline a proposal of a billing plan for an account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from togai_client.models.update_proposal_status import UpdateProposalStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProposalStatus from a JSON string
update_proposal_status_instance = UpdateProposalStatus.from_json(json)
# print the JSON string representation of the object
print(UpdateProposalStatus.to_json())

# convert the object into a dict
update_proposal_status_dict = update_proposal_status_instance.to_dict()
# create an instance of UpdateProposalStatus from a dict
update_proposal_status_from_dict = UpdateProposalStatus.from_dict(update_proposal_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


