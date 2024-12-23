# PricingCycleConfigStartOffset

Represents the start of pricing cycle in terms of  - dayOffset - number of days from beginning of week / month and  - monthOffset - number of months from beginning of interval (quarter, half-year or year) Note: If a day with offset doesn't exist for a month, closest previous day is considered Examples: WEEKLY -   - {dayOffset: 1, monthOffset: NIL} - First day of every week (Monday)   - {dayOffset: 3, monthOffset: NIL} - 3rd day of every week (Wednesday)   - {dayOffset: LAST, monthOffset: NIL} - Last day of every week (Sunday) MONTHLY -   - {dayOffset: 1, monthOffset: NIL} - First day of every month   - {dayOffset: 12, monthOffset: NIL} - 12th of every month   - {dayOffset: 28, monthOffset: NIL} - 28th of every month. i.e, 28th of Jan, 28th of Feb, ...   - {dayOffset: 30, monthOffset: NIL} - 30th of every month. i.e, 28th of Jan, 28th of Feb, ...   - {dayOffset: LAST, monthOffset: NIL} - Last day of every month. i.e, 31st of Jan, 28th of Feb, ... QUARTERLY   - {dayOffset: 15, monthOffset: FIRST} - 15th Jan, 15th Apr, 15th Jul and 15th Oct   - {dayOffset: 15, monthOffset: 2} - 15th Feb, 15th May, 15th Aug and 15th Nov   - {dayOffset: 15, monthOffset: LAST} - 15th Mar, 15th Jun, 15th Sep and 15th Dec   - {dayOffset: LAST, monthOffset: FIRST} - 31st Jan, 30th Apr, 30th Jul and 31th Oct HALF_YEARLY   - {dayOffset: 15, monthOffset: FIRST} - 15th Jan and 15th Jul   - {dayOffset: 15, monthOffset: 4} - 15th Apr and 15th Oct   - {dayOffset: 15, monthOffset: LAST} - 15th Jun and 15th Dec ANNUALLY   - {dayOffset: 15, monthOffset: FIRST} - 15th Jan   - {dayOffset: 15, monthOffset: 1} - 15th Jan   - {dayOffset: LAST, monthOffset: 2} - 29th Feb on Leap year, 28th otherwise    - {dayOffset: 15, monthOffset: 8} - 15th Aug   - {dayOffset: 15, monthOffset: LAST} - 15th Dec 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_offset** | **str** | If interval is WEEKLY, min: \&quot;1\&quot; and max: \&quot;7\&quot; as strings. Spl. string allowed: LAST Otherwise, min: \&quot;1\&quot; and max: \&quot;31\&quot; as strings. Spl. string allowed: LAST  | 
**month_offset** | **str** | min: \&quot;1\&quot; and max: \&quot;12\&quot;. Spl. string allowed: FIRST / LAST. For QUARTERLY only 1 - 3 is allowed and for HALF_YEARLY 1 - 6. This being an optional field, shouldn&#39;t be passed for MONTHLY.  | 

## Example

```python
from togai_client.models.pricing_cycle_config_start_offset import PricingCycleConfigStartOffset

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCycleConfigStartOffset from a JSON string
pricing_cycle_config_start_offset_instance = PricingCycleConfigStartOffset.from_json(json)
# print the JSON string representation of the object
print(PricingCycleConfigStartOffset.to_json())

# convert the object into a dict
pricing_cycle_config_start_offset_dict = pricing_cycle_config_start_offset_instance.to_dict()
# create an instance of PricingCycleConfigStartOffset from a dict
pricing_cycle_config_start_offset_from_dict = PricingCycleConfigStartOffset.from_dict(pricing_cycle_config_start_offset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


