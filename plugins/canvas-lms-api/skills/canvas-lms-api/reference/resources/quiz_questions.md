# Quiz Questions

> Canvas LMS REST API — `/quiz_questions` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/questions

**List questions in a quiz or a submission**  —  `list_questions_in_quiz_or_submission`

Returns the paginated list of QuizQuestions in this quiz.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `quiz_submission_id` | integer (int64) | query |  | If specified, the endpoint will return the questions that were presented for that submission. This is useful if the quiz has been modified after the submission was created and the latest quiz version's set of questions does not match the submission's. NOTE: you must specify quiz_submission_attempt as well if you specify this parameter. |
| `quiz_submission_attempt` | integer (int64) | query |  | The attempt of the submission you want the questions for. |

**Returns:** `array[QuizQuestion]`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}

**Get a single quiz question**  —  `get_single_quiz_question`

Returns the quiz question with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | integer (int64) | path | yes | The quiz question unique identifier. |

**Returns:** `QuizQuestion`

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/questions

**Create a single quiz question**  —  `create_single_quiz_question`

Create a new quiz question for this quiz

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `question[question_name]` | string | form |  | The name of the question. |
| `question[question_text]` | string | form |  | The text of the question. |
| `question[quiz_group_id]` | integer (int64) | form |  | The id of the quiz group to assign the question to. |
| `question[question_type]` | string | form |  | The type of question. Multiple optional fields depend upon the type of question to be used. Allowed: `calculated_question`, `essay_question`, `file_upload_question`, `fill_in_multiple_blanks_question`, `matching_question`, `multiple_answers_question`, `multiple_choice_question`, `multiple_dropdowns_question`, `numerical_question`, `short_answer_question`, `text_only_question`, `true_false_question` |
| `question[position]` | integer (int64) | form |  | The order in which the question will be displayed in the quiz in relation to other questions. |
| `question[points_possible]` | integer (int64) | form |  | The maximum amount of points received for answering this question correctly. |
| `question[correct_comments]` | string | form |  | The comment to display if the student answers the question correctly. |
| `question[incorrect_comments]` | string | form |  | The comment to display if the student answers incorrectly. |
| `question[neutral_comments]` | string | form |  | The comment to display regardless of how the student answered. |
| `question[text_after_answers]` | string | form |  | no description |
| `question[answers]` | [Answer] | form |  | no description |

**Returns:** `QuizQuestion`

## PUT /v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}

**Update an existing quiz question**  —  `update_existing_quiz_question`

Updates an existing quiz question for this quiz

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | integer (int64) | path | yes | The associated quiz's unique identifier. |
| `id` | integer (int64) | path | yes | The quiz question's unique identifier. |
| `question[question_name]` | string | form |  | The name of the question. |
| `question[question_text]` | string | form |  | The text of the question. |
| `question[quiz_group_id]` | integer (int64) | form |  | The id of the quiz group to assign the question to. |
| `question[question_type]` | string | form |  | The type of question. Multiple optional fields depend upon the type of question to be used. Allowed: `calculated_question`, `essay_question`, `file_upload_question`, `fill_in_multiple_blanks_question`, `matching_question`, `multiple_answers_question`, `multiple_choice_question`, `multiple_dropdowns_question`, `numerical_question`, `short_answer_question`, `text_only_question`, `true_false_question` |
| `question[position]` | integer (int64) | form |  | The order in which the question will be displayed in the quiz in relation to other questions. |
| `question[points_possible]` | integer (int64) | form |  | The maximum amount of points received for answering this question correctly. |
| `question[correct_comments]` | string | form |  | The comment to display if the student answers the question correctly. |
| `question[incorrect_comments]` | string | form |  | The comment to display if the student answers incorrectly. |
| `question[neutral_comments]` | string | form |  | The comment to display regardless of how the student answered. |
| `question[text_after_answers]` | string | form |  | no description |
| `question[answers]` | [Answer] | form |  | no description |

**Returns:** `QuizQuestion`

## DELETE /v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}

**Delete a quiz question**  —  `delete_quiz_question`

<b>204 No Content</b> response code is returned if the deletion was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | integer (int64) | path | yes | The associated quiz's unique identifier |
| `id` | integer (int64) | path | yes | The quiz question's unique identifier |

**Returns:** `void`


---

# Models


## QuizQuestion

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the quiz question. e.g. `1` |
| `quiz_id` | integer (int64) | yes | The ID of the Quiz the question belongs to. e.g. `2` |
| `assessment_question_bank_id` | integer (int64) |  | The ID of the assessment question bank this question belongs to. If assessment_question_bank_id has been enabled by SiteAdmin. e.g. `3` |
| `created_at` | string (date-time) |  | The date and time when the quiz question was created. e.g. `2013-01-23T23:59:00-07:00` |
| `position` | integer (int64) |  | The order in which the question will be retrieved and displayed. e.g. `1` |
| `question_name` | string |  | The name of the question. e.g. `Prime Number Identification` |
| `question_type` | string |  | The type of the question. e.g. `multiple_choice_question` |
| `question_text` | string |  | The text of the question. e.g. `Which of the following is NOT a prime number?` |
| `points_possible` | integer (int64) |  | The maximum amount of points possible received for getting this question correct. e.g. `5` |
| `correct_comments` | string |  | The comments to display if the student answers the question correctly. e.g. `That's correct!` |
| `incorrect_comments` | string |  | The comments to display if the student answers incorrectly. e.g. `Unfortunately, that IS a prime number.` |
| `neutral_comments` | string |  | The comments to display regardless of how the student answered. e.g. `Goldbach's conjecture proposes that every even integer greater than 2 can be expressed as the sum of two prime numbers.` |
| `answers` | array[Answer] |  | An array of available answers to display to the student. |


## Answer

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | The unique identifier for the answer.  Do not supply if this answer is part of a new question e.g. `6656` |
| `answer_text` | string | yes | The text of the answer. e.g. `Constantinople` |
| `answer_weight` | integer (int64) | yes | An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be 100. e.g. `100` |
| `answer_comments` | string |  | Specific contextual comments for a particular answer. e.g. `Remember to check your spelling prior to submitting this answer.` |
| `text_after_answers` | string |  | Used in missing word questions.  The text to follow the missing word e.g. `is the capital of Utah.` |
| `answer_match_left` | string |  | Used in matching questions.  The static value of the answer that will be displayed on the left for students to match for. e.g. `Salt Lake City` |
| `answer_match_right` | string |  | Used in matching questions. The correct match for the value given in answer_match_left.  Will be displayed in a dropdown with the other answer_match_right values.. e.g. `Utah` |
| `matching_answer_incorrect_matches` | string |  | Used in matching questions. A list of distractors, delimited by new lines ( ) that will be seeded with all the answer_match_right values. e.g. `Nevada California Washington` |
| `numerical_answer_type` | string |  | Used in numerical questions.  Values can be 'exact_answer', 'range_answer', or 'precision_answer'. e.g. `exact_answer` |
| `exact` | integer (int64) |  | Used in numerical questions of type 'exact_answer'.  The value the answer should equal. e.g. `42` |
| `margin` | integer (int64) |  | Used in numerical questions of type 'exact_answer'. The margin of error allowed for the student's answer. e.g. `4` |
| `approximate` | number (float64) |  | Used in numerical questions of type 'precision_answer'.  The value the answer should equal. e.g. `1234600000.0` |
| `precision` | integer (int64) |  | Used in numerical questions of type 'precision_answer'. The numerical precision that will be used when comparing the student's answer. e.g. `4` |
| `start` | integer (int64) |  | Used in numerical questions of type 'range_answer'. The start of the allowed range (inclusive). e.g. `1` |
| `end` | integer (int64) |  | Used in numerical questions of type 'range_answer'. The end of the allowed range (inclusive). e.g. `10` |
| `blank_id` | integer (int64) |  | Used in fill in multiple blank and multiple dropdowns questions. e.g. `1170` |
