# Plagiarism Detection Platform Users

> Canvas LMS REST API — `/plagiarism_detection_platform_users` resource. Base path `/api`.

## GET /lti/users/{id}

**Get a single user (lti)**  —  `get_single_user_lti`

Get a single Canvas user by Canvas id or LTI id. Tool providers may only access
users that have been assigned an assignment associated with their tool.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `User`

## GET /lti/groups/{group_id}/users

**Get all users in a group (lti)**  —  `get_all_users_in_group_lti`

Get all Canvas users in a group. Tool providers may only access
groups that belong to the context the tool is installed in.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[User]`
