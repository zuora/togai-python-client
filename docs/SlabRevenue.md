# SlabRevenue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | 
**usage** | **float** |  | 
**revenue** | **float** |  | 

## Example

```python
from togai_client.models.slab_revenue import SlabRevenue

# TODO update the JSON string below
json = "{}"
# create an instance of SlabRevenue from a JSON string
slab_revenue_instance = SlabRevenue.from_json(json)
# print the JSON string representation of the object
print(SlabRevenue.to_json())

# convert the object into a dict
slab_revenue_dict = slab_revenue_instance.to_dict()
# create an instance of SlabRevenue from a dict
slab_revenue_from_dict = SlabRevenue.from_dict(slab_revenue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


