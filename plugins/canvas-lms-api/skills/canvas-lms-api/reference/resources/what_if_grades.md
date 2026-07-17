# What If Grades

> Canvas LMS REST API — `/what_if_grades` resource. Base path `/api`.

## PUT /v1/submissions/{id}/what_if_grades

**Update a submission's what-if score and calculate grades**  —  `update_submission_s_what_if_score_and_calculate_grades`

Enter a what if score for a submission and receive the calculated grades
Grade calculation is a costly operation, so this API should be used sparingly

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `student_entered_score` | number (float) | form |  | The score the student wants to test |

**Returns:** `array[{"grades": Grades, "submission": Submission}]`

## PUT /v1/courses/{course_id}/what_if_grades/reset

**Reset the what-if scores for the current user for an entire course and recalculate grades**  —  `reset_what_if_scores_for_current_user_for_entire_course_and_recalculate_grades`

Resets all what-if scores for a student in a course and recalculates grades.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[{"grades": Grades}]`


---

# Models


## Grade

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `grade` | number |  | The grade for the course e.g. `120.0` |
| `total` | number |  | The total points earned in the course e.g. `24.0` |
| `possible` | number |  | The total points possible for the course e.g. `20.0` |
| `dropped` | array |  | The dropped grades for the course e.g. `[]` |


## AssignmentGroupGrade

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the Assignment Group e.g. `123` |
| `global_id` | integer |  | The global ID of the Assignment Group e.g. `10000000000001` |
| `score` | number |  | The score for the Assignment Group e.g. `20.0` |
| `possible` | number |  | The total points possible for the Assignment Group e.g. `10.0` |
| `weight` | number |  | The weight for the Assignment Group e.g. `0.0` |
| `grade` | number |  | The grade for the Assignment Group e.g. `200.0` |
| `dropped` | array |  | The dropped grades for the Assignment Group e.g. `[]` |


## GradeGroup

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `submission_id` | AssignmentGroupGrade |  |  |


## Grades

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `current` | Grade |  |  |
| `current_groups` | GradeGroup |  |  |
| `final` | Grade |  |  |
| `final_groups` | GradeGroup |  |  |


## Submission

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the submission e.g. `123` |
| `student_entered_score` | string |  | The score the student wants to test e.g. `20.0` |
