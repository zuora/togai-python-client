# ExternalPaymentReference

external payment reference object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_name** | **str** |  | 
**source_type** | **str** |  | 
**transaction_number** | **str** | Check number or Card transaction number | 
**description** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from togai_client.models.external_payment_reference import ExternalPaymentReference

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalPaymentReference from a JSON string
external_payment_reference_instance = ExternalPaymentReference.from_json(json)
# print the JSON string representation of the object
print(ExternalPaymentReference.to_json())

# convert the object into a dict
external_payment_reference_dict = external_payment_reference_instance.to_dict()
# create an instance of ExternalPaymentReference from a dict
external_payment_reference_from_dict = ExternalPaymentReference.from_dict(external_payment_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


