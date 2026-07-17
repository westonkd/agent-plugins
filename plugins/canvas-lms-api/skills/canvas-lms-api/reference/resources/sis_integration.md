# SIS Integration

> Canvas LMS REST API — `/sis_integration` resource. Base path `/api`.

## GET /sis/accounts/{account_id}/assignments

**Retrieve assignments enabled for grade export to SIS**  —  `retrieve_assignments_enabled_for_grade_export_to_sis_accounts`

Retrieve a list of published assignments flagged as "post_to_sis".
See the Assignments API for more details on assignments.
Assignment group and section information are included for convenience.

Each section includes course information for the origin course and the
cross-listed course, if applicable. The `origin_course` is the course to
which the section belongs or the course from which the section was
cross-listed. Generally, the `origin_course` should be preferred when
performing integration work. The `xlist_course` is provided for consistency
and is only present when the section has been cross-listed.
See Sections API and Courses Api for me details.

The `override` is only provided if the Differentiated Assignments course
feature is turned on and the assignment has an override for that section.
When there is an override for the assignment the override object's
keys/values can be merged with the top level assignment object to create a
view of the assignment object specific to that section.
See Assignments api for more information on assignment overrides.

restricts to courses that start before this date (if they have a start date)
restricts to courses that end after this date (if they have an end date)
information to include.

  "student_overrides":: returns individual student override information

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | integer (int64) | path | yes | The ID of the account to query. |
| `course_id` | integer (int64) | query |  | The ID of the course to query. |
| `starts_before` | DateTime | query |  | When searching on an account, |
| `ends_after` | DateTime | query |  | When searching on an account, |
| `include` | string | query |  | Array of additional Allowed: `student_overrides` |

**Returns:** `void`

## GET /sis/courses/{course_id}/assignments

**Retrieve assignments enabled for grade export to SIS**  —  `retrieve_assignments_enabled_for_grade_export_to_sis_courses`

Retrieve a list of published assignments flagged as "post_to_sis".
See the Assignments API for more details on assignments.
Assignment group and section information are included for convenience.

Each section includes course information for the origin course and the
cross-listed course, if applicable. The `origin_course` is the course to
which the section belongs or the course from which the section was
cross-listed. Generally, the `origin_course` should be preferred when
performing integration work. The `xlist_course` is provided for consistency
and is only present when the section has been cross-listed.
See Sections API and Courses Api for me details.

The `override` is only provided if the Differentiated Assignments course
feature is turned on and the assignment has an override for that section.
When there is an override for the assignment the override object's
keys/values can be merged with the top level assignment object to create a
view of the assignment object specific to that section.
See Assignments api for more information on assignment overrides.

restricts to courses that start before this date (if they have a start date)
restricts to courses that end after this date (if they have an end date)
information to include.

  "student_overrides":: returns individual student override information

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | integer (int64) | query |  | The ID of the account to query. |
| `course_id` | integer (int64) | path | yes | The ID of the course to query. |
| `starts_before` | DateTime | query |  | When searching on an account, |
| `ends_after` | DateTime | query |  | When searching on an account, |
| `include` | string | query |  | Array of additional Allowed: `student_overrides` |

**Returns:** `void`

## PUT /sis/courses/{course_id}/disable_post_to_sis

**Disable assignments currently enabled for grade export to SIS**  —  `disable_assignments_currently_enabled_for_grade_export_to_sis`

Disable all assignments flagged as "post_to_sis", with the option of making it
specific to a grading period, in a course.

On success, the response will be 204 No Content with an empty body.

On failure, the response will be 400 Bad Request with a body of a specific
message.

For disabling assignments in a specific grading period

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The ID of the course. |
| `grading_period_id` | integer (int64) | form |  | The ID of the grading period. |

**Returns:** `void`


---

# Models


## SisAssignment

Assignments that have post_to_sis enabled with other objects for convenience

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the assignment. e.g. `4` |
| `course_id` | integer |  | The unique identifier for the course. e.g. `6` |
| `name` | string |  | the name of the assignment e.g. `some assignment` |
| `created_at` | datetime |  | The time at which this assignment was originally created e.g. `2012-07-01T23:59:00-06:00` |
| `due_at` | datetime |  | the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. e.g. `2012-07-01T23:59:00-06:00` |
| `unlock_at` | datetime |  | (Optional) Time at which this was/will be unlocked. e.g. `2013-01-01T00:00:00-06:00` |
| `lock_at` | datetime |  | (Optional) Time at which this was/will be locked. e.g. `2013-02-01T00:00:00-06:00` |
| `points_possible` | integer |  | The maximum points possible for the assignment e.g. `12` |
| `submission_types` | array[string] |  | the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation' e.g. `['online_text_entry']` |
| `integration_id` | string |  | Third Party integration id for assignment e.g. `12341234` |
| `integration_data` | string |  | (optional, Third Party integration data for assignment) e.g. `other_data` |
| `include_in_final_grade` | boolean |  | If false, the assignment will be omitted from the student's final grade e.g. `True` |
| `assignment_group` | array[AssignmentGroupAttributes] |  | Includes attributes of a assignment_group for convenience. For more details see Assignments API. |
| `sections` | array[SectionAttributes] |  | Includes attributes of a section for convenience. For more details see Sections API. |
| `user_overrides` | array[UserAssignmentOverrideAttributes] |  | Includes attributes of a user assignment overrides. For more details see Assignments API. |


## AssignmentGroupAttributes

Some of the attributes of an Assignment Group. See Assignments API for more details

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the id of the Assignment Group e.g. `1` |
| `name` | string |  | the name of the Assignment Group e.g. `group2` |
| `group_weight` | integer |  | the weight of the Assignment Group e.g. `20` |
| `sis_source_id` | string |  | the sis source id of the Assignment Group e.g. `1234` |
| `integration_data` | object |  | the integration data of the Assignment Group e.g. `{'5678': '0954'}` |


## SectionAttributes

Some of the attributes of a section. For more details see Sections API.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the section. e.g. `1` |
| `name` | string |  | The name of the section. e.g. `Section A` |
| `sis_id` | string |  | The sis id of the section. e.g. `s34643` |
| `integration_id` | string |  | Optional: The integration ID of the section. e.g. `3452342345` |
| `origin_course` | CourseAttributes |  | The course to which the section belongs or the course from which the section was cross-listed |
| `xlist_course` | CourseAttributes |  | Optional: Attributes of the xlist course. Only present when the section has been cross-listed. See Courses API for more details |
| `override` | SectionAssignmentOverrideAttributes |  | Optional: Attributes of the assignment override that apply to the section. See Assignment API for more details |


## CourseAttributes

Attributes of a course object.  See Courses API for more details

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique Canvas identifier for the origin course e.g. `7` |
| `name` | string |  | The name of the origin course. e.g. `Section A` |
| `sis_id` | string |  | The sis id of the origin_course. e.g. `c34643` |
| `integration_id` | string |  | The integration ID of the origin_course. e.g. `I-2` |


## SectionAssignmentOverrideAttributes

Attributes of an assignment override that apply to the section object.  See Assignments API for more details

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `override_title` | string |  | The title for the assignment override e.g. `some section override` |
| `due_at` | datetime |  | the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. e.g. `2012-07-01T23:59:00-06:00` |
| `unlock_at` | datetime |  | (Optional) Time at which this was/will be unlocked. e.g. `2013-01-01T00:00:00-06:00` |
| `lock_at` | datetime |  | (Optional) Time at which this was/will be locked. e.g. `2013-02-01T00:00:00-06:00` |


## UserAssignmentOverrideAttributes

Attributes of assignment overrides that apply to users.  See Assignments API for more details

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique Canvas identifier for the assignment override e.g. `218` |
| `title` | string |  | The title of the assignment override. e.g. `Override title` |
| `due_at` | datetime |  | The time at which this assignment is due e.g. `2013-01-01T00:00:00-06:00` |
| `unlock_at` | datetime |  | (Optional) Time at which this was/will be unlocked. e.g. `2013-01-01T00:00:00-06:00` |
| `lock_at` | datetime |  | (Optional) Time at which this was/will be locked. e.g. `2013-02-01T00:00:00-06:00` |
| `students` | array[StudentAttributes] |  | Includes attributes of a student for convenience. For more details see Users API. |


## StudentAttributes

Attributes of student.  See Users API for more details

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `user_id` | integer |  | The unique Canvas identifier for the user e.g. `511` |
| `sis_user_id` | string |  | The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. e.g. `SHEL93921` |
