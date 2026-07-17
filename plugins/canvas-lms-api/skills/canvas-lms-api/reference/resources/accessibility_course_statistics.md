# Accessibility Course Statistics

> Canvas LMS REST API — `/accessibility_course_statistics` resource. Base path `/api`.

## GET /v1/users/{user_id}/educator_accessibility_course_statistics

**List accessibility course statistics**  —  `list_accessibility_course_statistics`

Returns per-course accessibility issue statistics for the current user's
active teacher and designer courses. Only courses where the accessibility
checker is enabled and whose workflow state is neither completed nor deleted
are included. Only statistic records with workflow_state "active" are returned.

Requires the educator_dashboard feature flag to be enabled on the root
account, and a11y_checker_account_statistics on site admin plus a11y_checker
on the account (i.e. a11y_checker_account_statistics? must be true).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | The ID of the user, or "self" for the current user. The requesting user may only retrieve their own statistics. |

**Returns:** `array[AccessibilityCourseStatistic]`


---

# Models


## AccessibilityCourseStatistic

Per-course accessibility issue counts for a user's active teacher/designer courses.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the accessibility course statistic record e.g. `1` |
| `course_id` | integer |  | The ID of the course e.g. `42` |
| `course_name` | string |  | The name of the course e.g. `Introduction to Biology` |
| `course_code` | string |  | The course code (short name) of the course e.g. `BIO101` |
| `published` | boolean |  | Whether the course is published e.g. `True` |
| `active_issue_count` | integer |  | The number of active accessibility issues in the course e.g. `5` |
| `resolved_issue_count` | integer |  | The number of resolved accessibility issues in the course e.g. `3` |
| `closed_issue_count` | integer |  | The number of closed accessibility issues in the course e.g. `2` |
| `workflow_state` | string |  | The workflow state of the statistic record e.g. `active` |
| `created_at` | datetime |  | The date and time the record was created e.g. `2026-01-01T00:00:00Z` |
| `updated_at` | datetime |  | The date and time the record was last updated e.g. `2026-01-02T00:00:00Z` |
