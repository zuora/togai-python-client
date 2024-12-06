# GetLicenseUpdatesResponse

Get license updates response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LicenseUpdateResponse]**](LicenseUpdateResponse.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.get_license_updates_response import GetLicenseUpdatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLicenseUpdatesResponse from a JSON string
get_license_updates_response_instance = GetLicenseUpdatesResponse.from_json(json)
# print the JSON string representation of the object
print(GetLicenseUpdatesResponse.to_json())

# convert the object into a dict
get_license_updates_response_dict = get_license_updates_response_instance.to_dict()
# create an instance of GetLicenseUpdatesResponse from a dict
get_license_updates_response_from_dict = GetLicenseUpdatesResponse.from_dict(get_license_updates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


