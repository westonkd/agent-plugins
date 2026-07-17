# PollSubmissions

> Canvas LMS REST API — `/poll_submissions` resource. Base path `/api`.

## GET /v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions/{id}

**Get a single poll submission**  —  `get_single_poll_submission`

Returns the poll submission with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `poll_session_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions

**Create a single poll submission**  —  `create_single_poll_submission`

Create a new poll submission for this poll session

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `poll_session_id` | string | path | yes | ID |
| `poll_submissions[poll_choice_id]` | array[integer] | form | yes | The chosen poll choice for this submission. |

**Returns:** `void`


---

# Models


## PollSubmission

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer | yes | The unique identifier for the poll submission. e.g. `1023` |
| `poll_choice_id` | integer |  | The unique identifier of the poll choice chosen for this submission. e.g. `155` |
| `user_id` | integer |  | the unique identifier of the user who submitted this poll submission. e.g. `4555` |
| `created_at` | string (date-time) |  | The date and time the poll submission was submitted. e.g. `2013-11-07T13:16:18Z` |
