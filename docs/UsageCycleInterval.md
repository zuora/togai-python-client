# UsageCycleInterval

UsageCycleInterval field allows you to treat the billing interval as many smaller windows. Revenue is calculated for each of the windows (usage cycles) and their sum is considered as the billing interval revenue. Example: 1 Named License being used across entire billing interval. Rate Value: $1/license CASE 1: Without usage cycle. $1 is charged for the entire billing cycle. CASE 2: Usage cycle is configure to be WEEKLY and the billing interval has 4 weeks. In this case $1 is charged  for each week totalling to $4 across for the billing interval 

## Enum

* `WEEKLY` (value: `'WEEKLY'`)

* `MONTHLY` (value: `'MONTHLY'`)

* `QUARTERLY` (value: `'QUARTERLY'`)

* `HALF_YEARLY` (value: `'HALF_YEARLY'`)

* `ANNUALLY` (value: `'ANNUALLY'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


