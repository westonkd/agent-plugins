# Roles

> Canvas LMS REST API — `/roles` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/roles

**List roles**  —  `list_roles`

A paginated list of the roles available to an account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | The id of the account to retrieve roles for. |
| `state` | array[string] | query |  | Filter by role state. If this argument is omitted, only 'active' roles are returned. Allowed: `active`, `inactive` |
| `show_inherited` | boolean | query |  | If this argument is true, all roles inherited from parent accounts will be included. |

**Returns:** `array[Role]`

## GET /v1/accounts/{account_id}/roles/{id}

**Get a single role**  —  `get_single_role`

Retrieve information about a single role

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `account_id` | string | path | yes | The id of the account containing the role |
| `role_id` | integer (int64) | query | yes | The unique identifier for the role |
| `role` | string | query |  | The name for the role |

**Returns:** `Role`

## POST /v1/accounts/{account_id}/roles

**Create a new role**  —  `create_new_role`

Create a new course-level or account-level role.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `label` | string | form | yes | Label for the role. |
| `role` | string | form |  | Deprecated alias for label. |
| `base_role_type` | string | form |  | Specifies the role type that will be used as a base for the permissions granted to this role.  Defaults to 'AccountMembership' if absent Allowed: `AccountMembership`, `StudentEnrollment`, `TeacherEnrollment`, `TaEnrollment`, `ObserverEnrollment`, `DesignerEnrollment` |
| `permissions[<X>][explicit]` | boolean | form |  | no description |
| `permissions[<X>][enabled]` | boolean | form |  | If explicit is 1 and enabled is 1, permission <X> will be explicitly granted to this role. If explicit is 1 and enabled has any other value (typically 0), permission <X> will be explicitly denied to this role. If explicit is any other value (typically 0) or absent, or if enabled is absent, the value for permission <X> will be inherited from upstream. Ignored if permission <X> is locked upstream (in an ancestor account).  May occur multiple times with unique values for <X>. Recognized permission names for <X> can be found on the {file:file.permissions.html Permissions list page}.  Some of these permissions are applicable only for roles on the site admin account, on a root account, or for course-level roles with a particular base role type; if a specified permission is inapplicable, it will be ignored.  Additional permissions may exist based on installed plugins.  A comprehensive list of all permissions are available:  Course Permissions PDF: http://bit.ly/cnvs-course-permissions  Account Permissions PDF: http://bit.ly/cnvs-acct-permissions |
| `permissions[<X>][locked]` | boolean | form |  | If the value is 1, permission <X> will be locked downstream (new roles in subaccounts cannot override the setting). For any other value, permission <X> is left unlocked. Ignored if permission <X> is already locked upstream. May occur multiple times with unique values for <X>. |
| `permissions[<X>][applies_to_self]` | boolean | form |  | If the value is 1, permission <X> applies to the account this role is in. The default value is 1. Must be true if applies_to_descendants is false. This value is only returned if enabled is true. |
| `permissions[<X>][applies_to_descendants]` | boolean | form |  | If the value is 1, permission <X> cascades down to sub accounts of the account this role is in. The default value is 1.  Must be true if applies_to_self is false.This value is only returned if enabled is true. |

**Returns:** `Role`

## DELETE /v1/accounts/{account_id}/roles/{id}

**Deactivate a role**  —  `deactivate_role`

Deactivates a custom role.  This hides it in the user interface and prevents it
from being assigned to new users.  Existing users assigned to the role will
continue to function with the same permissions they had previously.
Built-in roles cannot be deactivated.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `role_id` | integer (int64) | query | yes | The unique identifier for the role |
| `role` | string | query |  | The name for the role |

**Returns:** `Role`

## POST /v1/accounts/{account_id}/roles/{id}/activate

**Activate a role**  —  `activate_role`

Re-activates an inactive role (allowing it to be assigned to new users)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `role_id` | integer (int64) | form | yes | The unique identifier for the role |
| `role` | Deprecated | form |  | The name for the role |

**Returns:** `Role`

## PUT /v1/accounts/{account_id}/roles/{id}

**Update a role**  —  `update_role`

Update permissions for an existing role.

Recognized roles are:
* TeacherEnrollment
* StudentEnrollment
* TaEnrollment
* ObserverEnrollment
* DesignerEnrollment
* AccountAdmin
* Any previously created custom role

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `label` | string | form |  | The label for the role. Can only change the label of a custom role that belongs directly to the account. |
| `permissions[<X>][explicit]` | boolean | form |  | no description |
| `permissions[<X>][enabled]` | boolean | form |  | These arguments are described in the documentation for the {api:RoleOverridesController#add_role add_role method}. The list of available permissions can be found on the {file:file.permissions.html Permissions list page}. |
| `permissions[<X>][applies_to_self]` | boolean | form |  | If the value is 1, permission <X> applies to the account this role is in. The default value is 1. Must be true if applies_to_descendants is false. This value is only returned if enabled is true. |
| `permissions[<X>][applies_to_descendants]` | boolean | form |  | If the value is 1, permission <X> cascades down to sub accounts of the account this role is in. The default value is 1.  Must be true if applies_to_self is false.This value is only returned if enabled is true. |

**Returns:** `Role`

## GET /v1/accounts/{account_id}/roles/permissions

**List assignable permissions**  —  `list_assignable_permissions`

List all permissions that can be granted to roles in the given account.

This returns largely the same information documented on the {file:file.permissions.html Permissions list page},
with a few caveats:
* Permission labels and group labels returned by this API are localized (the same text visible in the web UI).
* This API includes permissions added by plugins.
* This API excludes permissions that are disabled in or otherwise do not apply to the given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `search_term` | string | query |  | If provided, return only permissions whose key, label, group, or group_label match the search string. |

**Returns:** `array[Permission]`

## GET /v1/permissions/{context_type}/{permission}/help

**Get help text for permissions**  —  `get_help_text_for_permissions`

these actions access only static (but localized) information about permissions,
but require a logged-in user to mitigate possible abuse
Retrieve information about what Canvas permissions do and considerations for their use.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_type` | string | path | yes | ID |
| `permission` | string | path | yes | ID |

**Returns:** `PermissionHelpText`

## GET /v1/permissions/groups

**Retrieve permission groups**  —  `retrieve_permission_groups`

Retrieve information about groups of granular permissions

The return value is a dictionary of permission group keys to objects
containing +label+ and +subtitle+ keys.

**Returns:** `void`


---

# Models


## RolePermissions

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `enabled` | boolean |  | Whether the role has the permission e.g. `True` |
| `locked` | boolean |  | Whether the permission is locked by this role e.g. `False` |
| `applies_to_self` | boolean |  | Whether the permission applies to the account this role is in. Only present if enabled is true e.g. `True` |
| `applies_to_descendants` | boolean |  | Whether the permission cascades down to sub accounts of the account this role is in. Only present if enabled is true e.g. `False` |
| `readonly` | boolean |  | Whether the permission can be modified in this role (i.e. whether the permission is locked by an upstream role). e.g. `False` |
| `explicit` | boolean |  | Whether the value of enabled is specified explicitly by this role, or inherited from an upstream role. e.g. `True` |
| `prior_default` | boolean |  | The value that would have been inherited from upstream if the role had not explicitly set a value. Only present if explicit is true. e.g. `False` |


## Role

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The id of the role e.g. `1` |
| `label` | string |  | The label of the role. e.g. `New Role` |
| `role` | string |  | The label of the role. (Deprecated alias for 'label') e.g. `New Role` |
| `base_role_type` | string |  | The role type that is being used as a base for this role. For account-level roles, this is 'AccountMembership'. For course-level roles, it is an enrollment type. e.g. `AccountMembership` |
| `is_account_role` | boolean |  | Whether this role applies to account memberships (i.e., not linked to an enrollment in a course). e.g. `True` |
| `account` | Account |  | JSON representation of the account the role is defined in. e.g. `{'id': 1019, 'name': 'CGNU', 'parent_account_id': 73, 'root_account_id': 1, 'sis_account_id': 'cgnu'}` |
| `workflow_state` | string |  | The state of the role: 'active', 'inactive', or 'built_in' e.g. `active` |
| `created_at` | datetime |  | The date and time the role was created. e.g. `2020-12-01T16:20:00-06:00` |
| `last_updated_at` | datetime |  | The date and time the role was last updated. e.g. `2023-10-31T23:59:00-06:00` |
| `permissions` | object |  | A dictionary of permissions keyed by name (see 'List assignable permissions' API). e.g. `{'read_course_content': {'enabled': True, 'locked': False, 'readonly': False, 'explicit': True, 'prior_default': False}, 'read_course_list': {'enabled': True, 'locked': True, 'readonly': True, 'explicit': False}, 'read_question_banks': {'enabled': False, 'locked': True, 'readonly': False, 'explicit': True, 'prior_default': False}, 'read_reports': {'enabled': True, 'locked': False, 'readonly': False, 'explicit': False}}` |


## Permission

A permission that can be granted to a role

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `key` | string |  | The API identifier for the permission e.g. `manage_lti_add` |
| `label` | string |  | The human-readable label for the permission e.g. `LTI - add` |
| `group` | string |  | The group this permission belongs to, if it is part of a granular permission group e.g. `manage_lti` |
| `group_label` | string |  | The human-readable label for the group this permission belongs to e.g. `Manage LTI` |
| `available_to` | array[string] |  | The base role types this permission can be enabled for e.g. `['AccountAdmin', 'AccountMembership', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment']` |
| `true_for` | array[string] |  | The base role types this permission is enabled for by default e.g. `['AccountAdmin', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment']` |


## PermissionHelpText

Information about a permission, including its purpose and considerations for use.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `details` | array[object] |  | Detailed explanations about what the permission does. e.g. `[{'title': 'Add External Tools', 'description': 'Allows users to add external tools (LTI) to courses.'}]` |
| `considerations` | array[object] |  | A list of considerations or warnings about using the permission. e.g. `[{'title': 'Security Risk', 'description': 'Granting this permission may expose your system to security vulnerabilities.'}]` |
