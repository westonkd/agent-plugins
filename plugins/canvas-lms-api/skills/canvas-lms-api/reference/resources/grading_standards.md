# Grading Standards

> Canvas LMS REST API — `/grading_standards` resource. Base path `/api`.

## POST /v1/accounts/{account_id}/grading_standards

**Create a new grading standard**  —  `create_new_grading_standard_accounts`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `title` | string | form | yes | The title for the Grading Standard. |
| `points_based` | boolean | form |  | Whether or not a grading scheme is points based. Defaults to false. |
| `scaling_factor` | integer (int64) | form |  | The factor by which to scale a percentage into a points based scheme grade. This is the maximum number of points possible in the grading scheme. Defaults to 1. Not required for percentage based grading schemes. |
| `grading_scheme_entry[name]` | array[string] | form | yes | The name for an entry value within a GradingStandard that describes the range of the value e.g. A- |
| `grading_scheme_entry[value]` | array[integer] | form | yes | The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93 |

**Returns:** `GradingStandard`

## POST /v1/courses/{course_id}/grading_standards

**Create a new grading standard**  —  `create_new_grading_standard_courses`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `title` | string | form | yes | The title for the Grading Standard. |
| `points_based` | boolean | form |  | Whether or not a grading scheme is points based. Defaults to false. |
| `scaling_factor` | integer (int64) | form |  | The factor by which to scale a percentage into a points based scheme grade. This is the maximum number of points possible in the grading scheme. Defaults to 1. Not required for percentage based grading schemes. |
| `grading_scheme_entry[name]` | array[string] | form | yes | The name for an entry value within a GradingStandard that describes the range of the value e.g. A- |
| `grading_scheme_entry[value]` | array[integer] | form | yes | The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93 |

**Returns:** `GradingStandard`

## GET /v1/courses/{course_id}/grading_standards

**List the grading standards available in a context.**  —  `list_grading_standards_available_in_context_courses`

Returns the paginated list of grading standards for the given context that are visible to the user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[GradingStandard]`

## GET /v1/accounts/{account_id}/grading_standards

**List the grading standards available in a context.**  —  `list_grading_standards_available_in_context_accounts`

Returns the paginated list of grading standards for the given context that are visible to the user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[GradingStandard]`

## GET /v1/courses/{course_id}/grading_standards/{grading_standard_id}

**Get a single grading standard in a context.**  —  `get_single_grading_standard_in_context_courses`

Returns a grading standard for the given context that is visible to the user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `grading_standard_id` | string | path | yes | ID |

**Returns:** `GradingStandard`

## GET /v1/accounts/{account_id}/grading_standards/{grading_standard_id}

**Get a single grading standard in a context.**  —  `get_single_grading_standard_in_context_accounts`

Returns a grading standard for the given context that is visible to the user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `grading_standard_id` | string | path | yes | ID |

**Returns:** `GradingStandard`

## PUT /v1/courses/{course_id}/grading_standards/{grading_standard_id}

**Update a grading standard**  —  `update_grading_standard_courses`

Updates the grading standard with the given id

If the grading standard has been used for grading, only the title can be updated.
The data, points_based, and scaling_factor cannot be modified once the grading
standard has been used to grade assignments.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `grading_standard_id` | string | path | yes | ID |
| `title` | string | form |  | The title for the Grading Standard |
| `points_based` | boolean | form |  | Whether or not a grading scheme is points based. Defaults to false. |
| `scaling_factor` | integer (int64) | form |  | The factor by which to scale a percentage into a points based scheme grade. This is the maximum number of points possible in the grading scheme. Defaults to 1. Not required for percentage based grading schemes. |
| `grading_scheme_entry[name]` | array[string] | form |  | The name for an entry value within a GradingStandard that describes the range of the value e.g. A- |
| `grading_scheme_entry[value]` | array[integer] | form | yes | The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93 |

**Returns:** `GradingStandard`

## PUT /v1/accounts/{account_id}/grading_standards/{grading_standard_id}

**Update a grading standard**  —  `update_grading_standard_accounts`

Updates the grading standard with the given id

If the grading standard has been used for grading, only the title can be updated.
The data, points_based, and scaling_factor cannot be modified once the grading
standard has been used to grade assignments.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `grading_standard_id` | string | path | yes | ID |
| `title` | string | form |  | The title for the Grading Standard |
| `points_based` | boolean | form |  | Whether or not a grading scheme is points based. Defaults to false. |
| `scaling_factor` | integer (int64) | form |  | The factor by which to scale a percentage into a points based scheme grade. This is the maximum number of points possible in the grading scheme. Defaults to 1. Not required for percentage based grading schemes. |
| `grading_scheme_entry[name]` | array[string] | form |  | The name for an entry value within a GradingStandard that describes the range of the value e.g. A- |
| `grading_scheme_entry[value]` | array[integer] | form | yes | The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. 93 |

**Returns:** `GradingStandard`

## DELETE /v1/courses/{course_id}/grading_standards/{grading_standard_id}

**Delete a grading standard**  —  `delete_grading_standard_courses`

Deletes the grading standard with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `grading_standard_id` | string | path | yes | ID |

**Returns:** `GradingStandard`

## DELETE /v1/accounts/{account_id}/grading_standards/{grading_standard_id}

**Delete a grading standard**  —  `delete_grading_standard_accounts`

Deletes the grading standard with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `grading_standard_id` | string | path | yes | ID |

**Returns:** `GradingStandard`


---

# Models


## GradingSchemeEntry

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `name` | string |  | The name for an entry value within a GradingStandard that describes the range of the value e.g. `A` |
| `value` | integer |  | The value for the name of the entry within a GradingStandard. The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or the maximum value for the scheme if there is no upper bound. The lowest value will have a lower bound range of 0. e.g. `0.9` |
| `calculated_value` | integer |  | The value that will be used to compare against a grade. For percentage based grading schemes, this is a number from 0 - 100 representing a percent. For point based grading schemes, this is the lower bound of points to achieve the grade. e.g. `90` |


## GradingStandard

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `title` | string |  | the title of the grading standard e.g. `Account Standard` |
| `id` | integer |  | the id of the grading standard e.g. `1` |
| `context_type` | string |  | the context this standard is associated with, either 'Account' or 'Course' e.g. `Account` |
| `context_id` | integer |  | the id for the context either the Account or Course id e.g. `1` |
| `points_based` | boolean |  | whether this is a points-based standard e.g. `False` |
| `scaling_factor` | number |  | the factor by which to scale a score. 1 for percentage based schemss and the max value of points for points based schemes. This number cannot be changed for percentage based schemes. e.g. `1.0` |
| `grading_scheme` | array[GradingSchemeEntry] |  | A list of GradingSchemeEntry that make up the Grading Standard as an array of values with the scheme name and value e.g. `[{'name': 'A', 'value': 0.9}, {'name': 'B', 'value': 0.8}, {'name': 'C', 'value': 0.7}, {'name': 'D', 'value': 0.6}]` |
