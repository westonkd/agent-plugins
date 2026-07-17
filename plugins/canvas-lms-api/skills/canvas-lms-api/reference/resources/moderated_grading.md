# Moderated Grading

> Canvas LMS REST API — `/moderated_grading` resource. Base path `/api`.

## GET /v1/courses/{course_id}/assignments/{assignment_id}/moderated_students

**List students selected for moderation**  —  `list_students_selected_for_moderation`

Returns a paginated list of students selected for moderation

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |

**Returns:** `array[User]`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/moderated_students

**Select students for moderation**  —  `select_students_for_moderation`

Returns an array of users that were selected for moderation

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `student_ids` | array[number] | form |  | user ids for students to select for moderation |

**Returns:** `array[User]`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/bulk_select

**Bulk select provisional grades**  —  `bulk_select_provisional_grades`

Choose which provisional grades will be received by associated students for an assignment.
The caller must be the final grader for the assignment or an admin with :select_final_grade rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/status

**Show provisional grade status for a student**  —  `show_provisional_grade_status_for_student`

Tell whether the student's submission needs one or more provisional grades.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `student_id` | integer (int64) | query |  | The id of the student to show the status for |

**Returns:** `void`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/select

**Select provisional grade**  —  `select_provisional_grade`

Choose which provisional grade the student should receive for a submission.
The caller must be the final grader for the assignment or an admin with :select_final_grade rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `provisional_grade_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/publish

**Publish provisional grades for an assignment**  —  `publish_provisional_grades_for_assignment`

Publish the selected provisional grade for all submissions to an assignment.
Use the "Select provisional grade" endpoint to choose which provisional grade to publish
for a particular submission.

Students not in the moderation set will have their one and only provisional grade published.

WARNING: This is irreversible. This will overwrite existing grades in the gradebook.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/anonymous_provisional_grades/status

**Show provisional grade status for a student**  —  `show_provisional_grade_status_for_student`

Determine whether or not the student's submission needs one or more provisional grades.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `anonymous_id` | string | query |  | The id of the student to show the status for |

**Returns:** `void`


---

# Models


## ProvisionalGrade

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `provisional_grade_id` | integer |  | The identifier for the provisional grade e.g. `23` |
| `score` | integer |  | The numeric score e.g. `90` |
| `grade` | string |  | The grade e.g. `A-` |
| `grade_matches_current_submission` | boolean |  | Whether the grade was applied to the most current submission (false if the student resubmitted after grading) e.g. `True` |
| `graded_at` | datetime |  | When the grade was given e.g. `2015-11-01T00:03:21-06:00` |
| `final` | boolean |  | Whether this is the 'final' provisional grade created by the moderator e.g. `False` |
| `speedgrader_url` | string |  | A link to view this provisional grade in SpeedGrader e.g. `http://www.example.com/courses/123/gradebook/speed_grader?...` |
