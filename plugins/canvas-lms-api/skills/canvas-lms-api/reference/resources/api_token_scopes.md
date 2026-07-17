# API Token Scopes

> Canvas LMS REST API — `/api_token_scopes` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/scopes

**List scopes**  —  `list_scopes`

A list of scopes that can be applied to developer keys and access tokens.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `group_by` | string | query |  | The attribute to group the scopes by. By default no grouping is done. Allowed: `resource_name` |

**Returns:** `array[Scope]`


---

# Models


## Scope

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `resource` | string |  | The resource the scope is associated with e.g. `courses` |
| `resource_name` | string |  | The localized resource name e.g. `Courses` |
| `controller` | string |  | The controller the scope is associated to e.g. `courses` |
| `action` | string |  | The controller action the scope is associated to e.g. `index` |
| `verb` | string |  | The HTTP verb for the scope e.g. `GET` |
| `scope` | string |  | The identifier for the scope e.g. `url:GET\|/api/v1/courses` |
