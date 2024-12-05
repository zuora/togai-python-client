# UsageLookupRange

Start and end dates of usage lookup if usage mode is LOOKUP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **datetime** |  | 
**end** | **datetime** |  | 

## Example

```python
from togai_client.models.usage_lookup_range import UsageLookupRange

# TODO update the JSON string below
json = "{}"
# create an instance of UsageLookupRange from a JSON string
usage_lookup_range_instance = UsageLookupRange.from_json(json)
# print the JSON string representation of the object
print(UsageLookupRange.to_json())

# convert the object into a dict
usage_lookup_range_dict = usage_lookup_range_instance.to_dict()
# create an instance of UsageLookupRange from a dict
usage_lookup_range_from_dict = UsageLookupRange.from_dict(usage_lookup_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


