# Quiz Extensions

> Canvas LMS REST API — `/quiz_extensions` resource. Base path `/api`.

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/extensions

**Set extensions for student quiz submissions**  —  `set_extensions_for_student_quiz_submissions`

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if you are not allowed to extend quizzes for this course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `quiz_extensions[user_id]` | array[integer] | form | yes | The ID of the user we want to add quiz extensions for. |
| `quiz_extensions[extra_attempts]` | array[integer] | form |  | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. This is limited to 1000 attempts or less. |
| `quiz_extensions[extra_time]` | array[integer] | form |  | The number of extra minutes to allow for all attempts. This will add to the existing time limit on the submission. This is limited to 10080 minutes (1 week) |
| `quiz_extensions[manually_unlocked]` | array[boolean] | form |  | Allow the student to take the quiz even if it's locked for everyone else. |
| `quiz_extensions[extend_from_now]` | array[integer] | form |  | The number of minutes to extend the quiz from the current time. This is mutually exclusive to extend_from_end_at. This is limited to 1440 minutes (24 hours) |
| `quiz_extensions[extend_from_end_at]` | array[integer] | form |  | The number of minutes to extend the quiz beyond the quiz's current ending time. This is mutually exclusive to extend_from_now. This is limited to 1440 minutes (24 hours) |

**Returns:** `void`


---

# Models


## QuizExtension

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `quiz_id` | integer (int64) | yes | The ID of the Quiz the quiz extension belongs to. e.g. `2` |
| `user_id` | integer (int64) | yes | The ID of the Student that needs the quiz extension. e.g. `3` |
| `extra_attempts` | integer (int64) |  | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. e.g. `1` |
| `extra_time` | integer (int64) |  | Amount of extra time allowed for the quiz submission, in minutes. e.g. `60` |
| `manually_unlocked` | boolean |  | The student can take the quiz even if it's locked for everyone else e.g. `True` |
| `end_at` | string (date-time) |  | The time at which the quiz submission will be overdue, and be flagged as a late submission. e.g. `2013-11-07T13:16:18Z` |
