# Attribute

Metric to be recorded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the event attribute | 
**value** | **str** | Value of the event attribute | 
**unit** | **str** | Unit with which the attribute value was measured. Natively supported units - \&quot;Meters, Miles, Kilometers, Grams, Kilograms, ounces, Pounds, Minutes, Hours, Seconds, Milliseconds, Microseconds, None\&quot;. Clients are free to add any other custom units. | [optional] 

## Example

```python
from togai_client.models.attribute import Attribute

# TODO update the JSON string below
json = "{}"
# create an instance of Attribute from a JSON string
attribute_instance = Attribute.from_json(json)
# print the JSON string representation of the object
print(Attribute.to_json())

# convert the object into a dict
attribute_dict = attribute_instance.to_dict()
# create an instance of Attribute from a dict
attribute_from_dict = Attribute.from_dict(attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


