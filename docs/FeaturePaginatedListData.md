# FeaturePaginatedListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FeatureListResponse]**](FeatureListResponse.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.feature_paginated_list_data import FeaturePaginatedListData

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePaginatedListData from a JSON string
feature_paginated_list_data_instance = FeaturePaginatedListData.from_json(json)
# print the JSON string representation of the object
print(FeaturePaginatedListData.to_json())

# convert the object into a dict
feature_paginated_list_data_dict = feature_paginated_list_data_instance.to_dict()
# create an instance of FeaturePaginatedListData from a dict
feature_paginated_list_data_from_dict = FeaturePaginatedListData.from_dict(feature_paginated_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


