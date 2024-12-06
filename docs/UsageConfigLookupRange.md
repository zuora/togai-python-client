# UsageConfigLookupRange

Range of usage to be looked up, this will be considered if mode is LOOKUP_RANGE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | 
**end** | **datetime** |  | 
**account_id** | **str** |  | 

## Example

```python
from togai_client.models.usage_config_lookup_range import UsageConfigLookupRange

# TODO update the JSON string below
json = "{}"
# create an instance of UsageConfigLookupRange from a JSON string
usage_config_lookup_range_instance = UsageConfigLookupRange.from_json(json)
# print the JSON string representation of the object
print(UsageConfigLookupRange.to_json())

# convert the object into a dict
usage_config_lookup_range_dict = usage_config_lookup_range_instance.to_dict()
# create an instance of UsageConfigLookupRange from a dict
usage_config_lookup_range_from_dict = UsageConfigLookupRange.from_dict(usage_config_lookup_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


