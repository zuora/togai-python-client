# ListPaymentResponse

List payments response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Payment]**](Payment.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.list_payment_response import ListPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPaymentResponse from a JSON string
list_payment_response_instance = ListPaymentResponse.from_json(json)
# print the JSON string representation of the object
print(ListPaymentResponse.to_json())

# convert the object into a dict
list_payment_response_dict = list_payment_response_instance.to_dict()
# create an instance of ListPaymentResponse from a dict
list_payment_response_from_dict = ListPaymentResponse.from_dict(list_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


