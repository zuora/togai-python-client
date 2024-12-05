# RateCardPaginatedResponse

Paginated response for rate card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RateCard]**](RateCard.md) |  | 
**next_token** | **str** |  | [optional] 

## Example

```python
from togai_client.models.rate_card_paginated_response import RateCardPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RateCardPaginatedResponse from a JSON string
rate_card_paginated_response_instance = RateCardPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(RateCardPaginatedResponse.to_json())

# convert the object into a dict
rate_card_paginated_response_dict = rate_card_paginated_response_instance.to_dict()
# create an instance of RateCardPaginatedResponse from a dict
rate_card_paginated_response_from_dict = RateCardPaginatedResponse.from_dict(rate_card_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


