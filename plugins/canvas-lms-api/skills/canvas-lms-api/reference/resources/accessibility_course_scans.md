# Accessibility Course Scans

> Canvas LMS REST API — `/accessibility_course_scans` resource. Base path `/api`.

## POST /v1/users/{user_id}/educator_accessibility_course_scan

**Trigger accessibility course scan**  —  `trigger_accessibility_course_scan`

Queues a background job that scans all a11y-enabled courses where the
user has an active teacher or designer enrollment. Idempotent — if a
scan is already queued or running, the existing Progress is returned.

Requires the educator_dashboard feature flag on the root account and
a11y_checker_account_statistics on site admin.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | The ID of the user, or "self" for the current user. The requesting user may only trigger a scan for themselves. |

**Returns:** `Progress`
