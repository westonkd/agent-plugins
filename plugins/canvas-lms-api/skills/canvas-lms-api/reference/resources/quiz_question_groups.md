# Quiz Question Groups

> Canvas LMS REST API — `/quiz_question_groups` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/groups

**List question groups in a quiz**  —  `list_question_groups_in_quiz`

Returns a list of question groups in a quiz.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}

**Get a single quiz group**  —  `get_single_quiz_group`

Returns details of the quiz group with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `QuizGroup`

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/groups

**Create a question group**  —  `create_question_group`

Create a new question group for this quiz

<b>201 Created</b> response code is returned if the creation was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `quiz_groups[name]` | array[string] | form |  | The name of the question group. |
| `quiz_groups[pick_count]` | array[integer] | form |  | The number of questions to randomly select for this group. |
| `quiz_groups[question_points]` | array[integer] | form |  | The number of points to assign to each question in the group. |
| `quiz_groups[assessment_question_bank_id]` | array[integer] | form |  | The id of the assessment question bank to pull questions from. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}

**Update a question group**  —  `update_question_group`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `quiz_groups[name]` | array[string] | form |  | The name of the question group. |
| `quiz_groups[pick_count]` | array[integer] | form |  | The number of questions to randomly select for this group. |
| `quiz_groups[question_points]` | array[integer] | form |  | The number of points to assign to each question in the group. |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}

**Delete a question group**  —  `delete_question_group`

Delete a question group

<b>204 No Content<b> response code is returned if the deletion was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder

**Reorder question groups**  —  `reorder_question_groups`

Change the order of the quiz questions within the group

<b>204 No Content<b> response code is returned if the reorder was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `order[id]` | array[integer] | form | yes | The associated item's unique identifier |
| `order[type]` | array[string] | form |  | The type of item is always 'question' for a group Allowed: `question` |

**Returns:** `void`


---

# Models


## QuizGroup

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the question group. e.g. `1` |
| `quiz_id` | integer (int64) | yes | The ID of the Quiz the question group belongs to. e.g. `2` |
| `name` | string |  | The name of the question group. e.g. `Fraction questions` |
| `pick_count` | integer (int64) |  | The number of questions to pick from the group to display to the student. e.g. `3` |
| `question_points` | integer (int64) |  | The amount of points allotted to each question in the group. e.g. `10` |
| `assessment_question_bank_id` | integer (int64) |  | The ID of the Assessment question bank to pull questions from. e.g. `2` |
| `position` | integer (int64) |  | The order in which the question group will be retrieved and displayed. e.g. `1` |
