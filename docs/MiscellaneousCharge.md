# MiscellaneousCharge

Miscellaneous charges are the charges that can be added to the invoice. A charge must either have rate and quantity or value. In case of rate and quantity, the value must not be provided as it is automatically calculated as (rate * quantity).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the miscellaneous charge | 
**rate** | **float** | Rate of the charge | [optional] 
**quantity** | **float** | Quantity of the charge | [optional] 
**value** | **str** | Value of the charge Possible values: 1. Fixed number [Example: 10] 2. Json Logic [Example: {\&quot;*\&quot;: [{\&quot;var\&quot;: \&quot;um.lineitem.id\&quot;}, 0.1]}]    You can use all line item ids as variables in the json logic  | [optional] 
**consider_for_revenue** | **bool** | Specifies whether to consider this miscellaneous charge for revenue or not | [optional] [default to False]

## Example

```python
from togai_client.models.miscellaneous_charge import MiscellaneousCharge

# TODO update the JSON string below
json = "{}"
# create an instance of MiscellaneousCharge from a JSON string
miscellaneous_charge_instance = MiscellaneousCharge.from_json(json)
# print the JSON string representation of the object
print(MiscellaneousCharge.to_json())

# convert the object into a dict
miscellaneous_charge_dict = miscellaneous_charge_instance.to_dict()
# create an instance of MiscellaneousCharge from a dict
miscellaneous_charge_from_dict = MiscellaneousCharge.from_dict(miscellaneous_charge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


