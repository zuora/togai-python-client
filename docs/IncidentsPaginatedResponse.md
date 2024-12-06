# IncidentsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Incident]**](Incident.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.incidents_paginated_response import IncidentsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentsPaginatedResponse from a JSON string
incidents_paginated_response_instance = IncidentsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(IncidentsPaginatedResponse.to_json())

# convert the object into a dict
incidents_paginated_response_dict = incidents_paginated_response_instance.to_dict()
# create an instance of IncidentsPaginatedResponse from a dict
incidents_paginated_response_from_dict = IncidentsPaginatedResponse.from_dict(incidents_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


