# Computation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Optional identifier describing the matcher and computation pair | [optional] 
**matcher** | **str** | Condition to be applied on event. Upon matching it the corresponding computation will be considered for usage_meter unit calculation. The result of the matcher needs to be [truthy](https://jsonlogic.com/truthy.html) in order to be considered as a match.  | [optional] 
**computation** | **str** | Computation to be applied on an event if it matches the matcher. In case of a COUNT aggregation type, computation should be passed as &#39;1&#39;  | 
**order** | **int** | The order in which multiple matched computations will get evaluated | 

## Example

```python
from togai_client.models.computation import Computation

# TODO update the JSON string below
json = "{}"
# create an instance of Computation from a JSON string
computation_instance = Computation.from_json(json)
# print the JSON string representation of the object
print(Computation.to_json())

# convert the object into a dict
computation_dict = computation_instance.to_dict()
# create an instance of Computation from a dict
computation_from_dict = Computation.from_dict(computation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


