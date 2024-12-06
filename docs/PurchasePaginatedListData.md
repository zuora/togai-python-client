# PurchasePaginatedListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PurchaseListResponse]**](PurchaseListResponse.md) |  | [optional] 
**next_token** | **str** |  | [optional] 
**context** | [**PaginationOptions**](PaginationOptions.md) |  | [optional] 

## Example

```python
from togai_client.models.purchase_paginated_list_data import PurchasePaginatedListData

# TODO update the JSON string below
json = "{}"
# create an instance of PurchasePaginatedListData from a JSON string
purchase_paginated_list_data_instance = PurchasePaginatedListData.from_json(json)
# print the JSON string representation of the object
print(PurchasePaginatedListData.to_json())

# convert the object into a dict
purchase_paginated_list_data_dict = purchase_paginated_list_data_instance.to_dict()
# create an instance of PurchasePaginatedListData from a dict
purchase_paginated_list_data_from_dict = PurchasePaginatedListData.from_dict(purchase_paginated_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


