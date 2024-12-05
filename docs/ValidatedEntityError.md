# ValidatedEntityError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **str** | Reference ID of the entity, can be Schedule Id or Purchase Id | 
**entity_id** | **str** | Identifier of the entity | 
**entity_type** | **str** | Type of the entity, can be Rate card or Pricing rule | 
**error_message** | **str** | Error message for the validation | 

## Example

```python
from togai_client.models.validated_entity_error import ValidatedEntityError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidatedEntityError from a JSON string
validated_entity_error_instance = ValidatedEntityError.from_json(json)
# print the JSON string representation of the object
print(ValidatedEntityError.to_json())

# convert the object into a dict
validated_entity_error_dict = validated_entity_error_instance.to_dict()
# create an instance of ValidatedEntityError from a dict
validated_entity_error_from_dict = ValidatedEntityError.from_dict(validated_entity_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


