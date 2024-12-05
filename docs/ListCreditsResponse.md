# ListCreditsResponse

List credits response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Credit]**](Credit.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.list_credits_response import ListCreditsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListCreditsResponse from a JSON string
list_credits_response_instance = ListCreditsResponse.from_json(json)
# print the JSON string representation of the object
print(ListCreditsResponse.to_json())

# convert the object into a dict
list_credits_response_dict = list_credits_response_instance.to_dict()
# create an instance of ListCreditsResponse from a dict
list_credits_response_from_dict = ListCreditsResponse.from_dict(list_credits_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


