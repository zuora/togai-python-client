# AlertTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Alert Template ID | 
**name** | **str** | Alert Template Name | 
**description** | **str** | Alert Template Description | [optional] 
**interval** | **int** | Cron Interval | 
**entity_schema** | **str** | Entity Schema | [optional] 
**entity_type** | **str** | Entity Type | [optional] 
**owner_schema** | **str** | Owner Schema | [optional] 
**owner_type** | **str** | Owner Type | [optional] 
**parameters_schema** | **str** | Parameters Schema | [optional] 
**created_at** | **datetime** | Created At | 
**updated_at** | **datetime** | Updated At | [optional] 

## Example

```python
from togai_client.models.alert_template import AlertTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTemplate from a JSON string
alert_template_instance = AlertTemplate.from_json(json)
# print the JSON string representation of the object
print(AlertTemplate.to_json())

# convert the object into a dict
alert_template_dict = alert_template_instance.to_dict()
# create an instance of AlertTemplate from a dict
alert_template_from_dict = AlertTemplate.from_dict(alert_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


