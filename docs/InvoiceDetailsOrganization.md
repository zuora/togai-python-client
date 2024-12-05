# InvoiceDetailsOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**business_name** | **str** |  | 
**address** | [**Address**](Address.md) |  | 
**primary_email** | **str** |  | 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from togai_client.models.invoice_details_organization import InvoiceDetailsOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDetailsOrganization from a JSON string
invoice_details_organization_instance = InvoiceDetailsOrganization.from_json(json)
# print the JSON string representation of the object
print(InvoiceDetailsOrganization.to_json())

# convert the object into a dict
invoice_details_organization_dict = invoice_details_organization_instance.to_dict()
# create an instance of InvoiceDetailsOrganization from a dict
invoice_details_organization_from_dict = InvoiceDetailsOrganization.from_dict(invoice_details_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


