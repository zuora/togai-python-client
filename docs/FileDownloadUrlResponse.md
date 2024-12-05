# FileDownloadUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download_url** | **str** |  | 

## Example

```python
from togai_client.models.file_download_url_response import FileDownloadUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownloadUrlResponse from a JSON string
file_download_url_response_instance = FileDownloadUrlResponse.from_json(json)
# print the JSON string representation of the object
print(FileDownloadUrlResponse.to_json())

# convert the object into a dict
file_download_url_response_dict = file_download_url_response_instance.to_dict()
# create an instance of FileDownloadUrlResponse from a dict
file_download_url_response_from_dict = FileDownloadUrlResponse.from_dict(file_download_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


