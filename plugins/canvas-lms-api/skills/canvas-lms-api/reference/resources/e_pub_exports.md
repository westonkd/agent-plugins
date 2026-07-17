# ePub Exports

> Canvas LMS REST API — `/e_pub_exports` resource. Base path `/api`.

## GET /v1/epub_exports

**List courses with their latest ePub export**  —  `list_courses_with_their_latest_epub_export`

A paginated list of all courses a user is actively participating in, and
the latest ePub export associated with the user & course.

**Returns:** `array[CourseEpubExport]`

## POST /v1/courses/{course_id}/epub_exports

**Create ePub Export**  —  `create_epub_export`

Begin an ePub export for a course.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The export's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:EpubExportsController#show Show content export} endpoint
to retrieve a download URL for the exported content.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `EpubExport`

## GET /v1/courses/{course_id}/epub_exports/{id}

**Show ePub export**  —  `show_epub_export`

Get information about a single ePub export.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `EpubExport`


---

# Models


## CourseEpubExport

Combination of a Course & EpubExport.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the course e.g. `101` |
| `name` | string |  | the name for the course e.g. `Maths 101` |
| `epub_export` | EpubExport |  | ePub export API object |


## EpubExport

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the export e.g. `101` |
| `created_at` | datetime |  | the date and time this export was requested e.g. `2014-01-01T00:00:00Z` |
| `attachment` | File |  | attachment api object for the export ePub (not present until the export completes) e.g. `{'url': 'https://example.com/api/v1/attachments/789?download_frd=1'}` |
| `progress_url` | string |  | The api endpoint for polling the current progress e.g. `https://example.com/api/v1/progress/4` |
| `user_id` | integer |  | The ID of the user who started the export e.g. `4` |
| `workflow_state` | string |  | Current state of the ePub export: created exporting exported generating generated failed e.g. `exported` |
