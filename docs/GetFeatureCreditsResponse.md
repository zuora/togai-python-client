# GetFeatureCreditsResponse

Get feature credits response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**feature_id** | **str** |  | 
**granted** | **float** |  | 
**balance** | **float** |  | 
**overage_limit** | **float** |  | [optional] 
**used_overage** | **float** |  | 

## Example

```python
from togai_client.models.get_feature_credits_response import GetFeatureCreditsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFeatureCreditsResponse from a JSON string
get_feature_credits_response_instance = GetFeatureCreditsResponse.from_json(json)
# print the JSON string representation of the object
print(GetFeatureCreditsResponse.to_json())

# convert the object into a dict
get_feature_credits_response_dict = get_feature_credits_response_instance.to_dict()
# create an instance of GetFeatureCreditsResponse from a dict
get_feature_credits_response_from_dict = GetFeatureCreditsResponse.from_dict(get_feature_credits_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


