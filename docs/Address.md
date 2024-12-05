# Address

billing address of the customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** | Contact number | [optional] 
**line1** | **str** | Address line 1 (eg. Street, PO Box, Company Name) | [optional] 
**line2** | **str** | Address line 2 (eg. apartment, suite, unit or building) | [optional] 
**postal_code** | **str** | ZIP or postal code | [optional] 
**city** | **str** | City, district, suburb, town or village | [optional] 
**state** | **str** | State, county, province or region | [optional] 
**country** | **str** | Two letter country code [ISO-3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | [optional] 

## Example

```python
from togai_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


