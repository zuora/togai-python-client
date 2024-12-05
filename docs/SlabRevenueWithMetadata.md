# SlabRevenueWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | 
**usage** | **float** |  | 
**revenue** | **float** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.slab_revenue_with_metadata import SlabRevenueWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SlabRevenueWithMetadata from a JSON string
slab_revenue_with_metadata_instance = SlabRevenueWithMetadata.from_json(json)
# print the JSON string representation of the object
print(SlabRevenueWithMetadata.to_json())

# convert the object into a dict
slab_revenue_with_metadata_dict = slab_revenue_with_metadata_instance.to_dict()
# create an instance of SlabRevenueWithMetadata from a dict
slab_revenue_with_metadata_from_dict = SlabRevenueWithMetadata.from_dict(slab_revenue_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


