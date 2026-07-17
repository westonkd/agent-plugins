# Poll Sessions

> Canvas LMS REST API — `/poll_sessions` resource. Base path `/api`.

## GET /v1/polls/{poll_id}/poll_sessions

**List poll sessions for a poll**  —  `list_poll_sessions_for_poll`

Returns the paginated list of PollSessions in this poll.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/polls/{poll_id}/poll_sessions/{id}

**Get the results for a single poll session**  —  `get_results_for_single_poll_session`

Returns the poll session with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/polls/{poll_id}/poll_sessions

**Create a single poll session**  —  `create_single_poll_session`

Create a new poll session for this poll

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `poll_sessions[course_id]` | array[integer] | form | yes | The id of the course this session is associated with. |
| `poll_sessions[course_section_id]` | array[integer] | form |  | The id of the course section this session is associated with. |
| `poll_sessions[has_public_results]` | array[boolean] | form |  | Whether or not results are viewable by students. |

**Returns:** `void`

## PUT /v1/polls/{poll_id}/poll_sessions/{id}

**Update a single poll session**  —  `update_single_poll_session`

Update an existing poll session for this poll

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `poll_sessions[course_id]` | array[integer] | form |  | The id of the course this session is associated with. |
| `poll_sessions[course_section_id]` | array[integer] | form |  | The id of the course section this session is associated with. |
| `poll_sessions[has_public_results]` | array[boolean] | form |  | Whether or not results are viewable by students. |

**Returns:** `void`

## DELETE /v1/polls/{poll_id}/poll_sessions/{id}

**Delete a poll session**  —  `delete_poll_session`

<b>204 No Content</b> response code is returned if the deletion was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/polls/{poll_id}/poll_sessions/{id}/open

**Open a poll session**  —  `open_poll_session`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/polls/{poll_id}/poll_sessions/{id}/close

**Close an opened poll session**  —  `close_opened_poll_session`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/poll_sessions/opened

**List opened poll sessions**  —  `list_opened_poll_sessions`

A paginated list of all opened poll sessions available to the current user.

**Returns:** `void`

## GET /v1/poll_sessions/closed

**List closed poll sessions**  —  `list_closed_poll_sessions`

A paginated list of all closed poll sessions available to the current user.

**Returns:** `void`


---

# Models


## PollSession

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer | yes | The unique identifier for the poll session. e.g. `1023` |
| `poll_id` | integer | yes | The id of the Poll this poll session is associated with e.g. `55` |
| `course_id` | integer | yes | The id of the Course this poll session is associated with e.g. `1111` |
| `course_section_id` | integer |  | The id of the Course Section this poll session is associated with e.g. `444` |
| `is_published` | boolean |  | Specifies whether or not this poll session has been published for students to participate in. e.g. `true` |
| `has_public_results` | boolean |  | Specifies whether the results are viewable by students. e.g. `true` |
| `created_at` | string (date-time) |  | The time at which the poll session was created. e.g. `2014-01-07T15:16:18Z` |
| `results` | object |  | The results of the submissions of the poll. Each key is the poll choice id, and the value is the count of submissions. e.g. `{'144': 10, '145': 3, '146': 27, '147': 8}` |
| `poll_submissions` | PollSubmission |  | If the poll session has public results, this will return an array of all submissions, viewable by both students and teachers. If the results are not public, for students it will return their submission only. |
