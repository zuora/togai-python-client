# EnrichmentDependency

enrichment dependency

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from togai_client.models.enrichment_dependency import EnrichmentDependency

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichmentDependency from a JSON string
enrichment_dependency_instance = EnrichmentDependency.from_json(json)
# print the JSON string representation of the object
print(EnrichmentDependency.to_json())

# convert the object into a dict
enrichment_dependency_dict = enrichment_dependency_instance.to_dict()
# create an instance of EnrichmentDependency from a dict
enrichment_dependency_from_dict = EnrichmentDependency.from_dict(enrichment_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


