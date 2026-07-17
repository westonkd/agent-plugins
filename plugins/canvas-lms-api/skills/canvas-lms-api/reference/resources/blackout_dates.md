# Blackout Dates

> Canvas LMS REST API — `/blackout_dates` resource. Base path `/api`.

## GET /v1/courses/{course_id}/blackout_dates

**List blackout dates**  —  `list_blackout_dates_courses`

Returns the list of blackout dates for the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[BlackoutDate]`

## GET /v1/accounts/{account_id}/blackout_dates

**List blackout dates**  —  `list_blackout_dates_accounts`

Returns the list of blackout dates for the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[BlackoutDate]`

## GET /v1/courses/{course_id}/blackout_dates/{id}

**Get a single blackout date**  —  `get_single_blackout_date_courses`

Returns the blackout date with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `BlackoutDate`

## GET /v1/accounts/{account_id}/blackout_dates/{id}

**Get a single blackout date**  —  `get_single_blackout_date_accounts`

Returns the blackout date with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `BlackoutDate`

## GET /v1/courses/{course_id}/blackout_dates/new

**New Blackout Date**  —  `new_blackout_date_courses`

Initialize an unsaved Blackout Date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `BlackoutDate`

## GET /v1/accounts/{account_id}/blackout_dates/new

**New Blackout Date**  —  `new_blackout_date_accounts`

Initialize an unsaved Blackout Date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `BlackoutDate`

## POST /v1/courses/{course_id}/blackout_dates

**Create Blackout Date**  —  `create_blackout_date_courses`

Create a blackout date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `start_date` | Date | form |  | The start date of the blackout date. |
| `end_date` | Date | form |  | The end date of the blackout date. |
| `event_title` | string | form |  | The title of the blackout date. |

**Returns:** `BlackoutDate`

## POST /v1/accounts/{account_id}/blackout_dates

**Create Blackout Date**  —  `create_blackout_date_accounts`

Create a blackout date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `start_date` | Date | form |  | The start date of the blackout date. |
| `end_date` | Date | form |  | The end date of the blackout date. |
| `event_title` | string | form |  | The title of the blackout date. |

**Returns:** `BlackoutDate`

## PUT /v1/courses/{course_id}/blackout_dates/{id}

**Update Blackout Date**  —  `update_blackout_date_courses`

Update a blackout date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `start_date` | Date | form |  | The start date of the blackout date. |
| `end_date` | Date | form |  | The end date of the blackout date. |
| `event_title` | string | form |  | The title of the blackout date. |

**Returns:** `BlackoutDate`

## PUT /v1/accounts/{account_id}/blackout_dates/{id}

**Update Blackout Date**  —  `update_blackout_date_accounts`

Update a blackout date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `start_date` | Date | form |  | The start date of the blackout date. |
| `end_date` | Date | form |  | The end date of the blackout date. |
| `event_title` | string | form |  | The title of the blackout date. |

**Returns:** `BlackoutDate`

## DELETE /v1/courses/{course_id}/blackout_dates/{id}

**Delete Blackout Date**  —  `delete_blackout_date_courses`

Delete a blackout date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `BlackoutDate`

## DELETE /v1/accounts/{account_id}/blackout_dates/{id}

**Delete Blackout Date**  —  `delete_blackout_date_accounts`

Delete a blackout date for the given context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `BlackoutDate`

## PUT /v1/courses/{course_id}/blackout_dates

**Update a list of Blackout Dates**  —  `update_list_of_blackout_dates`

Create, update, and delete blackout dates to sync the db with the incoming data.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `blackout_dates:` | string | form |  | [blackout_date, ...] An object containing the array of BlackoutDates we want to exist after this operation. For array entries, if it has an id it will be updated, if not created, and if an existing BlackoutDate id is missing from the array, it will be deleted. |

**Returns:** `array[BlackoutDate The result (which should match the input with maybe some different IDs).]`


---

# Models


## BlackoutDate

Blackout dates are used to prevent scheduling assignments on a given date in course pacing.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the blackout date e.g. `1` |
| `context_id` | integer |  | the context owning the blackout date e.g. `1` |
| `context_type` | string |  | e.g. `Course` |
| `start_date` | datetime |  | the start date of the blackout date e.g. `2022-01-01` |
| `end_date` | datetime |  | the end date of the blackout date e.g. `2022-01-02` |
| `event_title` | string |  | title of the blackout date e.g. `some title` |
