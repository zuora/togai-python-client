# FeatureCreditEntry

Get feature credits response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**source** | **str** | Source of the feature credit | 
**status** | **str** | Status of the feature credit entry | 
**effective_from** | **datetime** |  | 
**effective_until** | **datetime** |  | 
**granted** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**used** | **float** |  | 

## Example

```python
from togai_client.models.feature_credit_entry import FeatureCreditEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureCreditEntry from a JSON string
feature_credit_entry_instance = FeatureCreditEntry.from_json(json)
# print the JSON string representation of the object
print(FeatureCreditEntry.to_json())

# convert the object into a dict
feature_credit_entry_dict = feature_credit_entry_instance.to_dict()
# create an instance of FeatureCreditEntry from a dict
feature_credit_entry_from_dict = FeatureCreditEntry.from_dict(feature_credit_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


