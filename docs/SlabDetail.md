# SlabDetail

The details of a slab

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_after** | **float** |  | 
**price_type** | [**PriceType**](PriceType.md) |  | 
**slab_config** | **Dict[str, str]** |  | [optional] 
**rate** | **float** |  | 
**slab_rate_config** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.slab_detail import SlabDetail

# TODO update the JSON string below
json = "{}"
# create an instance of SlabDetail from a JSON string
slab_detail_instance = SlabDetail.from_json(json)
# print the JSON string representation of the object
print(SlabDetail.to_json())

# convert the object into a dict
slab_detail_dict = slab_detail_instance.to_dict()
# create an instance of SlabDetail from a dict
slab_detail_from_dict = SlabDetail.from_dict(slab_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


