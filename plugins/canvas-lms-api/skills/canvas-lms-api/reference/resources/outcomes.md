# Outcomes

> Canvas LMS REST API — `/outcomes` resource. Base path `/api`.

## GET /v1/outcomes/{id}

**Show an outcome**  —  `show_outcome`

Returns the details of the outcome with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `add_defaults` | boolean | query |  | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED |

**Returns:** `Outcome`

## PUT /v1/outcomes/{id}

**Update an outcome**  —  `update_outcome`

Modify an existing outcome. Fields not provided are left as is;
unrecognized fields are ignored.

If any new ratings are provided, the combination of all new ratings
provided completely replace any existing embedded rubric criterion; it is
not possible to tweak the ratings of the embedded rubric criterion.

A new embedded rubric criterion's mastery_points default to the maximum
points in the highest rating if not specified in the mastery_points
parameter. Any new ratings lacking a description are given a default of "No
description". Any new ratings lacking a point value are given a default of
0.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `title` | string | form |  | The new outcome title. |
| `display_name` | string | form |  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. |
| `description` | string | form |  | The new outcome description. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `mastery_points` | integer (int64) | form |  | The new mastery threshold for the embedded rubric criterion. |
| `ratings[description]` | array[string] | form |  | The description of a new rating level for the embedded rubric criterion. |
| `ratings[points]` | array[integer] | form |  | The points corresponding to a new rating level for the embedded rubric criterion. |
| `calculation_method` | string | form |  | The new calculation method. If the Outcomes New Decaying Average Calculation Method FF is ENABLED then "weighted_average" can be used and it is same as previous "decaying_average" and new "decaying_average" will have improved version of calculation. Allowed: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average` |
| `calculation_int` | integer (int64) | form |  | The new calculation int.  Only applies if the calculation_method is "decaying_average" or "n_mastery" |
| `add_defaults` | boolean | form |  | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED |

**Returns:** `Outcome`

## GET /v1/courses/{course_id}/outcome_alignments

**Get outcome alignments for a student or assignment**  —  `get_outcome_alignments_for_student_or_assignment`

Returns outcome alignments for a student or assignment in a course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the course |
| `student_id` | integer (int64) | query |  | The id of the student. Returns alignments filtered by student submissions. Can be combined with assignment_id to filter to a specific assignment. |
| `assignment_id` | integer (int64) | query |  | The id of the assignment. When provided without student_id, returns all outcome alignments for the assignment (requires manage_grades or view_all_grades permission). When provided with student_id, filters to that student's submission. |

**Returns:** `array[OutcomeAlignment]`


---

# Models


## Outcome

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the outcome e.g. `1` |
| `url` | string |  | the URL for fetching/updating the outcome. should be treated as opaque e.g. `/api/v1/outcomes/1` |
| `context_id` | integer |  | the context owning the outcome. may be null for global outcomes e.g. `1` |
| `context_type` | string |  | e.g. `Account` |
| `title` | string |  | title of the outcome e.g. `Outcome title` |
| `display_name` | string |  | Optional friendly name for reporting e.g. `My Favorite Outcome` |
| `description` | string |  | description of the outcome. omitted in the abbreviated form. e.g. `Outcome description` |
| `vendor_guid` | string |  | A custom GUID for the learning standard. e.g. `customid9000` |
| `points_possible` | integer |  | maximum points possible. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. e.g. `5` |
| `mastery_points` | integer |  | points necessary to demonstrate mastery outcomes. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. e.g. `3` |
| `calculation_method` | string |  | the method used to calculate a students score e.g. `decaying_average` |
| `calculation_int` | integer |  | this defines the variable value used by the calculation_method. included only if calculation_method uses it e.g. `65` |
| `ratings` | array[RubricRating] |  | possible ratings for this outcome. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. |
| `can_edit` | boolean |  | whether the current user can update the outcome e.g. `True` |
| `can_unlink` | boolean |  | whether the outcome can be unlinked e.g. `True` |
| `assessed` | boolean |  | whether this outcome has been used to assess a student e.g. `True` |
| `has_updateable_rubrics` | boolean |  | whether updates to this outcome will propagate to unassessed rubrics that have imported it e.g. `True` |


## OutcomeAlignment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the id of the aligned learning outcome. e.g. `1` |
| `assignment_id` | integer |  | the id of the aligned assignment (null for live assessments). e.g. `2` |
| `assessment_id` | integer |  | the id of the aligned live assessment (null for assignments). e.g. `3` |
| `submission_types` | string |  | a string representing the different submission types of an aligned assignment. e.g. `online_text_entry,online_url` |
| `url` | string |  | the URL for the aligned assignment. e.g. `/courses/1/assignments/5` |
| `title` | string |  | the title of the aligned assignment. e.g. `Unit 1 test` |
