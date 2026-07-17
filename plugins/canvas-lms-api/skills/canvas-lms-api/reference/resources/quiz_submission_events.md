# Quiz Submission Events

> Canvas LMS REST API — `/quiz_submission_events` resource. Base path `/api`.

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events

**Submit captured events**  —  `submit_captured_events`

Store a set of events which were captured during a quiz taking session.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `quiz_submission_events` | array[Array] | form | yes | The submission events to be recorded |

**Returns:** `void`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events

**Retrieve captured events**  —  `retrieve_captured_events`

Retrieve the set of events captured during a specific submission attempt.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `attempt` | integer (int64) | query |  | The specific submission attempt to look up the events for. If unspecified, the latest attempt will be used. |

**Returns:** `void`


---

# Models


## QuizSubmissionEvent

An event passed from the Quiz Submission take page

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `created_at` | datetime |  | a timestamp record of creation time e.g. `2014-10-08T19:29:58Z` |
| `event_type` | string |  | the type of event being sent e.g. `question_answered` |
| `event_data` | object |  | custom contextual data for the specific event type e.g. `{'answer': '42'}` |
