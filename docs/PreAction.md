# PreAction

Pre action to be performed before association or disassociation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of pre action to be performed | 
**config** | **Dict[str, str]** | Configuration required for performing pre action - &#x60;GRANT_LICENSE&#x60;: grant one time licenses to an account before association   - &#x60;licenseId&#x60; [Required]: Id of the license to be granted   - &#x60;updateType&#x60; [Required]: Type of update to be performed on the license (RELATIVE or ABSOLUTE)   - &#x60;quantity&#x60; [Required]: Quantity of license to be granted   - &#x60;effectiveFrom&#x60; [Optional]: Effective date from which the license will be granted  | [optional] 

## Example

```python
from togai_client.models.pre_action import PreAction

# TODO update the JSON string below
json = "{}"
# create an instance of PreAction from a JSON string
pre_action_instance = PreAction.from_json(json)
# print the JSON string representation of the object
print(PreAction.to_json())

# convert the object into a dict
pre_action_dict = pre_action_instance.to_dict()
# create an instance of PreAction from a dict
pre_action_from_dict = PreAction.from_dict(pre_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


