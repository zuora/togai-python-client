# UpdateAlertRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**status** | [**AlertStatus**](AlertStatus.md) |  | [optional] 
**interval** | **int** |  | [optional] 
**validity** | **int** |  | [optional] 
**parameters** | **Dict[str, object]** |  | [optional] 

## Example

```python
from togai_client.models.update_alert_request import UpdateAlertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAlertRequest from a JSON string
update_alert_request_instance = UpdateAlertRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateAlertRequest.to_json())

# convert the object into a dict
update_alert_request_dict = update_alert_request_instance.to_dict()
# create an instance of UpdateAlertRequest from a dict
update_alert_request_from_dict = UpdateAlertRequest.from_dict(update_alert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


