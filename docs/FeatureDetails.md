# FeatureDetails

details of feature associated with event schema with attribute name

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **str** |  | 
**attribute_name** | **str** |  | 

## Example

```python
from togai_client.models.feature_details import FeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureDetails from a JSON string
feature_details_instance = FeatureDetails.from_json(json)
# print the JSON string representation of the object
print(FeatureDetails.to_json())

# convert the object into a dict
feature_details_dict = feature_details_instance.to_dict()
# create an instance of FeatureDetails from a dict
feature_details_from_dict = FeatureDetails.from_dict(feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


