# Assessment Question Banks

> Canvas LMS REST API — `/assessment_question_banks` resource. Base path `/api`.

## GET /v1/question_banks

**List question banks**  —  `list_question_banks`

Returns the paginated list of question banks for a given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_type` | string | query | yes | The type of context. Must be either "Course" or "Account". Allowed: `Course`, `Account` |
| `context_id` | integer (int64) | query | yes | The id of the context. |
| `include_question_count` | boolean | query |  | Whether to include the number of questions in each bank. |

**Returns:** `array[AssessmentQuestionBank]`

## GET /v1/question_banks/{id}

**Get a single question bank**  —  `get_single_question_bank`

Returns the question bank with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | integer (int64) | path | yes | The question bank unique identifier. |
| `include_question_count` | boolean | query |  | Whether to include the number of questions in the bank. |

**Returns:** `AssessmentQuestionBank`

## GET /v1/question_banks/{id}/questions

**List assessment questions for a question bank**  —  `list_assessment_questions_for_question_bank`

Returns the paginated list of assessment questions in this bank.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | integer (int64) | path | yes | The question bank unique identifier. |

**Returns:** `array[AssessmentQuestion]`


---

# Models


## AssessmentQuestionBank

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the assessment question bank. e.g. `1` |
| `context_id` | integer (int64) | yes | The ID of the context (course or account) the question bank belongs to. e.g. `2` |
| `context_type` | string | yes | The type of context (Course or Account). e.g. `Course` |
| `title` | string | yes | The title of the question bank. e.g. `Chapter 1 Questions` |
| `workflow_state` | string |  | The workflow state of the question bank. e.g. `active` |
| `assessment_question_count` | integer (int64) |  | The number of questions in the bank. e.g. `10` |
| `context_code` | string |  | The combined context type and ID. e.g. `course_2` |
| `created_at` | string (date-time) |  | The date and time the question bank was created. e.g. `2013-01-01T00:00:00Z` |
| `updated_at` | string (date-time) |  | The date and time the question bank was last updated. e.g. `2013-01-01T00:00:00Z` |


## AssessmentQuestion

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the assessment question. e.g. `1` |
| `position` | integer (int64) |  | The order of the question. e.g. `1` |
| `assessment_question_bank_id` | integer (int64) |  | The ID of the question bank this question belongs to. e.g. `3` |
| `created_at` | string (date-time) |  | The date and time when the assessment question was created. e.g. `2013-01-23T23:59:00-07:00` |
| `question_name` | string |  | The name of the question. e.g. `Prime Number Identification` |
| `question_type` | string |  | The type of the question. e.g. `multiple_choice_question` |
| `question_text` | string |  | The text of the question. e.g. `Which of the following is NOT a prime number?` |
| `points_possible` | number |  | The maximum amount of points possible received for getting this question correct. e.g. `5` |
| `correct_comments` | string |  | The comments to display if the student answers the question correctly. e.g. `That's correct!` |
| `incorrect_comments` | string |  | The comments to display if the student answers incorrectly. e.g. `Unfortunately, that IS a prime number.` |
| `neutral_comments` | string |  | The comments to display regardless of how the student answered. e.g. `Goldbach's conjecture proposes that every even integer greater than 2 can be expressed as the sum of two prime numbers.` |
| `correct_comments_html` | string |  | The HTML version of the comments to display if the student answers the question correctly. e.g. `<p>That's correct!</p>` |
| `incorrect_comments_html` | string |  | The HTML version of the comments to display if the student answers incorrectly. e.g. `<p>Unfortunately, that IS a prime number.</p>` |
| `neutral_comments_html` | string |  | The HTML version of the comments to display regardless of how the student answered. e.g. `<p>Goldbach's conjecture proposes that every even integer greater than 2 can be expressed as the sum of two prime numbers.</p>` |
| `answers` | array[object] |  | An array of available answers. Each answer contains id, text, html, comments, comments_html, and weight properties. |
| `variables` | array |  | Variables for calculated questions. Null for other question types. |
| `formulas` | array |  | Formulas for calculated questions. Null for other question types. |
| `answer_tolerance` | string |  | The tolerance for numerical answers. Null for non-numerical question types. |
| `formula_decimal_places` | integer |  | The number of decimal places for formula results. Null for non-calculated question types. |
| `matches` | array |  | Matching pairs for matching questions. Null for other question types. |
| `matching_answer_incorrect_matches` | array |  | Incorrect match options for matching questions. Null for other question types. |
