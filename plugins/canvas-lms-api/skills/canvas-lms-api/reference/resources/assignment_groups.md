# Assignment Groups

> Canvas LMS REST API — `/assignment_groups` resource. Base path `/api`.

## GET /v1/courses/{course_id}/assignment_groups

**List assignment groups**  —  `list_assignment_groups`

Returns the paginated list of assignment groups for the current context.
The returned groups are sorted by their position field.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group. "discussion_topic", "all_dates", "can_edit", "assignment_visibility" & "submission" are only valid if "assignments" is also included. "score_statistics" requires that the "assignments" and "submission" options are included. The "assignment_visibility" option additionally requires that the Differentiated Assignments course feature be turned on. If "observed_users" is passed along with "assignments" and "submission", submissions for observed users will also be included as an array. The "peer_review" option requires that the Peer Review Grading course feature be turned on and that "assignments" is included. Allowed: `assignments`, `discussion_topic`, `all_dates`, `assignment_visibility`, `overrides`, `submission`, `observed_users`, `can_edit`, `score_statistics`, `peer_review` |
| `assignment_ids` | array[string] | query |  | If "assignments" are included, optionally return only assignments having their ID in this array. This argument may also be passed as a comma separated string. |
| `exclude_assignment_submission_types` | array[string] | query |  | If "assignments" are included, those with the specified submission types will be excluded from the assignment groups. Allowed: `online_quiz`, `discussion_topic`, `wiki_page`, `external_tool` |
| `override_assignment_dates` | boolean | query |  | Apply assignment overrides for each assignment, defaults to true. |
| `grading_period_id` | integer (int64) | query |  | The id of the grading period in which assignment groups are being requested (Requires grading periods to exist.) |
| `scope_assignments_to_student` | boolean | query |  | If true, all assignments returned will apply to the current user in the specified grading period. If assignments apply to other students in the specified grading period, but not the current user, they will not be returned. (Requires the grading_period_id argument and grading periods to exist. In addition, the current user must be a student.) |

**Returns:** `array[AssignmentGroup]`

## GET /v1/courses/{course_id}/assignment_groups/{assignment_group_id}

**Get an Assignment Group**  —  `get_assignment_group`

Returns the assignment group with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_group_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group. "discussion_topic" and "assignment_visibility" and "submission" are only valid if "assignments" is also included. "score_statistics" is only valid if "submission" and "assignments" are also included. The "assignment_visibility" option additionally requires that the Differentiated Assignments course feature be turned on. Allowed: `assignments`, `discussion_topic`, `assignment_visibility`, `submission`, `score_statistics` |
| `override_assignment_dates` | boolean | query |  | Apply assignment overrides for each assignment, defaults to true. |
| `grading_period_id` | integer (int64) | query |  | The id of the grading period in which assignment groups are being requested (Requires grading periods to exist on the account) |

**Returns:** `AssignmentGroup`

## POST /v1/courses/{course_id}/assignment_groups

**Create an Assignment Group**  —  `create_assignment_group`

Create a new assignment group for this course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `name` | string | form |  | The assignment group's name |
| `position` | integer (int64) | form |  | The position of this assignment group in relation to the other assignment groups |
| `group_weight` | number (float) | form |  | The percent of the total grade that this assignment group represents |
| `sis_source_id` | string | form |  | The sis source id of the Assignment Group |
| `integration_data` | Object | form |  | The integration data of the Assignment Group |

**Returns:** `AssignmentGroup`

## PUT /v1/courses/{course_id}/assignment_groups/{assignment_group_id}

**Edit an Assignment Group**  —  `edit_assignment_group`

Modify an existing Assignment Group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_group_id` | string | path | yes | ID |
| `name` | string | form |  | The assignment group's name |
| `position` | integer (int64) | form |  | The position of this assignment group in relation to the other assignment groups |
| `group_weight` | number (float) | form |  | The percent of the total grade that this assignment group represents |
| `sis_source_id` | string | form |  | The sis source id of the Assignment Group |
| `integration_data` | Object | form |  | The integration data of the Assignment Group |
| `rules` | string | form |  | The grading rules that are applied within this assignment group See the Assignment Group object definition for format |

**Returns:** `AssignmentGroup`

## DELETE /v1/courses/{course_id}/assignment_groups/{assignment_group_id}

**Destroy an Assignment Group**  —  `destroy_assignment_group`

Deletes the assignment group with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_group_id` | string | path | yes | ID |
| `move_assignments_to` | integer (int64) | query |  | The ID of an active Assignment Group to which the assignments that are currently assigned to the destroyed Assignment Group will be assigned. NOTE: If this argument is not provided, any assignments in this Assignment Group will be deleted. |

**Returns:** `AssignmentGroup`


---

# Models


## GradingRules

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `drop_lowest` | integer |  | Number of lowest scores to be dropped for each user. e.g. `1` |
| `drop_highest` | integer |  | Number of highest scores to be dropped for each user. e.g. `1` |
| `never_drop` | array[integer] |  | Assignment IDs that should never be dropped. e.g. `[33, 17, 24]` |


## AssignmentGroup

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the id of the Assignment Group e.g. `1` |
| `name` | string |  | the name of the Assignment Group e.g. `group2` |
| `position` | integer |  | the position of the Assignment Group e.g. `7` |
| `group_weight` | integer |  | the weight of the Assignment Group e.g. `20` |
| `sis_source_id` | string |  | the sis source id of the Assignment Group e.g. `1234` |
| `integration_data` | object |  | the integration data of the Assignment Group e.g. `{'5678': '0954'}` |
| `assignments` | array[integer] |  | the assignments in this Assignment Group (see the Assignment API for a detailed list of fields) e.g. `[]` |
| `rules` | GradingRules |  | the grading rules that this Assignment Group has |
