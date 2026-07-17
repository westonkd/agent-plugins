# Groups

> Canvas LMS REST API — `/groups` resource. Base path `/api`.

## GET /v1/users/self/groups

**List your groups**  —  `list_your_groups`

Returns a paginated list of active groups for the current user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_type` | string | query |  | Only include groups that are in this type of context. Allowed: `Account`, `Course` |
| `include` | array[string] | query |  | - "tabs": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. Allowed: `tabs` |

**Returns:** `array[Group]`

## GET /v1/accounts/{account_id}/groups

**List the groups available in a context.**  —  `list_groups_available_in_context_accounts`

Returns the paginated list of active groups in the given context that are visible to user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `only_own_groups` | boolean | query |  | Will only include groups that the user belongs to if this is set |
| `include` | array[string] | query |  | - "tabs": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. Allowed: `tabs` |
| `collaboration_state` | string | query |  | Filter groups by their collaboration state: - "all": Return both collaborative and non-collaborative groups - "collaborative": Return only collaborative groups (default) - "non_collaborative": Return only non-collaborative groups |

**Returns:** `array[Group]`

## GET /v1/courses/{course_id}/groups

**List the groups available in a context.**  —  `list_groups_available_in_context_courses`

Returns the paginated list of active groups in the given context that are visible to user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `only_own_groups` | boolean | query |  | Will only include groups that the user belongs to if this is set |
| `include` | array[string] | query |  | - "tabs": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. Allowed: `tabs` |
| `collaboration_state` | string | query |  | Filter groups by their collaboration state: - "all": Return both collaborative and non-collaborative groups - "collaborative": Return only collaborative groups (default) - "non_collaborative": Return only non-collaborative groups |

**Returns:** `array[Group]`

## GET /v1/courses/{course_id}/bulk_user_tags

**Bulk fetch user tags for multiple users in a course**  —  `bulk_fetch_user_tags_for_multiple_users_in_course`

Returns a mapping of user IDs to arrays of non-collaborative group (tag) IDs for each user in the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The ID of the course context (from the route). |
| `user_ids` | array[integer] | query |  | An array of user IDs to fetch tags for. |

**Returns:** `array[Hash A mapping of user IDs to arrays of tag (group) IDs. Example: { "35": 5, "79": 3, 4, 5 }]`

## GET /v1/groups/{group_id}

**Get a single group**  —  `get_single_group`

Returns the data for a single group, or a 401 if the caller doesn't have
the rights to see it.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "permissions": Include permissions the current user has   for the group. - "tabs": Include the list of tabs configured for each group.  See the   {api:TabsController#index List available tabs API} for more information. Allowed: `permissions`, `tabs` |

**Returns:** `Group`

## POST /v1/groups

**Create a group**  —  `create_group_groups`

Creates a new group. Groups created using the "/api/v1/groups/"
endpoint will be community groups.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `name` | string | form |  | The name of the group |
| `description` | string | form |  | A description of the group |
| `is_public` | boolean | form |  | whether the group is public (applies only to community groups) |
| `join_level` | string | form |  | no description Allowed: `parent_context_auto_join`, `parent_context_request`, `invitation_only` |
| `storage_quota_mb` | integer (int64) | form |  | The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission. |
| `sis_group_id` | string | form |  | The sis ID of the group. Must have manage_sis permission to set. |

**Returns:** `Group`

## POST /v1/group_categories/{group_category_id}/groups

**Create a group**  —  `create_group_group_categories`

Creates a new group. Groups created using the "/api/v1/groups/"
endpoint will be community groups.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_category_id` | string | path | yes | ID |
| `name` | string | form |  | The name of the group |
| `description` | string | form |  | A description of the group |
| `is_public` | boolean | form |  | whether the group is public (applies only to community groups) |
| `join_level` | string | form |  | no description Allowed: `parent_context_auto_join`, `parent_context_request`, `invitation_only` |
| `storage_quota_mb` | integer (int64) | form |  | The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission. |
| `sis_group_id` | string | form |  | The sis ID of the group. Must have manage_sis permission to set. |

**Returns:** `Group`

## PUT /v1/groups/{group_id}

**Edit a group**  —  `edit_group`

Modifies an existing group.  Note that to set an avatar image for the
group, you must first upload the image file to the group, and the use the
id in the response as the argument to this function.  See the
{file:file.file_uploads.html File Upload Documentation} for details on the file
upload workflow.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `name` | string | form |  | The name of the group |
| `description` | string | form |  | A description of the group |
| `is_public` | boolean | form |  | Whether the group is public (applies only to community groups). Currently you cannot set a group back to private once it has been made public. |
| `join_level` | string | form |  | no description Allowed: `parent_context_auto_join`, `parent_context_request`, `invitation_only` |
| `avatar_id` | integer (int64) | form |  | The id of the attachment previously uploaded to the group that you would like to use as the avatar image for this group. |
| `storage_quota_mb` | integer (int64) | form |  | The allowed file storage for the group, in megabytes. This parameter is ignored if the caller does not have the manage_storage_quotas permission. |
| `members` | array[string] | form |  | An array of user ids for users you would like in the group. Users not in the group will be sent invitations. Existing group members who aren't in the list will be removed from the group. |
| `sis_group_id` | string | form |  | The sis ID of the group. Must have manage_sis permission to set. |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `Group`

## DELETE /v1/groups/{group_id}

**Delete a group**  —  `delete_group`

Deletes a group and removes all members.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `Group`

## POST /v1/groups/{group_id}/invite

**Invite others to a group**  —  `invite_others_to_group`

Sends an invitation to all supplied email addresses which will allow the
receivers to join the group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `invitees` | array[string] | form | yes | An array of email addresses to be sent invitations. |

**Returns:** `void`

## GET /v1/groups/{group_id}/users

**List group's users**  —  `list_group_s_users`

Returns a paginated list of users in the group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters. |
| `include` | array[string] | query |  | "avatar_url": Include users' avatar_urls. Allowed: `avatar_url` |
| `exclude_inactive` | boolean | query |  | Whether to filter out inactive users from the results. Defaults to false unless explicitly provided. |

**Returns:** `array[User]`

## POST /v1/groups/{group_id}/files

**Upload a file**  —  `upload_file`

Upload a file to the group.

This API endpoint is the first step in uploading a file to a group.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Only those with the "Manage Files" permission on a group can upload files
to the group. By default, this is anybody participating in the
group, or any admin over the group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/groups/{group_id}/preview_html

**Preview processed html**  —  `preview_processed_html`

Preview html content processed for this group

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `html` | string | form |  | The html content to process |

**Returns:** `void`

## GET /v1/groups/{group_id}/activity_stream

**Group activity stream**  —  `group_activity_stream`

Returns the current user's group-specific activity stream, paginated.

For full documentation, see the API documentation for the user activity
stream, in the user api.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/groups/{group_id}/activity_stream/summary

**Group activity stream summary**  —  `group_activity_stream_summary`

Returns a summary of the current user's group-specific activity stream.

For full documentation, see the API documentation for the user activity
stream summary, in the user api.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/groups/{group_id}/permissions

**Permissions**  —  `permissions`

Returns permission information for the calling user in the given group.
See also the {api:AccountsController#permissions Account} and
{api:CoursesController#permissions Course} counterparts.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `permissions` | array[string] | query |  | List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. |

**Returns:** `void`

## GET /v1/groups/{group_id}/memberships

**List group memberships**  —  `list_group_memberships`

A paginated list of the members of a group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `filter_states` | array[string] | query |  | Only list memberships with the given workflow_states. By default it will return all memberships. Allowed: `accepted`, `invited`, `requested` |

**Returns:** `array[GroupMembership]`

## GET /v1/groups/{group_id}/memberships/{membership_id}

**Get a single group membership**  —  `get_single_group_membership_memberships`

Returns the group membership with the given membership id or user id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `membership_id` | string | path | yes | ID |

**Returns:** `GroupMembership`

## GET /v1/groups/{group_id}/users/{user_id}

**Get a single group membership**  —  `get_single_group_membership_users`

Returns the group membership with the given membership id or user id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `GroupMembership`

## POST /v1/groups/{group_id}/memberships

**Create a membership**  —  `create_membership`

Join, or request to join, a group, depending on the join_level of the
group. If the membership or join request already exists, then it is simply
returned.

For differentiation tags, you can bulk add users using one of two methods:

1. Provide an array of user IDs via the `members[]` parameter.

2. Use the course-wide option with the following parameters:
   - `all_in_group_course` [Boolean]: If set to true, the endpoint will add
     every currently enrolled student (from the course context) to the
     differentiation tag.
   - `exclude_user_ids[]` [Integer]: When using `all_in_group_course`, you can
     optionally exclude specific users by providing their IDs in this parameter.

In this context, these parameters only apply to differentiation tag memberships.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `user_id` | string | form |  | - The ID of the user for individual membership creation. |
| `members` | array[integer] | form |  | - Bulk add multiple users to a differentiation tag. |
| `all_in_group_course` | boolean | form |  | - If true, add all enrolled students from the course. |
| `exclude_user_ids` | array[integer] | form |  | - An array of user IDs to exclude when using all_in_group_course. |

**Returns:** `GroupMembership or a JSON response detailing partial failures if some memberships could not be created.`

## PUT /v1/groups/{group_id}/memberships/{membership_id}

**Update a membership**  —  `update_membership_memberships`

Accept a membership request, or add/remove moderator rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `membership_id` | string | path | yes | ID |
| `workflow_state` | string | form |  | Currently, the only allowed value is "accepted" Allowed: `accepted` |
| `moderator` | string | form |  | no description |

**Returns:** `GroupMembership`

## PUT /v1/groups/{group_id}/users/{user_id}

**Update a membership**  —  `update_membership_users`

Accept a membership request, or add/remove moderator rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `workflow_state` | string | form |  | Currently, the only allowed value is "accepted" Allowed: `accepted` |
| `moderator` | string | form |  | no description |

**Returns:** `GroupMembership`

## DELETE /v1/groups/{group_id}/memberships/{membership_id}

**Leave a group**  —  `leave_group_memberships`

Leave a group if you are allowed to leave (some groups, such as sets of
course groups created by teachers, cannot be left). You may also use 'self'
in place of a membership_id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `membership_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/users/{user_id}

**Leave a group**  —  `leave_group_users`

Leave a group if you are allowed to leave (some groups, such as sets of
course groups created by teachers, cannot be left). You may also use 'self'
in place of a membership_id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/users

**Bulk delete memberships
Bulk deletes memberships by providing an array of user IDs.**  —  `bulk_delete_memberships_bulk_deletes_memberships_by_providing_array_of_user_ids`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `user_ids` | array[integer] | query |  | - An array of user IDs to delete memberships in bulk. |

**Returns:** `array[JSON - For single deletion: `{ "ok": true }` - For bulk deletion: ```json { "message": "Bulk delete completed", "deleted_user_ids": 123, 456, "unauthorized_user_ids": 789 }]`


---

# Models


## Group

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the group. e.g. `17` |
| `name` | string |  | The display name of the group. e.g. `Math Group 1` |
| `description` | string |  | A description of the group. This is plain text. |
| `is_public` | boolean |  | Whether or not the group is public.  Currently only community groups can be made public.  Also, once a group has been set to public, it cannot be changed back to private. e.g. `False` |
| `followed_by_user` | boolean |  | Whether or not the current user is following this group. e.g. `False` |
| `join_level` | string |  | How people are allowed to join the group.  For all groups except for community groups, the user must share the group's parent course or account.  For student organized or community groups, where a user can be a member of as many or few as they want, the applicable levels are 'parent_context_auto_join', 'parent_context_request', and 'invitation_only'.  For class groups, where students are divided up and should only be part of one group of the category, this value will always be 'invitation_only', and is not relevant. * If 'parent_context_auto_join', anyone can join and will be automatically accepted. * If 'parent_context_request', anyone  can request to join, which must be approved by a group moderator. * If 'invitation_only', only those how have received an invitation my join the group, by accepting that invitation. e.g. `invitation_only` |
| `members_count` | integer |  | The number of members currently in the group e.g. `0` |
| `avatar_url` | string |  | The url of the group's avatar e.g. `https://<canvas>/files/avatar_image.png` |
| `context_type` | string |  | The course or account that the group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'account', the course_id field would be replaced by an account_id field. e.g. `Course` |
| `context_name` | string |  | The course or account name that the group belongs to. e.g. `Course 101` |
| `course_id` | integer |  | e.g. `3` |
| `role` | string |  | Certain types of groups have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account groups have a role of null. |
| `group_category_id` | integer |  | The ID of the group's category. e.g. `4` |
| `sis_group_id` | string |  | The SIS ID of the group. Only included if the user has permission to view SIS information. e.g. `group4a` |
| `sis_import_id` | integer |  | The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. e.g. `14` |
| `storage_quota_mb` | integer |  | the storage quota for the group, in megabytes e.g. `50` |
| `permissions` | object |  | optional: the permissions the user has for the group. returned only for a single group and include[]=permissions e.g. `{'create_discussion_topic': True, 'create_announcement': True}` |
| `users` | array[User] |  | optional: A list of users that are members in the group. Returned only if include[]=users. WARNING: this collection's size is capped (if there are an extremely large number of users in the group (thousands) not all of them will be returned). If you need to capture all the users in a group with certainty or experiencing slow response consider using the paginated /api/v1/groups/<group_id>/users endpoint. |
| `non_collaborative` | boolean |  | Indicates whether this group category is non-collaborative. A value of true means these group categories rely on the manage_tags permissions and do not have collaborative features |


## GroupMembership

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The id of the membership object e.g. `92` |
| `group_id` | integer |  | The id of the group object to which the membership belongs e.g. `17` |
| `user_id` | integer |  | The id of the user object to which the membership belongs e.g. `3` |
| `workflow_state` | string |  | The current state of the membership. Current possible values are 'accepted', 'invited', and 'requested' e.g. `accepted` |
| `moderator` | boolean |  | Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate) e.g. `True` |
| `just_created` | boolean |  | optional: whether or not the record was just created on a create call (POST), i.e. was the user just added to the group, or was the user already a member e.g. `True` |
| `sis_import_id` | integer |  | The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. e.g. `4` |
