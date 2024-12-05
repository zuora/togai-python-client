# CreateEntitySetting

Represents a setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **str** |  | 
**namespace** | **str** |  | 
**name** | **str** |  | 
**data_type** | [**SettingDataType**](SettingDataType.md) |  | 

## Example

```python
from togai_client.models.create_entity_setting import CreateEntitySetting

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEntitySetting from a JSON string
create_entity_setting_instance = CreateEntitySetting.from_json(json)
# print the JSON string representation of the object
print(CreateEntitySetting.to_json())

# convert the object into a dict
create_entity_setting_dict = create_entity_setting_instance.to_dict()
# create an instance of CreateEntitySetting from a dict
create_entity_setting_from_dict = CreateEntitySetting.from_dict(create_entity_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


