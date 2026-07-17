# Quiz Assignment Overrides

> Canvas LMS REST API — `/quiz_assignment_overrides` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes/assignment_overrides

**Retrieve assignment-overridden dates for Classic Quizzes**  —  `retrieve_assignment_overridden_dates_for_classic_quizzes`

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes
based on the assignment overrides active for the current API user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_assignment_overrides[quiz_ids]` | array[integer] | query |  | An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. |

**Returns:** `QuizAssignmentOverrideSetContainer`

## GET /v1/courses/{course_id}/new_quizzes/assignment_overrides

**Retrieve assignment-overridden dates for New Quizzes**  —  `retrieve_assignment_overridden_dates_for_new_quizzes`

Retrieve the actual due-at, unlock-at, and available-at dates for quizzes
based on the assignment overrides active for the current API user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_assignment_overrides[quiz_ids]` | array[integer] | query |  | An array of quiz IDs. If omitted, overrides for all quizzes available to the operating user will be returned. |

**Returns:** `QuizAssignmentOverrideSetContainer`


---

# Models


## QuizAssignmentOverrideSet

Set of assignment-overridden dates for a quiz.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `quiz_id` | string |  | ID of the quiz those dates are for. e.g. `1` |
| `due_dates` | QuizAssignmentOverride |  | An array of quiz assignment overrides. For students, this array will always contain a single item which is the set of dates that apply to that student. For teachers and staff, it may contain more. |
| `all_dates` | QuizAssignmentOverride |  | An array of all assignment overrides active for the quiz. This is visible only to teachers and staff. |


## QuizAssignmentOverrideSetContainer

Container for set of assignment-overridden dates for a quiz.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `quiz_assignment_overrides` | array[QuizAssignmentOverrideSet] |  | The QuizAssignmentOverrideSet |


## QuizAssignmentOverride

Set of assignment-overridden dates for a quiz.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | ID of the assignment override, unless this is the base construct, in which case the 'id' field is omitted. e.g. `1` |
| `due_at` | datetime |  | The date after which any quiz submission is considered late. e.g. `2014-02-21T06:59:59Z` |
| `unlock_at` | datetime |  | Date when the quiz becomes available for taking. |
| `lock_at` | datetime |  | When the quiz will stop being available for taking. A value of null means it can always be taken. e.g. `2014-02-21T06:59:59Z` |
| `title` | string |  | Title of the section this assignment override is for, if any. e.g. `Project X` |
| `base` | boolean |  | If this property is present, it means that dates in this structure are not based on an assignment override, but are instead for all students. e.g. `True` |
