# Course Quiz Extensions

> Canvas LMS REST API — `/course_quiz_extensions` resource. Base path `/api`.

## POST /v1/courses/{course_id}/quiz_extensions

**Set extensions for student quiz submissions**  —  `set_extensions_for_student_quiz_submissions`

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if you are not allowed to extend quizzes for this course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `user_id` | integer (int64) | form | yes | The ID of the user we want to add quiz extensions for. |
| `extra_attempts` | integer (int64) | form |  | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. This is limited to 1000 attempts or less. |
| `extra_time` | integer (int64) | form |  | The number of extra minutes to allow for all attempts. This will add to the existing time limit on the submission. This is limited to 10080 minutes (1 week) |
| `manually_unlocked` | boolean | form |  | Allow the student to take the quiz even if it's locked for everyone else. |
| `extend_from_now` | integer (int64) | form |  | The number of minutes to extend the quiz from the current time. This is mutually exclusive to extend_from_end_at. This is limited to 1440 minutes (24 hours) |
| `extend_from_end_at` | integer (int64) | form |  | The number of minutes to extend the quiz beyond the quiz's current ending time. This is mutually exclusive to extend_from_now. This is limited to 1440 minutes (24 hours) |

**Returns:** `void`


---

# Models


## CourseQuizExtension

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `user_id` | integer (int64) | yes | The ID of the Student that needs the quiz extension. e.g. `3` |
| `extra_attempts` | integer (int64) |  | Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. e.g. `1` |
| `extra_time` | integer (int64) |  | Amount of extra time allowed for the quiz submission, in minutes. e.g. `60` |
| `manually_unlocked` | boolean |  | The student can take the quiz even if it's locked for everyone else e.g. `True` |
| `end_at` | string (date-time) |  | The time at which the quiz submission will be overdue, and be flagged as a late submission. e.g. `2013-11-07T13:16:18Z` |
