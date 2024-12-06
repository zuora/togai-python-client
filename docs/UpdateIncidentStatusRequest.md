# UpdateIncidentStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Incident Status | 

## Example

```python
from togai_client.models.update_incident_status_request import UpdateIncidentStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIncidentStatusRequest from a JSON string
update_incident_status_request_instance = UpdateIncidentStatusRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateIncidentStatusRequest.to_json())

# convert the object into a dict
update_incident_status_request_dict = update_incident_status_request_instance.to_dict()
# create an instance of UpdateIncidentStatusRequest from a dict
update_incident_status_request_from_dict = UpdateIncidentStatusRequest.from_dict(update_incident_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


