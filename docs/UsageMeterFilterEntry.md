# UsageMeterFilterEntry

Filter entry with field and value

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from togai_client.models.usage_meter_filter_entry import UsageMeterFilterEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UsageMeterFilterEntry from a JSON string
usage_meter_filter_entry_instance = UsageMeterFilterEntry.from_json(json)
# print the JSON string representation of the object
print(UsageMeterFilterEntry.to_json())

# convert the object into a dict
usage_meter_filter_entry_dict = usage_meter_filter_entry_instance.to_dict()
# create an instance of UsageMeterFilterEntry from a dict
usage_meter_filter_entry_from_dict = UsageMeterFilterEntry.from_dict(usage_meter_filter_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


