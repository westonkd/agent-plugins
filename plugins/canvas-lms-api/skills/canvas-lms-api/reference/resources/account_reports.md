# Account Reports

> Canvas LMS REST API — `/account_reports` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/reports

**List Available Reports**  —  `list_available_reports`

Returns a paginated list of reports for the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include.  "description_html":: an HTML description of the report, with example output "parameters_html":: an HTML form for the report parameters Allowed: `description_html`, `params_html` |

**Returns:** `void`

## POST /v1/accounts/{account_id}/reports/{report}

**Start a Report**  —  `start_report`

Generates a report instance for the account. Note that "report" in the
request must match one of the available report names. To fetch a list of
available report names and parameters for each report (including whether or
not those parameters are required), see
{api:AccountReportsController#available_reports List Available Reports}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `report` | string | path | yes | ID |
| `parameters` | array[Hash] | form |  | The parameters will vary for each report. To fetch a list of available parameters for each report, see {api:AccountReportsController#available_reports List Available Reports}. A few example parameters have been provided below. Note that the example parameters provided below may not be valid for every report. |
| `parameters[skip_message]` | boolean | form |  | If true, no message will be sent to the user upon completion of the report. |
| `parameters[course_id]` | integer (int64) | form |  | The id of the course to report on. Note: this parameter has been listed to serve as an example and may not be valid for every report. |
| `parameters[users]` | boolean | form |  | If true, user data will be included. If false, user data will be omitted. Note: this parameter has been listed to serve as an example and may not be valid for every report. |

**Returns:** `Report`

## GET /v1/accounts/{account_id}/reports/{report}

**Index of Reports**  —  `index_of_reports`

Shows all reports that have been run for the account of a specific type.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `report` | string | path | yes | ID |

**Returns:** `array[Report]`

## GET /v1/accounts/{account_id}/reports/{report}/{id}

**Status of a Report**  —  `status_of_report`

Returns the status of a report.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `report` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Report`

## DELETE /v1/accounts/{account_id}/reports/{report}/{id}

**Delete a Report**  —  `delete_report`

Deletes a generated report instance.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `report` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Report`

## PUT /v1/accounts/{account_id}/reports/{report}/{id}/abort

**Abort a Report**  —  `abort_report`

Abort a report in progress

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `report` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Report`


---

# Models


## Report

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the report. e.g. `1` |
| `report` | string |  | The type of report. e.g. `sis_export_csv` |
| `file_url` | string |  | The url to the report download. e.g. `https://example.com/some/path` |
| `attachment` | File |  | The attachment api object of the report. Only available after the report has completed. |
| `status` | string |  | The status of the report e.g. `complete` |
| `created_at` | datetime |  | The date and time the report was created. e.g. `2013-12-01T23:59:00-06:00` |
| `started_at` | datetime |  | The date and time the report started processing. e.g. `2013-12-02T00:03:21-06:00` |
| `ended_at` | datetime |  | The date and time the report finished processing. e.g. `2013-12-02T00:03:21-06:00` |
| `run_time` | number |  | The time (in seconds) the report has been waiting to run, has been running so far, or took to run to completion, depending on its current state. e.g. `33.3` |
| `parameters` | ReportParameters |  | The report parameters e.g. `{'course_id': 2, 'start_at': '2012-07-13T10:55:20-06:00', 'end_at': '2012-07-13T10:55:20-06:00'}` |
| `progress` | integer |  | The progress of the report e.g. `100` |
| `current_line` | integer |  | This is the current line count being written to the report. It updates every 1000 records. e.g. `12000` |
| `user` | User |  | The user that initiated the account report. See the Users API for details. |


## ReportParameters

The parameters returned will vary for each report.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `enrollment_term_id` | integer |  | The canvas id of the term to get grades from e.g. `2` |
| `include_deleted` | boolean |  | If true, deleted objects will be included. If false, deleted objects will be omitted. e.g. `False` |
| `course_id` | integer |  | The id of the course to report on e.g. `2` |
| `order` | string |  | The sort order for the csv, Options: 'users', 'courses', 'outcomes'. e.g. `users` |
| `users` | boolean |  | If true, user data will be included. If false, user data will be omitted. e.g. `False` |
| `accounts` | boolean |  | If true, account data will be included. If false, account data will be omitted. e.g. `False` |
| `terms` | boolean |  | If true, term data will be included. If false, term data will be omitted. e.g. `False` |
| `courses` | boolean |  | If true, course data will be included. If false, course data will be omitted. e.g. `False` |
| `sections` | boolean |  | If true, section data will be included. If false, section data will be omitted. e.g. `False` |
| `enrollments` | boolean |  | If true, enrollment data will be included. If false, enrollment data will be omitted. e.g. `False` |
| `groups` | boolean |  | If true, group data will be included. If false, group data will be omitted. e.g. `False` |
| `xlist` | boolean |  | If true, data for crosslisted courses will be included. If false, data for crosslisted courses will be omitted. e.g. `False` |
| `sis_terms_csv` | integer |  | e.g. `1` |
| `sis_accounts_csv` | integer |  | e.g. `1` |
| `include_enrollment_state` | boolean |  | If true, enrollment state will be included. If false, enrollment state will be omitted. Defaults to false. e.g. `False` |
| `enrollment_state` | array[string] |  | Include enrollment state. Defaults to 'all' Options: ['active'\| 'invited'\| 'creation_pending'\| 'deleted'\| 'rejected'\| 'completed'\| 'inactive'\| 'all'] e.g. `['all']` |
| `start_at` | datetime |  | The beginning date for submissions. Max time range is 2 weeks. e.g. `2012-07-13T10:55:20-06:00` |
| `end_at` | datetime |  | The end date for submissions. Max time range is 2 weeks. e.g. `2012-07-13T10:55:20-06:00` |
