# SIS Import Errors

> Canvas LMS REST API — `/sis_import_errors` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/sis_imports/{id}/errors

**Get SIS import error list**  —  `get_sis_import_error_list_sis_imports`

Returns the list of SIS import errors for an account or a SIS import. Import
errors are only stored for 30 days.

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `failure` | boolean | query |  | If set, only shows errors on a sis import that would cause a failure. |

**Returns:** `array[SisImportError]`

## GET /v1/accounts/{account_id}/sis_import_errors

**Get SIS import error list**  —  `get_sis_import_error_list_sis_import_errors`

Returns the list of SIS import errors for an account or a SIS import. Import
errors are only stored for 30 days.

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

Example:
  curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
    -H "Authorization: Bearer <token>"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `failure` | boolean | query |  | If set, only shows errors on a sis import that would cause a failure. |

**Returns:** `array[SisImportError]`


---

# Models


## SisImportError

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `sis_import_id` | integer |  | The unique identifier for the SIS import. e.g. `1` |
| `file` | string |  | The file where the error message occurred. e.g. `courses.csv` |
| `message` | string |  | The error message that from the record. e.g. `No short_name given for course C001` |
| `row_info` | string |  | The contents of the line that had the error. e.g. `account_1, Sub account 1,, active` |
| `row` | integer |  | The line number where the error occurred. Some Importers do not yet support this. This is a 1 based index starting with the header row. e.g. `34` |
