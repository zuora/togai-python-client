# CreateCustomerContactRequest

Payload to create a contact for a customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preferred_username** | **str** |  | [optional] 
**name** | **str** |  | 
**password** | **str** |  | [optional] 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**login_access** | **bool** |  | [optional] [default to False]

## Example

```python
from togai_client.models.create_customer_contact_request import CreateCustomerContactRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerContactRequest from a JSON string
create_customer_contact_request_instance = CreateCustomerContactRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerContactRequest.to_json())

# convert the object into a dict
create_customer_contact_request_dict = create_customer_contact_request_instance.to_dict()
# create an instance of CreateCustomerContactRequest from a dict
create_customer_contact_request_from_dict = CreateCustomerContactRequest.from_dict(create_customer_contact_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


