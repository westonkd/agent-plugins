# Group Categories

> Canvas LMS REST API — `/group_categories` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/group_categories

**List group categories for a context**  —  `list_group_categories_for_context_accounts`

Returns a paginated list of group categories in a context. The list returned
depends on the permissions of the current user and the specified collaboration state.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `collaboration_state` | string | query |  | Filter group categories by their collaboration state: - "all": Return both collaborative and non-collaborative group categories - "collaborative": Return only collaborative group categories (default) - "non_collaborative": Return only non-collaborative group categories |

**Returns:** `array[GroupCategory]`

## GET /v1/courses/{course_id}/group_categories

**List group categories for a context**  —  `list_group_categories_for_context_courses`

Returns a paginated list of group categories in a context. The list returned
depends on the permissions of the current user and the specified collaboration state.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `collaboration_state` | string | query |  | Filter group categories by their collaboration state: - "all": Return both collaborative and non-collaborative group categories - "collaborative": Return only collaborative group categories (default) - "non_collaborative": Return only non-collaborative group categories |

**Returns:** `array[GroupCategory]`

## GET /v1/group_categories/{group_category_id}

**Get a single group category**  —  `get_single_group_category`

Returns the data for a single group category, or a 401 if the caller doesn't have
the rights to see it.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |

**Returns:** `GroupCategory`

## POST /v1/accounts/{account_id}/group_categories

**Create a Group Category**  —  `create_group_category_accounts`

Create a new group category

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `name` | string | form | yes | Name of the group category |
| `non_collaborative` | boolean | form |  | Can only be set by users with the Differentiation Tag - Add permission  If set to true, groups in this category will be only be visible to users with the Differentiation Tag - Manage permission. |
| `self_signup` | string | form |  | Allow students to sign up for a group themselves (Course Only). valid values are: "enabled":: allows students to self sign up for any group in course "restricted":: allows students to self sign up only for groups in the                same section null disallows self sign up Allowed: `enabled`, `restricted` |
| `auto_leader` | string | form |  | Assigns group leaders automatically when generating and allocating students to groups Valid values are: "first":: the first student to be allocated to a group is the leader "random":: a random student from all members is chosen as the leader Allowed: `first`, `random` |
| `group_limit` | integer (int64) | form |  | Limit the maximum number of users in each group (Course Only). Requires self signup. |
| `sis_group_category_id` | string | form |  | The unique SIS identifier. |
| `create_group_count` | integer (int64) | form |  | Create this number of groups (Course Only). |
| `split_group_count` | string | form |  | (Deprecated) Create this number of groups, and evenly distribute students among them. not allowed with "enable_self_signup". because the group assignment happens synchronously, it's recommended that you instead use the assign_unassigned_members endpoint. (Course Only) |

**Returns:** `GroupCategory`

## POST /v1/courses/{course_id}/group_categories

**Create a Group Category**  —  `create_group_category_courses`

Create a new group category

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `name` | string | form | yes | Name of the group category |
| `non_collaborative` | boolean | form |  | Can only be set by users with the Differentiation Tag - Add permission  If set to true, groups in this category will be only be visible to users with the Differentiation Tag - Manage permission. |
| `self_signup` | string | form |  | Allow students to sign up for a group themselves (Course Only). valid values are: "enabled":: allows students to self sign up for any group in course "restricted":: allows students to self sign up only for groups in the                same section null disallows self sign up Allowed: `enabled`, `restricted` |
| `auto_leader` | string | form |  | Assigns group leaders automatically when generating and allocating students to groups Valid values are: "first":: the first student to be allocated to a group is the leader "random":: a random student from all members is chosen as the leader Allowed: `first`, `random` |
| `group_limit` | integer (int64) | form |  | Limit the maximum number of users in each group (Course Only). Requires self signup. |
| `sis_group_category_id` | string | form |  | The unique SIS identifier. |
| `create_group_count` | integer (int64) | form |  | Create this number of groups (Course Only). |
| `split_group_count` | string | form |  | (Deprecated) Create this number of groups, and evenly distribute students among them. not allowed with "enable_self_signup". because the group assignment happens synchronously, it's recommended that you instead use the assign_unassigned_members endpoint. (Course Only) |

**Returns:** `GroupCategory`

## POST /v1/courses/{course_id}/group_categories/bulk_manage_differentiation_tag

**Bulk manage differentiation tags**  —  `bulk_manage_differentiation_tags`

This API is only meant for Groups and GroupCategories where non_collaborative is true.

Perform bulk operations on groups within a group category, or create a new group category
along with the groups in one transaction. If creation of the GroupCategory or any Group fails, the entire operation will be rolled back.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `operations` | Hash | form | yes | A hash containing arrays of create/update/delete operations: {   "create": [     { "name": "New Group A" },     { "name": "New Group B" }   ],   "update": [     { "id": 123, "name": "Updated Group Name A" },     { "id": 456, "name": "Updated Group Name B" }   ],   "delete": [     { "id": 789 },     { "id": 101 }   ] } |
| `group_category` | Hash | form | yes | Attributes for the GroupCategory. May include:   - id [Optional, Integer]: The ID of an existing GroupCategory.   - name [Optional, String]: A new name for the GroupCategory. If provided with an ID, the category name will be updated. |

**Returns:** `GroupCategory and groups operation results`

## POST /v1/courses/{course_id}/group_categories/import_tags

**Import differentiation tags**  —  `import_differentiation_tags`

Create Differentiation Tags through a CSV import

For more information on the format that's expected here, please see the
"Differentiation Tag CSV" section in the API docs.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `attachment` | string | form |  | There are two ways to post differentiation tag import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.  'attachment' is required for multipart/form-data style posts. Assumed to be tag data from a file upload form field named 'attachment'.  Examples:   curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/group_categories/import_tags'  If you decide to do a raw post, you can skip the 'attachment' argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the 'extension' argument.  Examples:   curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/group_categories_tags' |

**Returns:** `Progress`

## POST /v1/group_categories/{group_category_id}/import

**Import category groups**  —  `import_category_groups`

Create Groups in a Group Category through a CSV import

For more information on the format that's expected here, please see the
"Group Category CSV" section in the API docs.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |
| `attachment` | string | form |  | There are two ways to post group category import data - either via a multipart/form-data form-field-style attachment, or via a non-multipart raw post request.  'attachment' is required for multipart/form-data style posts. Assumed to be outcome data from a file upload form field named 'attachment'.  Examples:   curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/group_categories/<category_id>/import'  If you decide to do a raw post, you can skip the 'attachment' argument, but you will then be required to provide a suitable Content-Type header. You are encouraged to also provide the 'extension' argument.  Examples:   curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \       -H "Authorization: Bearer <token>" \       'https://<canvas>/api/v1/group_categories/<category_id>/import' |

**Returns:** `Progress`

## PUT /v1/group_categories/{group_category_id}

**Update a Group Category**  —  `update_group_category`

Modifies an existing group category.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |
| `name` | string | form |  | Name of the group category |
| `self_signup` | string | form |  | Allow students to sign up for a group themselves (Course Only). Valid values are: "enabled":: allows students to self sign up for any group in course "restricted":: allows students to self sign up only for groups in the                same section null disallows self sign up Allowed: `enabled`, `restricted` |
| `auto_leader` | string | form |  | Assigns group leaders automatically when generating and allocating students to groups Valid values are: "first":: the first student to be allocated to a group is the leader "random":: a random student from all members is chosen as the leader Allowed: `first`, `random` |
| `group_limit` | integer (int64) | form |  | Limit the maximum number of users in each group (Course Only). Requires self signup. |
| `sis_group_category_id` | string | form |  | The unique SIS identifier. |
| `create_group_count` | integer (int64) | form |  | Create this number of groups (Course Only). |
| `split_group_count` | string | form |  | (Deprecated) Create this number of groups, and evenly distribute students among them. not allowed with "enable_self_signup". because the group assignment happens synchronously, it's recommended that you instead use the assign_unassigned_members endpoint. (Course Only) |

**Returns:** `GroupCategory`

## DELETE /v1/group_categories/{group_category_id}

**Delete a Group Category**  —  `delete_group_category`

Deletes a group category and all groups under it. Protected group
categories can not be deleted, i.e. "communities" and "student_organized".

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/group_categories/{group_category_id}/groups

**List groups in group category**  —  `list_groups_in_group_category`

Returns a paginated list of groups in a group category

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |

**Returns:** `array[Group]`

## GET /v1/group_categories/{group_category_id}/export

**export groups in and users in category**  —  `export_groups_in_and_users_in_category`

Returns a csv file of users in format ready to import.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/group_categories/export_tags

**export tags and users in course**  —  `export_tags_and_users_in_course`

Returns a csv file of users in format ready to import.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/group_categories/{group_category_id}/users

**List users in group category**  —  `list_users_in_group_category`

Returns a paginated list of users in the group category.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters. |
| `unassigned` | boolean | query |  | Set this value to true if you wish only to search unassigned users in the group category. |

**Returns:** `array[User]`

## POST /v1/group_categories/{group_category_id}/assign_unassigned_members

**Assign unassigned members**  —  `assign_unassigned_members`

Assign all unassigned members as evenly as possible among the existing
student groups.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |
| `sync` | boolean | form |  | The assigning is done asynchronously by default. If you would like to override this and have the assigning done synchronously, set this value to true. |

**Returns:** `GroupMembership | Progress`


---

# Models


## GroupCategory

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the group category. e.g. `17` |
| `name` | string |  | The display name of the group category. e.g. `Math Groups` |
| `role` | string |  | Certain types of group categories have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account group categories have a role of null. e.g. `communities` |
| `self_signup` | string |  | If the group category allows users to join a group themselves, thought they may only be a member of one group per group category at a time. Values include 'restricted', 'enabled', and null 'enabled' allows students to assign themselves to a group 'restricted' restricts them to only joining a group in their section null disallows students from joining groups |
| `auto_leader` | string |  | Gives instructors the ability to automatically have group leaders assigned.  Values include 'random', 'first', and null; 'random' picks a student from the group at random as the leader, 'first' sets the first student to be assigned to the group as the leader |
| `context_type` | string |  | The course or account that the category group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'Course', the course_id field would be replaced by an course_id field. e.g. `Account` |
| `account_id` | integer |  | e.g. `3` |
| `group_limit` | integer |  | If self-signup is enabled, group_limit can be set to cap the number of users in each group. If null, there is no limit. |
| `sis_group_category_id` | string |  | The SIS identifier for the group category. This field is only included if the user has permission to manage or view SIS information. |
| `sis_import_id` | integer |  | The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. |
| `progress` | Progress |  | If the group category has not yet finished a randomly student assignment request, a progress object will be attached, which will contain information related to the progress of the assignment request. Refer to the Progress API for more information |
| `non_collaborative` | boolean |  | Indicates whether this group category is non-collaborative. A value of true means these group categories rely on the manage_tags permissions and do not have collaborative features |
