# AlertTemplatesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AlertTemplate]**](AlertTemplate.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.alert_templates_paginated_response import AlertTemplatesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTemplatesPaginatedResponse from a JSON string
alert_templates_paginated_response_instance = AlertTemplatesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(AlertTemplatesPaginatedResponse.to_json())

# convert the object into a dict
alert_templates_paginated_response_dict = alert_templates_paginated_response_instance.to_dict()
# create an instance of AlertTemplatesPaginatedResponse from a dict
alert_templates_paginated_response_from_dict = AlertTemplatesPaginatedResponse.from_dict(alert_templates_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


