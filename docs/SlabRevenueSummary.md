# SlabRevenueSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **int** |  | 
**usage** | **float** |  | 
**revenue** | **float** |  | 
**metadata** | [**SlabRevenueMetadata**](SlabRevenueMetadata.md) |  | [optional] 

## Example

```python
from togai_client.models.slab_revenue_summary import SlabRevenueSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SlabRevenueSummary from a JSON string
slab_revenue_summary_instance = SlabRevenueSummary.from_json(json)
# print the JSON string representation of the object
print(SlabRevenueSummary.to_json())

# convert the object into a dict
slab_revenue_summary_dict = slab_revenue_summary_instance.to_dict()
# create an instance of SlabRevenueSummary from a dict
slab_revenue_summary_from_dict = SlabRevenueSummary.from_dict(slab_revenue_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


