# Accounts

> Canvas LMS REST API — `/accounts` resource. Base path `/api`.

## GET /v1/accounts

**List accounts**  —  `list_accounts`

A paginated list of accounts that the current user can view or manage.
Typically, students and even teachers will get an empty list in response,
only account admins can view the accounts that they are in.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `include` | array[string] | query |  | Array of additional information to include.  "lti_guid":: the 'tool_consumer_instance_guid' that will be sent for this account on LTI launches "registration_settings":: returns info about the privacy policy and terms of use "services":: returns services and whether they are enabled (requires account management permissions) "course_count":: returns the number of courses directly under each account "sub_account_count":: returns the number of sub-accounts directly under each account Allowed: `lti_guid`, `registration_settings`, `services`, `course_count`, `sub_account_count` |

**Returns:** `array[Account]`

## GET /v1/horizon_accounts

**List horizon accounts**  —  `list_horizon_accounts`

A paginated list of horizon accounts that the current user can view or manage.
Returns all accounts with the horizon_account setting enabled. If there are any
horizon accounts and the user has access to Site Admin, Site Admin will also be
included in the results.

Typically, students and even teachers will get an empty list in response,
only account admins can view the accounts that they are in.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `include` | array[string] | query |  | Array of additional information to include.  "lti_guid":: the 'tool_consumer_instance_guid' that will be sent for this account on LTI launches "registration_settings":: returns info about the privacy policy and terms of use "services":: returns services and whether they are enabled (requires account management permissions) "course_count":: returns the number of courses directly under each account "sub_account_count":: returns the number of sub-accounts directly under each account "site_admin":: returns true if the account is the Site Admin account (only included if true) Allowed: `lti_guid`, `registration_settings`, `services`, `course_count`, `sub_account_count`, `site_admin` |

**Returns:** `array[Account]`

## GET /v1/manageable_accounts

**Get accounts that admins can manage**  —  `get_accounts_that_admins_can_manage`

A paginated list of accounts where the current user has permission to create
or manage courses. List will be empty for students and teachers as only admins
can view which accounts they are in.

**Returns:** `array[Account]`

## GET /v1/course_creation_accounts

**Get accounts that users can create courses in**  —  `get_accounts_that_users_can_create_courses_in`

A paginated list of accounts where the current user has permission to create
courses.

**Returns:** `array[Account]`

## GET /v1/course_accounts

**List accounts for course admins**  —  `list_accounts_for_course_admins`

A paginated list of accounts that the current user can view through their
admin course enrollments. (Teacher, TA, or designer enrollments).
Only returns "id", "name", "workflow_state", "root_account_id" and "parent_account_id"

**Returns:** `array[Account]`

## GET /v1/accounts/{id}

**Get a single account**  —  `get_single_account`

Retrieve information on an individual account, given by id or sis
sis_account_id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `Account`

## GET /v1/accounts/{account_id}/settings

**Settings**  —  `settings`

Returns a JSON object containing a subset of settings for the specified account.
It's possible an empty set will be returned if no settings are applicable.
The caller must be an Account admin with the manage_account_settings permission.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/settings/environment

**List environment settings**  —  `list_environment_settings`

Return a hash of global settings for the root account
This is the same information supplied to the web interface as +ENV.SETTINGS+.

**Returns:** `void`

## GET /v1/accounts/{account_id}/permissions

**Permissions**  —  `permissions`

Returns permission information for the calling user and the given account.
You may use `self` as the account id to check permissions against the domain root account.
The caller must have an account role or admin (teacher/TA/designer) enrollment in a course
in the account.

See also the {api:CoursesController#permissions Course} and {api:GroupsController#permissions Group}
counterparts.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `permissions` | array[string] | query |  | List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. |

**Returns:** `void`

## GET /v1/accounts/{account_id}/sub_accounts

**Get the sub-accounts of an account**  —  `get_sub_accounts_of_account`

List accounts that are sub-accounts of the given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `recursive` | boolean | query |  | If true, the entire account tree underneath this account will be returned (though still paginated). If false, only direct sub-accounts of this account will be returned. Defaults to false. |
| `order` | string | query |  | Sorts the accounts by id or name. Only applies when recursive is false. Defaults to id. Allowed: `id`, `name` |
| `include` | array[string] | query |  | Array of additional information to include.  "course_count":: returns the number of courses directly under each account "sub_account_count":: returns the number of sub-accounts directly under each account Allowed: `course_count`, `sub_account_count` |

**Returns:** `array[Account]`

## GET /v1/accounts/{account_id}/terms_of_service

**Get the Terms of Service**  —  `get_terms_of_service`

Returns the terms of service for that account

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `TermsOfService`

## GET /v1/accounts/{account_id}/help_links

**Get help links**  —  `get_help_links`

Returns the help links for that account

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `HelpLinks`

## GET /v1/manually_created_courses_account

**Get the manually-created courses sub-account for the domain root account**  —  `get_manually_created_courses_sub_account_for_domain_root_account`

Returns the sub-account that contains manually created courses for the domain root account.

**Returns:** `Account`

## GET /v1/accounts/{account_id}/courses

**List active courses in an account**  —  `list_active_courses_in_account`

Retrieve a paginated list of courses in this account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `with_enrollments` | boolean | query |  | If true, include only courses with at least one enrollment.  If false, include only courses with no enrollments.  If not present, do not filter on course enrollment status. |
| `enrollment_type` | array[string] | query |  | If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment types. Allowed: `teacher`, `student`, `ta`, `observer`, `designer` |
| `enrollment_workflow_state` | array[string] | query |  | If set, only return courses that have at least one user enrolled in in the course with one of the specified enrollment workflow states. Allowed: `active`, `completed`, `deleted`, `invited`, `pending`, `creation_pending`, `rejected`, `inactive` |
| `published` | boolean | query |  | If true, include only published courses.  If false, exclude published courses.  If not present, do not filter on published status. |
| `completed` | boolean | query |  | If true, include only completed courses (these may be in state 'completed', or their enrollment term may have ended).  If false, exclude completed courses.  If not present, do not filter on completed status. |
| `blueprint` | boolean | query |  | If true, include only blueprint courses. If false, exclude them. If not present, do not filter on this basis. |
| `blueprint_associated` | boolean | query |  | If true, include only courses that inherit content from a blueprint course. If false, exclude them. If not present, do not filter on this basis. |
| `public` | boolean | query |  | If true, include only public courses. If false, exclude them. If not present, do not filter on this basis. |
| `by_teachers` | array[integer] | query |  | List of User IDs of teachers; if supplied, include only courses taught by one of the referenced users. |
| `by_subaccounts` | array[integer] | query |  | List of Account IDs; if supplied, include only courses associated with one of the referenced subaccounts. |
| `hide_enrollmentless_courses` | boolean | query |  | If present, only return courses that have at least one enrollment. Equivalent to 'with_enrollments=true'; retained for compatibility. |
| `state` | array[string] | query |  | If set, only return courses that are in the given state(s). By default, all states but "deleted" are returned. Allowed: `created`, `claimed`, `available`, `completed`, `deleted`, `all` |
| `enrollment_term_id` | array[integer] | query |  | If set, only includes courses from the specified terms. Can be either a single ID or an array of enrollment term IDs. |
| `search_term` | string | query |  | The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters. |
| `include` | array[string] | query |  | - All explanations can be seen in the {api:CoursesController#index Course API index documentation} - "sections", "needs_grading_count" and "total_scores" are not valid options at the account level Allowed: `syllabus_body`, `term`, `course_progress`, `storage_quota_used_mb`, `total_students`, `teachers`, `account_name`, `concluded`, `post_manually` |
| `sort` | string | query |  | The column to sort results by. Allowed: `course_status`, `course_name`, `sis_course_id`, `teacher`, `account_name` |
| `order` | string | query |  | The order to sort the given column by. Allowed: `asc`, `desc` |
| `search_by` | string | query |  | The filter to search by. "course" searches for course names, course codes, and SIS IDs. "teacher" searches for teacher names Allowed: `course`, `teacher` |
| `starts_before` | Date | query |  | If set, only return courses that start before the value (inclusive) or their enrollment term starts before the value (inclusive) or both the course's start_at and the enrollment term's start_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `ends_after` | Date | query |  | If set, only return courses that end after the value (inclusive) or their enrollment term ends after the value (inclusive) or both the course's end_at and the enrollment term's end_at are set to null. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `homeroom` | boolean | query |  | If set, only return homeroom courses. |

**Returns:** `array[Course]`

## PUT /v1/accounts/{id}

**Update an account**  —  `update_account`

Update an existing account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `account[name]` | string | form |  | Updates the account name |
| `account[sis_account_id]` | string | form |  | Updates the account sis_account_id Must have manage_sis permission and must not be a root_account. |
| `account[default_time_zone]` | string | form |  | The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `account[default_storage_quota_mb]` | integer (int64) | form |  | The default course storage quota to be used, if not otherwise specified. |
| `account[default_user_storage_quota_mb]` | integer (int64) | form |  | The default user storage quota to be used, if not otherwise specified. |
| `account[default_group_storage_quota_mb]` | integer (int64) | form |  | The default group storage quota to be used, if not otherwise specified. |
| `account[course_template_id]` | integer (int64) | form |  | The ID of a course to be used as a template for all newly created courses. Empty means to inherit the setting from parent account, 0 means to not use a template even if a parent account has one set. The course must be marked as a template. |
| `account[parent_account_id]` | integer (int64) | form |  | The ID of a parent account to move the account to. The new parent account must be in the same root account as the original. The hierarchy of sub-accounts will be preserved in the new parent account. The caller must be an administrator in both the original parent account and the new parent account. |
| `account[settings][restrict_student_past_view][value]` | boolean | form |  | Restrict students from viewing courses after end date |
| `account[settings][restrict_student_past_view][locked]` | boolean | form |  | Lock this setting for sub-accounts and courses |
| `account[settings][restrict_student_future_view][value]` | boolean | form |  | Restrict students from viewing courses before start date |
| `account[settings][microsoft_sync_enabled]` | boolean | form |  | Determines whether this account has Microsoft Teams Sync enabled or not.  Note that if you are altering Microsoft Teams sync settings you must enable the Microsoft Group enrollment syncing feature flag. In addition, if you are enabling Microsoft Teams sync, you must also specify a tenant, login attribute, and a remote attribute. Specifying a suffix to use is optional. |
| `account[settings][microsoft_sync_tenant]` | string | form |  | The tenant this account should use when using Microsoft Teams Sync. This should be an Azure Active Directory domain name. |
| `account[settings][microsoft_sync_login_attribute]` | string | form |  | The attribute this account should use to lookup users when using Microsoft Teams Sync. Must be one of "sub", "email", "oid", "preferred_username", or "integration_id". |
| `account[settings][microsoft_sync_login_attribute_suffix]` | string | form |  | A suffix that will be appended to the result of the login attribute when associating Canvas users with Microsoft users. Must be under 255 characters and contain no whitespace. This field is optional. |
| `account[settings][microsoft_sync_remote_attribute]` | string | form |  | The Active Directory attribute to use when associating Canvas users with Microsoft users. Must be one of "mail", "mailNickname", or "userPrincipalName". |
| `account[settings][restrict_student_future_view][locked]` | boolean | form |  | Lock this setting for sub-accounts and courses |
| `account[settings][lock_all_announcements][value]` | boolean | form |  | Disable comments on announcements |
| `account[settings][lock_all_announcements][locked]` | boolean | form |  | Lock this setting for sub-accounts and courses |
| `account[settings][usage_rights_required][value]` | boolean | form |  | Copyright and license information must be provided for files before they are published. |
| `account[settings][usage_rights_required][locked]` | boolean | form |  | Lock this setting for sub-accounts and courses |
| `account[settings][restrict_student_future_listing][value]` | boolean | form |  | Restrict students from viewing future enrollments in course list |
| `account[settings][restrict_student_future_listing][locked]` | boolean | form |  | Lock this setting for sub-accounts and courses |
| `account[settings][conditional_release][value]` | boolean | form |  | Enable or disable individual learning paths for students based on assessment |
| `account[settings][conditional_release][locked]` | boolean | form |  | Lock this setting for sub-accounts and courses |
| `account[settings][enable_course_paces][value]` | boolean | form |  | Enable or disable course pacing |
| `account[settings][enable_course_paces][locked]` | boolean | form |  | Lock this setting for sub-accounts and courses |
| `account[settings][suppress_notifications]` | boolean | form |  | Suppress notification messages from being created and sent. When set to +true+, all notifications are suppressed. When set to an array of notification category slugs (e.g. +["grading", "announcement"]+), only notifications in those categories are suppressed. Set to +false+ to allow all notifications. Root account setting only. |
| `account[settings][password_policy]` | Hash | form |  | Hash of optional password policy configuration parameters for a root account  +allow_login_suspension+ boolean:: Allow suspension of user logins upon reaching maximum_login_attempts  +require_number_characters+ boolean:: Require the use of number characters when setting up a new password  +require_symbol_characters+ boolean:: Require the use of symbol characters when setting up a new password  +minimum_character_length+ integer:: Minimum number of characters required for a new password  +maximum_login_attempts+ integer:: Maximum number of login attempts before a user is locked out  _Required_ feature option:   Enhance password options |
| `account[settings][enable_as_k5_account][value]` | boolean | form |  | Enable or disable Canvas for Elementary for this account |
| `account[settings][use_classic_font_in_k5][value]` | boolean | form |  | Whether or not the classic font is used on the dashboard. Only applies if enable_as_k5_account is true. |
| `account[settings][horizon_account][value]` | boolean | form |  | Enable or disable Canvas Career for this account |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |
| `account[settings][lock_outcome_proficiency][value]` | boolean | form |  | [DEPRECATED] Restrict instructors from changing mastery scale |
| `account[lock_outcome_proficiency][locked]` | boolean | form |  | [DEPRECATED] Lock this setting for sub-accounts and courses |
| `account[settings][lock_proficiency_calculation][value]` | boolean | form |  | [DEPRECATED] Restrict instructors from changing proficiency calculation method |
| `account[lock_proficiency_calculation][locked]` | boolean | form |  | [DEPRECATED] Lock this setting for sub-accounts and courses |
| `account[services]` | Hash | form |  | Give this a set of keys and boolean values to enable or disable services matching the keys |

**Returns:** `Account`

## DELETE /v1/accounts/{account_id}/users/{user_id}

**Delete a user from the root account**  —  `delete_user_from_root_account`

Delete a user record from a Canvas root account. If a user is associated
with multiple root accounts (in a multi-tenant instance of Canvas), this
action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account.
If they do this, they won't be able to make API calls or log into Canvas at
that account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `User`

## DELETE /v1/accounts/{account_id}/users

**Delete multiple users from the root account**  —  `delete_multiple_users_from_root_account`

Delete multiple users from a Canvas root account. If a user is associated
with multiple root accounts (in a multi-tenant instance of Canvas), this
action will NOT remove them from the other accounts.

WARNING: This API will allow a user to remove themselves from the account.
If they do this, they won't be able to make API calls or log into Canvas at
that account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `Progress`

## PUT /v1/accounts/{account_id}/users/bulk_update

**Update multiple users**  —  `update_multiple_users`

Updates multiple users in bulk.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user_ids` | string | form |  | [Array<Integer>] The IDs of the users to update. |
| `user` | Hash | form |  | The attributes to update for each user. |

**Returns:** `Progress`

## PUT /v1/accounts/{account_id}/users/{user_id}/restore

**Restore a deleted user from a root account**  —  `restore_deleted_user_from_root_account`

Restore a user record along with the most recently deleted pseudonym
from a Canvas root account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `User`

## POST /v1/accounts/{account_id}/sub_accounts

**Create a new sub-account**  —  `create_new_sub_account`

Add a new sub-account to a given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `account[name]` | string | form | yes | The name of the new sub-account. |
| `account[sis_account_id]` | string | form |  | The account's identifier in the Student Information System. |
| `account[default_storage_quota_mb]` | integer (int64) | form |  | The default course storage quota to be used, if not otherwise specified. |
| `account[default_user_storage_quota_mb]` | integer (int64) | form |  | The default user storage quota to be used, if not otherwise specified. |
| `account[default_group_storage_quota_mb]` | integer (int64) | form |  | The default group storage quota to be used, if not otherwise specified. |

**Returns:** `Account`

## DELETE /v1/accounts/{account_id}/sub_accounts/{id}

**Delete a sub-account**  —  `delete_sub_account`

Cannot delete an account with active courses or active sub_accounts.
Cannot delete a root_account

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

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
| `default_storage_quota_mb` | integer |  | The storage quota for the account in megabytes, if not otherwise specified e.g. `500` |
| `default_user_storage_quota_mb` | integer |  | The storage quota for a user in the account in megabytes, if not otherwise specified e.g. `50` |
| `default_group_storage_quota_mb` | integer |  | The storage quota for a group in the account in megabytes, if not otherwise specified e.g. `50` |
| `default_time_zone` | string |  | The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. e.g. `America/Denver` |
| `sis_account_id` | string |  | The account's identifier in the Student Information System. Only included if the user has permission to view SIS information. e.g. `123xyz` |
| `integration_id` | string |  | The account's identifier in the Student Information System. Only included if the user has permission to view SIS information. e.g. `123xyz` |
| `sis_import_id` | integer |  | The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. e.g. `12` |
| `course_count` | integer |  | The number of courses directly under the account (available via include) e.g. `10` |
| `sub_account_count` | integer |  | The number of sub-accounts directly under the account (available via include) e.g. `10` |
| `lti_guid` | string |  | The account's identifier that is sent as context_id in LTI launches. e.g. `123xyz` |
| `workflow_state` | string |  | The state of the account. Can be 'active' or 'deleted'. e.g. `active` |


## TermsOfService

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | Terms Of Service id e.g. `1` |
| `terms_type` | string |  | The given type for the Terms of Service e.g. `default` Allowed: `default`, `custom`, `no_terms` |
| `passive` | boolean |  | Boolean dictating if the user must accept Terms of Service e.g. `False` |
| `account_id` | integer |  | The id of the root account that owns the Terms of Service e.g. `1` |
| `content` | string |  | Content of the Terms of Service e.g. `To be or not to be that is the question` |
| `self_registration_type` | string |  | The type of self registration allowed e.g. `['none', 'observer', 'all']` |


## HelpLink

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | The ID of the help link e.g. `instructor_question` |
| `text` | string |  | The name of the help link e.g. `Ask Your Instructor a Question` |
| `subtext` | string |  | The description of the help link e.g. `Questions are submitted to your instructor` |
| `url` | string |  | The URL of the help link e.g. `#teacher_feedback` |
| `type` | string |  | The type of the help link e.g. `default` Allowed: `default`, `custom` |
| `available_to` | array[string] |  | The roles that have access to this help link e.g. `['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled']` |


## HelpLinks

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `help_link_name` | string |  | Help link button title e.g. `Help And Policies` |
| `help_link_icon` | string |  | Help link button icon e.g. `help` |
| `custom_help_links` | array[HelpLink] |  | Help links defined by the account. Could include default help links. e.g. `[{'id': 'link1', 'text': 'Custom Link!', 'subtext': 'Something something.', 'url': 'https://google.com', 'type': 'custom', 'available_to': ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled'], 'is_featured': True, 'is_new': False, 'feature_headline': 'Check this out!'}]` |
| `default_help_links` | array[HelpLink] |  | Default help links provided when account has not set help links of their own. e.g. `[{'available_to': ['student'], 'text': 'Ask Your Instructor a Question', 'subtext': 'Questions are submitted to your instructor', 'url': '#teacher_feedback', 'type': 'default', 'id': 'instructor_question', 'is_featured': False, 'is_new': True, 'feature_headline': ''}, {'available_to': ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled'], 'text': 'Search the Canvas Guides', 'subtext': 'Find answers to common questions', 'url': 'https://community.canvaslms.com/t5/Guides/ct-p/guides', 'type': 'default', 'id': 'search_the_canvas_guides', 'is_featured': False, 'is_new': False, 'feature_headline': ''}, {'available_to': ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled'], 'text': 'Report a Problem', 'subtext': 'If Canvas misbehaves, tell us about it', 'url': '#create_ticket', 'type': 'default', 'id': 'report_a_problem', 'is_featured': False, 'is_new': False, 'feature_headline': ''}]` |
