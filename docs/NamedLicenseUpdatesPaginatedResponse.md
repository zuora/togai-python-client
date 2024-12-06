# NamedLicenseUpdatesPaginatedResponse

Named License updates paginated response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[NamedLicenseUpdate]**](NamedLicenseUpdate.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.named_license_updates_paginated_response import NamedLicenseUpdatesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NamedLicenseUpdatesPaginatedResponse from a JSON string
named_license_updates_paginated_response_instance = NamedLicenseUpdatesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(NamedLicenseUpdatesPaginatedResponse.to_json())

# convert the object into a dict
named_license_updates_paginated_response_dict = named_license_updates_paginated_response_instance.to_dict()
# create an instance of NamedLicenseUpdatesPaginatedResponse from a dict
named_license_updates_paginated_response_from_dict = NamedLicenseUpdatesPaginatedResponse.from_dict(named_license_updates_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


