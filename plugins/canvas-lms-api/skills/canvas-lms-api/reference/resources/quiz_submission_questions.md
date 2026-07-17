# Quiz Submission Questions

> Canvas LMS REST API — `/quiz_submission_questions` resource. Base path `/api`.

## GET /v1/quiz_submissions/{quiz_submission_id}/questions

**Get all quiz submission questions.**  —  `get_all_quiz_submission_questions`

Get a list of all the question records for this quiz submission.

<b>200 OK</b> response code is returned if the request was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `quiz_submission_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the quiz submission question. Allowed: `quiz_question` |

**Returns:** `void`

## POST /v1/quiz_submissions/{quiz_submission_id}/questions

**Answering questions**  —  `answering_questions`

Provide or update an answer to one or more QuizQuestions.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `quiz_submission_id` | string | path | yes | ID |
| `attempt` | integer (int64) | form | yes | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified. |
| `validation_token` | string | form | yes | The unique validation token you received when the Quiz Submission was created. |
| `access_code` | string | form |  | Access code for the Quiz, if any. |
| `quiz_questions` | array[QuizSubmissionQuestion] | form |  | Set of question IDs and the answer value.  See {Appendix: Question Answer Formats} for the accepted answer formats for each question type. |

**Returns:** `array[QuizSubmissionQuestion]`

## GET /v1/quiz_submissions/{quiz_submission_id}/questions/{id}/formatted_answer

**Get a formatted student numerical answer.**  —  `get_formatted_student_numerical_answer`

Matches the intended behavior of the UI when a numerical answer is entered
and returns the resulting formatted number

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `quiz_submission_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `answer` | Numeric | query | yes | no description |

**Returns:** `void`

## PUT /v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag

**Flagging a question.**  —  `flagging_question`

Set a flag on a quiz question to indicate that you want to return to it
later.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `quiz_submission_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `attempt` | integer (int64) | form | yes | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified. |
| `validation_token` | string | form | yes | The unique validation token you received when the Quiz Submission was created. |
| `access_code` | string | form |  | Access code for the Quiz, if any. |

**Returns:** `void`

## PUT /v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag

**Unflagging a question.**  —  `unflagging_question`

Remove the flag that you previously set on a quiz question after you've
returned to it.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `quiz_submission_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `attempt` | integer (int64) | form | yes | The attempt number of the quiz submission being taken. Note that this must be the latest attempt index, as questions for earlier attempts can not be modified. |
| `validation_token` | string | form | yes | The unique validation token you received when the Quiz Submission was created. |
| `access_code` | string | form |  | Access code for the Quiz, if any. |

**Returns:** `void`


---

# Models


## QuizSubmissionQuestion

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the QuizQuestion this answer is for. e.g. `1` |
| `flagged` | boolean |  | Whether this question is flagged. e.g. `True` |
| `answer` | string |  | The provided answer (if any) for this question. The format of this parameter depends on the type of the question, see the Appendix for more information. |
| `answers` | array[string] |  | The possible answers for this question when those possible answers are necessary.  The presence of this parameter is dependent on permissions. |
