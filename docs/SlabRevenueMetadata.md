# SlabRevenueMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_rate_applied** | **bool** |  | [optional] 
**maximum_rate_applied** | **bool** |  | [optional] 
**package_quantity** | **int** |  | [optional] 

## Example

```python
from togai_client.models.slab_revenue_metadata import SlabRevenueMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SlabRevenueMetadata from a JSON string
slab_revenue_metadata_instance = SlabRevenueMetadata.from_json(json)
# print the JSON string representation of the object
print(SlabRevenueMetadata.to_json())

# convert the object into a dict
slab_revenue_metadata_dict = slab_revenue_metadata_instance.to_dict()
# create an instance of SlabRevenueMetadata from a dict
slab_revenue_metadata_from_dict = SlabRevenueMetadata.from_dict(slab_revenue_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


