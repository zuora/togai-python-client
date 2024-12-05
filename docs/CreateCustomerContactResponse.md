# CreateCustomerContactResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**preferred_username** | **str** |  | [optional] 
**name** | **str** |  | 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**login_access** | **bool** |  | 
**created_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**verified** | **bool** |  | 

## Example

```python
from togai_client.models.create_customer_contact_response import CreateCustomerContactResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerContactResponse from a JSON string
create_customer_contact_response_instance = CreateCustomerContactResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerContactResponse.to_json())

# convert the object into a dict
create_customer_contact_response_dict = create_customer_contact_response_instance.to_dict()
# create an instance of CreateCustomerContactResponse from a dict
create_customer_contact_response_from_dict = CreateCustomerContactResponse.from_dict(create_customer_contact_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


