# CreateCustomerRequest

Payload to create customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Customer identifier | 
**name** | **str** | Name of the Customer | 
**primary_email** | **str** | Primary email of the customer | 
**address** | [**Address**](Address.md) |  | 
**settings** | [**List[CreateEntitySetting]**](CreateEntitySetting.md) |  | [optional] 
**account** | [**CreateAccountRequestWithoutCustomerId**](CreateAccountRequestWithoutCustomerId.md) |  | [optional] 

## Example

```python
from togai_client.models.create_customer_request import CreateCustomerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerRequest from a JSON string
create_customer_request_instance = CreateCustomerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerRequest.to_json())

# convert the object into a dict
create_customer_request_dict = create_customer_request_instance.to_dict()
# create an instance of CreateCustomerRequest from a dict
create_customer_request_from_dict = CreateCustomerRequest.from_dict(create_customer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


