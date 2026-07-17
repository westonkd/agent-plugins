# Notice Handlers

> Canvas LMS REST API — `/notice_handlers` resource. Base path `/api`.

## GET /lti/notice-handlers/{context_external_tool_id}

**Show notice handlers**  —  `show_notice_handlers`

List all notice handlers for the tool

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_external_tool_id` | string | path | yes | ID |

**Returns:** `NoticeCatalog`

## PUT /lti/notice-handlers/{context_external_tool_id}

**Set notice handler**  —  `set_notice_handler`

Subscribe (set) or unsubscribe (remove) a notice handler for the tool

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_external_tool_id` | string | path | yes | ID |
| `notice_type` | string | form | yes | The type of notice |
| `handler` | string | form | yes | URL to receive the notice, or an empty string to unsubscribe |
| `max_batch_size` | integer (int64) | form |  | The maximum number of notices to include in a single batch |

**Returns:** `NoticeHandler`


---

# Models


## NoticeCatalog

Set of notice handlers (one per notice type) for an LTI tool deployment.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `client_id` | string |  | The LTI tool's client ID (global developer key ID) e.g. `10000000000001` |
| `deployment_id` | string |  | String that identifies the Platform-Tool integration governing the notices e.g. `123:8865aa05b4b79b64a91a86042e43af5ea8ae79eb` |
| `notice_handlers` | array[NoticeHandler] |  | List of notice handlers for the tool e.g. `[{'handler': '', 'notice_type': 'LtiHelloWorldNotice'}]` |


## NoticeHandler

A notice handler for a particular tool deployment and notice type.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `handler` | string |  | URL to receive the notice e.g. `https://example.com/notice_handler` |
| `notice_type` | string |  | The type of notice e.g. `LtiHelloWorldNotice` |
| `max_batch_size` | integer |  | The maximum number of notices to include in a single batch, or 'null' if not set. e.g. `100` |
