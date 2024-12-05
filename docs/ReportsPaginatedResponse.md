# ReportsPaginatedResponse

Represents a list response for reports

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Report]**](Report.md) |  | [optional] 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.reports_paginated_response import ReportsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportsPaginatedResponse from a JSON string
reports_paginated_response_instance = ReportsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(ReportsPaginatedResponse.to_json())

# convert the object into a dict
reports_paginated_response_dict = reports_paginated_response_instance.to_dict()
# create an instance of ReportsPaginatedResponse from a dict
reports_paginated_response_from_dict = ReportsPaginatedResponse.from_dict(reports_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


