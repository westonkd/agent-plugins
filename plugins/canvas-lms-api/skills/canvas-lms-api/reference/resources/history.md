# History

> Canvas LMS REST API — `/history` resource. Base path `/api`.

## GET /v1/users/{user_id}/history

**List recent history for a user**  —  `list_recent_history_for_user`

Return a paginated list of the user's recent history. History entries are returned in descending order,
newest to oldest. You may list history entries for yourself (use +self+ as the user_id), for a student you observe,
or for a user you manage as an administrator. Note that the +per_page+ pagination argument is not supported
and the number of history entries returned per page will vary.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[HistoryEntry]`


---

# Models


## HistoryEntry

Information about a recently visited item or page in Canvas

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `asset_code` | string | yes | The asset string for the item viewed e.g. `assignment_123` |
| `asset_name` | string | yes | The name of the item e.g. `Test Assignment` |
| `asset_icon` | string |  | The icon type shown for the item. One of 'icon-announcement', 'icon-assignment', 'icon-calendar-month', 'icon-discussion', 'icon-document', 'icon-download', 'icon-gradebook', 'icon-home', 'icon-message', 'icon-module', 'icon-outcomes', 'icon-quiz', 'icon-user', 'icon-syllabus' e.g. `icon-assignment` |
| `asset_readable_category` | string |  | The associated category describing the asset_icon e.g. `Assignment` |
| `context_type` | string |  | The type of context of the item visited. One of 'Course', 'Group', 'User', or 'Account' e.g. `Course` |
| `context_id` | integer (int64) |  | The id of the context, if applicable e.g. `123` |
| `context_name` | string |  | The name of the context e.g. `Something 101` |
| `visited_url` | string | yes | The URL of the item e.g. `https://canvas.example.com/courses/123/assignments/456` |
| `visited_at` | datetime (iso8601) | yes | When the page was visited e.g. `2019-08-01T19:49:47Z` |
| `interaction_seconds` | integer (int64) |  | The estimated time spent on the page in seconds e.g. `400` |
