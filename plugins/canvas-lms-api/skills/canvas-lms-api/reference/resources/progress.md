# Progress

> Canvas LMS REST API — `/progress` resource. Base path `/api`.

## GET /v1/progress/{id}

**Query progress**  —  `query_progress`

Return completion and status information about an asynchronous job

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `Progress`

## POST /v1/progress/{id}/cancel

**Cancel progress**  —  `cancel_progress`

Cancel an asynchronous job associated with a Progress object
If you include "message" in the POSTed data, it will be set on
the Progress and returned. This is handy to distinguish between
cancel and fail for a workflow_state of "failed".

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `Progress`

## GET /lti/courses/{course_id}/progress/{id}

**Query progress**  —  `query_progress`

Return completion and status information about an asynchronous job

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Progress`


---

# Models


## Progress

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the Progress object e.g. `1` |
| `context_id` | integer |  | the context owning the job. e.g. `1` |
| `context_type` | string |  | e.g. `Account` |
| `user_id` | integer |  | the id of the user who started the job e.g. `123` |
| `tag` | string |  | the type of operation e.g. `course_batch_update` |
| `completion` | integer |  | percent completed e.g. `100` |
| `workflow_state` | string |  | the state of the job one of 'queued', 'running', 'completed', 'failed' e.g. `completed` |
| `created_at` | datetime |  | the time the job was created e.g. `2013-01-15T15:00:00Z` |
| `updated_at` | datetime |  | the time the job was last updated e.g. `2013-01-15T15:04:00Z` |
| `message` | string |  | optional details about the job e.g. `17 courses processed` |
| `results` | object |  | optional results of the job. omitted when job is still pending e.g. `{'id': '123'}` |
| `url` | string |  | url where a progress update can be retrieved with an LTI access token e.g. `https://canvas.example.edu/api/lti/courses/1/progress/1` |
