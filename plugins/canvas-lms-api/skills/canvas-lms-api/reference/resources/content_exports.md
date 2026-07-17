# Content Exports

> Canvas LMS REST API — `/content_exports` resource. Base path `/api`.

## GET /v1/courses/{course_id}/content_exports

**List content exports**  —  `list_content_exports_courses`

A paginated list of the past and pending content export jobs for a course,
group, or user. Exports are returned newest first.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[ContentExport]`

## GET /v1/groups/{group_id}/content_exports

**List content exports**  —  `list_content_exports_groups`

A paginated list of the past and pending content export jobs for a course,
group, or user. Exports are returned newest first.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[ContentExport]`

## GET /v1/users/{user_id}/content_exports

**List content exports**  —  `list_content_exports_users`

A paginated list of the past and pending content export jobs for a course,
group, or user. Exports are returned newest first.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[ContentExport]`

## GET /v1/courses/{course_id}/content_exports/{id}

**Show content export**  —  `show_content_export_courses`

Get information about a single content export.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentExport`

## GET /v1/groups/{group_id}/content_exports/{id}

**Show content export**  —  `show_content_export_groups`

Get information about a single content export.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentExport`

## GET /v1/users/{user_id}/content_exports/{id}

**Show content export**  —  `show_content_export_users`

Get information about a single content export.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentExport`

## POST /v1/courses/{course_id}/content_exports

**Export content**  —  `export_content_courses`

Begin a content export job for a course, group, or user.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The migration's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
to retrieve a download URL for the exported content.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `export_type` | string | form | yes | "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format "qti":: Export quizzes from a course in the QTI format "zip":: Export files from a course, group, or user in a zip file Allowed: `common_cartridge`, `qti`, `zip` |
| `skip_notifications` | boolean | form |  | Don't send the notifications about the export to the user. Default: false |
| `select` | Hash | form |  | The select parameter allows exporting specific data. The keys are object types like 'files', 'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an integer or a string.  Multiple object types can be selected in the same call. However, not all object types are valid for every export_type. Common Cartridge supports all object types. Zip and QTI only support the object types as described below.  "folders":: Also supported for zip export_type. "files":: Also supported for zip export_type. "quizzes":: Also supported for qti export_type. Allowed: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics` |

**Returns:** `ContentExport`

## POST /v1/groups/{group_id}/content_exports

**Export content**  —  `export_content_groups`

Begin a content export job for a course, group, or user.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The migration's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
to retrieve a download URL for the exported content.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `export_type` | string | form | yes | "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format "qti":: Export quizzes from a course in the QTI format "zip":: Export files from a course, group, or user in a zip file Allowed: `common_cartridge`, `qti`, `zip` |
| `skip_notifications` | boolean | form |  | Don't send the notifications about the export to the user. Default: false |
| `select` | Hash | form |  | The select parameter allows exporting specific data. The keys are object types like 'files', 'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an integer or a string.  Multiple object types can be selected in the same call. However, not all object types are valid for every export_type. Common Cartridge supports all object types. Zip and QTI only support the object types as described below.  "folders":: Also supported for zip export_type. "files":: Also supported for zip export_type. "quizzes":: Also supported for qti export_type. Allowed: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics` |

**Returns:** `ContentExport`

## POST /v1/users/{user_id}/content_exports

**Export content**  —  `export_content_users`

Begin a content export job for a course, group, or user.

You can use the {api:ProgressController#show Progress API} to track the
progress of the export. The migration's progress is linked to with the
_progress_url_ value.

When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
to retrieve a download URL for the exported content.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `export_type` | string | form | yes | "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format "qti":: Export quizzes from a course in the QTI format "zip":: Export files from a course, group, or user in a zip file Allowed: `common_cartridge`, `qti`, `zip` |
| `skip_notifications` | boolean | form |  | Don't send the notifications about the export to the user. Default: false |
| `select` | Hash | form |  | The select parameter allows exporting specific data. The keys are object types like 'files', 'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an integer or a string.  Multiple object types can be selected in the same call. However, not all object types are valid for every export_type. Common Cartridge supports all object types. Zip and QTI only support the object types as described below.  "folders":: Also supported for zip export_type. "files":: Also supported for zip export_type. "quizzes":: Also supported for qti export_type. Allowed: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics` |

**Returns:** `ContentExport`


---

# Models


## ContentExport

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the export e.g. `101` |
| `created_at` | datetime |  | the date and time this export was requested e.g. `2014-01-01T00:00:00Z` |
| `export_type` | string |  | the type of content migration: 'common_cartridge' or 'qti' e.g. `common_cartridge` |
| `attachment` | File |  | attachment api object for the export package (not present before the export completes or after it becomes unavailable for download.) e.g. `{'url': 'https://example.com/api/v1/attachments/789?download_frd=1'}` |
| `progress_url` | string |  | The api endpoint for polling the current progress e.g. `https://example.com/api/v1/progress/4` |
| `user_id` | integer |  | The ID of the user who started the export e.g. `4` |
| `workflow_state` | string |  | Current state of the content migration: created exporting exported failed e.g. `exported` |
