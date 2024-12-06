# SlabRate

Represents a rate for a slab

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | 
**rate** | **float** |  | 
**slab_rate_config** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.slab_rate import SlabRate

# TODO update the JSON string below
json = "{}"
# create an instance of SlabRate from a JSON string
slab_rate_instance = SlabRate.from_json(json)
# print the JSON string representation of the object
print(SlabRate.to_json())

# convert the object into a dict
slab_rate_dict = slab_rate_instance.to_dict()
# create an instance of SlabRate from a dict
slab_rate_from_dict = SlabRate.from_dict(slab_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


