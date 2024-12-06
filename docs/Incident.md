# Incident


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Incident ID | 
**alert_id** | **str** | Alert ID | 
**alert_version** | **int** | Alert Version | 
**alert_template_id** | **str** | Alert Template Id | 
**valid_until** | **datetime** |  | [optional] 
**report_data** | **Dict[str, object]** |  | [optional] 
**status** | **str** | Incident Status | 
**last_checked_at** | **datetime** | Last Checked At | [optional] 
**created_at** | **datetime** | Created At | 
**updated_at** | **datetime** | Updated At | [optional] 

## Example

```python
from togai_client.models.incident import Incident

# TODO update the JSON string below
json = "{}"
# create an instance of Incident from a JSON string
incident_instance = Incident.from_json(json)
# print the JSON string representation of the object
print(Incident.to_json())

# convert the object into a dict
incident_dict = incident_instance.to_dict()
# create an instance of Incident from a dict
incident_from_dict = Incident.from_dict(incident_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


