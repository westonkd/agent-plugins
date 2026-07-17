# Quiz Submissions

> Canvas LMS REST API — `/quiz_submissions` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/submissions

**Get all quiz submissions.**  —  `get_all_quiz_submissions`

Get a list of all submissions for this quiz. Users who can view or manage
grades for a course will have submissions from multiple users returned. A
user who can only submit will have only their own submissions returned. When
a user has an in-progress submission, only that submission is returned. When
there isn't an in-progress quiz_submission, all completed submissions,
including previous attempts, are returned.

<b>200 OK</b> response code is returned if the request was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the quiz submission. Allowed: `submission`, `quiz`, `user` |

**Returns:** `void`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/submission

**Get the quiz submission.**  —  `get_quiz_submission`

Get the submission for this quiz for the current user.

<b>200 OK</b> response code is returned if the request was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the quiz submission. Allowed: `submission`, `quiz`, `user` |

**Returns:** `void`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}

**Get a single quiz submission.**  —  `get_single_quiz_submission`

Get a single quiz submission.

<b>200 OK</b> response code is returned if the request was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the quiz submission. Allowed: `submission`, `quiz`, `user` |

**Returns:** `void`

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/submissions

**Create the quiz submission (start a quiz-taking session)**  —  `create_quiz_submission_start_quiz_taking_session`

Start taking a Quiz by creating a QuizSubmission which you can use to answer
questions and submit your answers.

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>400 Bad Request</b> if the quiz is locked
* <b>403 Forbidden</b> if an invalid access code is specified
* <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
* <b>409 Conflict</b> if a QuizSubmission already exists for this user and quiz

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `access_code` | string | form |  | Access code for the Quiz, if any. |
| `preview` | boolean | form |  | Whether this should be a preview QuizSubmission and not count towards the user's course record. Teachers only. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}

**Update student question scores and comments.**  —  `update_student_question_scores_and_comments`

Update the amount of points a student has scored for questions they've
answered, provide comments for the student about their answer(s), or simply
fudge the total score by a specific amount of points.

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if you are not a teacher in this course
* <b>400 Bad Request</b> if the attempt parameter is missing or invalid
* <b>400 Bad Request</b> if the specified QS attempt is not yet complete

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `quiz_submissions[attempt]` | array[integer] | form | yes | The attempt number of the quiz submission that should be updated. This attempt MUST be already completed. |
| `quiz_submissions[fudge_points]` | array[number] | form |  | Amount of positive or negative points to fudge the total score by. |
| `quiz_submissions[questions]` | array[Hash] | form |  | A set of scores and comments for each question answered by the student. The keys are the question IDs, and the values are hashes of `score` and `comment` entries. See {Appendix: Manual Scoring} for more on this parameter. |

**Returns:** `void`

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete

**Complete the quiz submission (turn it in).**  —  `complete_quiz_submission_turn_it_in`

Complete the quiz submission by marking it as complete and grading it. When
the quiz submission has been marked as complete, no further modifications
will be allowed.

<b>Responses</b>

* <b>200 OK</b> if the request was successful
* <b>403 Forbidden</b> if an invalid access code is specified
* <b>403 Forbidden</b> if the Quiz's IP filter restriction does not pass
* <b>403 Forbidden</b> if an invalid token is specified
* <b>400 Bad Request</b> if the QS is already complete
* <b>400 Bad Request</b> if the attempt parameter is missing
* <b>400 Bad Request</b> if the attempt parameter is not the latest attempt

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `attempt` | integer (int64) | form | yes | The attempt number of the quiz submission that should be completed. Note that this must be the latest attempt index, as earlier attempts can not be modified. |
| `validation_token` | string | form | yes | The unique validation token you received when this Quiz Submission was created. |
| `access_code` | string | form |  | Access code for the Quiz, if any. |

**Returns:** `void`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/time

**Get current quiz submission times.**  —  `get_current_quiz_submission_times`

Get the current timing data for the quiz attempt, both the end_at timestamp
and the time_left parameter.

<b>Responses</b>

* <b>200 OK</b> if the request was successful

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## QuizSubmission

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the quiz submission. e.g. `1` |
| `quiz_id` | integer (int64) | yes | The ID of the Quiz the quiz submission belongs to. e.g. `2` |
| `user_id` | integer (int64) |  | The ID of the Student that made the quiz submission. e.g. `3` |
| `submission_id` | integer (int64) |  | The ID of the Submission the quiz submission represents. e.g. `1` |
| `started_at` | string (date-time) |  | The time at which the student started the quiz submission. e.g. `2013-11-07T13:16:18Z` |
| `finished_at` | string (date-time) |  | The time at which the student submitted the quiz submission. e.g. `2013-11-07T13:16:18Z` |
| `end_at` | string (date-time) |  | The time at which the quiz submission will be overdue, and be flagged as a late submission. e.g. `2013-11-07T13:16:18Z` |
| `attempt` | integer (int64) |  | For quizzes that allow multiple attempts, this field specifies the quiz submission attempt number. e.g. `3` |
| `extra_attempts` | integer (int64) |  | Number of times the student was allowed to re-take the quiz over the multiple-attempt limit. e.g. `1` |
| `extra_time` | integer (int64) |  | Amount of extra time allowed for the quiz submission, in minutes. e.g. `60` |
| `manually_unlocked` | boolean |  | The student can take the quiz even if it's locked for everyone else e.g. `True` |
| `time_spent` | integer (int64) |  | Amount of time spent, in seconds. e.g. `300` |
| `score` | integer (int64) |  | The score of the quiz submission, if graded. e.g. `3` |
| `score_before_regrade` | integer (int64) |  | The original score of the quiz submission prior to any re-grading. e.g. `2` |
| `kept_score` | integer (int64) |  | For quizzes that allow multiple attempts, this is the score that will be used, which might be the score of the latest, or the highest, quiz submission. e.g. `5` |
| `fudge_points` | integer (int64) |  | Number of points the quiz submission's score was fudged by. e.g. `1` |
| `has_seen_results` | boolean |  | Whether the student has viewed their results to the quiz. e.g. `True` |
| `workflow_state` | string |  | The current state of the quiz submission. Possible values: ['untaken'\|'pending_review'\|'complete'\|'settings_only'\|'preview']. e.g. `untaken` |
| `overdue_and_needs_submission` | boolean |  | Indicates whether the quiz submission is overdue and needs submission e.g. `false` |
