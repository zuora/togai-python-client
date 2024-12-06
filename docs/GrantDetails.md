# GrantDetails

Grant details of Credit Grant Rate Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** |  | 
**expiry_type** | [**ExpiryType**](ExpiryType.md) |  | 
**expiry_duration** | **str** |  | [optional] 
**applicable_entity_ids** | **List[str]** |  | [optional] 

## Example

```python
from togai_client.models.grant_details import GrantDetails

# TODO update the JSON string below
json = "{}"
# create an instance of GrantDetails from a JSON string
grant_details_instance = GrantDetails.from_json(json)
# print the JSON string representation of the object
print(GrantDetails.to_json())

# convert the object into a dict
grant_details_dict = grant_details_instance.to_dict()
# create an instance of GrantDetails from a dict
grant_details_from_dict = GrantDetails.from_dict(grant_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


