# Late Policy

> Canvas LMS REST API — `/late_policy` resource. Base path `/api`.

## GET /v1/courses/{id}/late_policy

**Get a late policy**  —  `get_late_policy`

Returns the late policy for a course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{id}/late_policy

**Create a late policy**  —  `create_late_policy`

Create a late policy. If the course already has a late policy, a
bad_request is returned since there can only be one late policy
per course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `late_policy[missing_submission_deduction_enabled]` | boolean | form |  | Whether to enable the missing submission deduction late policy. |
| `late_policy[missing_submission_deduction]` | number | form |  | How many percentage points to deduct from a missing submission. |
| `late_policy[late_submission_deduction_enabled]` | boolean | form |  | Whether to enable the late submission deduction late policy. |
| `late_policy[late_submission_deduction]` | number | form |  | How many percentage points to deduct per the late submission interval. |
| `late_policy[late_submission_interval]` | string | form |  | The interval for late policies. |
| `late_policy[late_submission_minimum_percent_enabled]` | boolean | form |  | Whether to enable the late submission minimum percent for a late policy. |
| `late_policy[late_submission_minimum_percent]` | number | form |  | The minimum grade a submissions can have in percentage points. |

**Returns:** `void`

## PATCH /v1/courses/{id}/late_policy

**Patch a late policy**  —  `patch_late_policy`

Patch a late policy. No body is returned upon success.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `late_policy[missing_submission_deduction_enabled]` | boolean | form |  | Whether to enable the missing submission deduction late policy. |
| `late_policy[missing_submission_deduction]` | number | form |  | How many percentage points to deduct from a missing submission. |
| `late_policy[late_submission_deduction_enabled]` | boolean | form |  | Whether to enable the late submission deduction late policy. |
| `late_policy[late_submission_deduction]` | number | form |  | How many percentage points to deduct per the late submission interval. |
| `late_policy[late_submission_interval]` | string | form |  | The interval for late policies. |
| `late_policy[late_submission_minimum_percent_enabled]` | boolean | form |  | Whether to enable the late submission minimum percent for a late policy. |
| `late_policy[late_submission_minimum_percent]` | number | form |  | The minimum grade a submissions can have in percentage points. |

**Returns:** `void`


---

# Models


## LatePolicy

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the late policy e.g. `123` |
| `course_id` | integer |  | the unique identifier for the course e.g. `123` |
| `missing_submission_deduction_enabled` | boolean |  | whether to enable missing submission deductions e.g. `True` |
| `missing_submission_deduction` | number |  | amount of percentage points to deduct e.g. `12.34` |
| `late_submission_deduction_enabled` | boolean |  | whether to enable late submission deductions e.g. `True` |
| `late_submission_deduction` | number |  | amount of percentage points to deduct per late_submission_interval e.g. `12.34` |
| `late_submission_interval` | string |  | time interval for late submission deduction e.g. `hour` Allowed: `hour`, `day` |
| `late_submission_minimum_percent_enabled` | boolean |  | whether to enable late submission minimum percent e.g. `True` |
| `late_submission_minimum_percent` | number |  | the minimum score a submission can receive in percentage points e.g. `12.34` |
| `created_at` | datetime |  | the time at which this late policy was originally created e.g. `2012-07-01T23:59:00-06:00` |
| `updated_at` | datetime |  | the time at which this late policy was last modified in any way e.g. `2012-07-01T23:59:00-06:00` |
