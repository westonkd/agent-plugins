# Microsoft Sync - Groups

> Canvas LMS REST API — `/microsoft_sync___groups` resource. Base path `/api`.


---

# Models


## MicrosoftSync::Group

The membership of a Microsoft group as well as the status of syncing Canvas enrollments to that group.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The id of the MicrosoftSync::Group e.g. `4` |
| `course_id` | integer |  | The id of the course related to the MicrosoftSync::Group e.g. `8` |
| `workflow_state` | string |  | The current state of the MicrosoftSync::Group e.g. `pending` Allowed: `pending`, `running`, `errored`, `completed` |
| `job_state` | string |  | Internal data about the last step run for a job in the 'retrying' state. Only returned for site admins |
| `last_synced_at` | datetime |  | The time of the last successful sync e.g. `2012-07-20T15:00:00-06:00` |
| `last_error` | string |  | The last error encountered during an attempted sync |
| `last_error_report_id` | integer |  | The ErrorReport ID for the last_error. Only returned for site admins |
| `root_account_id` | integer |  | The root account the MicrosoftSync::Group belongs to e.g. `1` |
| `created_at` | datetime |  | The time the MicrosoftSync::Group was created e.g. `2012-07-20T15:00:00-06:00` |
| `updated_at` | datetime |  | The time the MicrosoftSync::Group was updated e.g. `2012-07-20T15:00:00-06:00` |
| `debug_info` | array[object] |  | List of strings with debugging info (localized). Only returned for site admins. e.g. `[{'timestamp': '2024-01-03T11:50:07Z', 'msg': '2 Canvas users without corresponding Microsoft user:', 'user_ids': [1, 3]}]` |
