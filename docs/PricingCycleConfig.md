# PricingCycleConfig

Represents configurations related to pricing cycle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | [**PricingCycleInterval**](PricingCycleInterval.md) |  | 
**start_offset** | [**PricingCycleConfigStartOffset**](PricingCycleConfigStartOffset.md) |  | [optional] 
**grace_period** | **int** | Togai allows you to ingest past dated events that will be processed by a pricing cycle till the end grace period.  For example: Pricing cycle is Monthly from 1st to 30th and gracePeriod is 5 days which next month 1 to 5th date, you can ingest past dated events during this grace period.  | 
**anniversary_cycle** | **bool** | Togai calculates the startOffsets based on the date of association instead of requiring from the user and  these offsets will be applied as an override if this flag is enabled. Examples: WEEKLY -   - 23/10/2023 (Monday) - {dayOffset: 1, monthOffset: NIL}    - 25/10/2023 (Wednesday) - {dayOffset: 3, monthOffset: NIL}    - 29/10/2023 (Sunday) - {dayOffset: 7, monthOffset: NIL} MONTHLY -   - 1st Oct - {dayOffset: 1, monthOffset: NIL}   - 12th Oct - {dayOffset: 12, monthOffset: NIL}   - 28th Oct - {dayOffset: 28, monthOffset: NIL}   - 30th Oct - {dayOffset: 30, monthOffset: NIL}   - 31th Oct - {dayOffset: LAST, monthOffset: NIL} QUARTERLY   - 15th Jan, 15th Apr, 15th Jul and 15th Oct - {dayOffset: 15, monthOffset: 1}   - 15th Feb, 15th May, 15th Aug and 15th Nov - {dayOffset: 15, monthOffset: 2}    - 15th Mar, 15th Jun, 15th Sep and 15th Dec - {dayOffset: 15, monthOffset: 3} HALF_YEARLY   - 15th Jan and 15th Jul - {dayOffset: 15, monthOffset: 1}    - 15th Apr and 15th Oct - {dayOffset: 15, monthOffset: 4}    - 15th Jun and 15th Dec - {dayOffset: 15, monthOffset: 6} ANNUALLY   - 15th Jan - {dayOffset: 15, monthOffset: 1}   - 29th Feb on Leap year  - {dayOffset: LAST, monthOffset: 2}   - 28th Feb  - {dayOffset: LAST, monthOffset: 2}   - 15th Aug - {dayOffset: 15, monthOffset: 8}   - 15th Dec - {dayOffset: 15, monthOffset: 12}  | [optional] 

## Example

```python
from togai_client.models.pricing_cycle_config import PricingCycleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCycleConfig from a JSON string
pricing_cycle_config_instance = PricingCycleConfig.from_json(json)
# print the JSON string representation of the object
print(PricingCycleConfig.to_json())

# convert the object into a dict
pricing_cycle_config_dict = pricing_cycle_config_instance.to_dict()
# create an instance of PricingCycleConfig from a dict
pricing_cycle_config_from_dict = PricingCycleConfig.from_dict(pricing_cycle_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


