# Originality Reports

> Canvas LMS REST API — `/originality_reports` resource. Base path `/api`.

## POST /lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report

**Create an Originality Report**  —  `create_originality_report`

Create a new OriginalityReport for the specified file

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `originality_report[file_id]` | integer (int64) | form |  | The id of the file being given an originality score. Required if creating a report associated with a file. |
| `originality_report[originality_score]` | number (float) | form | yes | A number between 0 and 100 representing the measure of the specified file's originality. |
| `originality_report[originality_report_url]` | string | form |  | The URL where the originality report for the specified file may be found. |
| `originality_report[originality_report_file_id]` | integer (int64) | form |  | The ID of the file within Canvas that contains the originality report for the submitted file provided in the request URL. |
| `originality_report[tool_setting][resource_type_code]` | string | form |  | The resource type code of the resource handler Canvas should use for the LTI launch for viewing originality reports. If set Canvas will launch to the message with type 'basic-lti-launch-request' in the specified resource handler rather than using the originality_report_url. |
| `originality_report[tool_setting][resource_url]` | string | form |  | The URL Canvas should launch to when showing an LTI originality report. Note that this value is inferred from the specified resource handler's message "path" value (See `resource_type_code`) unless it is specified. If this parameter is used a `resource_type_code` must also be specified. |
| `originality_report[workflow_state]` | string | form |  | May be set to "pending", "error", or "scored". If an originality score is provided a workflow state of "scored" will be inferred. |
| `originality_report[error_message]` | string | form |  | A message describing the error. If set, the "workflow_state" will be set to "error." |
| `originality_report[attempt]` | integer (int64) | form |  | If no `file_id` is given, and no file is required for the assignment (that is, the assignment allows an online text entry), this parameter may be given to clarify which attempt number the report is for (in the case of resubmissions). If this field is omitted and no `file_id` is given, the report will be created (or updated, if it exists) for the first submission attempt with no associated file. |

**Returns:** `OriginalityReport`

## PUT /lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id}

**Edit an Originality Report**  —  `edit_originality_report_submissions`

Modify an existing originality report. An alternative to this endpoint is
to POST the same parameters listed below to the CREATE endpoint.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `originality_report[originality_score]` | number (float) | form |  | A number between 0 and 100 representing the measure of the specified file's originality. |
| `originality_report[originality_report_url]` | string | form |  | The URL where the originality report for the specified file may be found. |
| `originality_report[originality_report_file_id]` | integer (int64) | form |  | The ID of the file within Canvas that contains the originality report for the submitted file provided in the request URL. |
| `originality_report[tool_setting][resource_type_code]` | string | form |  | The resource type code of the resource handler Canvas should use for the LTI launch for viewing originality reports. If set Canvas will launch to the message with type 'basic-lti-launch-request' in the specified resource handler rather than using the originality_report_url. |
| `originality_report[tool_setting][resource_url]` | string | form |  | The URL Canvas should launch to when showing an LTI originality report. Note that this value is inferred from the specified resource handler's message "path" value (See `resource_type_code`) unless it is specified. If this parameter is used a `resource_type_code` must also be specified. |
| `originality_report[workflow_state]` | string | form |  | May be set to "pending", "error", or "scored". If an originality score is provided a workflow state of "scored" will be inferred. |
| `originality_report[error_message]` | string | form |  | A message describing the error. If set, the "workflow_state" will be set to "error." |

**Returns:** `OriginalityReport`

## PUT /lti/assignments/{assignment_id}/files/{file_id}/originality_report

**Edit an Originality Report**  —  `edit_originality_report_files`

Modify an existing originality report. An alternative to this endpoint is
to POST the same parameters listed below to the CREATE endpoint.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `file_id` | string | path | yes | ID |
| `originality_report[originality_score]` | number (float) | form |  | A number between 0 and 100 representing the measure of the specified file's originality. |
| `originality_report[originality_report_url]` | string | form |  | The URL where the originality report for the specified file may be found. |
| `originality_report[originality_report_file_id]` | integer (int64) | form |  | The ID of the file within Canvas that contains the originality report for the submitted file provided in the request URL. |
| `originality_report[tool_setting][resource_type_code]` | string | form |  | The resource type code of the resource handler Canvas should use for the LTI launch for viewing originality reports. If set Canvas will launch to the message with type 'basic-lti-launch-request' in the specified resource handler rather than using the originality_report_url. |
| `originality_report[tool_setting][resource_url]` | string | form |  | The URL Canvas should launch to when showing an LTI originality report. Note that this value is inferred from the specified resource handler's message "path" value (See `resource_type_code`) unless it is specified. If this parameter is used a `resource_type_code` must also be specified. |
| `originality_report[workflow_state]` | string | form |  | May be set to "pending", "error", or "scored". If an originality score is provided a workflow state of "scored" will be inferred. |
| `originality_report[error_message]` | string | form |  | A message describing the error. If set, the "workflow_state" will be set to "error." |

**Returns:** `OriginalityReport`

## GET /lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id}

**Show an Originality Report**  —  `show_originality_report_submissions`

Get a single originality report

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `OriginalityReport`

## GET /lti/assignments/{assignment_id}/files/{file_id}/originality_report

**Show an Originality Report**  —  `show_originality_report_files`

Get a single originality report

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `file_id` | string | path | yes | ID |

**Returns:** `OriginalityReport`


---

# Models


## ToolSetting

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `resource_type_code` | string |  | the resource type code of the resource handler to use to display originality reports e.g. `originality_reports` |
| `resource_url` | string |  | a URL that may be used to override the launch URL inferred by the specified resource_type_code. If used a 'resource_type_code' must also be specified. e.g. `http://www.test.com/originality_report` |


## OriginalityReport

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The id of the OriginalityReport e.g. `4` |
| `file_id` | integer |  | The id of the file receiving the originality score e.g. `8` |
| `originality_score` | number |  | A number between 0 and 100 representing the originality score e.g. `0.16` |
| `originality_report_file_id` | integer |  | The ID of the file within Canvas containing the originality report document (if provided) e.g. `23` |
| `originality_report_url` | string |  | A non-LTI launch URL where the originality score of the file may be found. e.g. `http://www.example.com/report` |
| `tool_setting` | ToolSetting |  | A ToolSetting object containing optional 'resource_type_code' and 'resource_url' |
| `error_report` | string |  | A message describing the error. If set, the workflow_state will become 'error.' |
| `submission_time` | datetime |  | The submitted_at date time of the submission. |
| `root_account_id` | integer |  | The id of the root Account associated with the OriginalityReport e.g. `1` |
