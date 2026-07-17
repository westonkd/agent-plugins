# Accounts (LTI)

> Canvas LMS REST API — `/accounts_(lti)` resource. Base path `/api`.

## GET /lti/accounts/{account_id}

**Get account**  —  `get_account`

Retrieve information on an individual account, given by local or global ID.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `Account`


---

# Models


## Account

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the Account object e.g. `2` |
| `name` | string |  | The display name of the account e.g. `Canvas Account` |
| `uuid` | string |  | The UUID of the account e.g. `WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5` |
| `parent_account_id` | integer |  | The account's parent ID, or null if this is the root account e.g. `1` |
| `root_account_id` | integer |  | The ID of the root account, or null if this is the root account e.g. `1` |
| `workflow_state` | string |  | The state of the account. Can be 'active' or 'deleted'. e.g. `active` |
