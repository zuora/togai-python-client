# Alert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Alert ID | 
**version** | **int** | Alert Version | 
**description** | **str** | Alert Description | [optional] 
**status** | [**AlertStatus**](AlertStatus.md) |  | 
**validity** | **int** | Validity of the alert in minutes, if null then alert will be valid forever | [optional] 
**alert_template_id** | **str** | Alert Template Id | 
**interval** | **int** | Interval | 
**entity_details** | **Dict[str, object]** |  | [optional] 
**owner_details** | **Dict[str, object]** |  | [optional] 
**parameters** | **Dict[str, object]** |  | [optional] 
**created_at** | **datetime** | Created At | 
**updated_at** | **datetime** | Updated At | [optional] 

## Example

```python
from togai_client.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


