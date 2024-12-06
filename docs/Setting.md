# Setting

Represents a setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **str** |  | 
**entity_type** | **str** |  | 
**entity_id** | **str** |  | 
**namespace** | **str** |  | 
**name** | **str** |  | 
**data_type** | [**SettingDataType**](SettingDataType.md) |  | 

## Example

```python
from togai_client.models.setting import Setting

# TODO update the JSON string below
json = "{}"
# create an instance of Setting from a JSON string
setting_instance = Setting.from_json(json)
# print the JSON string representation of the object
print(Setting.to_json())

# convert the object into a dict
setting_dict = setting_instance.to_dict()
# create an instance of Setting from a dict
setting_from_dict = Setting.from_dict(setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


