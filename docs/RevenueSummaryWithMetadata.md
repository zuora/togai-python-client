# RevenueSummaryWithMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**revenue** | **float** |  | 
**revenue_summary** | [**List[RevenueSummaryWithMetadata]**](RevenueSummaryWithMetadata.md) | Field: revenue is computed for all rate cards Field: slabRevenues is supported for only usage/license Field: metadata is populated based on application of rateConfig(&#39;minimumRate&#39;, &#39;maximumRate&#39;)  | [optional] 
**slab_revenues** | [**List[SlabRevenueWithMetadata]**](SlabRevenueWithMetadata.md) |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.revenue_summary_with_metadata import RevenueSummaryWithMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueSummaryWithMetadata from a JSON string
revenue_summary_with_metadata_instance = RevenueSummaryWithMetadata.from_json(json)
# print the JSON string representation of the object
print(RevenueSummaryWithMetadata.to_json())

# convert the object into a dict
revenue_summary_with_metadata_dict = revenue_summary_with_metadata_instance.to_dict()
# create an instance of RevenueSummaryWithMetadata from a dict
revenue_summary_with_metadata_from_dict = RevenueSummaryWithMetadata.from_dict(revenue_summary_with_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


