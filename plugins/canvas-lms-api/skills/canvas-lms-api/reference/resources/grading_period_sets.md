# Grading Period Sets

> Canvas LMS REST API — `/grading_period_sets` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/grading_period_sets

**List grading period sets**  —  `list_grading_period_sets`

Returns the paginated list of grading period sets

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/accounts/{account_id}/grading_period_sets

**Create a grading period set**  —  `create_grading_period_set`

Create and return a new grading period set

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `enrollment_term_ids` | array[Array] | form |  | A list of associated term ids for the grading period set |
| `grading_period_set[title]` | string | form | yes | The title of the grading period set |
| `grading_period_set[weighted]` | boolean | form |  | A boolean to determine whether the grading periods in the set are weighted |
| `grading_period_set[display_totals_for_all_grading_periods]` | boolean | form |  | A boolean to determine whether the totals for all grading periods in the set are displayed |

**Returns:** `void`

## PATCH /v1/accounts/{account_id}/grading_period_sets/{id}

**Update a grading period set**  —  `update_grading_period_set`

Update an existing grading period set

<b>204 No Content</b> response code is returned if the update was
successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `enrollment_term_ids` | array[Array] | form |  | A list of associated term ids for the grading period set |
| `grading_period_set[title]` | array[string] | form | yes | The title of the grading period set |
| `grading_period_set[weighted]` | array[boolean] | form |  | A boolean to determine whether the grading periods in the set are weighted |
| `grading_period_set[display_totals_for_all_grading_periods]` | array[boolean] | form |  | A boolean to determine whether the totals for all grading periods in the set are displayed |

**Returns:** `void`

## DELETE /v1/accounts/{account_id}/grading_period_sets/{id}

**Delete a grading period set**  —  `delete_grading_period_set`

<b>204 No Content</b> response code is returned if the deletion was
successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## GradingPeriodSets

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `title` | string | yes | The title of the grading period set. e.g. `Hello World` |
| `weighted` | boolean |  | If true, the grading periods in the set are weighted. e.g. `True` |
| `display_totals_for_all_grading_periods` | boolean |  | If true, the totals for all grading periods in the set are displayed. e.g. `True` |
