# SIS Imports

> Canvas LMS REST API — `/sis_imports` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/sis_imports

**Get SIS import list**  —  `get_sis_import_list`

Returns the list of SIS imports for an account

Example:
  curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports \
    -H 'Authorization: Bearer <token>'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `created_since` | DateTime | query |  | If set, only shows imports created after the specified date (use ISO8601 format) |
| `created_before` | DateTime | query |  | If set, only shows imports created before the specified date (use ISO8601 format) |
| `workflow_state` | array[string] | query |  | If set, only returns imports that are in the given state. Allowed: `initializing`, `created`, `importing`, `cleanup_batch`, `imported`, `imported_with_messages`, `aborted`, `failed`, `failed_with_messages`, `restoring`, `partially_restored`, `restored` |

**Returns:** `array[SisImport]`

## GET /v1/accounts/{account_id}/sis_imports/importing

**Get the current importing SIS import**  —  `get_current_importing_sis_import`

Returns the SIS imports that are currently processing for an account. If no
imports are running, will return an empty array.

Example:
  curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/importing \
    -H 'Authorization: Bearer <token>'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `SisImport`

## POST /v1/accounts/{account_id}/sis_imports

**Import SIS data**  —  `import_sis_data`

Import SIS data into Canvas. Must be on a root account with SIS imports
enabled.

For more information on the format that's expected here, please see the
"SIS CSV" section in the API docs.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `import_type` | string | form |  | Choose the data format for reading SIS data. With a standard Canvas install, this option can only be 'instructure_csv', and if unprovided, will be assumed to be so. Can be part of the query string. |
| `attachment` | string | form |  | There are three ways to post SIS import data: 1. As a multipart/form-data form field named +attachment+ 2. As a raw post with a Content-Type of application/zip or application/octet-stream 3. Using the {file:file.file_uploads.html File Upload} process, which can be more reliable    for large files. Use the +pre_attachment[name]+ argument to start that flow. See that    parameter below for more information.  +attachment+ is required for multipart/form-data style posts. Assumed to be SIS data from a file upload form field named +attachment+.  Examples:   curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \       https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv  If you decide to do a raw post, you can skip the 'attachment' argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the 'extension' argument.  Examples:   curl -H 'Content-Type: application/octet-stream' --data-binary @<filename>.zip \       -H "Authorization: Bearer <token>" \       https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&extension=zip    curl -H 'Content-Type: application/zip' --data-binary @<filename>.zip \       -H "Authorization: Bearer <token>" \       https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv    curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv    curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&batch_mode=1&batch_mode_term_id=15  If the attachment is a zip file, the uncompressed file(s) cannot be 100x larger than the zip, or the import will fail. For example, if the zip file is 1KB but the total size of the uncompressed file(s) is 100KB or greater the import will fail. There is a hard cap of 50 GB. |
| `pre_attachment[name]` | string | form |  | The name of the file to be uploaded (in a separate request) via the {file:file.file_uploads.html File Upload} workflow. This is the recommended way to upload larger batches, since the upload itself no longer has to finish within the 1-minute Canvas request timeout period. This argument cannot be combined with the +attachment+ argument; use one or the other.  To use this flow: 1. Perform a POST to this endpoint with file information in +pre_attachment+ 2. {file:file.file_uploads.html Upload the file} using the data in the response's +pre_attachment+ 3. Once the file has been uploaded, the SIS import will begin. 4. {api:SisImportsApiController#show Check the progress} of the import as usual.  NOTE: this option must be sent as either a query parameter or as a JSON body parameter; +application/x-www-form-urlencoded+ is not supported due to conflicts with raw post body data. |
| `pre_attachment[*]` | string | form |  | Other file upload properties; see {file:file.file_uploads.html File Upload Documentation} |
| `extension` | string | form |  | Recommended for raw post request style imports. This field will be used to distinguish between zip, xml, csv, and other file format extensions that would usually be provided with the filename in the multipart post request scenario. If not provided, this value will be inferred from the Content-Type, falling back to zip-file format if all else fails. |
| `batch_mode` | boolean | form |  | If set, this SIS import will be run in batch mode, deleting any data previously imported via SIS that is not present in this latest import. See the SIS CSV Format page for details. Batch mode cannot be used with diffing. |
| `batch_mode_term_id` | string | form |  | Limit deletions to only this term. Required if batch mode is enabled. |
| `multi_term_batch_mode` | boolean | form |  | Runs batch mode against all terms in terms file. Requires change_threshold. |
| `skip_deletes` | boolean | form |  | When set the import will skip any deletes. This does not account for objects that are deleted during the batch mode cleanup process. |
| `override_sis_stickiness` | boolean | form |  | Default is false. If true, any fields containing “sticky” or UI changes will be overridden. See SIS CSV Format documentation for information on which fields can have SIS stickiness |
| `add_sis_stickiness` | boolean | form |  | This option, if present, will process all changes as if they were UI changes. This means that "stickiness" will be added to changed fields. This option is only processed if 'override_sis_stickiness' is also provided. |
| `clear_sis_stickiness` | boolean | form |  | This option, if present, will clear "stickiness" from all fields processed by this import. Requires that 'override_sis_stickiness' is also provided. If 'add_sis_stickiness' is also provided, 'clear_sis_stickiness' will overrule the behavior of 'add_sis_stickiness' |
| `update_sis_id_if_login_claimed` | boolean | form |  | This option, if present, will override the old (or non-existent) non-matching SIS ID with the new SIS ID in the upload, if a pseudonym is found from the login field and the SIS ID doesn't match. |
| `diffing_data_set_identifier` | string | form |  | If set on a CSV import, Canvas will attempt to optimize the SIS import by comparing this set of CSVs to the previous set that has the same data set identifier, and only applying the difference between the two. See the SIS CSV Format documentation for more details. Diffing cannot be used with batch_mode |
| `diffing_remaster_data_set` | boolean | form |  | If true, and diffing_data_set_identifier is sent, this SIS import will be part of the data set, but diffing will not be performed. See the SIS CSV Format documentation for details. |
| `diffing_drop_status` | string | form |  | If diffing_drop_status is passed, this SIS import will use this status for enrollments that are not included in the sis_batch. Defaults to 'deleted' Allowed: `deleted`, `completed`, `inactive` |
| `diffing_user_remove_status` | string | form |  | For users removed from one batch to the next one using the same diffing_data_set_identifier, set their status to the value of this argument. Defaults to 'deleted'. Allowed: `deleted`, `suspended` |
| `batch_mode_enrollment_drop_status` | string | form |  | If batch_mode_enrollment_drop_status is passed, this SIS import will use this status for enrollments that are not included in the sis_batch. This will have an effect if multi_term_batch_mode is set. Defaults to 'deleted' This will still mark courses and sections that are not included in the sis_batch as deleted, and subsequently enrollments in the deleted courses and sections as deleted. Allowed: `deleted`, `completed`, `inactive` |
| `change_threshold` | integer (int64) | form |  | If set with batch_mode, the batch cleanup process will not run if the number of items deleted is higher than the percentage set. If set to 10 and a term has 200 enrollments, and batch would delete more than 20 of the enrollments the batch will abort before the enrollments are deleted. The change_threshold will be evaluated for course, sections, and enrollments independently. If set with diffing, diffing will not be performed if the files are greater than the threshold as a percent. If set to 5 and the file is more than 5% smaller or more than 5% larger than the file that is being compared to, diffing will not be performed. If the files are less than 5%, diffing will be performed. The way the percent is calculated is by taking the size of the current import and dividing it by the size of the previous import. The formula used is: \|(1 - current_file_size / previous_file_size)\| * 100 See the SIS CSV Format documentation for more details. Required for multi_term_batch_mode. |
| `diff_row_count_threshold` | integer (int64) | form |  | If set with diffing, diffing will not be performed if the number of rows to be run in the fully calculated diff import exceeds the threshold. |

**Returns:** `SisImport`

## GET /v1/accounts/{account_id}/sis_imports/{id}

**Get SIS import status**  —  `get_sis_import_status`

Get the status of an already created SIS import.

  Examples:
    curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id> \
        -H 'Authorization: Bearer <token>'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `SisImport`

## PUT /v1/accounts/{account_id}/sis_imports/{id}/restore_states

**Restore workflow_states of SIS imported items**  —  `restore_workflow_states_of_sis_imported_items`

This will restore the the workflow_state for all the items that changed
their workflow_state during the import being restored.
This will restore states for items imported with the following importers:
accounts.csv terms.csv courses.csv sections.csv group_categories.csv
groups.csv users.csv admins.csv
This also restores states for other items that changed during the import.
An example would be if an enrollment was deleted from a sis import and the
group_membership was also deleted as a result of the enrollment deletion,
both items would be restored when the sis batch is restored.

Restore data is retained for 30 days post-import. This endpoint is
unavailable after that time.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `batch_mode` | boolean | form |  | If set, will only restore items that were deleted from batch_mode. |
| `undelete_only` | boolean | form |  | If set, will only restore items that were deleted. This will ignore any items that were created or modified. |
| `unconclude_only` | boolean | form |  | If set, will only restore enrollments that were concluded. This will ignore any items that were created or deleted. |

**Returns:** `Progress`

## PUT /v1/accounts/{account_id}/sis_imports/{id}/abort

**Abort SIS import**  —  `abort_sis_import`

Abort a SIS import that has not completed.

Aborting a sis batch that is running can take some time for every process to
see the abort event. Subsequent sis batches begin to process 10 minutes
after the abort to allow each process to clean up properly.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `SisImport`

## PUT /v1/accounts/{account_id}/sis_imports/abort_all_pending

**Abort all pending SIS imports**  —  `abort_all_pending_sis_imports`

Abort already created but not processed or processing SIS imports.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `boolean`


---

# Models


## SisImportData

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `import_type` | string |  | The type of SIS import e.g. `instructure_csv` |
| `supplied_batches` | array[string] |  | Which files were included in the SIS import e.g. `['term', 'course', 'section', 'user', 'enrollment']` |
| `counts` | SisImportCounts |  | The number of rows processed for each type of import |


## SisImportStatistic

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `created` | integer |  | This is the number of items that were created. e.g. `18` |
| `concluded` | integer |  | This is the number of items that marked as completed. This only applies to courses and enrollments. e.g. `3` |
| `deactivated` | integer |  | This is the number of Enrollments that were marked as 'inactive'. This only applies to enrollments. e.g. `1` |
| `restored` | integer |  | This is the number of items that were set to an active state from a completed, inactive, or deleted state. e.g. `2` |
| `deleted` | integer |  | This is the number of items that were deleted. e.g. `40` |


## SisImportStatistics

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `total_state_changes` | integer |  | This is the total number of items that were changed in the sis import. There are a few caveats that can cause this number to not add up to the individual counts. There are some state changes that happen that have no impact to the object. An example would be changing a course from 'created' to 'claimed'. Both of these would be considered an active course, but would increment this counter. In this example the course would not increment the created or restored counters for course statistic. e.g. `382` |
| `Account` | SisImportStatistic |  | This contains that statistics for accounts. |
| `EnrollmentTerm` | SisImportStatistic |  | This contains that statistics for terms. |
| `CommunicationChannel` | SisImportStatistic |  | This contains that statistics for communication channels. This is an indirect effect from creating or deleting a user. |
| `AbstractCourse` | SisImportStatistic |  | This contains that statistics for abstract courses. |
| `Course` | SisImportStatistic |  | This contains that statistics for courses. |
| `CourseSection` | SisImportStatistic |  | This contains that statistics for course sections. |
| `Enrollment` | SisImportStatistic |  | This contains that statistics for enrollments. |
| `GroupCategory` | SisImportStatistic |  | This contains that statistics for group categories. |
| `Group` | SisImportStatistic |  | This contains that statistics for groups. |
| `GroupMembership` | SisImportStatistic |  | This contains that statistics for group memberships. This can be a direct impact from the import or indirect from an enrollment being deleted. |
| `Pseudonym` | SisImportStatistic |  | This contains that statistics for pseudonyms. Pseudonyms are logins for users, and are the object that ties an enrollment to a user. This would be impacted from the user importer. |
| `UserObserver` | SisImportStatistic |  | This contains that statistics for user observers. |
| `AccountUser` | SisImportStatistic |  | This contains that statistics for account users. |


## SisImportCounts

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `accounts` | integer |  | e.g. `0` |
| `terms` | integer |  | e.g. `3` |
| `abstract_courses` | integer |  | e.g. `0` |
| `courses` | integer |  | e.g. `121` |
| `sections` | integer |  | e.g. `278` |
| `xlists` | integer |  | e.g. `0` |
| `users` | integer |  | e.g. `346` |
| `enrollments` | integer |  | e.g. `1542` |
| `groups` | integer |  | e.g. `0` |
| `group_memberships` | integer |  | e.g. `0` |
| `grade_publishing_results` | integer |  | e.g. `0` |
| `batch_courses_deleted` | integer |  | the number of courses that were removed because they were not included in the batch for batch_mode imports. Only included if courses were deleted e.g. `11` |
| `batch_sections_deleted` | integer |  | the number of sections that were removed because they were not included in the batch for batch_mode imports. Only included if sections were deleted e.g. `0` |
| `batch_enrollments_deleted` | integer |  | the number of enrollments that were removed because they were not included in the batch for batch_mode imports. Only included if enrollments were deleted e.g. `150` |
| `error_count` | integer |  | e.g. `0` |
| `warning_count` | integer |  | e.g. `0` |


## SisImport

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the SIS import. e.g. `1` |
| `created_at` | datetime |  | The date the SIS import was created. e.g. `2013-12-01T23:59:00-06:00` |
| `ended_at` | datetime |  | The date the SIS import finished. Returns null if not finished. e.g. `2013-12-02T00:03:21-06:00` |
| `updated_at` | datetime |  | The date the SIS import was last updated. e.g. `2013-12-02T00:03:21-06:00` |
| `workflow_state` | string |  | The current state of the SIS import.  - 'initializing': The SIS import is being created, if this gets stuck in initializing, it will not import and will continue on to next import.  - 'created': The SIS import has been created.  - 'importing': The SIS import is currently processing.  - 'cleanup_batch': The SIS import is currently cleaning up courses, sections, and enrollments not included in the batch for batch_mode imports.  - 'imported': The SIS import has completed successfully.  - 'imported_with_messages': The SIS import completed with errors or warnings.  - 'aborted': The SIS import was aborted.  - 'failed_with_messages': The SIS import failed with errors.  - 'failed': The SIS import failed.  - 'restoring': The SIS import is restoring states of imported items.  - 'partially_restored': The SIS import is restored some of the states of imported items. This is generally due to passing a param like undelete only.  - 'restored': The SIS import is restored all of the states of imported items. e.g. `imported` |
| `data` | SisImportData |  | data |
| `statistics` | SisImportStatistics |  | statistics |
| `progress` | string |  | The progress of the SIS import. The progress will reset when using batch_mode and have a different progress for the cleanup stage e.g. `100` |
| `errors_attachment` | File |  | The errors_attachment api object of the SIS import. Only available if there are errors or warning and import has completed. |
| `user` | User |  | The user that initiated the sis_batch. See the Users API for details. |
| `processing_warnings` | array[array] |  | Only imports that are complete will get this data. An array of CSV_file/warning_message pairs. e.g. `[['students.csv', "user John Doe has already claimed john_doe's requested login information, skipping"]]` |
| `processing_errors` | array[array] |  | An array of CSV_file/error_message pairs. e.g. `[['students.csv', 'Error while importing CSV. Please contact support.']]` |
| `batch_mode` | boolean |  | Whether the import was run in batch mode. e.g. `true` |
| `batch_mode_term_id` | string |  | The term the batch was limited to. e.g. `1234` |
| `multi_term_batch_mode` | boolean |  | Enables batch mode against all terms in term file. Requires change_threshold to be set. e.g. `false` |
| `skip_deletes` | boolean |  | When set the import will skip any deletes. e.g. `false` |
| `override_sis_stickiness` | boolean |  | Whether UI changes were overridden. e.g. `false` |
| `add_sis_stickiness` | boolean |  | Whether stickiness was added to the batch changes. e.g. `false` |
| `clear_sis_stickiness` | boolean |  | Whether stickiness was cleared. e.g. `false` |
| `diffing_threshold_exceeded` | boolean |  | Whether a diffing job failed because the threshold limit got exceeded. e.g. `true` |
| `diffing_data_set_identifier` | string |  | The identifier of the data set that this SIS batch diffs against e.g. `account-5-enrollments` |
| `diffing_remaster` | boolean |  | Whether diffing remaster data was enabled. e.g. `false` |
| `diffed_against_import_id` | integer |  | The ID of the SIS Import that this import was diffed against e.g. `1` |
| `csv_attachments` | array[array] |  | An array of CSV files for processing e.g. `[]` |
