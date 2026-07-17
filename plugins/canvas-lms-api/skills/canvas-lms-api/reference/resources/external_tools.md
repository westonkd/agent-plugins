# External Tools

> Canvas LMS REST API — `/external_tools` resource. Base path `/api`.

## GET /v1/courses/{course_id}/external_tools

**List external tools**  —  `list_external_tools_courses`

Returns the paginated list of external tools for the current context.
See the get request docs for a single tool for a list of properties on an external tool.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name of the tools to match and return. |
| `selectable` | boolean | query |  | If true, then only tools that are meant to be selectable are returned. |
| `include_parents` | boolean | query |  | If true, then include tools installed in all accounts above the current context |
| `placement` | string | query |  | The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of 'editor_button' |

**Returns:** `array[ContextExternalTool]`

## GET /v1/accounts/{account_id}/external_tools

**List external tools**  —  `list_external_tools_accounts`

Returns the paginated list of external tools for the current context.
See the get request docs for a single tool for a list of properties on an external tool.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name of the tools to match and return. |
| `selectable` | boolean | query |  | If true, then only tools that are meant to be selectable are returned. |
| `include_parents` | boolean | query |  | If true, then include tools installed in all accounts above the current context |
| `placement` | string | query |  | The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of 'editor_button' |

**Returns:** `array[ContextExternalTool]`

## GET /v1/groups/{group_id}/external_tools

**List external tools**  —  `list_external_tools_groups`

Returns the paginated list of external tools for the current context.
See the get request docs for a single tool for a list of properties on an external tool.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name of the tools to match and return. |
| `selectable` | boolean | query |  | If true, then only tools that are meant to be selectable are returned. |
| `include_parents` | boolean | query |  | If true, then include tools installed in all accounts above the current context |
| `placement` | string | query |  | The placement type to filter by.  Return all tools at the current context as well as all tools from the parent, and filter the tools list to only those with a placement of 'editor_button' |

**Returns:** `array[ContextExternalTool]`

## GET /v1/courses/{course_id}/external_tools/sessionless_launch

**Get a sessionless launch url for an external tool.**  —  `get_sessionless_launch_url_for_external_tool_courses`

Returns a sessionless launch url for an external tool.
Prefers the resource_link_lookup_uuid, but defaults to the other passed
  parameters id, url, and launch_type

NOTE: Either the resource_link_lookup_uuid, id, or url must be provided unless launch_type is assessment or module_item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | query |  | The external id of the tool to launch. |
| `url` | string | query |  | The LTI launch url for the external tool. |
| `assignment_id` | string | query |  | The assignment id for an assignment launch. Required if launch_type is set to "assessment". |
| `module_item_id` | string | query |  | The assignment id for a module item launch. Required if launch_type is set to "module_item". |
| `launch_type` | string | query |  | The type of launch to perform on the external tool. Placement names (eg. "course_navigation") can also be specified to use the custom launch url for that placement; if done, the tool id must be provided. Allowed: `assessment`, `module_item` |
| `resource_link_lookup_uuid` | string | query |  | The identifier to lookup a resource link. |

**Returns:** `void`

## GET /v1/accounts/{account_id}/external_tools/sessionless_launch

**Get a sessionless launch url for an external tool.**  —  `get_sessionless_launch_url_for_external_tool_accounts`

Returns a sessionless launch url for an external tool.
Prefers the resource_link_lookup_uuid, but defaults to the other passed
  parameters id, url, and launch_type

NOTE: Either the resource_link_lookup_uuid, id, or url must be provided unless launch_type is assessment or module_item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | query |  | The external id of the tool to launch. |
| `url` | string | query |  | The LTI launch url for the external tool. |
| `assignment_id` | string | query |  | The assignment id for an assignment launch. Required if launch_type is set to "assessment". |
| `module_item_id` | string | query |  | The assignment id for a module item launch. Required if launch_type is set to "module_item". |
| `launch_type` | string | query |  | The type of launch to perform on the external tool. Placement names (eg. "course_navigation") can also be specified to use the custom launch url for that placement; if done, the tool id must be provided. Allowed: `assessment`, `module_item` |
| `resource_link_lookup_uuid` | string | query |  | The identifier to lookup a resource link. |

**Returns:** `void`

## GET /v1/courses/{course_id}/external_tools/{external_tool_id}

**Get a single external tool**  —  `get_single_external_tool_courses`

Returns the specified external tool.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `external_tool_id` | string | path | yes | ID |

**Returns:** `ContextExternalTool`

## GET /v1/accounts/{account_id}/external_tools/{external_tool_id}

**Get a single external tool**  —  `get_single_external_tool_accounts`

Returns the specified external tool.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `external_tool_id` | string | path | yes | ID |

**Returns:** `ContextExternalTool`

## POST /v1/courses/{course_id}/external_tools

**Create an external tool**  —  `create_external_tool_courses`

Create an external tool in the specified course/account.
The created tool will be returned, see the "show" endpoint for an example.
If a client ID is supplied canvas will attempt to create a context external
tool using the LTI 1.3 standard.

See the <a href="file.lti_dev_key_config.html#placements-params">Placements Documentation</a> for more information on what
placements are available, the possible fields, and their accepted values.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `client_id` | string | form | yes | The client id is attached to the developer key. If supplied all other parameters are unnecessary and will be ignored |
| `name` | string | form | yes | The name of the tool |
| `privacy_level` | string | form | yes | How much user information to send to the external tool. Allowed: `anonymous`, `name_only`, `email_only`, `public` |
| `consumer_key` | string | form | yes | The consumer key for the external tool |
| `shared_secret` | string | form | yes | The shared secret with the external tool |
| `description` | string | form |  | A description of the tool |
| `url` | string | form |  | The url to match links against. Either "url" or "domain" should be set, not both. |
| `domain` | string | form |  | The domain to match links against. Either "url" or "domain" should be set, not both. |
| `icon_url` | string | form |  | The url of the icon to show for this tool |
| `text` | string | form |  | The default text to show for this tool |
| `custom_fields[field_name]` | string | form |  | Custom fields that will be sent to the tool consumer; can be used multiple times |
| `is_rce_favorite` | boolean | form |  | (Deprecated in favor of {api:ExternalToolsController#mark_rce_favorite Mark tool to RCE Favorites} and {api:ExternalToolsController#unmark_rce_favorite Unmark tool from RCE Favorites}) Whether this tool should appear in a preferred location in the RCE. This only applies to tools in root account contexts that have an editor button placement. |
| `<placement_name>[<placement_configuration_key>]` | variable | form |  | Set the <placement_configuration_key> value for a specific placement. |
| `config_type` | string | form |  | Configuration can be passed in as Common Cartridge XML instead of using query parameters. If this value is "by_url" or "by_xml" then an XML configuration will be expected in either the "config_xml" or "config_url" parameter. Note that the name parameter overrides the tool name provided in the XML. Allowed: `by_url`, `by_xml` |
| `config_xml` | string | form |  | XML tool configuration, as specified in the Common Cartridge XML specification. This is required if "config_type" is set to "by_xml" |
| `config_url` | string | form |  | URL where the server can retrieve an XML tool configuration, as specified in the Common Cartridge XML specification. This is required if "config_type" is set to "by_url" |
| `not_selectable` | boolean | form |  | Default: false. If set to true, and if resource_selection is set to false, the tool won't show up in the external tool selection UI in modules and assignments |
| `oauth_compliant` | boolean | form |  | Default: false, if set to true LTI query params will not be copied to the post body. |
| `unified_tool_id` | string | form |  | The unique identifier for the tool in LearnPlatform |

**Returns:** `ContextExternalTool`

## POST /v1/accounts/{account_id}/external_tools

**Create an external tool**  —  `create_external_tool_accounts`

Create an external tool in the specified course/account.
The created tool will be returned, see the "show" endpoint for an example.
If a client ID is supplied canvas will attempt to create a context external
tool using the LTI 1.3 standard.

See the <a href="file.lti_dev_key_config.html#placements-params">Placements Documentation</a> for more information on what
placements are available, the possible fields, and their accepted values.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `client_id` | string | form | yes | The client id is attached to the developer key. If supplied all other parameters are unnecessary and will be ignored |
| `name` | string | form | yes | The name of the tool |
| `privacy_level` | string | form | yes | How much user information to send to the external tool. Allowed: `anonymous`, `name_only`, `email_only`, `public` |
| `consumer_key` | string | form | yes | The consumer key for the external tool |
| `shared_secret` | string | form | yes | The shared secret with the external tool |
| `description` | string | form |  | A description of the tool |
| `url` | string | form |  | The url to match links against. Either "url" or "domain" should be set, not both. |
| `domain` | string | form |  | The domain to match links against. Either "url" or "domain" should be set, not both. |
| `icon_url` | string | form |  | The url of the icon to show for this tool |
| `text` | string | form |  | The default text to show for this tool |
| `custom_fields[field_name]` | string | form |  | Custom fields that will be sent to the tool consumer; can be used multiple times |
| `is_rce_favorite` | boolean | form |  | (Deprecated in favor of {api:ExternalToolsController#mark_rce_favorite Mark tool to RCE Favorites} and {api:ExternalToolsController#unmark_rce_favorite Unmark tool from RCE Favorites}) Whether this tool should appear in a preferred location in the RCE. This only applies to tools in root account contexts that have an editor button placement. |
| `<placement_name>[<placement_configuration_key>]` | variable | form |  | Set the <placement_configuration_key> value for a specific placement. |
| `config_type` | string | form |  | Configuration can be passed in as Common Cartridge XML instead of using query parameters. If this value is "by_url" or "by_xml" then an XML configuration will be expected in either the "config_xml" or "config_url" parameter. Note that the name parameter overrides the tool name provided in the XML. Allowed: `by_url`, `by_xml` |
| `config_xml` | string | form |  | XML tool configuration, as specified in the Common Cartridge XML specification. This is required if "config_type" is set to "by_xml" |
| `config_url` | string | form |  | URL where the server can retrieve an XML tool configuration, as specified in the Common Cartridge XML specification. This is required if "config_type" is set to "by_url" |
| `not_selectable` | boolean | form |  | Default: false. If set to true, and if resource_selection is set to false, the tool won't show up in the external tool selection UI in modules and assignments |
| `oauth_compliant` | boolean | form |  | Default: false, if set to true LTI query params will not be copied to the post body. |
| `unified_tool_id` | string | form |  | The unique identifier for the tool in LearnPlatform |

**Returns:** `ContextExternalTool`

## PUT /v1/courses/{course_id}/external_tools/{external_tool_id}

**Edit an external tool**  —  `edit_external_tool_courses`

Update the specified external tool. Uses same parameters as create. Returns the updated tool.

NOTE: Any updates made to LTI 1.3 tools with this API will be overridden if any changes are
made to the tool's associated LTI Registration/Developer Key configuration. In almost all cases,
changes should be made to the tool's associated LTI Registration configuration, not individual tools.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `external_tool_id` | string | path | yes | ID |

**Returns:** `ContextExternalTool`

## PUT /v1/accounts/{account_id}/external_tools/{external_tool_id}

**Edit an external tool**  —  `edit_external_tool_accounts`

Update the specified external tool. Uses same parameters as create. Returns the updated tool.

NOTE: Any updates made to LTI 1.3 tools with this API will be overridden if any changes are
made to the tool's associated LTI Registration/Developer Key configuration. In almost all cases,
changes should be made to the tool's associated LTI Registration configuration, not individual tools.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `external_tool_id` | string | path | yes | ID |

**Returns:** `ContextExternalTool`

## DELETE /v1/courses/{course_id}/external_tools/{external_tool_id}

**Delete an external tool**  —  `delete_external_tool_courses`

Remove the specified external tool

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `external_tool_id` | string | path | yes | ID |

**Returns:** `ContextExternalTool`

## DELETE /v1/accounts/{account_id}/external_tools/{external_tool_id}

**Delete an external tool**  —  `delete_external_tool_accounts`

Remove the specified external tool

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `external_tool_id` | string | path | yes | ID |

**Returns:** `ContextExternalTool`

## POST /v1/accounts/{account_id}/external_tools/rce_favorites/{id}

**Mark tool as RCE Favorite**  —  `mark_tool_as_rce_favorite`

Mark the specified editor_button external tool as a favorite in the RCE editor
for courses in the given account and its subaccounts (if the subaccounts
haven't set their own RCE Favorites). This places the tool in a preferred location
in the RCE. Cannot mark more than 2 tools as RCE Favorites.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/accounts/{account_id}/external_tools/rce_favorites/{id}

**Unmark tool as RCE Favorite**  —  `unmark_tool_as_rce_favorite`

Unmark the specified external tool as a favorite in the RCE editor
for the given account. The tool will remain available but will no longer
appear in the preferred favorites location.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/accounts/{account_id}/external_tools/top_nav_favorites/{id}

**Add tool to Top Navigation Favorites**  —  `add_tool_to_top_navigation_favorites`

Adds a dedicated button in Top Navigation for the specified tool for the given account.
Cannot set more than 2 top_navigation Favorites.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/accounts/{account_id}/external_tools/top_nav_favorites/{id}

**Remove tool from Top Navigation Favorites**  —  `remove_tool_from_top_navigation_favorites`

Removes the dedicated button in Top Navigation for the specified tool for the given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/external_tools/visible_course_nav_tools

**Get visible course navigation tools**  —  `get_visible_course_navigation_tools`

Get a list of external tools with the course_navigation placement that have not been hidden in
course settings and whose visibility settings apply to the requesting user. These tools are the
same that appear in the course navigation.

The response format is the same as for List external tools, but with additional context_id and
context_name fields on each element in the array.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_codes` | array[string] | query | yes | List of context_codes to retrieve visible course nav tools for (for example, +course_123+). Only courses are presently supported. |

**Returns:** `void`

## GET /v1/courses/{course_id}/external_tools/visible_course_nav_tools

**Get visible course navigation tools for a single course**  —  `get_visible_course_navigation_tools_for_single_course`

Get a list of external tools with the course_navigation placement that have not been hidden in
course settings and whose visibility settings apply to the requesting user. These tools are the
same that appear in the course navigation.

The response format is the same as Get visible course navigation tools.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## ContextExternalTool

An external tool configured for a specific context

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the external tool e.g. `37` |
| `name` | string |  | The name of the external tool e.g. `Basic 1.1 tool` |
| `description` | string |  | A description of the external tool e.g. `Basic LTI 1.1 Tool` |
| `url` | string |  | The launch URL for the external tool e.g. `http://example.com/launch` |
| `domain` | string |  | The domain to match links against. Note that this doesn't contain the protocol. e.g. `example.com` |
| `consumer_key` | string |  | The consumer key used by the tool (The associated shared secret is not returned) e.g. `key` |
| `created_at` | string |  | Timestamp of the tool's creation e.g. `2037-07-21T13:29:31Z` |
| `updated_at` | string |  | Timestamp of the tool's last update e.g. `2037-07-28T19:38:31Z` |
| `privacy_level` | string |  | How much user information to send to the external tool e.g. `anonymous` Allowed: `anonymous`, `name_only`, `email_only`, `public` |
| `custom_fields` | object |  | Custom fields that will be sent to the tool consumer e.g. `{'key': 'value'}` |
| `workflow_state` | string |  | The current state of the external tool e.g. `public` Allowed: `public`, `anonymous`, `deleted` |
| `is_rce_favorite` | boolean |  | Boolean determining whether this tool should be in a preferred location in the RCE. Only present if the tool can be an RCE favorite. e.g. `False` |
| `is_top_nav_favorite` | boolean |  | Boolean determining whether this tool should have a dedicated button in Top Navigation. Only present if the tool can be a top nav favorite. e.g. `False` |
| `selection_width` | integer |  | The pixel width of the iFrame that the tool will be rendered in e.g. `500` |
| `selection_height` | integer |  | The pixel height of the iFrame that the tool will be rendered in e.g. `500` |
| `icon_url` | string |  | The URL for the tool icon e.g. `https://example.com/icon.png` |
| `not_selectable` | boolean |  | Whether the tool is not selectable from assignment and modules e.g. `False` |
| `version` | string |  | The LTI version of the tool e.g. `1.1` Allowed: `1.1`, `1.3` |
| `unified_tool_id` | string |  | The unique identifier for the tool in LearnPlatform |
| `developer_key_id` | integer |  | The developer key id associated with this tool. Only present for LTI 1.3 tools. e.g. `123` |
| `lti_registration_id` | integer |  | The LTI registration id associated with this tool. Only present for LTI 1.3 tools. e.g. `456` |
| `deployment_id` | string |  | The unique identifier for the deployment of the tool e.g. `37:b82229c6e10bcb87beb1f1b287faee560ddc3109` |
| `allow_membership_service_access` | boolean |  | Whether the tool can access the membership service. Only present if the feature is enabled. e.g. `False` |
| `prefer_sis_email` | boolean |  | Whether to send the SIS email address in launches e.g. `False` |
| `estimated_duration` | EstimatedDuration |  | The estimated duration for completing this tool. Only present for horizon courses when the tool has an estimated duration. |
| `account_navigation` | ContextExternalToolPlacement |  | Configuration for account navigation placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `analytics_hub` | ContextExternalToolPlacement |  | Configuration for analytics hub placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `assignment_edit` | ContextExternalToolPlacement |  | Configuration for assignment edit placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `assignment_group_menu` | ContextExternalToolPlacement |  | Configuration for assignment group menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `assignment_index_menu` | ContextExternalToolPlacement |  | Configuration for assignment index menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `assignment_menu` | ContextExternalToolPlacement |  | Configuration for assignment menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `assignment_selection` | ContextExternalToolPlacement |  | Configuration for assignment selection placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `assignment_view` | ContextExternalToolPlacement |  | Configuration for assignment view placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `collaboration` | ContextExternalToolPlacement |  | Configuration for collaboration placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `conference_selection` | ContextExternalToolPlacement |  | Configuration for conference selection placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `course_assignments_menu` | ContextExternalToolPlacement |  | Configuration for course assignments menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `course_home_sub_navigation` | ContextExternalToolPlacement |  | Configuration for course home sub navigation placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `course_navigation` | ContextExternalToolPlacement |  | Configuration for course navigation placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `course_settings_sub_navigation` | ContextExternalToolPlacement |  | Configuration for course settings sub navigation placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `discussion_topic_index_menu` | ContextExternalToolPlacement |  | Configuration for discussion topic index menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `discussion_topic_menu` | ContextExternalToolPlacement |  | Configuration for discussion topic menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `editor_button` | ContextExternalToolPlacement |  | Configuration for editor button placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `file_index_menu` | ContextExternalToolPlacement |  | Configuration for file index menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `file_menu` | ContextExternalToolPlacement |  | Configuration for file menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `global_navigation` | ContextExternalToolPlacement |  | Configuration for global navigation placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `homework_submission` | ContextExternalToolPlacement |  | Configuration for homework submission placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `link_selection` | ContextExternalToolPlacement |  | Configuration for link selection placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `migration_selection` | ContextExternalToolPlacement |  | Configuration for migration selection placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `module_group_menu` | ContextExternalToolPlacement |  | Configuration for module group menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `module_index_menu` | ContextExternalToolPlacement |  | Configuration for module index menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `module_index_menu_modal` | ContextExternalToolPlacement |  | Configuration for module index menu modal placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `module_menu_modal` | ContextExternalToolPlacement |  | Configuration for module menu modal placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `module_menu` | ContextExternalToolPlacement |  | Configuration for module menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `page_index_menu` | ContextExternalToolPlacement |  | Configuration for page index menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `page_menu` | ContextExternalToolPlacement |  | Configuration for page menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `post_grades` | ContextExternalToolPlacement |  | Configuration for post grades (sync grades) placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `quiz_index_menu` | ContextExternalToolPlacement |  | Configuration for quiz index menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `quiz_menu` | ContextExternalToolPlacement |  | Configuration for quiz menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `resource_selection` | ContextExternalToolPlacement |  | Configuration for resource selection placement. Null if not configured for this placement. This placement is deprecated. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `similarity_detection` | ContextExternalToolPlacement |  | Configuration for similarity detection placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `student_context_card` | ContextExternalToolPlacement |  | Configuration for student context card placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `submission_type_selection` | ContextExternalToolPlacement |  | Configuration for submission type selection placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `tool_configuration` | ContextExternalToolPlacement |  | Configuration for tool configuration placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `top_navigation` | ContextExternalToolPlacement |  | Configuration for top navigation placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `user_navigation` | ContextExternalToolPlacement |  | Configuration for user navigation placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `wiki_index_menu` | ContextExternalToolPlacement |  | Configuration for wiki index menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `wiki_page_menu` | ContextExternalToolPlacement |  | Configuration for wiki page menu placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `ActivityAssetProcessor` | ContextExternalToolPlacement |  | Configuration for activity asset processor placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `ActivityAssetProcessorContribution` | ContextExternalToolPlacement |  | Configuration for activity asset processor contribution placement. Null if not configured for this placement. e.g. `{'type': 'ContextExternalToolPlacement'}` |
| `message_settings` | array[ContextExternalToolMessageSettings] |  | Configuration for placementless message types (currently only LtiEulaRequest). e.g. `[{'type': 'LtiEulaRequest', 'enabled': True, 'target_link_uri': 'https://example.com/eula', 'custom_fields': {'agreement_version': '2.1'}}]` |


## ContextExternalToolPlacement

Configuration for a specific placement of an external tool. If null, no configuration is present.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `enabled` | boolean |  | Whether this placement is enabled e.g. `True` |
| `url` | string |  | The launch URL for this specific placement. Overrides the tool's default URL. For LTI 1.1 tools only. e.g. `http://example.com/launch?placement=course_navigation` |
| `target_link_uri` | string |  | The launch URL for this specific placement. Overrides the tool's default target_link_uri. For LTI 1.3 tools only. e.g. `http://example.com/launch?placement=course_navigation` |
| `text` | string |  | The text/label to display for this placement. Overridable by 'labels' in placement configuration. e.g. `Course Navigation Tool` |
| `label` | string |  | The localized label for this placement. This is the resolved text after applying internationalization. e.g. `Course Navigation Tool` |
| `labels` | object |  | Internationalization labels for this placement. Keys are locale codes, values are localized text. e.g. `{'en': 'Course Navigation', 'es': 'Navegación del Curso'}` |
| `message_type` | string |  | The LTI message type for this placement. Not all placements support all message types. e.g. `LtiResourceLinkRequest` Allowed: `basic_lti_request`, `ContentItemSelectionRequest`, `LtiResourceLinkRequest`, `LtiDeepLinkingRequest` |
| `selection_width` | integer |  | The width of the iframe or popup for this placement e.g. `500` |
| `selection_height` | integer |  | The height of the iframe or popup for this placement e.g. `500` |
| `launch_width` | integer |  | The width of the launch window. Not standard everywhere yet. e.g. `800` |
| `launch_height` | integer |  | The height of the launch window. Not standard everywhere yet. e.g. `600` |
| `icon_url` | string |  | The URL of the icon for this placement e.g. `https://example.com/icon.png` |
| `canvas_icon_class` | string |  | The Canvas icon class to use for this placement instead of an icon URL e.g. `icon-lti` |
| `allow_fullscreen` | boolean |  | Whether to allow fullscreen mode for this placement (top_navigation placement only) e.g. `True` |
| `custom_fields` | object |  | Custom fields to be sent with this placement's launch. Merged with tool-level custom fields. e.g. `{'placement_id': 'course_nav', 'special_param': 'value'}` |
| `visibility` | string |  | Controls who can see this placement e.g. `members` Allowed: `public`, `members`, `admins` |
| `required_permissions` | string |  | Comma-separated list of Canvas permissions required to launch from this placement. The user must have all permissions in order to launch the tool. e.g. `manage_course_content_edit,manage_course_content_read` |
| `default` | string |  | Default display state for navigation placements. Only applies to account_navigation and course_navigation placements. e.g. `disabled` Allowed: `enabled`, `disabled` |
| `display_type` | string |  | The layout type to use when launching the tool. For global_navigation and analytics_hub, defaults to 'full_width'. e.g. `full_width_in_context` Allowed: `default`, `full_width`, `full_width_in_context`, `full_width_with_nav`, `in_nav_context`, `borderless` |
| `windowTarget` | string |  | When set to '_blank', opens placement in a new tab. Only '_blank' is supported. e.g. `_blank` Allowed: `_blank` |
| `accept_media_types` | string |  | Comma-separated list of media types that the tool can accept. Only valid for file_menu placement. e.g. `image/*,video/*` |
| `use_tray` | boolean |  | If true, the tool will be launched in the tray. Only used by the editor_button placement. e.g. `True` |
| `icon_svg_path_64` | string |  | An SVG path to use instead of an icon_url. Only valid for global_navigation placement. e.g. `M100,37L70.1,10.5v176H37...` |
| `root_account_only` | boolean |  | Whether this placement should only be available at the root account level. Only applies to account_navigation placement. e.g. `False` |
| `description` | string |  | A description of this placement. Only valid for submission_type_selection placement. Maximum length of 255 characters. e.g. `Submit your work using our external tool` |
| `require_resource_selection` | boolean |  | Whether resource selection is required for this placement. Only valid for submission_type_selection placement. e.g. `True` |
| `prefer_sis_email` | boolean |  | If true, the tool will send the SIS email in the lis_person_contact_email_primary launch property. LTI 1.1 only. e.g. `False` |
| `oauth_compliant` | boolean |  | If true, query parameters from the launch URL will not be copied to the POST body. LTI 1.1 only. e.g. `True` |


## ContextExternalToolMessageSettings

Configuration for a placementless message type (message type that doesn't belong to a specific placement)

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `type` | string |  | The message type identifier (e.g., 'LtiEulaRequest') e.g. `LtiEulaRequest` |
| `enabled` | boolean |  | Whether this message type is enabled e.g. `True` |
| `target_link_uri` | string |  | The target URI for launching this message type e.g. `https://example.com/eula` |
| `custom_fields` | object |  | Custom fields specific to this message type. e.g. `{'key': 'value'}` |


## EstimatedDuration

An estimated duration for completing a learning activity

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the estimated duration e.g. `123` |
| `duration` | string |  | The estimated duration in ISO 8601 format e.g. `PT30M` |
| `created_at` | string |  | Timestamp of when the estimated duration was created e.g. `2024-01-01T00:00:00Z` |
| `updated_at` | string |  | Timestamp of when the estimated duration was last updated e.g. `2024-01-01T00:00:00Z` |
