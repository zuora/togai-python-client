# PricePlanInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from togai_client.models.price_plan_info import PricePlanInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PricePlanInfo from a JSON string
price_plan_info_instance = PricePlanInfo.from_json(json)
# print the JSON string representation of the object
print(PricePlanInfo.to_json())

# convert the object into a dict
price_plan_info_dict = price_plan_info_instance.to_dict()
# create an instance of PricePlanInfo from a dict
price_plan_info_from_dict = PricePlanInfo.from_dict(price_plan_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


