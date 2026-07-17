# Users

> Canvas LMS REST API — `/users` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/users

**List users in account**  —  `list_users_in_account`

A paginated list of users associated with this account.

 @example_request
   curl https://<canvas>/api/v1/accounts/self/users?search_term=<search value> \
      -X GET \
      -H 'Authorization: Bearer <token>'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name or full ID of the users to match and return in the results list. Must be at least 3 characters.  Note that the API will prefer matching on canonical user ID if the ID has a numeric form. It will only search against other fields if non-numeric in form, or if the numeric value doesn't yield any matches. Queries by administrative users will search on SIS ID, Integration ID, login ID, name, or email address |
| `enrollment_type` | string | query |  | When set, only return users enrolled with the specified course-level base role. This can be a base role type of 'student', 'teacher', 'ta', 'observer', or 'designer'. |
| `sort` | string | query |  | The column to sort results by. For efficiency, use +id+ if you intend to retrieve many pages of results. In the future, other sort options may be rate-limited after 50 pages. Allowed: `username`, `email`, `sis_id`, `integration_id`, `last_login`, `id` |
| `order` | string | query |  | The order to sort the given column by. Allowed: `asc`, `desc` |
| `include_deleted_users` | boolean | query |  | When set to true and used with an account context, returns users who have deleted pseudonyms for the context |
| `uuids` | Array | query |  | When set, only return users with the specified UUIDs. UUIDs after the first 100 are ignored. |

**Returns:** `array[User]`

## GET /v1/users/self/activity_stream

**List the activity stream**  —  `list_activity_stream_self`

Returns the current user's global activity stream, paginated.

There are many types of objects that can be returned in the activity
stream. All object types have the same basic set of shared attributes:
  !!!javascript
  {
    'created_at': '2011-07-13T09:12:00Z',
    'updated_at': '2011-07-25T08:52:41Z',
    'id': 1234,
    'title': 'Stream Item Subject',
    'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
    'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
    'read_state': false,
    'context_type': 'course', // course|group
    'course_id': 1,
    'group_id': null,
    'html_url': "http://..." // URL to the Canvas web UI for this stream item
  }

In addition, each item type has its own set of attributes available.

DiscussionTopic:

  !!!javascript
  {
    'type': 'DiscussionTopic',
    'discussion_topic_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': true,
    'root_discussion_entries': {
      ...
    }
  }

For DiscussionTopic, the message is truncated at 4kb.

Announcement:

  !!!javascript
  {
    'type': 'Announcement',
    'announcement_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': null,
    'root_discussion_entries': {
      ...
    }
  }

For Announcement, the message is truncated at 4kb.

Conversation:

  !!!javascript
  {
    'type': 'Conversation',
    'conversation_id': 1234,
    'private': false,
    'participant_count': 3,
  }

Message:

  !!!javascript
  {
    'type': 'Message',
    'message_id': 1234,
    'notification_category': 'Assignment Graded'
  }

Submission:

Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.

Conference:

  !!!javascript
  {
    'type': 'Conference',
    'web_conference_id': 1234
  }

Collaboration:

  !!!javascript
  {
    'type': 'Collaboration',
    'collaboration_id': 1234
  }

AssessmentRequest:

  !!!javascript
  {
    'type': 'AssessmentRequest',
    'assessment_request_id': 1234
  }

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `only_active_courses` | boolean | query |  | If true, will only return objects for courses the user is actively participating in |

**Returns:** `void`

## GET /v1/users/activity_stream

**List the activity stream**  —  `list_activity_stream_activity_stream`

Returns the current user's global activity stream, paginated.

There are many types of objects that can be returned in the activity
stream. All object types have the same basic set of shared attributes:
  !!!javascript
  {
    'created_at': '2011-07-13T09:12:00Z',
    'updated_at': '2011-07-25T08:52:41Z',
    'id': 1234,
    'title': 'Stream Item Subject',
    'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
    'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
    'read_state': false,
    'context_type': 'course', // course|group
    'course_id': 1,
    'group_id': null,
    'html_url': "http://..." // URL to the Canvas web UI for this stream item
  }

In addition, each item type has its own set of attributes available.

DiscussionTopic:

  !!!javascript
  {
    'type': 'DiscussionTopic',
    'discussion_topic_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': true,
    'root_discussion_entries': {
      ...
    }
  }

For DiscussionTopic, the message is truncated at 4kb.

Announcement:

  !!!javascript
  {
    'type': 'Announcement',
    'announcement_id': 1234,
    'total_root_discussion_entries': 5,
    'require_initial_post': true,
    'user_has_posted': null,
    'root_discussion_entries': {
      ...
    }
  }

For Announcement, the message is truncated at 4kb.

Conversation:

  !!!javascript
  {
    'type': 'Conversation',
    'conversation_id': 1234,
    'private': false,
    'participant_count': 3,
  }

Message:

  !!!javascript
  {
    'type': 'Message',
    'message_id': 1234,
    'notification_category': 'Assignment Graded'
  }

Submission:

Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.

Conference:

  !!!javascript
  {
    'type': 'Conference',
    'web_conference_id': 1234
  }

Collaboration:

  !!!javascript
  {
    'type': 'Collaboration',
    'collaboration_id': 1234
  }

AssessmentRequest:

  !!!javascript
  {
    'type': 'AssessmentRequest',
    'assessment_request_id': 1234
  }

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `only_active_courses` | boolean | query |  | If true, will only return objects for courses the user is actively participating in |

**Returns:** `void`

## GET /v1/users/self/activity_stream/summary

**Activity stream summary**  —  `activity_stream_summary`

Returns a summary of the current user's global activity stream.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `only_active_courses` | boolean | query |  | If true, will only return objects for courses the user is actively participating in |

**Returns:** `void`

## GET /v1/users/self/todo

**List the TODO items**  —  `list_todo_items`

A paginated list of the current user's list of todo items.

There is a limit to the number of items returned.

The `ignore` and `ignore_permanently` URLs can be used to update the user's
preferences on what items will be displayed.
Performing a DELETE request against the `ignore` URL will hide that item
from future todo item requests, until the item changes.
Performing a DELETE request against the `ignore_permanently` URL will hide
that item forever.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `include` | array[string] | query |  | "ungraded_quizzes":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. "grading_counts":: Optionally include segmented submission counts on grading-type items:                    +on_time_needs_grading_count+, +late_needs_grading_count+,                    +resubmitted_needs_grading_count+, +submitted_submissions_count+, and                    +total_submissions_count+. Only honored when the account has the                    +educator_dashboard+ feature enabled; otherwise silently ignored. Allowed: `ungraded_quizzes`, `grading_counts` |
| `course_ids` | array[string] | query |  | Restrict results to todo items in the given courses. Accepts numeric IDs and SIS IDs of the form +sis_course_id:foo+. Applies to grading, submitting, checkpoint, and ungraded quiz items alike. Courses the user is not enrolled in (or that cannot be resolved) are silently dropped. When the parameter is present but no valid courses resolve, an empty list is returned rather than the unfiltered list. |

**Returns:** `void`

## GET /v1/users/self/todo_item_count

**List counts for todo items**  —  `list_counts_for_todo_items`

Counts of different todo items such as the number of assignments needing grading as well as the number of assignments needing submitting.

There is a limit to the number of todo items this endpoint will count.
It will only look at the first 100 todo items for the user. If the user has more than 100 todo items this count may not be reliable.
The largest reliable number for both counts is 100.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `include` | array[string] | query |  | "ungraded_quizzes":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.                      These will be returned under a +quiz+ key instead of an +assignment+ key in response elements. Allowed: `ungraded_quizzes` |

**Returns:** `void`

## GET /v1/users/self/upcoming_events

**List upcoming assignments, calendar events**  —  `list_upcoming_assignments_calendar_events`

A paginated list of the current user's upcoming events.

**Returns:** `void`

## GET /v1/users/{user_id}/missing_submissions

**List Missing Submissions**  —  `list_missing_submissions`

A paginated list of past-due assignments for which the student does not have a submission.
The user sending the request must either be the student, an admin or a parent observer using the parent app

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | the student's ID |
| `observed_user_id` | string | query |  | Return missing submissions for the given observed user. Must be accompanied by course_ids[]. The user making the request must be observing the observed user in all the courses specified by course_ids[]. |
| `include` | array[string] | query |  | "planner_overrides":: Optionally include the assignment's associated planner override, if it exists, for the current user.                       These will be returned under a +planner_override+ key "course":: Optionally include the assignments' courses Allowed: `planner_overrides`, `course` |
| `filter` | array[string] | query |  | "submittable":: Only return assignments that the current user can submit (i.e. filter out locked assignments) "current_grading_period":: Only return missing assignments that are in the current grading period Allowed: `submittable`, `current_grading_period` |
| `course_ids` | array[string] | query |  | Optionally restricts the list of past-due assignments to only those associated with the specified course IDs. Required if observed_user_id is passed. |

**Returns:** `array[Assignment]`

## DELETE /v1/users/self/activity_stream/{id}

**Hide a stream item**  —  `hide_stream_item`

Hide the given stream item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/users/self/activity_stream

**Hide all stream items**  —  `hide_all_stream_items`

Hide all stream items for the user

**Returns:** `void`

## POST /v1/users/{user_id}/files

**Upload a file**  —  `upload_file`

Upload a file to the user's personal files section.

This API endpoint is the first step in uploading a file to a user's files.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Note that typically users will only be able to upload files to their
own files section. Passing a user_id of +self+ is an easy shortcut
to specify the current user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/users/{id}

**Show user details**  —  `show_user_details`

Shows details for user.

Also includes an attribute "permissions", a non-comprehensive list of permissions for the user.
Example:
  !!!javascript
  "permissions": {
   "can_update_name": true, // Whether the user can update their name.
   "can_update_avatar": false, // Whether the user can update their avatar.
   "limit_parent_app_web_access": false // Whether the user can interact with Canvas web from the Canvas Parent app.
  }

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include on the user record. "locale", "avatar_url", "permissions", "email", and "effective_locale" will always be returned Allowed: `uuid`, `last_login` |

**Returns:** `User`

## POST /v1/accounts/{account_id}/users

**Create a user**  —  `create_user`

Create and return a new user and pseudonym for an account.

[DEPRECATED (for self-registration only)] If you don't have the "Modify
login details for users" permission, but self-registration is enabled
on the account, you can still use this endpoint to register new users.
Certain fields will be required, and others will be ignored (see below).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user[name]` | string | form |  | The full name of the user. This name will be used by teacher for grading. Required if this is a self-registration. |
| `user[short_name]` | string | form |  | User's name as it will be displayed in discussions, messages, and comments. |
| `user[sortable_name]` | string | form |  | User's name as used to sort alphabetically in lists. |
| `user[time_zone]` | string | form |  | The time zone for the user. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `user[locale]` | string | form |  | The user's preferred language, from the list of languages Canvas supports. This is in RFC-5646 format. |
| `user[terms_of_use]` | boolean | form |  | Whether the user accepts the terms of use. Required if this is a self-registration and this canvas instance requires users to accept the terms (on by default).  If this is true, it will mark the user as having accepted the terms of use. |
| `user[skip_registration]` | boolean | form |  | Automatically mark the user as registered.  If this is true, it is recommended to set <tt>"pseudonym[send_confirmation]"</tt> to true as well. Otherwise, the user will not receive any messages about their account creation.  The users communication channel confirmation can be skipped by setting <tt>"communication_channel[skip_confirmation]"</tt> to true as well. |
| `pseudonym[unique_id]` | string | form | yes | User's login ID. If this is a self-registration, it must be a valid email address. |
| `pseudonym[password]` | string | form |  | User's password. Cannot be set during self-registration. |
| `pseudonym[sis_user_id]` | string | form |  | SIS ID for the user's account. To set this parameter, the caller must be able to manage SIS permissions. |
| `pseudonym[integration_id]` | string | form |  | Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions. The Integration ID is a secondary identifier useful for more complex SIS integrations. |
| `pseudonym[send_confirmation]` | boolean | form |  | Send user notification of account creation if true. Automatically set to true during self-registration. |
| `pseudonym[force_self_registration]` | boolean | form |  | Send user a self-registration style email if true. Setting it means the users will get a notification asking them to "complete the registration process" by clicking it, setting a password, and letting them in.  Will only be executed on if the user does not need admin approval. Defaults to false unless explicitly provided. |
| `pseudonym[authentication_provider_id]` | string | form |  | The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider). |
| `communication_channel[type]` | string | form |  | The communication channel type, e.g. 'email' or 'sms'. |
| `communication_channel[address]` | string | form |  | The communication channel address, e.g. the user's email address. |
| `communication_channel[confirmation_url]` | boolean | form |  | Only valid for account admins. If true, returns the new user account confirmation URL in the response. |
| `communication_channel[skip_confirmation]` | boolean | form |  | Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel.  If this is true, it is recommended to set <tt>"pseudonym[send_confirmation]"</tt> to true as well. Otherwise, the user will not receive any messages about their account creation. |
| `force_validations` | boolean | form |  | If true, validations are performed on the newly created user (and their associated pseudonym) even if the request is made by a privileged user like an admin. When set to false, or not included in the request parameters, any newly created users are subject to validations unless the request is made by a user with a 'manage_user_logins' right. In which case, certain validations such as 'require_acceptance_of_terms' and 'require_presence_of_name' are not enforced. Use this parameter to return helpful json errors while building users with an admin request. |
| `enable_sis_reactivation` | boolean | form |  | When true, will first try to re-activate a deleted user with matching sis_user_id if possible. This is commonly done with +user[skip_registration]+ and +communication_channel[skip_confirmation]+ so that the default communication_channel is also restored. |
| `destination` | URL | form |  | If you're setting the password for the newly created user, you can provide this param with a valid URL pointing into this Canvas installation, and the response will include a destination field that's a URL that you can redirect a browser to and have the newly created user automatically logged in. The URL is only valid for a short time, and must match the domain this request is directed to, and be for a well-formed path that Canvas can recognize. |
| `initial_enrollment_type` | string | form |  | `observer` if doing a self-registration with a pairing code. This allows setting the password during user creation. |
| `pairing_code[code]` | string | form |  | If provided and valid, will link the new user as an observer to the student's whose pairing code is given. |

**Returns:** `User`

## POST /v1/accounts/{account_id}/self_registration

**[DEPRECATED] Self register a user**  —  `deprecated_self_register_user`

Self register and return a new user and pseudonym for an account.

If self-registration is enabled on the account, you can use this
endpoint to self register new users.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user[name]` | string | form | yes | The full name of the user. This name will be used by teacher for grading. |
| `user[short_name]` | string | form |  | User's name as it will be displayed in discussions, messages, and comments. |
| `user[sortable_name]` | string | form |  | User's name as used to sort alphabetically in lists. |
| `user[time_zone]` | string | form |  | The time zone for the user. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `user[locale]` | string | form |  | The user's preferred language, from the list of languages Canvas supports. This is in RFC-5646 format. |
| `user[terms_of_use]` | boolean | form | yes | Whether the user accepts the terms of use. |
| `pseudonym[unique_id]` | string | form | yes | User's login ID. Must be a valid email address. |
| `communication_channel[type]` | string | form |  | The communication channel type, e.g. 'email' or 'sms'. |
| `communication_channel[address]` | string | form |  | The communication channel address, e.g. the user's email address. |

**Returns:** `User`

## GET /v1/users/{id}/settings

**Update user settings.**  —  `update_user_settings`

Update an existing user's settings.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `manual_mark_as_read` | boolean | query |  | If true, require user to manually mark discussion posts as read (don't auto-mark as read). |
| `release_notes_badge_disabled` | boolean | query |  | If true, hide the badge for new release notes. |
| `collapse_global_nav` | boolean | query |  | If true, the user's page loads with the global navigation collapsed |
| `collapse_course_nav` | boolean | query |  | If true, the user's course pages will load with the course navigation collapsed. |
| `hide_dashcard_color_overlays` | boolean | query |  | If true, images on course cards will be presented without being tinted to match the course color. |
| `comment_library_suggestions_enabled` | boolean | query |  | If true, suggestions within the comment library will be shown. |
| `elementary_dashboard_disabled` | boolean | query |  | If true, will display the user's preferred class Canvas dashboard view instead of the canvas for elementary view. |
| `widget_dashboard_user_preference` | boolean | query |  | If true, enables the widget dashboard for the user. Only applies when the widget_dashboard feature is enabled at the account level. Defaults to true when the feature becomes available. |
| `widget_dashboard_dark_mode` | boolean | query |  | If true, enables the dark color theme for the widget dashboard. |

**Returns:** `void`

## GET /v1/users/{id}/colors

**Get custom colors**  —  `get_custom_colors`

Returns all custom colors that have been saved for a user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/users/{id}/colors/{asset_string}

**Get custom color**  —  `get_custom_color`

Returns the custom colors that have been saved for a user for a given context.

The asset_string parameter should be in the format 'context_id', for example
'course_42'.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `asset_string` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/users/{id}/colors/{asset_string}

**Update custom color**  —  `update_custom_color`

Updates a custom color for a user for a given context.  This allows
colors for the calendar and elsewhere to be customized on a user basis.

The asset string parameter should be in the format 'context_id', for example
'course_42'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `asset_string` | string | path | yes | ID |
| `hexcode` | string | form |  | The hexcode of the color to set for the context, if you choose to pass the hexcode as a query parameter rather than in the request body you should NOT include the '#' unless you escape it first. |

**Returns:** `void`

## PUT /v1/users/{id}/text_editor_preference

**Update text editor preference**  —  `update_text_editor_preference`

Updates a user's default choice for text editor.  This allows
the Choose an Editor propmts to preload the user's preference.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `text_editor_preference` | string | form |  | The identifier for the editor. Allowed: `block_editor`, `rce`, `` |

**Returns:** `void`

## PUT /v1/users/{id}/files_ui_version_preference

**Update files UI version preference**  —  `update_files_ui_version_preference`

Updates a user's default choice for files UI version. This allows
the files UI to preload the user's preference.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `files_ui_version` | string | form |  | The identifier for the files UI version. Allowed: `v1`, `v2` |

**Returns:** `void`

## GET /v1/users/{id}/dashboard_positions

**Get dashboard positions**  —  `get_dashboard_positions`

Returns all dashboard positions that have been saved for a user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/users/{id}/dashboard_positions

**Update dashboard positions**  —  `update_dashboard_positions`

Updates the dashboard positions for a user for a given context.  This allows
positions for the dashboard cards and elsewhere to be customized on a per
user basis.

The asset string parameter should be in the format 'context_id', for example
'course_42'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/users/{id}

**Edit a user**  —  `edit_user`

Modify an existing user. To modify a user's login, see the documentation for logins.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `user[name]` | string | form |  | The full name of the user. This name will be used by teacher for grading. |
| `user[short_name]` | string | form |  | User's name as it will be displayed in discussions, messages, and comments. |
| `user[sortable_name]` | string | form |  | User's name as used to sort alphabetically in lists. |
| `user[time_zone]` | string | form |  | The time zone for the user. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `user[email]` | string | form |  | The default email address of the user. |
| `user[locale]` | string | form |  | The user's preferred language, from the list of languages Canvas supports. This is in RFC-5646 format. |
| `user[avatar][token]` | string | form |  | A unique representation of the avatar record to assign as the user's current avatar. This token can be obtained from the user avatars endpoint. This supersedes the +user[avatar][url]+ argument, and if both are included the url will be ignored. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client. |
| `user[avatar][url]` | string | form |  | To set the user's avatar to point to an external url, do not include a token and instead pass the url here. Warning: For maximum compatibility, please use 128 px square images. |
| `user[avatar][state]` | string | form |  | To set the state of user's avatar. Only valid for account administrator. Allowed: `none`, `submitted`, `approved`, `locked`, `reported`, `re_reported` |
| `user[title]` | string | form |  | Sets a title on the user profile. (See {api:ProfileController#settings Get user profile}.) Profiles must be enabled on the root account. |
| `user[bio]` | string | form |  | Sets a bio on the user profile. (See {api:ProfileController#settings Get user profile}.) Profiles must be enabled on the root account. |
| `user[pronunciation]` | string | form |  | Sets name pronunciation on the user profile. (See {api:ProfileController#settings Get user profile}.) Profiles and name pronunciation must be enabled on the root account. |
| `user[pronouns]` | string | form |  | Sets pronouns on the user profile. Passing an empty string will empty the user's pronouns Only Available Pronouns set on the root account are allowed Adding and changing pronouns must be enabled on the root account. |
| `user[event]` | string | form |  | Suspends or unsuspends all logins for this user that the calling user has permission to Allowed: `suspend`, `unsuspend` |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `User`

## DELETE /v1/users/{id}/sessions

**Terminate all user sessions**  —  `terminate_all_user_sessions`

Terminates all sessions for a user. This includes all browser-based
sessions and all access tokens, including manually generated ones.
The user can immediately re-authenticate to access Canvas again if
they have the current credentials. All integrations will need to
be re-authorized.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/users/mobile_sessions

**Log users out of all mobile apps**  —  `log_users_out_of_all_mobile_apps_mobile_sessions`

Permanently expires any active mobile sessions, forcing them to re-authorize.

The route that takes a user id will expire mobile sessions for that user.
The route that doesn't take a user id will expire mobile sessions for *all* users
in the institution (except for account administrators if +skip_admins+ is given).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `skip_admins` | boolean | query |  | If true, will not expire mobile sessions for account administrators. |

**Returns:** `void`

## DELETE /v1/users/{id}/mobile_sessions

**Log users out of all mobile apps**  —  `log_users_out_of_all_mobile_apps_id`

Permanently expires any active mobile sessions, forcing them to re-authorize.

The route that takes a user id will expire mobile sessions for that user.
The route that doesn't take a user id will expire mobile sessions for *all* users
in the institution (except for account administrators if +skip_admins+ is given).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `skip_admins` | boolean | query |  | If true, will not expire mobile sessions for account administrators. |

**Returns:** `void`

## PUT /v1/users/{id}/merge_into/{destination_user_id}

**Merge user into another user**  —  `merge_user_into_another_user_destination_user_id`

Merge a user into another user.
To merge users, the caller must have permissions to manage both users. This
should be considered irreversible. This will delete the user and move all
the data into the destination user.

User merge details and caveats:
The from_user is the user that was deleted in the user_merge process.
The destination_user is the user that remains, that is being split.

Avatars:
When both users have avatars, only the destination_users avatar will remain.
When one user has an avatar, it will end up on the destination_user.

Terms of Use:
If either user has accepted terms of use, it will be be left as accepted.

Communication Channels:
All unique communication channels moved to the destination_user.
All notification preferences are moved to the destination_user.

Enrollments:
All unique enrollments are moved to the destination_user.
When there is an enrollment that would end up making it so that a user would
be observing themselves, the enrollment is not moved over.
Everything that is tied to the from_user at the course level relating to the
enrollment is also moved to the destination_user.

Submissions:
All submissions are moved to the destination_user. If there are enrollments
for both users in the same course, we prefer submissions that have grades
then submissions that have work in them, and if there are no grades or no
work, they are not moved.

Other notes:
Access Tokens are moved on merge.
Conversations are moved on merge.
Favorites are moved on merge.
Courses will commonly use LTI tools. LTI tools reference the user with IDs
that are stored on a user object. Merging users deletes one user and moves
all records from the deleted user to the destination_user. These IDs are
kept for all enrollments, group_membership, and account_users for the
from_user at the time of the merge. When the destination_user launches an
LTI tool from a course that used to be the from_user's, it doesn't appear as
a new user to the tool provider. Instead it will send the stored ids. The
destination_user's LTI IDs remain as they were for the courses that they
originally had. Future enrollments for the destination_user will use the IDs
that are on the destination_user object. LTI IDs that are kept and tracked
per context include lti_context_id, lti_id and uuid. APIs that return the
LTI ids will return the one for the context that it is called for, except
for the user uuid. The user UUID will display the destination_users uuid,
and when getting the uuid from an api that is in a context that was
recorded from a merge event, an additional attribute is added as past_uuid.

When finding users by SIS ids in different accounts the
destination_account_id is required.

The account can also be identified by passing the domain in destination_account_id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `destination_user_id` | string | path | yes | ID |

**Returns:** `User`

## PUT /v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id}

**Merge user into another user**  —  `merge_user_into_another_user_accounts`

Merge a user into another user.
To merge users, the caller must have permissions to manage both users. This
should be considered irreversible. This will delete the user and move all
the data into the destination user.

User merge details and caveats:
The from_user is the user that was deleted in the user_merge process.
The destination_user is the user that remains, that is being split.

Avatars:
When both users have avatars, only the destination_users avatar will remain.
When one user has an avatar, it will end up on the destination_user.

Terms of Use:
If either user has accepted terms of use, it will be be left as accepted.

Communication Channels:
All unique communication channels moved to the destination_user.
All notification preferences are moved to the destination_user.

Enrollments:
All unique enrollments are moved to the destination_user.
When there is an enrollment that would end up making it so that a user would
be observing themselves, the enrollment is not moved over.
Everything that is tied to the from_user at the course level relating to the
enrollment is also moved to the destination_user.

Submissions:
All submissions are moved to the destination_user. If there are enrollments
for both users in the same course, we prefer submissions that have grades
then submissions that have work in them, and if there are no grades or no
work, they are not moved.

Other notes:
Access Tokens are moved on merge.
Conversations are moved on merge.
Favorites are moved on merge.
Courses will commonly use LTI tools. LTI tools reference the user with IDs
that are stored on a user object. Merging users deletes one user and moves
all records from the deleted user to the destination_user. These IDs are
kept for all enrollments, group_membership, and account_users for the
from_user at the time of the merge. When the destination_user launches an
LTI tool from a course that used to be the from_user's, it doesn't appear as
a new user to the tool provider. Instead it will send the stored ids. The
destination_user's LTI IDs remain as they were for the courses that they
originally had. Future enrollments for the destination_user will use the IDs
that are on the destination_user object. LTI IDs that are kept and tracked
per context include lti_context_id, lti_id and uuid. APIs that return the
LTI ids will return the one for the context that it is called for, except
for the user uuid. The user UUID will display the destination_users uuid,
and when getting the uuid from an api that is in a context that was
recorded from a merge event, an additional attribute is added as past_uuid.

When finding users by SIS ids in different accounts the
destination_account_id is required.

The account can also be identified by passing the domain in destination_account_id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `destination_account_id` | string | path | yes | ID |
| `destination_user_id` | string | path | yes | ID |

**Returns:** `User`

## POST /v1/users/{id}/split

**Split merged users into separate users**  —  `split_merged_users_into_separate_users`

Merged users cannot be fully restored to their previous state, but this will
attempt to split as much as possible to the previous state.
To split a merged user, the caller must have permissions to manage all of
the users logins. If there are multiple users that have been merged into one
user it will split each merge into a separate user.
A split can only happen within 180 days of a user merge. A user merge deletes
the previous user and may be permanently deleted. In this scenario we create
a new user object and proceed to move as much as possible to the new user.
The user object will not have preserved the name or settings from the
previous user. Some items may have been deleted during a user_merge that
cannot be restored, and/or the data has become stale because of other
changes to the objects since the time of the user_merge.

Split users details and caveats:

The from_user is the user that was deleted in the user_merge process.
The destination_user is the user that remains, that is being split.

Avatars:
When both users had avatars, both will be remain.
When from_user had an avatar and destination_user did not have an avatar,
the destination_user's avatar will be deleted if it still matches what was
there are the time of the merge.
If the destination_user's avatar was changed at anytime after the merge, it
will remain on the destination user.
If the from_user had an avatar it will be there after split.

Terms of Use:
If from_user had not accepted terms of use, they will be prompted again
to accept terms of use after the split.
If the destination_user had not accepted terms of use, hey will be prompted
again to accept terms of use after the split.
If neither user had accepted the terms of use, but since the time of the
merge had accepted, both will be prompted to accept terms of use.
If both had accepted terms of use, this will remain.

Communication Channels:
All communication channels are restored to what they were prior to the
merge. If a communication channel was added after the merge, it will remain
on the destination_user.
Notification preferences remain with the communication channels.

Enrollments:
All enrollments from the time of the merge will be moved back to where they
were. Enrollments created since the time of the merge that were created by
sis_import will go to the user that owns that sis_id used for the import.
Other new enrollments will remain on the destination_user.
Everything that is tied to the destination_user at the course level relating
to an enrollment is moved to the from_user. When both users are in the same
course prior to merge this can cause some unexpected items to move.

Submissions:
Unlike other items tied to a course, submissions are explicitly recorded to
avoid problems with grades.
All submissions were moved are restored to the spot prior to merge.
All submission that were created in a course that was moved in enrollments
are moved over to the from_user.

Other notes:
Access Tokens are moved back on split.
Conversations are moved back on split.
Favorites that existing at the time of merge are moved back on split.
LTI ids are restored to how they were prior to merge.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `array[User]`

## POST /v1/users/self/pandata_events_token

**Get a Pandata Events jwt token and its expiration date**  —  `get_pandata_events_jwt_token_and_its_expiration_date`

Returns a jwt auth and props token that can be used to send events to
Pandata.

NOTE: This is currently only available to the mobile developer keys.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `app_key` | string | form |  | The pandata events appKey for this mobile app |

**Returns:** `void`

## GET /v1/users/{id}/graded_submissions

**Get a users most recently graded submissions**  —  `get_users_most_recently_graded_submissions`

Returns a list of the user's most recently graded submissions.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group Allowed: `assignment` |
| `only_current_enrollments` | boolean | query |  | Returns submissions for only currently active enrollments |
| `only_published_assignments` | boolean | query |  | Returns submissions for only published assignments |

**Returns:** `array[Submission]`

## GET /v1/users/{user_id}/profile

**Get user profile**  —  `get_user_profile`

Returns user profile data, including user id, name, and profile pic.

When requesting the profile for the user accessing the API, the user's
calendar feed URL and LTI user id will be returned as well.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include.  "links":: include the user's profile links in the response           as an array of objects with +url+ and +title+ fields "user_services":: include names and links for the user's connected services "uuid":: include the user's uuid in the response Allowed: `links`, `user_services`, `uuid` |

**Returns:** `Profile`

## GET /v1/users/{user_id}/avatars

**List avatar options**  —  `list_avatar_options`

A paginated list of the possible user avatar options that can be set with the user update endpoint. The response will be an array of avatar records. If the 'type' field is 'attachment', the record will include all the normal attachment json fields; otherwise it will include only the 'url' and 'display_name' fields. Additionally, all records will include a 'type' field and a 'token' field. The following explains each field in more detail
type:: ["gravatar"|"attachment"|"no_pic"] The type of avatar record, for categorization purposes.
url:: The url of the avatar
token:: A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.
display_name:: A textual description of the avatar record
id:: ['attachment' type only] the internal id of the attachment
content-type:: ['attachment' type only] the content-type of the attachment
filename:: ['attachment' type only] the filename of the attachment
size:: ['attachment' type only] the size of the attachment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[Avatar]`

## GET /v1/users/{user_id}/page_views

**List user page views**  —  `list_user_page_views`

Return a paginated list of the user's page view history in json format,
similar to the available CSV download. Page views are returned in
descending order, newest to oldest.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want page views. |
| `end_time` | DateTime | query |  | The end of the time range from which you want page views. |

**Returns:** `array[PageView]`

## POST /v1/users/{user_id}/page_views/query

**BETA - Initiate page views query**  —  `beta_initiate_page_views_query`

Initiates an asynchronous query for user page views data within a specified date range.
This method enqueues a background job to process the page views query and returns
a polling URL that can be used to check the query status and retrieve results when ready.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `start_date` | string | form |  | The start date for the page views query in YYYY-MM-DD format. Must be the first day of a month. |
| `end_date` | string | form |  | The end date for the page views query in YYYY-MM-DD format. Must be the first day of a month and after start_date. |
| `results_format` | string | form |  | The desired format for the query results. Supported formats: "csv", "jsonl" |

**Returns:** `AsyncQueryResponse`

## GET /v1/users/{user_id}/page_views/query/{query_id}

**BETA - Poll query status**  —  `beta_poll_query_status`

Checks the status of a previously initiated page views query. Returns the current
processing status and provides a result URL when the query is complete.

The query may fail with status "failed" and error_code
"RESULT_SIZE_LIMIT_EXCEEDED" if the result exceeds 500 MB.
If this happens, narrow the date range or query smaller
time intervals.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `query_id` | string | path | yes | The UUID of the query to check status for |

**Returns:** `AsyncQueryStatusResponse`

## GET /v1/users/{user_id}/page_views/query/{query_id}/results

**BETA - Get query results**  —  `beta_get_query_results`

Retrieves the results of a completed page views query. Returns the data in the
format specified when the query was initiated (CSV or JSON). The response may
be compressed with gzip encoding.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

Note: PageView payloads use two types of identifiers: globalId and localId. Global identifier is equal to (shardId*10000000000000)+localId.
Please note our global identifiers might change if your Canvas instance goes through shard migration process, in this case your current
shardId in the global identifier will change to a new shardId. Local identifiers do not change after shard migration and stay unique in the
context of the Canvas account. The following fields in the PageView payload are global identifiers: `links_user`, `links_context`, `links_asset`,
`links_real_user`, `links_account`, `developer_key_id`, `asset_user_access_id`.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `query_id` | string | path | yes | The UUID of the completed query to retrieve results for |

**Returns:** `QueryResultsResponse`

## POST /v1/users/page_views/query

**BETA - Initiate batch page views query**  —  `beta_initiate_batch_page_views_query`

Initiates an asynchronous query for page views data across multiple users.
This method enqueues a background job to process the batch page views query and returns
a polling URL that can be used to check the query status and retrieve results when ready.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_ids` | Array | form |  | Array of user IDs to query page views for. Must contain at least one user ID. Duplicate user IDs are not allowed. |
| `start_date` | string | form |  | The start date for the page views query in YYYY-MM-DD format. Must be the first day of a month. |
| `end_date` | string | form |  | The end date for the page views query in YYYY-MM-DD format. Must be the first day of a month and after start_date. |
| `results_format` | string | form |  | The desired format for the query results. Supported formats: "csv", "jsonl" |

**Returns:** `AsyncQueryResponse`

## GET /v1/users/page_views/query/{query_id}

**BETA - Poll batch query status**  —  `beta_poll_batch_query_status`

Checks the status of a previously initiated batch page views query. Returns the current
processing status and provides a result URL when the query is complete.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `query_id` | string | path | yes | The UUID of the query to check status for |

**Returns:** `AsyncQueryStatusResponse`

## GET /v1/users/page_views/query/{query_id}/results

**BETA - Get batch query results**  —  `beta_get_batch_query_results`

Retrieves the results of a completed batch page views query. Returns the data in the
format specified when the query was initiated (CSV or JSON). The response may
be compressed with gzip encoding.

As this is a beta endpoint, it is subject to change or removal at any time without the standard notice periods outlined in the API policy.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `query_id` | string | path | yes | The UUID of the completed query to retrieve results for |

**Returns:** `QueryResultsResponse`

## PUT /v1/users/{user_id}/custom_data

**Store custom data**  —  `store_custom_data`

Store arbitrary user data as JSON.

Arbitrary JSON data can be stored for a User.
A typical scenario would be an external site/service that registers users in Canvas
and wants to capture additional info about them.  The part of the URL that follows
+/custom_data/+ defines the scope of the request, and it reflects the structure of
the JSON data to be stored or retrieved.

The value +self+ may be used for +user_id+ to store data associated with the calling user.
In order to access another user's custom data, you must be an account administrator with
permission to manage users.

A namespace parameter, +ns+, is used to prevent custom_data collisions between
different apps.  This parameter is required for all custom_data requests.

A request with Content-Type multipart/form-data or Content-Type
application/x-www-form-urlencoded can only be used to store strings.

Example PUT with multipart/form-data data:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
    -X PUT \
    -F 'ns=com.my-organization.canvas-app' \
    -F 'data=555-1234' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "555-1234"
  }

Subscopes (or, generated scopes) can also be specified by passing values to
+data+[+subscope+].

Example PUT specifying subscopes:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \
    -X PUT \
    -F 'ns=com.my-organization.canvas-app' \
    -F 'data[waist]=32in' \
    -F 'data[inseam]=34in' \
    -F 'data[chest]=40in' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "chest": "40in",
      "waist": "32in",
      "inseam": "34in"
    }
  }

Following such a request, subsets of the stored data to be retrieved directly from a subscope.

Example {api:UsersController#get_custom_data GET} from a generated scope
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "40in"
  }

If you want to store more than just strings (i.e. numbers, arrays, hashes, true, false,
and/or null), you must make a request with Content-Type application/json as in the following
example.

Example PUT with JSON data:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -H 'Content-Type: application/json' \
    -X PUT \
    -d '{
          "ns": "com.my-organization.canvas-app",
          "data": {
            "a-number": 6.02e23,
            "a-bool": true,
            "a-string": "true",
            "a-hash": {"a": {"b": "ohai"}},
            "an-array": [1, "two", null, false]
          }
        }' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "a-number": 6.02e+23,
      "a-bool": true,
      "a-string": "true",
      "a-hash": {
        "a": {
          "b": "ohai"
        }
      },
      "an-array": [1, "two", null, false]
    }
  }

If the data is an Object (as it is in the above example), then subsets of the data can
be accessed by including the object's (possibly nested) keys in the scope of a GET request.

Example {api:UsersController#get_custom_data GET} with a generated scope:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "ohai"
  }


On success, this endpoint returns an object containing the data that was stored.

Responds with status code 200 if the scope already contained data, and it was overwritten
by the data specified in the request.

Responds with status code 201 if the scope was previously empty, and the data specified
in the request was successfully stored there.

Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid, or if
the +data+ parameter is missing.

Responds with status code 409 if the requested scope caused a conflict and data was not stored.
This happens when storing data at the requested scope would cause data at an outer scope
to be lost.  e.g., if +/custom_data+ was +{"fashion_app": {"hair": "blonde"}}+, but
you tried to +`PUT /custom_data/fashion_app/hair/style -F data=buzz`+, then for the request
to succeed,the value of +/custom_data/fashion_app/hair+ would have to become a hash, and its
old string value would be lost.  In this situation, an error object is returned with the
following format:

  !!!javascript
  {
    "message": "write conflict for custom_data hash",
    "conflict_scope": "fashion_app/hair",
    "type_at_conflict": "String",
    "value_at_conflict": "blonde"
  }

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `ns` | string | form | yes | The namespace under which to store the data.  This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization. |
| `data` | JSON | form | yes | The data you want to store for the user, at the specified scope.  If the data is composed of (possibly nested) JSON objects, scopes will be generated for the (nested) keys (see examples). |

**Returns:** `void`

## GET /v1/users/{user_id}/custom_data

**Load custom data**  —  `load_custom_data`

Load custom user data.

Arbitrary JSON data can be stored for a User.  This API call
retrieves that data for a (optional) given scope.
See {api:UsersController#set_custom_data Store Custom Data} for details and
examples.

On success, this endpoint returns an object containing the data that was requested.

Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
or if the specified scope does not contain any data.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `ns` | string | query | yes | The namespace from which to retrieve the data.  This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization. |

**Returns:** `void`

## DELETE /v1/users/{user_id}/custom_data

**Delete custom data**  —  `delete_custom_data`

Delete custom user data.

Arbitrary JSON data can be stored for a User.  This API call
deletes that data for a given scope.  Without a scope, all custom_data is deleted.
See {api:UsersController#set_custom_data Store Custom Data} for details and
examples of storage and retrieval.

As an example, we'll store some data, then delete a subset of it.

Example {api:UsersController#set_custom_data PUT} with valid JSON data:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -X PUT \
    -F 'ns=com.my-organization.canvas-app' \
    -F 'data[fruit][apple]=so tasty' \
    -F 'data[fruit][kiwi]=a bit sour' \
    -F 'data[veggies][root][onion]=tear-jerking' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "fruit": {
        "apple": "so tasty",
        "kiwi": "a bit sour"
      },
      "veggies": {
        "root": {
          "onion": "tear-jerking"
        }
      }
    }
  }

Example DELETE:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \
    -X DELETE \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "a bit sour"
  }

Example {api:UsersController#get_custom_data GET} following the above DELETE:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "fruit": {
        "apple": "so tasty"
      },
      "veggies": {
        "root": {
          "onion": "tear-jerking"
        }
      }
    }
  }

Note that hashes left empty after a DELETE will get removed from the custom_data store.
For example, following the previous commands, if we delete /custom_data/veggies/root/onion,
then the entire /custom_data/veggies scope will be removed.

Example DELETE that empties a parent scope:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \
    -X DELETE \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": "tear-jerking"
  }

Example {api:UsersController#get_custom_data GET} following the above DELETE:
  curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
    -X GET \
    -F 'ns=com.my-organization.canvas-app' \
    -H 'Authorization: Bearer <token>'

Response:
  !!!javascript
  {
    "data": {
      "fruit": {
        "apple": "so tasty"
      }
    }
  }

On success, this endpoint returns an object containing the data that was deleted.

Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
or if the specified scope does not contain any data.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `ns` | string | query | yes | The namespace from which to delete the data.  This should be something other Canvas API apps aren't likely to use, such as a reverse DNS for your organization. |

**Returns:** `void`

## GET /v1/users/self/course_nicknames

**List course nicknames**  —  `list_course_nicknames`

Returns all course nicknames you have set.

**Returns:** `array[CourseNickname]`

## GET /v1/users/self/course_nicknames/{course_id}

**Get course nickname**  —  `get_course_nickname`

Returns the nickname for a specific course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `CourseNickname`

## PUT /v1/users/self/course_nicknames/{course_id}

**Set course nickname**  —  `set_course_nickname`

Set a nickname for the given course. This will replace the course's name
in output of API calls you make subsequently, as well as in selected
places in the Canvas web user interface.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `nickname` | string | form | yes | The nickname to set.  It must be non-empty and shorter than 60 characters. |

**Returns:** `CourseNickname`

## DELETE /v1/users/self/course_nicknames/{course_id}

**Remove course nickname**  —  `remove_course_nickname`

Remove the nickname for the given course.
Subsequent course API calls will return the actual name for the course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `CourseNickname`

## DELETE /v1/users/self/course_nicknames

**Clear course nicknames**  —  `clear_course_nicknames`

Remove all stored course nicknames.

**Returns:** `void`


---

# Models


## UserDisplay

This mini-object is used for secondary user responses, when we just want to provide enough information to display a user.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | The ID of the user. e.g. `2` |
| `short_name` | string |  | A short name the user has selected, for use in conversations or other less formal places through the site. e.g. `Shelly` |
| `avatar_image_url` | string |  | If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar. e.g. `https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g` |
| `html_url` | string |  | URL to access user, either nested to a context or directly. e.g. `https://school.instructure.com/courses/:course_id/users/:user_id` |


## AnonymousUserDisplay

This mini-object is returned in place of UserDisplay when returning student data for anonymous assignments, and includes an anonymous ID to identify a user within the scope of a single assignment.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `anonymous_id` | string |  | A unique short ID identifying this user within the scope of a particular assignment. e.g. `xn29Q` |
| `avatar_image_url` | string |  | A URL to retrieve a generic avatar. e.g. `https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g` |
| `display_name` | string |  | The anonymized display name for the student. e.g. `Student 2` |


## User

A Canvas user, e.g. a student, teacher, administrator, observer, etc.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the user. e.g. `2` |
| `name` | string |  | The name of the user. e.g. `Sheldon Cooper` |
| `sortable_name` | string |  | The name of the user that is should be used for sorting groups of users, such as in the gradebook. e.g. `Cooper, Sheldon` |
| `last_name` | string |  | The last name of the user. e.g. `Cooper` |
| `first_name` | string |  | The first name of the user. e.g. `Sheldon` |
| `short_name` | string |  | A short name the user has selected, for use in conversations or other less formal places through the site. e.g. `Shelly` |
| `sis_user_id` | string |  | The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. e.g. `SHEL93921` |
| `sis_import_id` | integer (int64) |  | The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information. e.g. `18` |
| `integration_id` | string |  | The integration_id associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. e.g. `ABC59802` |
| `login_id` | string |  | The unique login id for the user.  This is what the user uses to log in to Canvas. e.g. `sheldon@caltech.example.com` |
| `avatar_url` | string |  | If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar. e.g. `https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g` |
| `avatar_state` | string |  | Optional: If avatars are enabled and caller is admin, this field can be requested and will contain the current state of the user's avatar. e.g. `approved` |
| `enrollments` | array[Enrollment] |  | Optional: This field can be requested with certain API calls, and will return a list of the users active enrollments. See the List enrollments API for more details about the format of these records. |
| `email` | string |  | Optional: This field can be requested with certain API calls, and will return the users primary email address. e.g. `sheldon@caltech.example.com` |
| `locale` | string |  | Optional: This field can be requested with certain API calls, and will return the users locale in RFC 5646 format. e.g. `tlh` |
| `last_login` | string (date-time) |  | Optional: This field is only returned in certain API calls, and will return a timestamp representing the last time the user logged in to canvas. e.g. `2012-05-30T17:45:25Z` |
| `time_zone` | string |  | Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone. e.g. `America/Denver` |
| `bio` | string |  | Optional: The user's bio. e.g. `I like the Muppets.` |
| `pronouns` | string |  | Optional: This field is only returned if pronouns are enabled, and will return the pronouns of the user. e.g. `he/him` |


## Profile

Profile details for a Canvas user.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the user. e.g. `1234` |
| `name` | string |  | Sample User e.g. `Sample User` |
| `short_name` | string |  | Sample User e.g. `Sample User` |
| `sortable_name` | string |  | user, sample e.g. `user, sample` |
| `title` | string |  |  |
| `bio` | string |  |  |
| `pronunciation` | string |  | Name pronunciation e.g. `Sample name pronunciation` |
| `primary_email` | string |  | sample_user@example.com e.g. `sample_user@example.com` |
| `login_id` | string |  | sample_user@example.com e.g. `sample_user@example.com` |
| `sis_user_id` | string |  | sis1 e.g. `sis1` |
| `lti_user_id` | string |  |  |
| `avatar_url` | string |  | The avatar_url can change over time, so we recommend not caching it for more than a few hours e.g. `..url..` |
| `calendar` | CalendarLink |  |  |
| `time_zone` | string |  | Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone. e.g. `America/Denver` |
| `locale` | string |  | The users locale. |
| `k5_user` | boolean |  | Optional: Whether or not the user is a K5 user. This field is nil if the user settings are not for the user making the request. e.g. `True` |
| `use_classic_font_in_k5` | boolean |  | Optional: Whether or not the user should see the classic font on the dashboard. Only applies if k5_user is true. This field is nil if the user settings are not for the user making the request. e.g. `False` |


## Avatar

Possible avatar for a user.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `type` | string | yes | ['gravatar'\|'attachment'\|'no_pic'] The type of avatar record, for categorization purposes. e.g. `gravatar` |
| `url` | string | yes | The url of the avatar e.g. `https://secure.gravatar.com/avatar/2284...` |
| `token` | string | yes | A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client. e.g. `<opaque_token>` |
| `display_name` | string | yes | A textual description of the avatar record. e.g. `user, sample` |
| `id` | integer |  | ['attachment' type only] the internal id of the attachment e.g. `12` |
| `content-type` | string |  | ['attachment' type only] the content-type of the attachment. e.g. `image/jpeg` |
| `filename` | string |  | ['attachment' type only] the filename of the attachment e.g. `profile.jpg` |
| `size` | integer |  | ['attachment' type only] the size of the attachment e.g. `32649` |


## PageView

The record of a user page view access in Canvas

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string (uuid) | yes | A UUID representing the page view.  This is also the unique request id e.g. `3e246700-e305-0130-51de-02e33aa501ef` |
| `app_name` | string |  | If the request is from an API request, the app that generated the access token e.g. `Canvas for iOS` |
| `url` | string |  | The URL requested e.g. `https://canvas.instructure.com/conversations` |
| `context_type` | string |  | The type of context for the request e.g. `Course` |
| `asset_type` | string |  | The type of asset in the context for the request, if any e.g. `Discussion` |
| `controller` | string |  | The rails controller that handled the request e.g. `discussions` |
| `action` | string |  | The rails action that handled the request e.g. `index` |
| `contributed` | boolean |  | This field is deprecated, and will always be false e.g. `false` |
| `interaction_seconds` | number |  | An approximation of how long the user spent on the page, in seconds e.g. `7.21` |
| `created_at` | datetime (iso8601) |  | When the request was made e.g. `2013-10-01T19:49:47Z` |
| `user_request` | boolean |  | A flag indicating whether the request was user-initiated, or automatic (such as an AJAX call). Not available in history CSV. e.g. `true` |
| `render_time` | number |  | How long the response took to render, in seconds. Not available in history CSV. e.g. `0.369` |
| `user_agent` | string |  | The user-agent of the browser or program that made the request e.g. `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1` |
| `participated` | boolean |  | True if the request counted as participating, such as submitting homework e.g. `false` |
| `http_method` | string |  | The HTTP method such as GET or POST e.g. `GET` |
| `remote_ip` | string |  | The origin IP address of the request e.g. `173.194.46.71` |
| `session_id` | string (uuid) |  | The session identifier for the user session that made the request e.g. `b4f5c8e0-e2f3-0130-51e0-02e33aa501ef` |
| `developer_key_id` | number |  | The ID of the developer key that authorized the API request, if applicable e.g. `42` |
| `asset_user_access_id` | number |  | The ID of the asset (e.g. an assignment) associated with this page view, if applicable e.g. `9876` |
| `links` | PageViewLinks |  | The page view links to define the relationships e.g. `{'user': 1234, 'account': 1234}` |


## PageViewLinks

The links of a page view access in Canvas

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `user` | integer (int64) |  | The ID of the user for this page view e.g. `1234` |
| `context` | integer (int64) |  | The ID of the context for the request (course id if context_type is Course, etc) e.g. `1234` |
| `asset` | integer (int64) |  | The ID of the asset for the request, if any. Not available in history CSV. e.g. `1234` |
| `real_user` | integer (int64) |  | The ID of the actual user who made this request, if the request was made by a user who was masquerading e.g. `1234` |
| `account` | integer (int64) |  | The ID of the account context for this page view e.g. `1234` |


## AsyncApiErrorResponse

Error response structure returned by the API when validation or processing failures occur

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `errors` | array[string] |  | Array of error messages describing what went wrong with the request e.g. `['start_date and end_date must be the first day of the month', 'end_date must be after start_date', 'end_date cannot be in a future month', 'The requested data cannot be older than %d months']` |


## AsyncQueryResponse

Response returned when successfully initiating a page views query

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `poll_url` | string (uri) | yes | URL endpoint to poll for query status updates e.g. `/api/v1/users/123/page_views/query/550e8400-e29b-41d4-a716-446655440000` |


## AsyncQueryStatusResponse

Response containing the current status of a page views query

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `query_id` | string (uuid) | yes | The UUID of the query being polled e.g. `550e8400-e29b-41d4-a716-446655440000` |
| `status` | string | yes | Current processing status of the query e.g. `finished` Allowed: `queued`, `processing`, `finished`, `failed` |
| `format` | string | yes | The format that results will be returned in e.g. `csv` Allowed: `csv`, `json` |
| `results_url` | string (uri) |  | URL to retrieve query results. Only present when status is 'finished' e.g. `/api/v1/users/123/page_views/query/550e8400-e29b-41d4-a716-446655440000/results` |
| `error_code` | string |  | Error code indicating the reason for query failure, if applicable e.g. `RESULT_SIZE_LIMIT_EXCEEDED` |


## AsyncQueryResultsResponse

File download response containing page views query results

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `content` | string (binary) |  | The query results data in the requested format (CSV or JSON) |
| `filename` | string |  | Suggested filename for the downloaded results e.g. `550e8400-e29b-41d4-a716-446655440000.csv` |
| `content_type` | string |  | MIME type of the response content e.g. `text/csv` Allowed: `text/csv`, `application/jsonl` |
| `content_encoding` | string |  | Content encoding if the response is compressed e.g. `gzip` |


## CourseNickname

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `course_id` | integer |  | the ID of the course e.g. `88` |
| `name` | string |  | the actual name of the course e.g. `S1048576 DPMS1200 Intro to Newtonian Mechanics` |
| `nickname` | string |  | the calling user's nickname for the course e.g. `Physics` |
