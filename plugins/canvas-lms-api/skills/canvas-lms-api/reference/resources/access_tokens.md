# Access Tokens

> Canvas LMS REST API — `/access_tokens` resource. Base path `/api`.

## GET /v1/users/{user_id}/user_generated_tokens

**List access tokens for a user**  —  `list_access_tokens_for_user`

Returns a list of manually generated access tokens for the specified user.
Note that the actual token values are only returned when the token is first created.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `per_page` | integer (int64) | query |  | The number of results to return per page. Defaults to 10. Maximum of 100. |

**Returns:** `array[Token]`

## GET /v1/users/{user_id}/tokens/{id}

**Show an access token**  —  `show_access_token`

The ID can be the actual database ID of the token, or the 'token_hint' value.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/users/{user_id}/tokens

**Create an access token**  —  `create_access_token`

Create a new access token for the specified user.
If the user is not the current user, the token will be created as "pending",
and must be activated by the user before it can be used.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `token[purpose]` | string | form | yes | The purpose of the token. |
| `token[expires_at]` | DateTime | form |  | The time at which the token will expire. |
| `token[scopes]` | array[Array] | form |  | The scopes to associate with the token. Ignored if the default developer key does not have the "enable scopes" option enabled. In such cases, the token will inherit the user's permissions instead. |

**Returns:** `void`

## PUT /v1/users/{user_id}/tokens/{id}

**Update an access token**  —  `update_access_token`

Update an existing access token.

The ID can be the actual database ID of the token, or the 'token_hint' value.

Regenerating an expired token requires a new expiration date.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `token[purpose]` | string | form |  | The purpose of the token. |
| `token[expires_at]` | DateTime | form |  | The time at which the token will expire. |
| `token[scopes]` | array[Array] | form |  | The scopes to associate with the token. |
| `token[regenerate]` | boolean | form |  | Regenerate the actual token. |

**Returns:** `void`

## DELETE /v1/users/{user_id}/tokens/{id}

**Delete an access token**  —  `delete_access_token`

The ID can be the actual database ID of the token, or the 'token_hint' value.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## Token

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The internal database ID of the token. |
| `created_at` | string (date-time) |  | The time the token was created. |
| `expires_at` | ['string', 'null'] (date-time) |  | The time the token will permanently expire, or null if it does not permanently expire. |
| `workflow_state` | string |  | The current state of the token. One of 'active', 'pending', 'disabled', or 'deleted'. |
| `remember_access` | boolean |  | Whether the token should be remembered across sessions. Only applicable for OAuth tokens. |
| `scopes` | array[string] |  | The scopes associated with the token. If empty, there are no scope limitations. |
| `real_user_id` | ['integer', 'null'] |  | If the token was created while masquerading, this is the ID of the real user. Otherwise, null. |
| `token` | string |  | The actual access token. Only included when the token is first created. |
| `token_hint` | string |  | A short, unique string that can be used to look up the token. |
| `user_id` | integer |  | The ID of the user the token belongs to. |
| `purpose` | string |  | The purpose of the token. |
| `app_name` | ['string', 'null'] |  | If the token was created by an OAuth application, this is the name of that application. Otherwise, null. |
| `can_manually_regenerate` | boolean |  | Whether the current user can manually regenerate this token. |
