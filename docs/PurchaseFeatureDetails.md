# PurchaseFeatureDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**credits_granted** | **float** |  | 
**credits_available** | **float** |  | 
**updated_at** | **datetime** |  | 
**effective_from** | **datetime** |  | 
**effective_until** | **datetime** |  | 

## Example

```python
from togai_client.models.purchase_feature_details import PurchaseFeatureDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseFeatureDetails from a JSON string
purchase_feature_details_instance = PurchaseFeatureDetails.from_json(json)
# print the JSON string representation of the object
print(PurchaseFeatureDetails.to_json())

# convert the object into a dict
purchase_feature_details_dict = purchase_feature_details_instance.to_dict()
# create an instance of PurchaseFeatureDetails from a dict
purchase_feature_details_from_dict = PurchaseFeatureDetails.from_dict(purchase_feature_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


