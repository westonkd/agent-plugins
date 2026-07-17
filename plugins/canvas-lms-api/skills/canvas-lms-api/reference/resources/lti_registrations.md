# LTI Registrations

> Canvas LMS REST API — `/lti_registrations` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/lti_registrations

**List LTI Registrations in an account**  —  `list_lti_registrations_in_account`

Returns all LTI registrations in the specified account.
Includes registrations created in this account, those set to 'allow' from a
parent root account (like Site Admin) and 'on' for this account,
and those enabled 'on' at the parent root account level.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `per_page` | integer (int64) | query |  | The number of registrations to return per page. Defaults to 15. |
| `page` | integer (int64) | query |  | The page number to return. Defaults to 1. |
| `sort` | string | query |  | The field to sort by. Choices are: name, nickname, lti_version, installed, installed_by, updated_by, updated, and on. Defaults to installed. |
| `dir` | string | query |  | The order to sort the given column by. Defaults to desc. Allowed: `asc`, `desc` |
| `include` | array[string] | query |  | Array of additional data to include. Always includes [account_binding].  "account_binding":: the registration's binding to the given account "configuration":: the registration's Canvas-style tool configuration, without any overlays applied. "overlaid_configuration":: the registration's Canvas-style tool configuration, with all overlays applied. "overlay":: the registration's admin-defined configuration overlay |

**Returns:** `ListLtiRegistrationsResponse`

## GET /v1/accounts/{account_id}/lti_registrations/{id}

**Show an LTI Registration**  —  `show_lti_registration`

Return details about the specified LTI registration, including the
configuration and account binding.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional data to include. Always includes [account_binding configuration].  "account_binding":: the registration's binding to the given account "configuration":: the registration's Canvas-style tool configuration, without any overlays applied. "overlaid_configuration":: the registration's Canvas-style tool configuration, with all overlays applied. "overlaid_legacy_configuration":: the registration's legacy-style configuration, with all overlays applied. "overlay":: the registration's admin-defined configuration overlay "overlay_versions":: the registration's overlay's edit history |

**Returns:** `Lti::Registration`

## POST /v1/accounts/{account_id}/lti_registrations

**Create an LTI Registration**  —  `create_lti_registration`

Create a new LTI Registration, as well as an associated Tool Configuration, Developer Key, and Registration Account
binding.
To install/create using Dynamic Registration, please use the
{file:file.registration.html Dynamic Registration API}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `name` | string | form |  | The name of the tool. If one isn't provided, it will be inferred from the configuration's title. |
| `admin_nickname` | string | form |  | A friendly nickname set by admins to override the tool name |
| `vendor` | string | form |  | The vendor of the tool |
| `description` | string | form |  | A description of the tool. Cannot exceed 2048 bytes. |
| `configuration` | string | form |  | [Required, Lti::ToolConfiguration \| Lti::LegacyConfiguration] The LTI 1.3 configuration for the tool |
| `overlay` | string | form |  | [Lti::Overlay] The overlay configuration for the tool. Overrides values in the base configuration. |
| `unified_tool_id` | string | form |  | The unique identifier for the tool, used for analytics. If not provided, one will be generated. |
| `lock_deploying` | boolean | form |  | When true, no new deployments of this registration can be created. |
| `workflow_state` | string | form |  | "on"/"off"/"allow" set the account binding state directly (binding vocabulary). "active"/"inactive" set the registration state directly (registration vocabulary). All five values update both the binding and the registration to equivalent states. "allow" is only valid for Site Admin registrations. Defaults to "off". Allowed: `on`, `off`, `allow`, `active`, `inactive` |

**Returns:** `Lti::Registration`

## GET /v1/accounts/{account_id}/lti_registration_by_client_id/{client_id}

**Show an LTI Registration (via the client_id)**  —  `show_lti_registration_via_client_id`

Returns details about the specified LTI registration, including the
configuration and account binding.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `client_id` | string | path | yes | ID |

**Returns:** `Lti::Registration`

## GET /v1/accounts/{account_id}/lti_registrations/by_utid/{utid}

**Get LTI Registration by Unified Tool ID**  —  `get_lti_registration_by_unified_tool_id`

Returns an LTI registration by looking up its unified_tool_id.
Searches both manual configurations and IMS registrations.
Only returns registrations that are active and accessible from the
current account (owned by account, Site Admin, or has binding).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `utid` | string | path | yes | ID |

**Returns:** `Lti::Registration`

## GET /v1/accounts/{account_id}/lti_registrations/install_status/{client_id}

**Check LTI Registration Install Status**  —  `check_lti_registration_install_status`

Returns the local installation status for a Site Admin LTI registration.
If the developer key's registration is in Site Admin, returns the local copy
in the current account (if installed). If the registration is already in the
current account, returns it directly.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `client_id` | string | path | yes | ID |

**Returns:** `Lti::Registration`

## PUT /v1/accounts/{account_id}/lti_registrations/{id}

**Update an LTI Registration**  —  `update_lti_registration`

Update the specified LTI registration with the provided parameters. Note that updating the base tool configuration
of a registration that is associated with a Dynamic Registration will return a 422. All other fields can be updated
freely.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `name` | string | form |  | The name of the tool |
| `admin_nickname` | string | form |  | The admin-configured friendly display name for the registration |
| `description` | string | form |  | A description of the tool. Cannot exceed 2048 bytes. |
| `configuration` | string | form |  | [Lti::ToolConfiguration \| Lti::LegacyConfiguration] The LTI 1.3 configuration for the tool. Note that updating the base tool configuration of a registration associated with a Dynamic Registration is not allowed. |
| `overlay` | string | form |  | [Lti::Overlay] The overlay configuration for the tool. Overrides values in the base configuration. Note that updating the overlay of a registration associated with a Dynamic Registration IS allowed. |
| `workflow_state` | string | form |  | "on"/"off"/"allow" set the account binding state directly (binding vocabulary) and will be deprecated soon. "active"/"inactive" set the registration state directly (registration vocabulary). All five values update both the binding and the registration to equivalent states. "allow" is only valid for Site Admin registrations. Allowed: `on`, `off`, `allow`, `active`, `inactive` |
| `comment` | string | form |  | A comment explaining why this change was made. Cannot exceed 2000 characters. |
| `lock_deploying` | boolean | form |  | When true, no new deployments of this registration can be created. |

**Returns:** `Lti::Registration`

## PUT /v1/accounts/{account_id}/lti_registrations/{id}/reset

**Reset an LTI Registration to Defaults**  —  `reset_lti_registration_to_defaults`

Reset the specified LTI registration to its default settings in this context. This removes all customizations
that were present in the overlay associated with this context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::Registration`

## DELETE /v1/accounts/{account_id}/lti_registrations/{id}

**Delete an LTI Registration**  —  `delete_lti_registration`

Remove the specified LTI registration

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::Registration`

## POST /v1/accounts/{account_id}/lti_registrations/{id}/bind

**Bind an LTI Registration to a Root Account**  —  `bind_lti_registration_to_root_account`

Enable or disable the specified LTI registration for the specified root account.
To enable an inherited registration (eg from Site Admin), pass the registration's global ID.

Only allowed for root accounts.

<b>Specifics for centrally-managed/federated consortia:</b>
Child root accounts may not bind inherited registrations.
For parent root account, binding also applies to all child root accounts.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `workflow_state` | string | form | yes | The desired state for this registration/account binding. Allowed: `on`, `off` |

**Returns:** `Lti::RegistrationAccountBinding`

## DELETE /v1/accounts/{account_id}/lti_registrations/{id}/bind

**Remove an Inherited LTI Registration**  —  `remove_inherited_lti_registration`

Deletes the account binding for this registration, effectively removing it from the account.

Only available when the lti_deactivate_registrations feature flag is enabled.
Only valid for inherited (Site Admin) registrations — use destroy for registrations owned by this account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::RegistrationAccountBinding`

## POST /v1/accounts/{account_id}/lti_registrations/{id}/install_from_template

**Install an LTI Registration from a Template**  —  `install_lti_registration_from_template`

This endpoint installs a local copy of a "template" LTI registration from Site Admin into the specified account.
The local copy can then be customized for the account without affecting the template registration.

Only allowed for root accounts and for registrations from Site Admin marked as templates.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::Registration`

## GET /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{deployment_id}/context_search

**Search for Accounts and Courses**  —  `search_for_accounts_and_courses`

This is a utility endpoint used by the Canvas Apps UI and may not serve general use cases.

Search for accounts and courses that match the search term on name, SIS id, or course code.
Returns all matching accounts and courses, including those nested in sub-accounts.
Returns bare-bones data about each account and course, and only up to 20 of each.
Used to populate the search dropdowns when managing LTI registration availability.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `deployment_id` | string | path | yes | ID |
| `only_children_of` | string | query |  | Account ID. If provided, only searches within this account and only returns direct children of this account. |
| `search_term` | string | query |  | String to search for in account names, SIS ids, or course codes. |

**Returns:** `ContextSearchResponse`

## GET /v1/accounts/{account_id}/lti_registrations/{id}/overlay_history

**Get LTI Registration Overlay History**  —  `get_lti_registration_overlay_history`

Returns the overlay history items for the specified LTI registration.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `limit` | integer (int64) | query |  | The maximum number of history items to return. Defaults to 10. Maximum allowed is 100. |

**Returns:** `array[Lti::OverlayVersion]`

## GET /v1/accounts/{account_id}/lti_registrations/{id}/history

**Get LTI Registration History**  —  `get_lti_registration_history`

Returns the history entries for the specified LTI registration.
This endpoint provides comprehensive change tracking for all fields associated
with the registration, including registration fields, developer key changes,
internal configuration changes, and overlay changes. Supports pagination using the `page` and `per_page` parameters.
The default page size is 10.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array[Lti::RegistrationHistoryEntry]`

## GET /v1/accounts/{account_id}/lti_registrations/{id}/update_requests/{update_request_id}

**Get LTI Registration Update Request**  —  `get_lti_registration_update_request`

Retrieves details about a specific registration update request.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | integer (int64) | path | yes | The id of the registration. |
| `update_request_id` | integer (int64) | path | yes | The id of the registration update request to retrieve. |

**Returns:** `Lti::RegistrationUpdateRequest`

## GET /v1/accounts/{account_id}/lti_registrations/{id}/latest_update_request

**Get Latest LTI Registration Update Request**  —  `get_latest_lti_registration_update_request`

Retrieves the most recent update request for a registration, regardless of its status.
Returns 404 if there are no update requests for this registration.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | integer (int64) | path | yes | The id of the registration. |

**Returns:** `Lti::RegistrationUpdateRequest`

## PUT /v1/accounts/{account_id}/lti_registrations/{id}/update_requests/{update_request_id}/apply

**Apply LTI Registration Update Requst**  —  `apply_lti_registration_update_requst`

Applies a registration update request to an existing registration,
replacing the existing configuration and overlay with the new values.
If the request is rejected, marks it as rejected without applying changes.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | integer (int64) | path | yes | The id of the registration to update. |
| `update_request_id` | integer (int64) | path | yes | The id of the registration update request to apply. |
| `accepted` | boolean | form | yes | Whether to accept (true) or reject (false) the registration update request. |
| `overlay` | LtiConfigurationOverlay | form |  | Optional overlay data to apply on top of the new configuration. |
| `comment` | string | form |  | Optional comment explaining the reason for applying this update. |

**Returns:** `Lti::Registration`


---

# Models


## Lti::Registration

A registration of an LTI tool in Canvas

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the Canvas ID of the Lti::Registration object e.g. `2` |
| `name` | string |  | Tool-provided registration name e.g. `My LTI Tool` |
| `admin_nickname` | string |  | Admin-configured friendly display name e.g. `My LTI Tool (Campus A)` |
| `icon_url` | string |  | Tool-provided URL to the tool's icon e.g. `https://mytool.com/icon.png` |
| `vendor` | string |  | Tool-provided name of the tool vendor e.g. `My Tool LLC` |
| `account_id` | integer |  | The Canvas id of the account that owns this registration e.g. `1` |
| `internal_service` | boolean |  | Flag indicating if registration is internally-owned e.g. `False` |
| `lock_deploying` | boolean |  | Flag indicating if registration is locked for deployment e.g. `False` |
| `inherited` | boolean |  | Flag indicating if registration is owned by this account, or inherited from Site Admin e.g. `False` |
| `template_registration_id` | integer |  | The Canvas ID of the template registration, if this registration is inherited from a template e.g. `1` |
| `lti_version` | string |  | LTI version of the registration, either 1.1 or 1.3 e.g. `1.3` |
| `dynamic_registration` | boolean |  | Flag indicating if registration was created using LTI Dynamic Registration. Only present if lti_version is 1.3 e.g. `False` |
| `workflow_state` | string |  | The state of the registration e.g. `active` Allowed: `active`, `deleted` |
| `created_at` | string |  | Timestamp of the registration's creation e.g. `2024-01-01T00:00:00Z` |
| `updated_at` | string |  | Timestamp of the registration's last update e.g. `2024-01-01T00:00:00Z` |
| `created_by` | User |  | The user that created this registration. Not always present. If a string, this registration was created by Instructure. e.g. `{'type': 'User'}` |
| `updated_by` | User |  | The user that last updated this registration. Not always present. If a string, this registration was last updated by Instructure. e.g. `{'type': 'User'}` |
| `root_account_id` | integer |  | The Canvas id of the root account e.g. `1` |
| `account_binding` | Lti::RegistrationAccountBinding |  | The binding for this registration and this account e.g. `{'type': 'Lti::RegistrationAccountBinding'}` |
| `configuration` | Lti::ToolConfiguration |  | The Canvas-style tool configuration for this registration e.g. `{'type': 'Lti::ToolConfiguration'}` |


## Lti::RegistrationAccountBinding

A binding between an LTI registration and an account, defining the registration's availability in that account

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the Canvas ID of the Lti::RegistrationAccountBinding object e.g. `10` |
| `account_id` | integer |  | The Canvas id of the account e.g. `1` |
| `root_account_id` | integer |  | The Canvas id of the root account e.g. `1` |
| `registration_id` | integer |  | The Canvas id of the Lti::Registration e.g. `2` |
| `workflow_state` | string |  | The state of the binding (on, off, allow, deleted) e.g. `on` Allowed: `on`, `off`, `allow`, `deleted` |
| `created_at` | string |  | Timestamp of the binding's creation e.g. `2024-01-01T00:00:00Z` |
| `updated_at` | string |  | Timestamp of the binding's last update e.g. `2024-01-01T00:00:00Z` |
| `created_by` | User |  | The user that created this binding e.g. `{'type': 'User'}` |
| `updated_by` | User |  | The user that last updated this binding e.g. `{'type': 'User'}` |


## Lti::LegacyConfiguration

A legacy configuration format for LTI 1.3 tools.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `title` | string |  | The display name of the tool e.g. `My Tool` |
| `description` | string |  | The description of the tool e.g. `My Tool is built by me, for me.` |
| `custom_fields` | object |  | A key-value listing of all custom fields the tool has requested e.g. `{'context_title': '$Context.title', 'special_tool_thing': 'foo1234'}` |
| `target_link_uri` | string |  | The default launch URL for the tool. Overridable by placements. e.g. `https://mytool.com/launch` |
| `oidc_initiation_url` | string |  | 1.3 specific. URL used for initial login request e.g. `https://mytool.com/1_3/login` |
| `oidc_initiation_urls` | object |  | 1.3 specific. Region-specific login URLs for data protection compliance e.g. `{'eu-west-1': 'https://dub.mytool.com/1_3/login'}` |
| `public_jwk` | object |  | 1.3 specific. The tool's public JWK in JSON format. Discouraged in favor of a url hosting a JWK set. e.g. `{'e': 'AQAB', 'etc': 'etc'}` |
| `public_jwk_url` | string |  | 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas may cache JWKs up to 5 minutes. e.g. `https://mytool.com/1_3/jwks` |
| `scopes` | array[string] |  | 1.3 specific. List of LTI scopes requested by the tool e.g. `['https://purl.imsglobal.org/spec/lti-ags/scope/lineitem']` |
| `extensions` | array[object] |  | Array of extensions for the tool |


## Lti::ToolConfiguration

A Registration's Canvas-specific tool configuration.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `title` | string |  | The display name of the tool e.g. `My Tool` |
| `description` | string |  | The description of the tool e.g. `My Tool is built by me, for me.` |
| `custom_fields` | object |  | A key-value listing of all custom fields the tool has requested e.g. `{'context_title': '$Context.title', 'special_tool_thing': 'foo1234'}` |
| `target_link_uri` | string |  | The default launch URL for the tool. Overridable by placements. e.g. `https://mytool.com/launch` |
| `domain` | string |  | The tool's main domain. Highly recommended for deep linking, used to match links to the tool. e.g. `mytool.com` |
| `tool_id` | string |  | Tool-provided identifier, can be anything e.g. `MyTool` |
| `privacy_level` | string |  | Canvas-defined privacy level for the tool e.g. `public` Allowed: `public`, `anonymous`, `name_only`, `email_only` |
| `oidc_initiation_url` | string |  | 1.3 specific. URL used for initial login request e.g. `https://mytool.com/1_3/login` |
| `oidc_initiation_urls` | object |  | 1.3 specific. Region-specific login URLs for data protection compliance e.g. `{'eu-west-1': 'https://dub.mytool.com/1_3/login'}` |
| `public_jwk` | object |  | 1.3 specific. The tool's public JWK in JSON format. Discouraged in favor of a url hosting a JWK set. e.g. `{'e': 'AQAB', 'etc': 'etc'}` |
| `public_jwk_url` | string |  | 1.3 specific. The tool-hosted URL containing its public JWK keyset. Canvas may cache JWKs up to 5 minutes. e.g. `https://mytool.com/1_3/jwks` |
| `scopes` | array[string] |  | 1.3 specific. List of LTI scopes requested by the tool e.g. `['https://purl.imsglobal.org/spec/lti-ags/scope/lineitem']` |
| `redirect_uris` | array[string] |  | 1.3 specific. List of possible launch URLs for after the Canvas authorize redirect step e.g. `['https://mytool.com/launch', 'https://mytool.com/1_3/launch']` |
| `launch_settings` | Lti::LaunchSettings |  | Default launch settings for all placements e.g. `{'message_type': 'LtiResourceLinkRequest'}` |
| `placements` | array[Lti::Placement] |  | List of placements configured by the tool e.g. `[{'type': 'Lti::Placement'}]` |


## Lti::LaunchSettings

Default launch settings for all placements

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `message_type` | string |  | Default message type for all placements e.g. `LtiResourceLinkRequest` Allowed: `LtiResourceLinkRequest`, `LtiDeepLinkingRequest` |
| `text` | string |  | The text of the link to the tool (if applicable). e.g. `Hello World` |
| `labels` | object |  | Canvas-specific i18n for placement text. See the Navigation Placement docs. e.g. `{'en': 'Hello World', 'es': 'Hola Mundo'}` |
| `custom_fields` | object |  | Placement-specific custom fields to send in the launch. Merged with tool-level custom fields. e.g. `{'special_placement_thing': 'foo1234'}` |
| `selection_height` | number |  | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. e.g. `800` |
| `selection_width` | number |  | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. e.g. `1000` |
| `launch_height` | number |  | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. e.g. `800` |
| `launch_width` | number |  | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. e.g. `1000` |
| `icon_url` | string |  | Default icon URL. Not valid for all placements. Overrides tool-level icon_url. e.g. `https://mytool.com/icon.png` |
| `canvas_icon_class` | string |  | The HTML class name of an InstUI Icon. Used instead of an icon_url in select placements. e.g. `icon-lti` |
| `required_permissions` | string |  | Comma-separated list of Canvas permission short names required for a user to launch from this placement. e.g. `manage_course_content_edit,manage_course_content_read` |
| `windowTarget` | string |  | When set to '_blank', opens placement in a new tab. e.g. `_blank` |
| `display_type` | string |  | The Canvas layout to use when launching the tool. See the Navigation Placement docs. e.g. `full_width_in_context` Allowed: `default`, `full_width`, `full_width_in_context`, `full_width_with_nav`, `in_nav_context`, `borderless` |
| `url` | string |  | The 1.1 launch URL for this placement. Overrides tool-level url. e.g. `https://mytool.com/launch?placement=course_navigation` |
| `target_link_uri` | string |  | The 1.3 launch URL for this placement. Overrides tool-level target_link_uri. e.g. `https://mytool.com/launch?placement=course_navigation` |
| `visibility` | string |  | Specifies types of users that can see this placement. Only valid for some placements like course_navigation. e.g. `admins` |
| `prefer_sis_email` | boolean |  | 1.1 specific. If true, the tool will send the SIS email in the lis_person_contact_email_primary launch property e.g. `False` |
| `oauth_compliant` | boolean |  | 1.1 specific. If true, query parameters from the launch URL will not be copied to the POST body. e.g. `True` |
| `icon_svg_path_64` | string |  | An SVG to use instead of an icon_url. Only valid for global_navigation. e.g. `M100,37L70.1,10.5v176H37...` |
| `default` | string |  | Default display state for course_navigation. If 'enabled', will show in course sidebar. If 'disabled', will be hidden. e.g. `disabled` |
| `accept_media_types` | string |  | Comma-separated list of media types that the tool can accept. Only valid for file_item. e.g. `image/*,video/*` |
| `use_tray` | boolean |  | If true, the tool will be launched in the tray. Only used by the editor_button placement. e.g. `True` |


## Lti::Placement

The tool's configuration for a specific placement

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `placement` | string |  | The name of the placement. e.g. `course_navigation` Allowed: `account_navigation`, `analytics_hub`, `assignment_edit`, `assignment_group_menu`, `assignment_index_menu`, `assignment_menu`, `assignment_selection`, `assignment_view`, `collaboration`, `conference_selection`, `course_assignments_menu`, `course_home_sub_navigation`, `course_navigation`, `course_settings_sub_navigation`, `discussion_topic_index_menu`, `discussion_topic_menu`, `file_index_menu`, `file_menu`, `global_navigation`, `homework_submission`, `link_selection`, `migration_selection`, `module_group_menu`, `module_index_menu`, `module_index_menu_modal`, `module_menu_modal`, `module_menu`, `post_grades`, `quiz_index_menu`, `quiz_menu`, `resource_selection`, `similarity_detection`, `student_context_card`, `submission_type_selection`, `tool_configuration`, `top_navigation`, `user_navigation`, `wiki_index_menu`, `wiki_page_menu`, `editor_button` |
| `enabled` | boolean |  | If true, the tool will show in this placement. If false, it will not. e.g. `True` |
| `message_type` | string |  | Default message type for all placements e.g. `LtiResourceLinkRequest` Allowed: `LtiResourceLinkRequest`, `LtiDeepLinkingRequest` |
| `text` | string |  | The text of the link to the tool (if applicable). e.g. `Hello World` |
| `labels` | object |  | Canvas-specific i18n for placement text. See the Navigation Placement docs. e.g. `{'en': 'Hello World', 'es': 'Hola Mundo'}` |
| `custom_fields` | object |  | Placement-specific custom fields to send in the launch. Merged with tool-level custom fields. e.g. `{'special_placement_thing': 'foo1234'}` |
| `selection_height` | number |  | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. e.g. `800` |
| `selection_width` | number |  | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. e.g. `1000` |
| `launch_height` | number |  | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. e.g. `800` |
| `launch_width` | number |  | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. e.g. `1000` |
| `icon_url` | string |  | Default icon URL. Not valid for all placements. Overrides tool-level icon_url. e.g. `https://mytool.com/icon.png` |
| `canvas_icon_class` | string |  | The HTML class name of an InstUI Icon. Used instead of an icon_url in select placements. e.g. `icon-lti` |
| `required_permissions` | string |  | Comma-separated list of Canvas permission short names required for a user to launch from this placement. e.g. `manage_course_content_edit,manage_course_content_read` |
| `windowTarget` | string |  | When set to '_blank', opens placement in a new tab. e.g. `_blank` |
| `display_type` | string |  | The Canvas layout to use when launching the tool. See the Navigation Placement docs. e.g. `full_width_in_context` Allowed: `default`, `full_width`, `full_width_in_context`, `full_width_with_nav`, `in_nav_context`, `borderless` |
| `url` | string |  | The 1.1 launch URL for this placement. Overrides tool-level url. e.g. `https://mytool.com/launch?placement=course_navigation` |
| `target_link_uri` | string |  | The 1.3 launch URL for this placement. Overrides tool-level target_link_uri. e.g. `https://mytool.com/launch?placement=course_navigation` |
| `visibility` | string |  | Specifies types of users that can see this placement. Only valid for some placements like course_navigation. e.g. `admins` Allowed: `admins`, `members`, `public` |
| `prefer_sis_email` | boolean |  | 1.1 specific. If true, the tool will send the SIS email in the lis_person_contact_email_primary launch property e.g. `False` |
| `oauth_compliant` | boolean |  | 1.1 specific. If true, query parameters from the launch URL will not be copied to the POST body. e.g. `True` |
| `icon_svg_path_64` | string |  | An SVG to use instead of an icon_url. Only valid for global_navigation. e.g. `M100,37L70.1,10.5v176H37...` |
| `default` | string |  | Default display state for course_navigation. If 'enabled', will show in course sidebar. If 'disabled', will be hidden. e.g. `disabled` |
| `accept_media_types` | string |  | Comma-separated list of media types that the tool can accept. Only valid for file_item. e.g. `image/*,video/*` |
| `use_tray` | boolean |  | If true, the tool will be launched in the tray. Only used by the editor_button placement. e.g. `True` |


## Lti::Overlay

Changes made by a Canvas admin to a tool's configuration.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `title` | string |  | The display name of the tool e.g. `My Tool` |
| `description` | string |  | The description of the tool e.g. `My Tool is built by me, for me.` |
| `custom_fields` | object |  | A key-value listing of all custom fields the tool has requested e.g. `{'context_title': '$Context.title', 'special_tool_thing': 'foo1234'}` |
| `target_link_uri` | string |  | The default launch URL for the tool. Overridable by placements. e.g. `https://mytool.com/launch` |
| `domain` | string |  | The tool's main domain. Highly recommended for deep linking, used to match links to the tool. e.g. `mytool.com` |
| `privacy_level` | string |  | Canvas-defined privacy level for the tool e.g. `public` Allowed: `public`, `anonymous`, `name_only`, `email_only` |
| `oidc_initiation_url` | string |  | 1.3 specific. URL used for initial login request e.g. `https://mytool.com/1_3/login` |
| `disabled_scopes` | array[string] |  | 1.3 specific. List of LTI scopes that the tool has requested but an admin has disabled e.g. `['https://purl.imsglobal.org/spec/lti-ags/scope/lineitem']` |
| `disabled_placements` | array[string] |  | List of placements that the tool has requested but an admin has disabled e.g. `['course_navigation']` |
| `placements` | object |  | Placement-specific settings changed by an admin e.g. `{'course_navigation': {'$ref': 'Lti::Placement'}}` |


## Lti::OverlayVersion

A single version of a tool's configuration overlay

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `root_account_id` | integer |  | The Canvas id of the root account e.g. `1` |
| `created_at` | string |  | Timestamp of the version's creation e.g. `2024-01-01T00:00:00Z` |
| `updated_at` | string |  | Timestamp of the version's last update e.g. `2024-01-01T00:00:00Z` |
| `caused_by_reset` | boolean |  | Whether or not this change was caused by a reset of the tool's configuration e.g. `False` |
| `created_by` | User |  | The user that created this version. If a string, this registration was created by Instructure. e.g. `{'type': 'User'}` |
| `diff` | array[array] |  | A list of changes made in this version compared to the previous version e.g. `[['+', 'disabled_placements[0]', 'top_navigation']]` |
| `lti_overlay_id` | integer |  | The id of the overlay this version is for e.g. `1` |
| `account_id` | integer |  | The id of the account this version is for e.g. `1` |


## Lti::PlacementOverlay

Changes made by a Canvas admin to a tool's configuration for a specific placement.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `text` | string |  | The text of the link to the tool (if applicable). e.g. `Hello World` |
| `target_link_uri` | string |  | The default launch URL for the tool. Overridable by placements. e.g. `https://mytool.com/launch` |
| `message_type` | string |  | Default message type for all placements e.g. `LtiResourceLinkRequest` Allowed: `LtiResourceLinkRequest`, `LtiDeepLinkingRequest` |
| `launch_height` | number |  | Default iframe height. Not valid for all placements. Overrides tool-level launch_height. e.g. `800` |
| `launch_width` | number |  | Default iframe width. Not valid for all placements. Overrides tool-level launch_width. e.g. `1000` |
| `icon_url` | string |  | Default icon URL. Not valid for all placements. Overrides tool-level icon_url. e.g. `https://mytool.com/icon.png` |
| `default` | string |  | Default display state for course_navigation. If 'enabled', will show in course sidebar. If 'disabled', will be hidden. e.g. `disabled` |


## ListLtiRegistrationsResponse

The response for the List LTI Registrations API endpoint

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `total` | integer |  | The total number of LTI registrations across all pages e.g. `1` |
| `data` | array[Lti::Registration] |  | The paginated list of LTI::Registrations e.g. `[{'$ref': 'Lti::Registration'}]` |


## ContextSearchResponse

The response for the Search Accounts and Courses API endpoint

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `accounts` | array[SearchableAccount] |  | Accounts that match the search query. Limited to 100. e.g. `[{'$ref': 'Account'}]` |
| `courses` | array[SearchableCourse] |  | Courses that match the search query. Limited to 100. e.g. `[{'$ref': 'Course'}]` |


## SearchableAccount

A minimal representation of an Account for Canvas Apps search purposes

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | The Canvas DB ID e.g. `1` |
| `name` | string |  | The account name e.g. `An Account` |
| `sis_id` | string |  | The SIS ID of the account, if any. Only present if user can read or manage SIS. e.g. `sis-account-1` |
| `display_path` | array[string] |  | Names of the accounts in this account's hierarchy, excluding the root and this account. e.g. `['Sub Account']` |


## SearchableCourse

A minimal representation of a Course for Canvas Apps search purposes

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | The Canvas DB ID e.g. `1` |
| `name` | string |  | The course name e.g. `A Course` |
| `sis_id` | string |  | The SIS ID of the course, if any. Only present if user can read or manage SIS. e.g. `sis-course-1` |
| `display_path` | array[string] |  | Names of the accounts in this course's account hierarchy, excluding the root. e.g. `['Sub Account']` |
| `course_code` | string |  | The course code e.g. `COURSE-101` |
