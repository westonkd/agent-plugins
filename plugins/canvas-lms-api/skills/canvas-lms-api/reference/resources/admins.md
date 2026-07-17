# Admins

> Canvas LMS REST API — `/admins` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/admins

**List account admins**  —  `list_account_admins`

A paginated list of the admins in the account

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user_id` | array[Integer] | query |  | Scope the results to those with user IDs equal to any of the IDs specified here. |
| `search_term` | string | query |  | The partial name or full ID of the admins to match and return in the results list. Must be at least 2 characters. |
| `include_deleted` | boolean | query |  | When set to true, returns admins who have been deleted |

**Returns:** `array[Admin]`

## POST /v1/accounts/{account_id}/admins

**Make an account admin**  —  `make_account_admin`

Flag an existing user as an admin within the account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user_id` | integer (int64) | form | yes | The id of the user to promote. |
| `role` | string | form |  | [DEPRECATED] The user's admin relationship with the account will be created with the given role. Defaults to 'AccountAdmin'. |
| `role_id` | integer (int64) | form |  | The user's admin relationship with the account will be created with the given role. Defaults to the built-in role for 'AccountAdmin'. |
| `send_confirmation` | boolean | form |  | Send a notification email to the new admin if true. Default is true. |

**Returns:** `Admin`

## DELETE /v1/accounts/{account_id}/admins/{user_id}

**Remove account admin**  —  `remove_account_admin`

Remove the rights associated with an account admin role from a user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `role` | string | query |  | [DEPRECATED] Account role to remove from the user. |
| `role_id` | integer (int64) | query | yes | The id of the role representing the user's admin relationship with the account. |

**Returns:** `Admin`

## GET /v1/accounts/{account_id}/admins/self

**List my admin roles**  —  `list_my_admin_roles`

A paginated list of the current user's roles in the account. The results are the same
as those returned by the {api:AdminsController#index List account admins} endpoint with
+user_id+ set to +self+, except the "Admins - Add / Remove" permission is not required.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[Admin]`


---

# Models


## Admin

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer | yes | The unique identifier for the account role/user assignment. e.g. `1023` |
| `role` | string |  | The account role assigned. This can be 'AccountAdmin' or a user-defined role created by the Roles API. e.g. `AccountAdmin` |
| `user` | User |  | The user the role is assigned to. See the Users API for details. |
| `workflow_state` | string |  | The status of the account role/user assignment. e.g. `deleted` |
