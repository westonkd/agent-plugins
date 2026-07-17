# Search

> Canvas LMS REST API — `/search` resource. Base path `/api`.

## GET /v1/conversations/find_recipients

**Find recipients**  —  `find_recipients_conversations`

Find valid recipients (users, courses and groups) that the current user
can send messages to. The /api/v1/search/recipients path is the preferred
endpoint, /api/v1/conversations/find_recipients is deprecated.

Pagination is supported.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `search` | string | query |  | Search terms used for matching users/courses/groups (e.g. "bob smith"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. |
| `context` | string | query |  | Limit the search to a particular course/group (e.g. "course_3" or "group_4"). |
| `exclude` | array[string] | query |  | Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with "course_" or "group_" respectively, e.g. exclude[]=1&exclude[]=2&exclude[]=course_3 |
| `type` | string | query |  | Limit the search just to users or contexts (groups/courses). Allowed: `user`, `context` |
| `user_id` | integer (int64) | query |  | Search for a specific user id. This ignores the other above parameters, and will never return more than one result. |
| `from_conversation_id` | integer (int64) | query |  | When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations. |
| `permissions` | array[string] | query |  | Array of permission strings to be checked for each matched context (e.g. "send_messages"). This argument determines which permissions may be returned in the response; it won't prevent contexts from being returned if they don't grant the permission(s). |

**Returns:** `void`

## GET /v1/search/recipients

**Find recipients**  —  `find_recipients_search`

Find valid recipients (users, courses and groups) that the current user
can send messages to. The /api/v1/search/recipients path is the preferred
endpoint, /api/v1/conversations/find_recipients is deprecated.

Pagination is supported.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `search` | string | query |  | Search terms used for matching users/courses/groups (e.g. "bob smith"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. |
| `context` | string | query |  | Limit the search to a particular course/group (e.g. "course_3" or "group_4"). |
| `exclude` | array[string] | query |  | Array of ids to exclude from the search. These may be user ids or course/group ids prefixed with "course_" or "group_" respectively, e.g. exclude[]=1&exclude[]=2&exclude[]=course_3 |
| `type` | string | query |  | Limit the search just to users or contexts (groups/courses). Allowed: `user`, `context` |
| `user_id` | integer (int64) | query |  | Search for a specific user id. This ignores the other above parameters, and will never return more than one result. |
| `from_conversation_id` | integer (int64) | query |  | When searching by user_id, only users that could be normally messaged by this user will be returned. This parameter allows you to specify a conversation that will be referenced for a shared context -- if both the current user and the searched user are in the conversation, the user will be returned. This is used to start new side conversations. |
| `permissions` | array[string] | query |  | Array of permission strings to be checked for each matched context (e.g. "send_messages"). This argument determines which permissions may be returned in the response; it won't prevent contexts from being returned if they don't grant the permission(s). |

**Returns:** `void`

## GET /v1/search/all_courses

**List all courses**  —  `list_all_courses`

A paginated list of all courses visible in the public index

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `search` | string | query |  | Search terms used for matching users/courses/groups (e.g. "bob smith"). If multiple terms are given (separated via whitespace), only results matching all terms will be returned. |
| `public_only` | boolean | query |  | Only return courses with public content. Defaults to false. |
| `open_enrollment_only` | boolean | query |  | Only return courses that allow self enrollment. Defaults to false. |

**Returns:** `void`
