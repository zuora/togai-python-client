# CreateCreditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits** | [**List[Credit]**](Credit.md) |  | 

## Example

```python
from togai_client.models.create_credit_response import CreateCreditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCreditResponse from a JSON string
create_credit_response_instance = CreateCreditResponse.from_json(json)
# print the JSON string representation of the object
print(CreateCreditResponse.to_json())

# convert the object into a dict
create_credit_response_dict = create_credit_response_instance.to_dict()
# create an instance of CreateCreditResponse from a dict
create_credit_response_from_dict = CreateCreditResponse.from_dict(create_credit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


