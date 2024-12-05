# IngestEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**status_code** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 

## Example

```python
from togai_client.models.ingest_event_response import IngestEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IngestEventResponse from a JSON string
ingest_event_response_instance = IngestEventResponse.from_json(json)
# print the JSON string representation of the object
print(IngestEventResponse.to_json())

# convert the object into a dict
ingest_event_response_dict = ingest_event_response_instance.to_dict()
# create an instance of IngestEventResponse from a dict
ingest_event_response_from_dict = IngestEventResponse.from_dict(ingest_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


