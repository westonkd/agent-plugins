# Course Reports

> Canvas LMS REST API — `/course_reports` resource. Base path `/api`.

## GET /v1/courses/{course_id}/reports/{report_type}/{id}

**Status of a Report**  —  `status_of_report`

Returns the status of a report.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `report_type` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Report`

## POST /v1/courses/{course_id}/reports/{report_type}

**Start a Report**  —  `start_report`

Generates a report instance for the account. Note that "report" in the
request must match one of the available report names.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the course to report on. |
| `report_type` | string | path | yes | The type of report to generate. |
| `parameters` | array[Hash] | form |  | The parameters will vary for each report. A few example parameters have been provided below. Note: the example parameters provided below may not be valid for every report. |
| `parameters[section_ids]` | array[integer] | form |  | The sections of the course to report on. Note: this parameter has been listed to serve as an example and may not be valid for every report. |

**Returns:** `Report`

## GET /v1/courses/{course_id}/reports/{report_type}

**Status of last Report**  —  `status_of_last_report`

Returns the status of the last report initiated by the current user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `report_type` | string | path | yes | ID |

**Returns:** `Report`


---

# Models


## Report

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the report. e.g. `1` |
| `file_url` | string |  | The url to the report download. e.g. `https://example.com/some/path` |
| `attachment` | File |  | The attachment api object of the report. Only available after the report has completed. |
| `status` | string |  | The status of the report e.g. `complete` |
| `created_at` | datetime |  | The date and time the report was created. e.g. `2013-12-01T23:59:00-06:00` |
| `started_at` | datetime |  | The date and time the report started processing. e.g. `2013-12-02T00:03:21-06:00` |
| `ended_at` | datetime |  | The date and time the report finished processing. e.g. `2013-12-02T00:03:21-06:00` |
| `parameters` | ReportParameters |  | The report parameters e.g. `{'course_id': 2, 'start_at': '2012-07-13T10:55:20-06:00', 'end_at': '2012-07-13T10:55:20-06:00'}` |
| `progress` | integer |  | The progress of the report e.g. `100` |


## ReportParameters

The parameters returned will vary for each report.
