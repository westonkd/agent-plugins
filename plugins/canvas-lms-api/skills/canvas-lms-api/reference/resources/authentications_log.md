# Authentications Log

> Canvas LMS REST API — `/authentications_log` resource. Base path `/api`.

## GET /v1/audit/authentication/logins/{login_id}

**Query by login.**  —  `query_by_login`

List authentication events for a given login.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `login_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. Events are stored for one year. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `void`

## GET /v1/audit/authentication/accounts/{account_id}

**Query by account.**  —  `query_by_account`

List authentication events for a given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. Events are stored for one year. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `void`

## GET /v1/audit/authentication/users/{user_id}

**Query by user.**  —  `query_by_user`

List authentication events for a given user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. Events are stored for one year. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `void`


---

# Models


## AuthenticationEvent

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `created_at` | datetime |  | timestamp of the event e.g. `2012-07-19T15:00:00-06:00` |
| `event_type` | string |  | authentication event type ('login' or 'logout') e.g. `login` |
| `pseudonym_id` | integer |  | ID of the pseudonym (login) associated with the event e.g. `9478` |
| `account_id` | integer |  | ID of the account associated with the event. will match the account_id in the associated pseudonym. e.g. `2319` |
| `user_id` | integer |  | ID of the user associated with the event will match the user_id in the associated pseudonym. e.g. `362` |
