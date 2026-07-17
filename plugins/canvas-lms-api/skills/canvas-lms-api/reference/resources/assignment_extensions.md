# Assignment Extensions

> Canvas LMS REST API — `/assignment_extensions` resource. Base path `/api`.

## POST /v1/courses/{course_id}/assignments/{assignment_id}/extensions

**Set extensions for student assignment submissions**  —  `set_extensions_for_student_assignment_submissions`

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if you are not allowed to extend assignments for this course
* <b>400 Bad Request</b> if any of the extensions are invalid

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `assignment_extensions[user_id]` | array[integer] | form | yes | The ID of the user we want to add assignment extensions for. |
| `assignment_extensions[extra_attempts]` | array[integer] | form | yes | Number of times the student is allowed to re-take the assignment over the limit. |

**Returns:** `void`


---

# Models


## AssignmentExtension

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `assignment_id` | integer (int64) | yes | The ID of the Assignment the extension belongs to. e.g. `2` |
| `user_id` | integer (int64) | yes | The ID of the Student that needs the assignment extension. e.g. `3` |
| `extra_attempts` | integer (int64) |  | Number of times the student is allowed to re-submit the assignment e.g. `2` |
