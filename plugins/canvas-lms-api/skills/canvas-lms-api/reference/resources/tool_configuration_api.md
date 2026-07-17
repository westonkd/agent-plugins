# Tool Configuration API

> Canvas LMS REST API — `/tool_configuration_api` resource. Base path `/api`.

## POST /lti/accounts/{account_id}/developer_keys/tool_configuration

**Create Tool configuration**  —  `create_tool_configuration`

Creates tool configuration with the provided parameters.

Settings may be provided directly as JSON through the "settings"
parameter or indirectly through the "settings_url" parameter.

If both the "settings" and "settings_url" parameters are set,
the "settings_url" parameter will be ignored.

When "settings_url" parameter is set, the DeveloperKey.redirect_uris will
be created with "target_link_uri" from the JSON tool configuration, in case,
the developer_key.redirect_uris parameter is not given.

Use of this endpoint will create a new developer_key.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `settings` | Object | form |  | JSON representation of the tool configuration |
| `settings_url` | string | form |  | URL of settings JSON |
| `developer_key` | Object | form |  | JSON representation of the developer key fields to use when creating the developer key for the tool configuration. Valid fields are: "name", "email", "notes", "test_cluster_only", "client_credentials_audience", and "scopes". |
| `disabled_placements` | Array | form |  | An array of strings indicating which Canvas placements should be excluded from the tool configuration. |
| `custom_fields` | string | form |  | A new line separated string of key/value pairs to be used as custom fields in the LTI launch. Example: foo=bar\ncourse=$Canvas.course.id |

**Returns:** `ToolConfiguration`

## PUT /lti/developer_keys/{developer_key_id}/tool_configuration

**Update Tool configuration**  —  `update_tool_configuration`

Update tool configuration with the provided parameters.

Settings may be provided directly as JSON through the "settings"
parameter. The settings_url is not used for updates.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `settings` | Object | form |  | JSON representation of the tool configuration |
| `developer_key_id` | string | path | yes | no description |
| `developer_key` | Object | form |  | JSON representation of the developer key fields to use when updating the developer key for the tool configuraiton. Valid fields are: "name", "email", "notes", "test_cluster_only", "client_credentials_audience", "scopes". |
| `disabled_placements` | Array | form |  | An array of strings indicating which Canvas placements should be excluded from the tool configuration. |
| `custom_fields` | string | form |  | A new line seperated string of key/value pairs to be used as custom fields in the LTI launch. Example: foo=bar\ncourse=$Canvas.course.id |
| `comment` | string | form |  | A comment explaining why this change was made, to be recorded in the change-log. Must not exceed 2000 characters. Optional. |

**Returns:** `ToolConfiguration`

## GET /lti/accounts/{account_id}/developer_keys/{developer_key_id}/tool_configuration

**Show Tool configuration**  —  `show_tool_configuration_accounts`

Show tool configuration for specified developer key.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `developer_key_id` | string | path | yes | ID |

**Returns:** `ToolConfiguration`

## GET /lti/courses/{course_id}/developer_keys/{developer_key_id}/tool_configuration

**Show Tool configuration**  —  `show_tool_configuration_courses`

Show tool configuration for specified developer key.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `developer_key_id` | string | path | yes | ID |

**Returns:** `ToolConfiguration`

## DELETE /lti/developer_keys/{developer_key_id}/tool_configuration

**Show Tool configuration**  —  `show_tool_configuration`

Destroy the tool configuration for the specified developer key.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `developer_key_id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## ToolConfiguration

A tool configuration associated with a developer key

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `developer_key_id` | integer |  | The tool configuration's developer key id e.g. `23` |
| `settings` | object |  | The tool configuration JSON e.g. `{'name': 'LTI 1.3 Tool'}` |
