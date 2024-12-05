# CreateBulkAliasRequest

Create bulk alias

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | [**List[CreateAliasRequest]**](CreateAliasRequest.md) |  | 

## Example

```python
from togai_client.models.create_bulk_alias_request import CreateBulkAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBulkAliasRequest from a JSON string
create_bulk_alias_request_instance = CreateBulkAliasRequest.from_json(json)
# print the JSON string representation of the object
print(CreateBulkAliasRequest.to_json())

# convert the object into a dict
create_bulk_alias_request_dict = create_bulk_alias_request_instance.to_dict()
# create an instance of CreateBulkAliasRequest from a dict
create_bulk_alias_request_from_dict = CreateBulkAliasRequest.from_dict(create_bulk_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


