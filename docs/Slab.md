# Slab

Represents a pricing priceType (rates + slabs) for usage price plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | 
**start_after** | **float** |  | 
**price_type** | [**PriceType**](PriceType.md) |  | 
**slab_config** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.slab import Slab

# TODO update the JSON string below
json = "{}"
# create an instance of Slab from a JSON string
slab_instance = Slab.from_json(json)
# print the JSON string representation of the object
print(Slab.to_json())

# convert the object into a dict
slab_dict = slab_instance.to_dict()
# create an instance of Slab from a dict
slab_from_dict = Slab.from_dict(slab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


