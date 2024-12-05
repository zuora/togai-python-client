# UpdateCustomerRequest

Payload to update customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Customer | [optional] 
**primary_email** | **str** | Primary email of the customer | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 

## Example

```python
from togai_client.models.update_customer_request import UpdateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerRequest from a JSON string
update_customer_request_instance = UpdateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomerRequest.to_json())

# convert the object into a dict
update_customer_request_dict = update_customer_request_instance.to_dict()
# create an instance of UpdateCustomerRequest from a dict
update_customer_request_from_dict = UpdateCustomerRequest.from_dict(update_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


