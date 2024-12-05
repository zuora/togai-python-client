# FeatureConfig

Feature configuration object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effective_from** | **str** |  | [optional] 
**effective_until** | **str** |  | 
**feature_credit_limit** | **float** |  | 

## Example

```python
from togai_client.models.feature_config import FeatureConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FeatureConfig from a JSON string
feature_config_instance = FeatureConfig.from_json(json)
# print the JSON string representation of the object
print(FeatureConfig.to_json())

# convert the object into a dict
feature_config_dict = feature_config_instance.to_dict()
# create an instance of FeatureConfig from a dict
feature_config_from_dict = FeatureConfig.from_dict(feature_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


