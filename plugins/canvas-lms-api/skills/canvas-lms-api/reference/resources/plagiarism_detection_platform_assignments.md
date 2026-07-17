# Plagiarism Detection Platform Assignments

> Canvas LMS REST API — `/plagiarism_detection_platform_assignments` resource. Base path `/api`.

## GET /lti/assignments/{assignment_id}

**Get a single assignment (lti)**  —  `get_single_assignment_lti`

Get a single Canvas assignment by Canvas id or LTI id. Tool providers may only access
assignments that are associated with their tool.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | query |  | The id of the user. Can be a Canvas or LTI id for the user. |

**Returns:** `LtiAssignment`


---

# Models


## LtiAssignment

A Canvas assignment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | e.g. `4` |
| `name` | string |  | e.g. `Midterm Review` |
| `description` | string |  | e.g. `<p>Do the following:</p>...` |
| `points_possible` | integer |  | e.g. `10` |
| `due_at` | datetime |  | The due date for the assignment. If a user id is supplied and an assignment override is in place this field will reflect the due date as it applies to the user. e.g. `2012-07-01T23:59:00-06:00` |
| `lti_id` | string |  | e.g. `86157096483e6b3a50bfedc6bac902c0b20a824f` |
| `course_id` | integer |  | e.g. `10000000000060` |
| `lti_course_id` | string |  | e.g. `66157096483e6b3a50bfedc6bac902c0b20a8241` |
