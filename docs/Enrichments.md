# Enrichments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencies** | [**List[Dependency]**](Dependency.md) |  | [optional] 
**fields** | [**List[ModelField]**](ModelField.md) |  | 

## Example

```python
from togai_client.models.enrichments import Enrichments

# TODO update the JSON string below
json = "{}"
# create an instance of Enrichments from a JSON string
enrichments_instance = Enrichments.from_json(json)
# print the JSON string representation of the object
print(Enrichments.to_json())

# convert the object into a dict
enrichments_dict = enrichments_instance.to_dict()
# create an instance of Enrichments from a dict
enrichments_from_dict = Enrichments.from_dict(enrichments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


