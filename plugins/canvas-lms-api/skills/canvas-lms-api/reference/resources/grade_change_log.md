# Grade Change Log

> Canvas LMS REST API — `/grade_change_log` resource. Base path `/api`.

## GET /v1/audit/grade_change/assignments/{assignment_id}

**Query by assignment**  —  `query_by_assignment`

List grade change events for a given assignment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `array[GradeChangeEvent]`

## GET /v1/audit/grade_change/courses/{course_id}

**Query by course**  —  `query_by_course`

List grade change events for a given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `array[GradeChangeEvent]`

## GET /v1/audit/grade_change/students/{student_id}

**Query by student**  —  `query_by_student`

List grade change events for a given student.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `student_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `array[GradeChangeEvent]`

## GET /v1/audit/grade_change/graders/{grader_id}

**Query by grader**  —  `query_by_grader`

List grade change events for a given grader.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `grader_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `array[GradeChangeEvent]`

## GET /v1/audit/grade_change

**Advanced query**  —  `advanced_query`

List grade change events satisfying all given parameters. Teachers may query for events in courses they teach.
Queries without +course_id+ or +assignment_id+ require account administrator rights.

At least one of +course_id+, +assignment_id+, +student_id+, or +grader_id+ must be specified.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | query |  | Restrict query to events in the specified course. |
| `assignment_id` | integer (int64) | query |  | Restrict query to the given assignment. If "override" is given, query the course final grade override instead. |
| `student_id` | integer (int64) | query |  | User id of a student to search grading events for. |
| `grader_id` | integer (int64) | query |  | User id of a grader to search grading events for. |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `array[GradeChangeEvent]`


---

# Models


## GradeChangeEventLinks

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `assignment` | integer |  | ID of the assignment associated with the event e.g. `2319` |
| `course` | integer |  | ID of the course associated with the event. will match the context_id in the associated assignment if the context type for the assignment is a course e.g. `2319` |
| `student` | integer |  | ID of the student associated with the event. will match the user_id in the associated submission. e.g. `2319` |
| `grader` | integer |  | ID of the grader associated with the event. will match the grader_id in the associated submission. e.g. `2319` |
| `page_view` | string |  | ID of the page view during the event if it exists. e.g. `e2b76430-27a5-0131-3ca1-48e0eb13f29b` |


## GradeChangeEvent

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | ID of the event. e.g. `e2b76430-27a5-0131-3ca1-48e0eb13f29b` |
| `created_at` | datetime |  | timestamp of the event e.g. `2012-07-19T15:00:00-06:00` |
| `event_type` | string |  | GradeChange event type e.g. `grade_change` |
| `excused_after` | boolean |  | Boolean indicating whether the submission was excused after the change. e.g. `True` |
| `excused_before` | boolean |  | Boolean indicating whether the submission was excused before the change. e.g. `False` |
| `grade_after` | string |  | The grade after the change. e.g. `8` |
| `grade_before` | string |  | The grade before the change. e.g. `8` |
| `graded_anonymously` | boolean |  | Boolean indicating whether the student name was visible when the grade was given. Could be null if the grade change record was created before this feature existed. e.g. `True` |
| `version_number` | string |  | Version Number of the grade change submission. e.g. `1` |
| `request_id` | string |  | The unique request id of the request during the grade change. e.g. `e2b76430-27a5-0131-3ca1-48e0eb13f29b` |
| `links` | GradeChangeEventLinks |  |  |
