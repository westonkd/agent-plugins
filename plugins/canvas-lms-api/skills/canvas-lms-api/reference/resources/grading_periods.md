# Grading Periods

> Canvas LMS REST API — `/grading_periods` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/grading_periods

**List grading periods**  —  `list_grading_periods_accounts`

Returns the paginated list of grading periods for the current course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/grading_periods

**List grading periods**  —  `list_grading_periods_courses`

Returns the paginated list of grading periods for the current course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/grading_periods/{id}

**Get a single grading period**  —  `get_single_grading_period`

Returns the grading period with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/grading_periods/{id}

**Update a single grading period**  —  `update_single_grading_period`

Update an existing grading period.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `grading_periods[start_date]` | array[Date] | form | yes | The date the grading period starts. |
| `grading_periods[end_date]` | array[Date] | form | yes | no description |
| `grading_periods[weight]` | array[number] | form |  | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/grading_periods/{id}

**Delete a grading period**  —  `delete_grading_period_courses`

<b>204 No Content</b> response code is returned if the deletion was
successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/accounts/{account_id}/grading_periods/{id}

**Delete a grading period**  —  `delete_grading_period_accounts`

<b>204 No Content</b> response code is returned if the deletion was
successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## PATCH /v1/courses/{course_id}/grading_periods/batch_update

**Batch update grading periods**  —  `batch_update_grading_periods_courses`

Update multiple grading periods

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `set_id` | string | form | yes | The id of the grading period set. |
| `grading_periods[id]` | array[string] | form |  | The id of the grading period. If the id parameter does not exist, a new grading period will be created. |
| `grading_periods[title]` | array[string] | form | yes | The title of the grading period. The title is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[start_date]` | array[Date] | form | yes | The date the grading period starts. The start_date is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[end_date]` | array[Date] | form | yes | The date the grading period ends. The end_date is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[close_date]` | array[Date] | form | yes | The date after which grades can no longer be changed for a grading period. The close_date is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[weight]` | array[number] | form |  | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade |

**Returns:** `void`

## PATCH /v1/grading_period_sets/{set_id}/grading_periods/batch_update

**Batch update grading periods**  —  `batch_update_grading_periods_grading_period_sets`

Update multiple grading periods

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `set_id` | string | path | yes | The id of the grading period set. |
| `grading_periods[id]` | array[string] | form |  | The id of the grading period. If the id parameter does not exist, a new grading period will be created. |
| `grading_periods[title]` | array[string] | form | yes | The title of the grading period. The title is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[start_date]` | array[Date] | form | yes | The date the grading period starts. The start_date is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[end_date]` | array[Date] | form | yes | The date the grading period ends. The end_date is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[close_date]` | array[Date] | form | yes | The date after which grades can no longer be changed for a grading period. The close_date is required for creating a new grading period, but not for updating an existing grading period. |
| `grading_periods[weight]` | array[number] | form |  | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade |

**Returns:** `void`


---

# Models


## GradingPeriod

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer | yes | The unique identifier for the grading period. e.g. `1023` |
| `title` | string |  | The title for the grading period. e.g. `First Block` |
| `start_date` | string (date-time) | yes | The start date of the grading period. e.g. `2014-01-07T15:04:00Z` |
| `end_date` | string (date-time) | yes | The end date of the grading period. e.g. `2014-05-07T17:07:00Z` |
| `close_date` | string (date-time) |  | Grades can only be changed before the close date of the grading period. e.g. `2014-06-07T17:07:00Z` |
| `weight` | integer |  | A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade e.g. `33.33` |
| `is_closed` | boolean |  | If true, the grading period's close_date has passed. e.g. `True` |
