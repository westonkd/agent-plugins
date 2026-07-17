# Outcome Imports

> Canvas LMS REST API — `/outcome_imports` resource. Base path `/api`.

## POST /v1/accounts/{account_id}/outcome_imports

**Import Outcomes**  —  `import_outcomes_accounts`

Import outcomes into Canvas.

For more information on the format that's expected here, please see the
"Outcomes CSV" section in the API docs.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `import_type` | string | form |  | Choose the data format for reading outcome data. With a standard Canvas install, this option can only be 'instructure_csv', and if unprovided, will be assumed to be so. Can be part of the query string. |
| `attachment` | string | form |  | There are two ways to post outcome import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.  'attachment' is required for multipart/form-data style posts. Assumed to be outcome data from a file upload form field named 'attachment'.  Examples:   curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'   curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv'  If you decide to do a raw post, you can skip the 'attachment' argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the 'extension' argument.  Examples:   curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'    curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv' |
| `extension` | string | form |  | Recommended for raw post request style imports. This field will be used to distinguish between csv and other file format extensions that would usually be provided with the filename in the multipart post request scenario. If not provided, this value will be inferred from the Content-Type, falling back to csv-file format if all else fails. |

**Returns:** `OutcomeImport`

## POST /v1/courses/{course_id}/outcome_imports

**Import Outcomes**  —  `import_outcomes_courses`

Import outcomes into Canvas.

For more information on the format that's expected here, please see the
"Outcomes CSV" section in the API docs.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `import_type` | string | form |  | Choose the data format for reading outcome data. With a standard Canvas install, this option can only be 'instructure_csv', and if unprovided, will be assumed to be so. Can be part of the query string. |
| `attachment` | string | form |  | There are two ways to post outcome import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.  'attachment' is required for multipart/form-data style posts. Assumed to be outcome data from a file upload form field named 'attachment'.  Examples:   curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'   curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv'  If you decide to do a raw post, you can skip the 'attachment' argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the 'extension' argument.  Examples:   curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'    curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv' |
| `extension` | string | form |  | Recommended for raw post request style imports. This field will be used to distinguish between csv and other file format extensions that would usually be provided with the filename in the multipart post request scenario. If not provided, this value will be inferred from the Content-Type, falling back to csv-file format if all else fails. |

**Returns:** `OutcomeImport`

## GET /v1/accounts/{account_id}/outcome_imports/{id}

**Get Outcome import status**  —  `get_outcome_import_status_accounts`

Get the status of an already created Outcome import. Pass 'latest' for the outcome import id
for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeImport`

## GET /v1/courses/{course_id}/outcome_imports/{id}

**Get Outcome import status**  —  `get_outcome_import_status_courses`

Get the status of an already created Outcome import. Pass 'latest' for the outcome import id
for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeImport`

## GET /v1/accounts/{account_id}/outcome_imports/{id}/created_group_ids

**Get IDs of outcome groups created after successful import**  —  `get_ids_of_outcome_groups_created_after_successful_import_accounts`

Get the IDs of the outcome groups created after a successful import.
Pass 'latest' for the outcome import id for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/outcomes_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/outcome_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array of outcome ids`

## GET /v1/courses/{course_id}/outcome_imports/{id}/created_group_ids

**Get IDs of outcome groups created after successful import**  —  `get_ids_of_outcome_groups_created_after_successful_import_courses`

Get the IDs of the outcome groups created after a successful import.
Pass 'latest' for the outcome import id for the latest import.

  Examples:
    curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/outcomes_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"
    curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/outcome_group_ids/<outcome_import_id>' \
        -H "Authorization: Bearer <token>"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array of outcome ids`


---

# Models


## OutcomeImportData

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `import_type` | string |  | The type of outcome import e.g. `instructure_csv` |


## OutcomeImport

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the outcome import. e.g. `1` |
| `learning_outcome_group_id` | integer |  | The unique identifier for the group into which the outcomes will be imported to, or NULL. e.g. `1` |
| `created_at` | datetime |  | The date the outcome import was created. e.g. `2013-12-01T23:59:00-06:00` |
| `ended_at` | datetime |  | The date the outcome import finished. Returns null if not finished. e.g. `2013-12-02T00:03:21-06:00` |
| `updated_at` | datetime |  | The date the outcome import was last updated. e.g. `2013-12-02T00:03:21-06:00` |
| `workflow_state` | string |  | The current state of the outcome import.  - 'created': The outcome import has been created.  - 'importing': The outcome import is currently processing.  - 'succeeded': The outcome import has completed successfully.  - 'failed': The outcome import failed. e.g. `imported` |
| `data` | OutcomeImportData |  | See the OutcomeImportData specification above. |
| `progress` | string |  | The progress of the outcome import. e.g. `100` |
| `user` | User |  | The user that initiated the outcome_import. See the Users API for details. |
| `processing_errors` | array[array] |  | An array of row number / error message pairs. Returns the first 25 errors. e.g. `[[1, 'Missing required fields: title']]` |
