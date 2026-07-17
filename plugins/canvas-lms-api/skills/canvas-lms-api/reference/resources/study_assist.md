# Study Assist

> Canvas LMS REST API — `/study_assist` resource. Base path `/api`.

## POST /v1/courses/{course_id}/study_assist

**Request a study assist response**  —  `request_study_assist_response`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `prompt` | string | form |  | Short prompt (e.g. "Summarize"). Blank returns chips. |
| `state` | Hash | form |  | Content state with courseID, and one of pageID or fileID. |
| `regenerate` | boolean | form |  | If true, bypasses the LLM response cache. |

**Returns:** `AssistResponse`
