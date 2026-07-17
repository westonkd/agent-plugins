# Developer Key Account Bindings

> Canvas LMS REST API — `/developer_key_account_bindings` resource. Base path `/api`.

## POST /v1/accounts/{account_id}/developer_keys/{developer_key_id}/developer_key_account_bindings

**Create a Developer Key Account Binding**  —  `create_developer_key_account_binding`

Create a new Developer Key Account Binding. The developer key specified
in the request URL must be available in the requested account or the
requested account's account chain. If the binding already exists for the
specified account/key combination it will be updated.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `developer_key_id` | string | path | yes | ID |
| `workflow_state` | string | form |  | The workflow state for the binding. Must be one of "on", "off", or "allow". Defaults to "off". |

**Returns:** `DeveloperKeyAccountBinding`


---

# Models


## DeveloperKeyAccountBinding

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | number |  | The Canvas ID of the binding e.g. `1` |
| `account_id` | number |  | The global Canvas ID of the account in the binding e.g. `10000000000001` |
| `developer_key_id` | number |  | The global Canvas ID of the developer key in the binding e.g. `10000000000008` |
| `workflow_state` | number |  | The workflow state of the binding. Will be one of 'on', 'off', or 'allow.' e.g. `on` |
| `account_owns_binding` | boolean |  | True if the requested context owns the binding e.g. `true` |
