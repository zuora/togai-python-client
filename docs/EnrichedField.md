# EnrichedField

enriched field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from togai_client.models.enriched_field import EnrichedField

# TODO update the JSON string below
json = "{}"
# create an instance of EnrichedField from a JSON string
enriched_field_instance = EnrichedField.from_json(json)
# print the JSON string representation of the object
print(EnrichedField.to_json())

# convert the object into a dict
enriched_field_dict = enriched_field_instance.to_dict()
# create an instance of EnrichedField from a dict
enriched_field_from_dict = EnrichedField.from_dict(enriched_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


