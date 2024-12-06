# GetFeatureCreditEntriesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FeatureCreditEntry]**](FeatureCreditEntry.md) |  | [optional] 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.get_feature_credit_entries_paginated_response import GetFeatureCreditEntriesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeatureCreditEntriesPaginatedResponse from a JSON string
get_feature_credit_entries_paginated_response_instance = GetFeatureCreditEntriesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeatureCreditEntriesPaginatedResponse.to_json())

# convert the object into a dict
get_feature_credit_entries_paginated_response_dict = get_feature_credit_entries_paginated_response_instance.to_dict()
# create an instance of GetFeatureCreditEntriesPaginatedResponse from a dict
get_feature_credit_entries_paginated_response_from_dict = GetFeatureCreditEntriesPaginatedResponse.from_dict(get_feature_credit_entries_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


