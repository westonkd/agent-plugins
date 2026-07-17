# Quiz IP Filters

> Canvas LMS REST API — `/quiz_ip_filters` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/ip_filters

**Get available quiz IP filters.**  —  `get_available_quiz_ip_filters`

Get a list of available IP filters for this Quiz.

<b>200 OK</b> response code is returned if the request was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## QuizIPFilter

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `name` | string | yes | A unique name for the filter. e.g. `Current Filter` |
| `account` | string | yes | Name of the Account (or Quiz) the IP filter is defined in. e.g. `Some Quiz` |
| `filter` | string | yes | An IP address (or range mask) this filter embodies. e.g. `192.168.1.1/24` |
