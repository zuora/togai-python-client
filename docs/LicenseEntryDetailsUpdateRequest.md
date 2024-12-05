# LicenseEntryDetailsUpdateRequest

License Entry Details update request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The account id for which the license is being updated | 
**effective_from** | **datetime** | The effective from date of the license entry | 
**metadata** | **Dict[str, str]** |  | 

## Example

```python
from togai_client.models.license_entry_details_update_request import LicenseEntryDetailsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseEntryDetailsUpdateRequest from a JSON string
license_entry_details_update_request_instance = LicenseEntryDetailsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(LicenseEntryDetailsUpdateRequest.to_json())

# convert the object into a dict
license_entry_details_update_request_dict = license_entry_details_update_request_instance.to_dict()
# create an instance of LicenseEntryDetailsUpdateRequest from a dict
license_entry_details_update_request_from_dict = LicenseEntryDetailsUpdateRequest.from_dict(license_entry_details_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


