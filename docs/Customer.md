# Customer

Structure of customer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier of customer | 
**togai_customer_id** | **str** | Unique identifier of customer | 
**name** | **str** | Name of the Customer | 
**primary_email** | **str** | Primary email of the customer | 
**billing_address** | **str** | billing address of the customer | 
**address** | [**Address**](Address.md) |  | 
**status** | **str** | Status of the customer | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from togai_client.models.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


