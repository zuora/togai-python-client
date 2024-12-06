# UpdateFeatureCreditsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_until** | **datetime** | Expiry date-time for a feature credits entry | [optional] 
**granted** | **float** | Granted units for a feature credits entry | [optional] 

## Example

```python
from togai_client.models.update_feature_credits_request import UpdateFeatureCreditsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFeatureCreditsRequest from a JSON string
update_feature_credits_request_instance = UpdateFeatureCreditsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFeatureCreditsRequest.to_json())

# convert the object into a dict
update_feature_credits_request_dict = update_feature_credits_request_instance.to_dict()
# create an instance of UpdateFeatureCreditsRequest from a dict
update_feature_credits_request_from_dict = UpdateFeatureCreditsRequest.from_dict(update_feature_credits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


