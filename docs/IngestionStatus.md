# IngestionStatus

Status about the event ingestion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Ingestion status | 
**status_description** | **str** |  | [optional] 

## Example

```python
from togai_client.models.ingestion_status import IngestionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IngestionStatus from a JSON string
ingestion_status_instance = IngestionStatus.from_json(json)
# print the JSON string representation of the object
print(IngestionStatus.to_json())

# convert the object into a dict
ingestion_status_dict = ingestion_status_instance.to_dict()
# create an instance of IngestionStatus from a dict
ingestion_status_from_dict = IngestionStatus.from_dict(ingestion_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


