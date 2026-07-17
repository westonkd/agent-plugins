# Canvas LMS — Account & Course Permissions (RBAC)

Each Canvas role permission, what it enables, and its dependencies. `grep -i <permission>` to jump to one. Permission keys match the `manage_*` / `view_*` names used by the Roles API.

## Overview: account-level vs course-level permissions

This document lists permissions that can be granted to account- and course-level roles in Canvas.

## For Account-level roles only

| Key | Permission |
| --- | --- |
| `access_oak` | IgniteAI Agent - Admins |
| `become_user` | Users - act as |
| `import_sis` | SIS Data - import |
| `manage_account_memberships` | Admins - add / remove |
| `manage_account_settings` | Account-level settings - manage |
| `manage_alerts` | Global Announcements - add / edit / delete |
| `manage_catalog` | Catalog - manage |
| `manage_data_services` | Data Services - manage |
| `manage_developer_keys` | Developer Keys - manage |
| `manage_dsr_requests` | Users - create DSR export |
| `manage_feature_flags` | Feature Options - enable / disable |
| `manage_frozen_assignments` | Manage (edit / delete) frozen assignments |
| `manage_impact` | Impact - Manage |
| `manage_lti_registrations` | LTI Registrations - Manage |
| `manage_master_courses` | Blueprint Courses - add / edit / associate / delete |
| `manage_role_overrides` | Permissions - manage |
| `manage_sis` | SIS Data - manage |
| `manage_storage_quotas` | Storage Quotas - manage |
| `manage_user_logins` | Users - manage login details |
| `manage_user_observers` | Users - manage observers |
| `manage_users_in_bulk` | Bulk actions - people page |
| `moderate_user_content` | Users - moderate content |
| `new_quizzes_view_ip_address` | New Quizzes - view IP address |
| `read_course_content` | Course Content - view |
| `read_course_list` | Courses - view list |
| `reset_any_mfa` | Reset Multi-Factor Authentication |
| `undelete_courses` | Courses - undelete |
| `view_admin_analytics` | Admin Analytics - view and export data |
| `view_analytics_hub` | Analytics Hub |
| `view_course_changes` | Courses - view change logs |
| `view_feature_flags` | Feature Options - view |
| `view_grade_changes` | Grades - view change logs |
| `view_notifications` | Notifications - view |
| `view_quiz_answer_audits` | Quizzes - view submission log |
| `view_statistics` | Statistics - view |

### Automation Rules

| Key | Permission |
| --- | --- |
| `manage_rules_add` | Automation Rules - add |
| `manage_rules_delete` | Automation Rules - delete |
| `manage_rules_edit` | Automation Rules - edit |
| `manage_rules_view` | Automation Rules - view |

### Intelligent Insights

| Key | Permission |
| --- | --- |
| `manage_ask_questions_analytics_context` | Ask Your Data's Context Library - modify |
| `view_accessibility_insights` | Accessibility Insights |
| `view_ask_questions_analytics` | Ask Your Data - use |
| `view_ask_questions_pinboards` | Pinboards - view |
| `view_course_readiness` | Course Readiness |
| `view_rsi_report` | Regular and Substantive Interaction |
| `view_students_in_need` | Students in Need of Attention |
| `view_title_iv_financial_aid_report` | Title IV Financial Aid Report |

### Manage Account Calendars

| Key | Permission |
| --- | --- |
| `manage_account_calendar_events` | Account Calendars - add / edit / delete events |
| `manage_account_calendar_visibility` | Account Calendars - change visibility |

### Manage Course Templates

| Key | Permission |
| --- | --- |
| `add_course_template` | Course Templates - create |
| `delete_course_template` | Course Templates - delete |
| `edit_course_template` | Course Templates - edit |

### Manage Courses

| Key | Permission |
| --- | --- |
| `manage_courses_add` | Courses - add |
| `manage_courses_admin` | Courses - manage / update |

### Manage Institutional Tags

| Key | Permission |
| --- | --- |
| `manage_institutional_tags_create` | Institutional Tags - create |
| `manage_institutional_tags_edit` | Institutional Tags - edit |
| `manage_institutional_tags_view` | Institutional Tags - view |

### Users - Manage Access Tokens

| Key | Permission |
| --- | --- |
| `create_access_tokens` | Access Tokens - create / update |
| `delete_access_tokens` | Access Tokens - delete |
| `view_user_generated_access_tokens` | Manually Generated Access Tokens - view |

### Users - Temporary Enrollments

| Key | Permission |
| --- | --- |
| `temporary_enrollments_add` | Temporary Enrollments - add |
| `temporary_enrollments_delete` | Temporary Enrollments - delete |
| `temporary_enrollments_edit` | Temporary Enrollments - edit |

## For both Account-level and Course-level roles

Note: Applicable enrollment types for course-level roles are given in brackets: S = student, T = teacher (instructor), A = TA, D = designer, O = observer. Lower-case letters indicate permissions that are off by default. A missing letter indicates the permission cannot be enabled for the role or any derived custom roles.

| Key | Available To | Permission |
| --- | --- | --- |
| `access_oak_teacher` | `TaD` | IgniteAI Agent - Faculty & Support |
| `allow_course_admin_actions` | `Tad` | Users - allow administrative actions in courses |
| `apply_default_discussion_options` | `T` | Discussions - apply default options |
| `block_editor_global_template_editor` | `t d` | Block Editor Global Templates - edit |
| `block_editor_template_editor` | `t d` | Block Editor Templates - edit |
| `create_collaborations` | `STADo` | Student Collaborations - create |
| `create_conferences` | `STADo` | Web Conferences - create |
| `create_forum` | `STADo` | Discussions - create |
| `edit_discussion_anonymity` | `T` | Discussions - edit anonymous discussion |
| `edit_discussion_options` | `T` | Discussions - edit options |
| `edit_discussion_views` | `T` | Discussions - edit view |
| `generate_observer_pairing_code` | `tado` | Users - generate observer pairing codes for students |
| `import_outcomes` | `TaDo` | Learning Outcomes - import |
| `manage_account_banks` | `t d` | Item Banks - manage account |
| `manage_calendar` | `sTADo` | Course Calendar - add / edit / delete |
| `manage_course_details` | `TaD` | Manage Course Details |
| `manage_course_feature_options` | `TaD` | Manage Course Feature Options |
| `manage_course_navigation` | `TaD` | Manage Course Navigation |
| `manage_course_visibility` | `TAD` | Courses - change visibility |
| `manage_grades` | `TA` | Grades - edit |
| `manage_interaction_alerts` | `Ta` | Alerts - add / edit / delete |
| `manage_nav_menu_links` | `tad` | Custom Links - manage |
| `manage_outcomes` | `sTaDo` | Learning Outcomes - add / edit / delete |
| `manage_proficiency_calculations` | `t d` | Outcome Proficiency Calculations - add / edit |
| `manage_proficiency_scales` | `t d` | Outcome Mastery Scales - add / edit |
| `manage_rubrics` | `TAD` | Rubrics - add / edit / delete |
| `manage_students` | `TAD` | Users - manage students in courses |
| `moderate_forum` | `sTADo` | Discussions - moderate |
| `new_quizzes_multiple_session_detection` | `t` | New Quizzes - view multi session information |
| `post_to_forum` | `STADo` | Discussions - post |
| `proxy_assignment_submission` | `ta` | Submission - Submit on behalf of student |
| `read_announcements` | `STADO` | Announcements - view |
| `read_email_addresses` | `sTAdo` | Users - view primary email address |
| `read_forum` | `STADO` | Discussions - view |
| `read_question_banks` | `TADo` | Question banks - view and link |
| `read_reports` | `TAD` | Reports - manage |
| `read_roster` | `STADo` | Users - view list |
| `read_sis` | `sTa` | SIS Data - read |
| `select_final_grade` | `TA` | Grades - select final grade for moderation |
| `send_messages` | `STADo` | Conversations - send messages to individual course members |
| `send_messages_all` | `sTADo` | Conversations - send messages to entire class |
| `share_banks_with_subaccounts` | `tad` | Item Banks - share with subaccounts |
| `view_all_grades` | `TAd` | Grades - view all grades |
| `view_audit_trail` | `t` | Grades - view audit trail |
| `view_group_pages` | `sTADo` | Groups - view all student groups |
| `view_students_in_need_in_course` | `Ta` | Intelligent Insights - Students in Need of Attention - Course Level |
| `view_user_logins` | `TA` | Users - view login IDs |

### Manage Assignments and Quizzes

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_assignments_add` | `TADo` | Assignments and Quizzes - add |
| `manage_assignments_delete` | `TADo` | Assignments and Quizzes - delete |
| `manage_assignments_edit` | `TADo` | Assignments and Quizzes - edit |

### Manage Course Content

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_course_content_add` | `TADo` | Course Content - add |
| `manage_course_content_delete` | `TADo` | Course Content - delete |
| `manage_course_content_edit` | `TADo` | Course Content - edit |

### Manage Course Files

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_files_add` | `TADo` | Course Files - add |
| `manage_files_delete` | `TADo` | Course Files - delete |
| `manage_files_edit` | `TADo` | Course Files - edit |

### Manage Course Sections

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_sections_add` | `TaD` | Course Sections - add |
| `manage_sections_delete` | `TaD` | Course Sections - delete |
| `manage_sections_edit` | `TaD` | Course Sections - edit |

### Manage Courses

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_courses_conclude` | `TaD` | Courses - conclude |
| `manage_courses_delete` | `t d` | Courses - delete |
| `manage_courses_publish` | `TaD` | Courses - publish |
| `manage_courses_reset` | `t d` | Courses - reset |
| `view_archived_courses` | `t d` | Courses - view archived |

### Manage Differentiation Tags

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_tags_add` | `Tad` | Differentiation Tags - add |
| `manage_tags_delete` | `Tad` | Differentiation Tags - delete |
| `manage_tags_manage` | `Tad` | Differentiation Tags - manage |

### Manage Groups

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_groups_add` | `TAD` | Groups - add |
| `manage_groups_delete` | `TAD` | Groups - delete |
| `manage_groups_manage` | `TAD` | Groups - manage |

### Manage LTI

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_lti_add` | `TAD` | LTI - add |
| `manage_lti_delete` | `TAD` | LTI - delete |
| `manage_lti_edit` | `TAD` | LTI - edit |

### Manage Pages

| Key | Available To | Permission |
| --- | --- | --- |
| `manage_wiki_create` | `TADo` | Pages - create |
| `manage_wiki_delete` | `TADo` | Pages - delete |
| `manage_wiki_update` | `TADo` | Pages - update |

### Users - Designers

| Key | Available To | Permission |
| --- | --- | --- |
| `add_designer_to_course` | `Tad` | Designers - add |
| `remove_designer_from_course` | `Tad` | Designers - remove |

### Users - Observers

| Key | Available To | Permission |
| --- | --- | --- |
| `add_observer_to_course` | `TAD` | Observers - add |
| `remove_observer_from_course` | `TAD` | Observers - remove |

### Users - Students

| Key | Available To | Permission |
| --- | --- | --- |
| `add_student_to_course` | `TAD` | Students - add |
| `remove_student_from_course` | `TAD` | Students - remove |

### Users - TAs

| Key | Available To | Permission |
| --- | --- | --- |
| `add_ta_to_course` | `Tad` | TAs - add |
| `remove_ta_from_course` | `Tad` | TAs - remove |

### Users - Teachers

| Key | Available To | Permission |
| --- | --- | --- |
| `add_teacher_to_course` | `Tad` | Teachers - add |
| `remove_teacher_from_course` | `Tad` | Teachers - remove |

## Index

- **`access_oak`** — IgniteAI Agent - Admins
- **`access_oak_teacher`** — IgniteAI Agent - Faculty & Support
- **`allow_course_admin_actions`** — Users - allow administrative actions in courses
- **`apply_default_discussion_options`** — Discussions - apply default options
- **`become_user`** — Users - act as
- **`block_editor_global_template_editor`** — Block Editor Global Templates - edit
- **`block_editor_template_editor`** — Block Editor Templates - edit
- **`create_access_tokens`** — Access Tokens - create / update
- **`create_collaborations`** — Student Collaborations - create
- **`create_conferences`** — Web Conferences - create
- **`create_forum`** — Discussions - create
- **`delete_access_tokens`** — Access Tokens - delete
- **`edit_discussion_anonymity`** — Discussions - edit anonymous discussion
- **`edit_discussion_options`** — Discussions - edit options
- **`edit_discussion_views`** — Discussions - edit view
- **`generate_observer_pairing_code`** — Users - generate observer pairing codes for students
- **`import_outcomes`** — Learning Outcomes - import
- **`import_sis`** — SIS Data - import
- **`manage_account_banks`** — Item Banks - manage account
- **`manage_account_calendar`** — Manage Account Calendars
- **`manage_account_memberships`** — Admins - add / remove
- **`manage_account_settings`** — Account-level settings - manage
- **`manage_alerts`** — Global Announcements - add / edit / delete
- **`manage_ask_questions_analytics_context`** — Ask Your Data's Context Library - modify
- **`manage_assignments_and_quizzes`** — Manage Assignments and Quizzes
- **`manage_calendar`** — Course Calendar - add / edit / delete
- **`manage_course_content`** — Manage Course Content
- **`manage_course_designer_enrollments`** — Users - Designers
- **`manage_course_details`** — Manage Course Details
- **`manage_course_feature_options`** — Manage Course Feature Options
- **`manage_course_navigation`** — Manage Course Navigation
- **`manage_course_observer_enrollments`** — Users - Observers
- **`manage_course_student_enrollments`** — Users - Students
- **`manage_course_ta_enrollments`** — Users - TAs
- **`manage_course_teacher_enrollments`** — Users - Teachers
- **`manage_course_templates`** — Manage Course Templates
- **`manage_course_visibility`** — Courses - change visibility
- **`manage_courses`** — Manage Courses
- **`manage_data_services`** — Data Services - manage
- **`manage_developer_keys`** — Developer Keys - manage
- **`manage_differentiation_tags`** — Manage Differentiation Tags
- **`manage_dsr_requests`** — Users - create DSR export
- **`manage_feature_flags`** — Feature Options - enable / disable
- **`manage_files`** — Manage Course Files
- **`manage_grades`** — Grades - edit
- **`manage_groups`** — Manage Groups
- **`manage_impact`** — Impact - Manage
- **`manage_institutional_tags`** — Manage Institutional Tags
- **`manage_institutional_tags_create`** — Institutional Tags - create
- **`manage_institutional_tags_edit`** — Institutional Tags - edit
- **`manage_institutional_tags_view`** — Institutional Tags - view
- **`manage_interaction_alerts`** — Alerts - add / edit / delete
- **`manage_lti`** — Manage LTI
- **`manage_lti_registrations`** — LTI Registrations - Manage
- **`manage_master_courses`** — Blueprint Courses - add / edit / associate / delete
- **`manage_nav_menu_links`** — Custom Links - manage
- **`manage_outcomes`** — Learning Outcomes - add / edit / delete
- **`manage_proficiency_calculations`** — Outcome Proficiency Calculations - add / edit
- **`manage_proficiency_scales`** — Outcome Mastery Scales - add / edit
- **`manage_rate_limiting`** — Site Admin - Rate Limiting
- **`manage_role_overrides`** — Permissions - manage
- **`manage_rubrics`** — Rubrics - add / edit / delete
- **`manage_rules`** — Automation Rules
- **`manage_rules_add`** — Automation Rules - add
- **`manage_rules_delete`** — Automation Rules - delete
- **`manage_rules_edit`** — Automation Rules - edit
- **`manage_rules_view`** — Automation Rules - view
- **`manage_sections`** — Manage Course Sections
- **`manage_sis`** — SIS Data - manage
- **`manage_storage_quotas`** — Storage Quotas - manage
- **`manage_students`** — Users - manage students in courses
- **`manage_tags_add`** — Differentiation Tags - add
- **`manage_tags_delete`** — Differentiation Tags - delete
- **`manage_tags_manage`** — Differentiation Tags - manage
- **`manage_temporary_enrollments`** — Users - Temporary Enrollments
- **`manage_user_logins`** — Users - manage login details
- **`manage_user_observers`** — Users - manage observers
- **`manage_users_in_bulk`** — Bulk actions - people page
- **`manage_wiki`** — Manage Pages
- **`moderate_forum`** — Discussions - moderate
- **`moderate_user_content`** — Users - moderate content
- **`modify_site_admin_developer_keys`** — Developer Keys - modify Site Admin developer keys
- **`new_quizzes_multiple_session_detection`** — New Quizzes - view multi session information
- **`new_quizzes_view_ip_address`** — New Quizzes - view IP address
- **`post_to_forum`** — Discussions - post
- **`proxy_assignment_submission`** — Submission - Submit on behalf of student
- **`read_announcements`** — Announcements - view
- **`read_course_content`** — Course Content - view
- **`read_course_list`** — Courses - view list
- **`read_email_addresses`** — Users - view primary email address
- **`read_forum`** — Discussions - view
- **`read_question_banks`** — Question banks - view and link
- **`read_reports`** — Reports - manage
- **`read_roster`** — Users - view list
- **`read_sis`** — SIS Data - read
- **`select_final_grade`** — Grades - select final grade for moderation
- **`send_messages`** — Conversations - send messages to individual course members
- **`send_messages_all`** — Conversations - send messages to entire class
- **`share_banks_with_subaccounts`** — Item Banks - share with subaccounts
- **`undelete_courses`** — Courses - undelete
- **`users_manage_access_tokens`** — Users - Manage Access Tokens
- **`view_admin_analytics`** — Admin Analytics - view and export data
- **`view_all_grades`** — Grades - view all grades
- **`view_analytics_hub`** — Analytics Hub
- **`view_ask_questions_analytics`** — Ask Your Data - use
- **`view_ask_questions_pinboards`** — Pinboards - view
- **`view_audit_trail`** — Grades - view audit trail
- **`view_course_changes`** — Courses - view change logs
- **`view_course_readiness`** — Course Readiness
- **`view_feature_flags`** — Feature Options - view
- **`view_grade_changes`** — Grades - view change logs
- **`view_group_pages`** — Groups - view all student groups
- **`view_notifications`** — Notifications - view
- **`view_quiz_answer_audits`** — Quizzes - view submission log
- **`view_rsi_report`** — Regular and Substantive Interaction
- **`view_statistics`** — Statistics - view
- **`view_students_in_need`** — Students in Need of Attention
- **`view_title_iv_financial_aid_report`** — Title IV Financial Aid Report
- **`view_user_generated_access_tokens`** — Manually Generated Access Tokens - view
- **`view_user_logins`** — Users - view login IDs

---


## `access_oak` — IgniteAI Agent - Admins

## What it Does

### IgniteAI Agent - Admins

Allows user to access the IgniteAI Agent for Canvas LMS.

## Additional Considerations

### IgniteAI Agent - Admins

The IgniteAI Agent feature flag must be enabled for the account to assign this permission.

## `access_oak_teacher` — IgniteAI Agent - Faculty & Support

## What it Does

### IgniteAI Agent - Faculty & Support

Allows user to access the IgniteAI Agent for Canvas LMS.

## Additional Considerations

### IgniteAI Agent - Faculty & Support

The IgniteAI Agent feature flag must be enabled for the account to assign this permission.

## `allow_course_admin_actions` — Users - allow administrative actions in courses

## What it Does

### People (Course)

Allows user to view login ID information for users.

Allows user to view user details for course users.

Allows user to edit a user’s section or role (if not added via SIS).

## Additional Considerations

### People (Account)

To edit user details, modify login details, or change user passwords, Users - manage login details must also be enabled.

### People (Course)

To view the People page, Courses - view list must be enabled.

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

To view SIS IDs, SIS Data - read must be enabled.

To edit a user’s section, Conversations - send to individual course members must be enabled.

### Observers (Course)

To link an observer to a student, Users - manage login details and Conversations - send to individual course members must be enabled.

To generate a pairing code on behalf of a student to share with an observer, Users - Generate observer pairing code for students must also be enabled.

## `apply_default_discussion_options` — Discussions - apply default options

## What it Does

### Discussions - apply default options

Allows the user to toggle whether or not a newly created discussion will have the selected default options applied to it.

## Additional Considerations

Importing a Discussion via the 'Import Course Content' feature will keep its original options selected.

## `become_user` — Users - act as

## What it Does

### People (Account)

Allows user to act as other users in the account.

This permission should only be assigned to users that your institution has authorized to act as other users in your entire Canvas account.

Users with this permission may be able to use the Act as feature to manage account settings, view and adjust grades, access user information, etc.

### Student Context Card

Allows user to access the Act as User link on student context cards.

### SpeedGrader

Allows user to delete a submission file.

### People (Course)

Allows user to view Login IDs in a course People page.

## Additional Considerations

### API

The Roles API refers to this permission as become_user.

### People (Account)

To view the list of users in an account, Users - view list must be enabled.

### Student Context Card

Student Context Cards must be enabled for an account by an admin.

### Subaccounts

Not available at the subaccount level.

## `block_editor_global_template_editor` — Block Editor Global Templates - edit

## What it Does

### Block Editor Templates - global edit

Allows user to create and edit global templates from within the Block Editor.

## `block_editor_template_editor` — Block Editor Templates - edit

## What it Does

### Block Editor Templates - edit

Allows user to create and edit templates from within the Block Editor.

## `create_access_tokens` — Access Tokens - create / update

## What it Does

### Access Tokens

Allows user to create and update other user's access tokens.

## Additional Considerations

### Subaccounts

Not available at the subaccount level

## `create_collaborations` — Student Collaborations - create

## What it Does

### Collaborations

Allows user to create collaborations.

Allows user to view, edit, and delete collaborations they created.

## Additional Considerations

### Collaborations

To allow view edit delete functionality of collaborations created by other users, Course Content - add / edit / delete must also be enabled.

If Course Content - add / edit / delete is enabled and Student Collaborations - create is disabled, the user will not be able to create new collaborations but will be able to view edit delete all collaborations.

To add students to a collaboration, Users - view list must also be enabled.

To add a course group to a collaboration, Groups - add must also be enabled.

## `create_conferences` — Web Conferences - create

## What it Does

### Conferences

Allows user to create new conferences in courses and groups.

Allows user to start conferences they created.

## Additional Considerations

### Conferences

To allow full management of conferences created by the user or others, the Course Content permission must also be enabled.

To end a long-running conference, the Course Content permission must be enabled.

If the Course Content permission enabled and Web Conferences - create is disabled, the user can still manage conferences.

## `create_forum` — Discussions - create

## What it Does

### Discussions

Allows user to add discussions in the Discussions page.

## Additional Considerations

### Announcements

To create announcements, Discussions - moderate must also be enabled.

### Discussions

To view discussions in a course, Discussions - view must be enabled.

Both Discussions - create and Discussions - moderate allow the user to create a discussion in the Discussions page.

To manage discussions, Discussions - moderate must also be enabled.

## `delete_access_tokens` — Access Tokens - delete

## What it Does

### Access Tokens

Allows user to delete other user's access tokens.

## Additional Considerations

### Subaccounts

Not available at the subaccount level

## `edit_discussion_anonymity` — Discussions - edit anonymous discussion

## What it Does

### Discussions - edit anonymous discussion

Allows the user to edit anonymous discussion settings.

## `edit_discussion_options` — Discussions - edit options

## What it Does

### Discussions - edit options

Allows the user to edit discussion options (threaded replies, podcast, liking, etc.).

## `edit_discussion_views` — Discussions - edit view

## What it Does

### Discussions - edit view

Allows the user to edit discussion view settings (sort order, thread state).

## `generate_observer_pairing_code` — Users - generate observer pairing codes for students

## What it Does

### People (Course)

Allows user to generate a pairing code on behalf of a student to share with an observer.

## Additional Considerations

### People (Course)

To generate a pairing code from a student`s User Settings page, the User - act as permission must also be enabled.

To generate a pairing code from a student`s User Details page, the Users - allow administrative actions in courses permission must also be enabled.

Pairing codes are only supported when self registration is enabled for the account.

QR codes are not the same as pairing codes and are only used to help users log into their own accounts via the Canvas mobile apps. To disable QR code logins for all users in your account, please contact your Customer Success Manager.

## `import_outcomes` — Learning Outcomes - import

## What it Does

### Outcomes

Allows user to import account learning outcomes.

## `import_sis` — SIS Data - import

## What it Does

### Account Navigation

Determines visibility and management of SIS Import link in Account Navigation.

### SIS Import

Allows user to import SIS data.

## Additional Considerations

### SIS Import

To manage SIS data, SIS Data - manage must also be enabled.

### Subaccounts

Not available at the subaccount level

## `manage_account_banks` — Item Banks - manage account

## What it Does

### Item Banks

Allows a user to view and manage all item banks in an account directly from within a course and account.

## Additional Considerations

### Item Banks

This permission must be disabled for users to only view item banks created by them, shared with them from another user, or shared indirectly via the course they are enrolled in as an instructor.

## `manage_account_calendar` — Manage Account Calendars

## What it Does

### Account Calendars - add / edit / delete events

Allows user to add, edit, and delete events in account calendars.

### Account Calendars - change visibility

Allows user to change visibility of account calendars.

## Additional Considerations

### Account Calendars

Even with the Account Calendars - add / edit / delete events permission enabled, events can only be created in account calendars that are visible.

## `manage_account_memberships` — Admins - add / remove

## What it Does

### Account Settings

Allows user to add and remove other account admins.

### Commons

Allows user to access and edit the Admin settings in Commons.

Allows user to create and manage Groups. Allows user to manage shared resources in the account.

Allows user to manage shared resources in the account.

## `manage_account_settings` — Account-level settings - manage

## What it Does

### Account Settings

Allows user to view and manage the Settings and Notifications tabs in Account Settings.

### Authentication

Allows user to view and manage authentication options for the whole account.

### Subaccounts

Allows user to view and manage subaccounts for the account.

### Terms

Allows user to view and manage terms for the account.

### Theme Editor

Allows user to access the Theme Editor.

## Additional Considerations

### Announcements

The Announcements tab is always visible to admins; however, to manage announcements, Global Announcements - add / edit / delete must also be enabled.

### Feature Options (Account Settings)

To manage the Feature Options tab, Feature Options - enable disable - must also be enabled.

### Reports (Account Settings)

To view the Reports tab, Reports - manage must also be enabled.

### Subaccount Navigation (Account Settings)

Not all settings options are available at the subaccount level, including the Notifications tab.

## `manage_alerts` — Global Announcements - add / edit / delete

## What it Does

### Announcements (Account)

Allows user to add, edit, and delete global announcements.

## `manage_ask_questions_analytics_context` — Ask Your Data's Context Library - modify

## What it Does

### Account Settings

Allows Ask Your Data users to access and modify the product's Context Library feature, to influence and tailor AI responses for all users.

### Subaccounts

Not available at the subaccount level.

## Additional Considerations

### Account Settings

Requires Ask Your Data permission to use.

## `manage_assignments_and_quizzes` — Manage Assignments and Quizzes

## What it Does

### Assignments and Quizzes - add

Allows user to add assignments in a course.

Allows user to add assignment groups in a course.

Allows user to duplicate assignments in a course.

Allows user to add new assignments to a module.

Allows user to add new question banks to a course or account.

Allows user to add new questions to new or existing question banks in a course or account.

Allows user to add quizzes in a course.

Allows user to duplicate quizzes in a course.

### Assignments and Quizzes - edit

Allows user to edit and publish/unpublish assignments.

Allows user to manage assignment settings.

Allows user to weight assignment groups.

Allows user to edit lock settings on the Assignments and Quizzes index pages.

Allows user to share an assignment to Commons.

Allows user to share a quiz to Commons.

Determines visibility and management of the Question Banks link in Account Navigation.

Allows user to edit and publish/unpublish quizzes.

Allows user to edit question banks in a course or account.

### Assignments and Quizzes - delete

Allows user to delete assignments in a course.

Allows user to delete assignment groups in a course.

Allows user to delete quizzes in a course.

Allows user to delete question banks in a course or account.

## Additional Considerations

### Assignments

To access the Assignments Index Page, Course Content - view must be enabled.

To differentiate assignments to individual students, Users - view list must also be enabled.

### Blueprint Courses

To edit lock settings from the Assignments index page, Blueprint Courses - add / edit / associate / delete and Courses - manage must also be enabled.

If Blueprint Courses - add / edit / associate / delete and Courses - manage are enabled, but Assignments and Quizzes - edit is not enabled, blueprint lock settings for an assignment can be managed from the assignment’s details page.

To edit lock settings on an individual quiz, or on the Quizzes index page, Blueprint Courses - add / edit / associate / delete and Courses - manage must also be enabled.

### Course Settings

To import assignments and quizzes using the Course Import Tool, Course Content - add / edit / delete must be enabled.

### Discussions

These permissions do not manage Discussions. Discussions are managed via individual Discussion permissions.

To edit assignment details on individual discussions, Discussions - manage must also be enabled.

### Grades

To manage moderated grading, Grades - Select final grade for moderation must also be enabled.

### Quizzes

To access the Quizzes Index Page, Course Content - view must be enabled.

To moderate a quiz, Grades - edit must also be enabled.

To access item banks for a course or account, Item Banks - manage account must also be enabled.

### Rubrics

Disabling the Assignments and Quizzes - add permission will override (if enabled) the Rubrics - add / edit / delete permission, preventing user from creating rubrics for an individual assignment.

Disabling the Assignments and Quizzes - edit permission will override (if enabled) the Rubrics - add / edit / delete permission, preventing users from editing rubrics from an individual assignment.

Disabling the Assignments and Quizzes - delete permission will override (if enabled) the Rubrics - add / edit / delete permission, preventing user from deleting rubrics for an individual assignment.

## `manage_calendar` — Course Calendar - add / edit / delete

## What it Does

### Calendar

Allows user to add, edit, and delete events in the course calendar.

### Scheduler

Allows user to create and manage appointments on the calendar using Scheduler.

## Additional Considerations

### Calendar

Regardless of whether this permission is enabled or disabled, users will still be able to manage events in their personal calendar.

### Scheduler

Scheduler must be enabled for your account.

## `manage_course_content` — Manage Course Content

## What it Does

### Course Content - add

Allows user to share course items directly with other users.

Allows user to copy individual course items to another course.

Allows user to view course copy status.

Allows user to create content migrations.

Allows user to create blackout dates.

Allows user to add events to Calendar List View Dashboard via the Add to Student To-Do checkbox.

Allows user to create a course pace via Course Pacing.

Allows user to import resources from Commons into a course.

Allows user to import content using the Course Import Tool.

Allows user to add non-graded discussions to List View Dashboard via the Add to Student To-Do checkbox.

Allows user to create, add items, and duplicate modules.

Allows user to add pages to List View Dashboard via the Add to Student To-Do checkbox.

### Course Content - edit

Allows user to lock / unlock selected announcements individually or in bulk.

Allows user to edit a list of assignment blackout dates.

Allows user to share assignments to Commons or edit previously shared content.

Allows user to edit to-do date on a course Page that supports it.

Allows user to edit Conferences.

Allows user to edit title, and description on all collaborations.

Allows user to update modules (edit module settings, publish, unpublish, batch edit, assign modules).

Allows user to edit content migrations.

Allows user to edit and publish a course pace via Course Pacing.

Allows user to edit the course syllabus.

Allows user to edit course tabs.

### Course Content - delete

Allows user to remove selected announcements individually or in bulk.

Allows user to remove assignment blackout dates.

Allows user to remove collaborators on all collaborations.

### Course Content - add / edit / or delete

Allows user to have full section visibility when viewing announcements.

Allows user to access the Attendance tool.

Allows user to view Course Status, Choose Home Page, and Course Setup Checklist buttons in the Home page.

Allows user to access the Chat tool.

Allows user to view course Conferences.

Allows user to view and list content migrations.

Allows user to view a content migration content list by type.

Allows user access to LTI sub navigation tool selection for assignment syllabus configuration.

Allows user to view or retrieve a list of assignment blackout dates.

Allows user to view a content migration notice to an "import in progress".

Allows user to view previously created collaborations.

Allows user to view and list course paces via Course Pacing.

Allows user to view and initiate course link validation.

## Additional Considerations

### Attendance

The Attendance tool must be enabled by your Canvas admin.

### Chat

The Chat tool must be enabled by your Canvas admin.

### Commons

To share a Discussion to Commons, Discussions - view must also be enabled.

### Course Home Page

Teachers, designers, and TAs can select a course home page without the Course content - add / edit / delete permission.

### Course Settings

The Course Status buttons (unpublished and published) are only displayed until a student submission is received. Courses cannot be unpublished with student submissions.

### Modules

Module items cannot be unpublished if there are student submissions.

### Course Pacing

Course Pacing feature preview must be enabled in your institution.

## `manage_course_designer_enrollments` — Users - Designers

## What it Does

### Designers - add

Allows user to add designers to a course from the account Courses page.

Allows user to add designers to a course.

### Designers - remove

Allows user to remove designers from a course.

Allows user to deactivate designers in a course.

## Additional Considerations

### Courses (Account)

If the Open Registration account setting is enabled, users with this permission can add designers to a course from the Courses page via email address or login ID even if a designer does not already have a Canvas account.

To add a user via SIS ID, SIS Data - manage must also be enabled.

To access the account Courses page, Courses - view list must be enabled.

### People (Course)

If an enrollment is created via SIS, only admins can remove the enrollment from a course.

To remove a user via SIS ID, SIS Data - manage must also be enabled.

## `manage_course_details` — Manage Course Details

## What it Does

### Manage Course Details

Allows the user to edit the Course Details tab in the Course Settings page.

## `manage_course_feature_options` — Manage Course Feature Options

## What it Does

### Manage Course Feature Options

Allows the user to toggle the state of feature options in the Course Settings.

## `manage_course_navigation` — Manage Course Navigation

## What it Does

### Manage Course Navigation

Allows the user to reorder, enable, or disable items in the Course Navigation.

## `manage_course_observer_enrollments` — Users - Observers

## What it Does

### Observers - add

Allows user to add observers to a course from the account Courses page.

Allows user to add observers to a course.

### Observers - remove

Allows user to remove observers from a course.

Allows user to deactivate observers in a course.

## Additional Considerations

### Courses (Account)

If the Open Registration account setting is enabled, users with this permission can add observers to a course from the Courses page via email address or login ID even if an observer does not already have a Canvas account.

To add a user via SIS ID, SIS Data - manage must also be enabled.

To access the account Courses page, Courses - view list must be enabled.

### People (Course)

If an enrollment is created via SIS, only admins can remove the enrollment from a course.

To remove a user via SIS ID, SIS Data - manage must also be enabled.

## `manage_course_student_enrollments` — Users - Students

## What it Does

### Students - add

Allows user to add students to a course from the account Courses page.

Allows user to update a student’s section enrollment or role.

Allows user to add students to a course.

### Students - remove

Allows user to remove students from a course.

Allows user to remove a student’s section enrollment or role.

Allows user to deactivate students in a course.

## Additional Considerations

### Courses (Account)

If the Open Registration account setting is enabled, users with this permission can add students to a course from the Courses page via email address or login ID even if a student does not already have a Canvas account.

To add a user via SIS ID, SIS Data - manage must also be enabled.

To access the account Courses page, Courses - view list must be enabled.

### People (Course)

If an enrollment is created via SIS, only admins can remove the enrollment from a course.

To remove a user via SIS ID, SIS Data - manage must also be enabled.

## `manage_course_ta_enrollments` — Users - TAs

## What it Does

### TAs - add

Allows user to add TAs to a course from the account Courses page.

Allows user to add TAs in the course.

### TAs - remove

Allows user to remove TAs from a course.

Allows user to deactivate TAs in a course.

## Additional Considerations

### Courses (Account)

If the Open Registration account setting is enabled, users with this permission can add TAs to a course from the Courses page via email address or login ID even if a TA does not already have a Canvas account.

To add a user via SIS ID, SIS Data - manage must also be enabled.

To access the account Courses page, Courses - view list must be enabled.

### People (Course)

If an enrollment is created via SIS, only admins can remove the enrollment from a course.

To remove a user via SIS ID, SIS Data - manage must also be enabled.

## `manage_course_teacher_enrollments` — Users - Teachers

## What it Does

### Teachers - add

Allows user to add teachers to a course from the account Courses page.

Allows user to add teachers to a course.

### Teachers - remove

Allows user to remove teachers from a course.

Allows user to deactivate teachers in a course.

## Additional Considerations

### Courses (Account)

If the Open Registration account setting is enabled, users with this permission can add teachers to a course from the Courses page via email address or login ID even if a teacher does not already have a Canvas account.

To add a user via SIS ID, SIS Data - manage must also be enabled.

To access the account Courses page, Courses - view list must be enabled.

### People (Course)

If an enrollment is created via SIS, only admins can remove the enrollment from a course.

To remove a user via SIS ID, SIS Data - manage must also be enabled.

## `manage_course_templates` — Manage Course Templates

## What it Does

### Course Templates - create

Allows user to set a template for an account.

Allows user to select a course as a course template in Course Settings.

Allows user to view names of course templates in the root account.

### Course Templates - delete

Allows user to remove a course as a course template in Course Settings.

Allows user to set an account to not use a template.

### Course Templates - edit

Allows user to change the template being used by an account.

Allows user to view names of course templates in the root account.

## Additional Considerations

### Account Settings

To access the Account Settings tab, Account-level settings - manage must also be enabled.

### Courses

To create a new course to use as a course template, Courses - add must also be enabled.

## `manage_course_visibility` — Courses - change visibility

## What it Does

### Course Settings

Allows user to manage the Visibility options in Course Settings or when creating a new course.

## `manage_courses` — Manage Courses

## What it Does

### Courses - add

Allows user to add new courses to an account.

### Courses - manage

Allows user to sync Blueprint Courses.

Allows user to view Blueprint Sync history.

Allows user to view and manage courses in the account.

Allows user to view the Course Setup Checklist button.

Allows user to access the Navigation tab.

Allows user to edit course image, name, course code, time zone, subaccount, term, and other options in Course Details tab.

Allows user to access Student View (test student), Copy this Course, and Permanently Delete Course buttons.

Allows user to view student context cards in announcement and discussion replies.

### Courses - conclude

Allows user to view the Conclude Course button.

### Courses - delete

Allows user to view the Delete this Course button.

### Courses - publish

Allows user to view the Publish Course and Unpublish Course buttons in the Course Home page. Allows user to view the Publish button in a course card for an unpublished course (Card View Dashboard).

### Courses - reset

Allows user to view the Reset Course Content button.

## Additional Considerations

### Blueprint Courses

If Courses - manage is enabled, but Blueprint Courses - add / edit / associate / delete is not enabled, users can still sync Blueprint Courses and view Sync history.

### Courses - Account Settings

To access the Courses link in Account Navigation, Courses - view list must be enabled.

To add a course, Courses - add must also be enabled.

To restore a deleted course, Courses - delete, Courses - undelete, and Course Content - view must also be enabled.

### Course Content

To manage course content, Courses - manage and Course Content - add / edit / delete must be enabled.

To view Choose Home Page and Course Setup Checklist buttons, Courses - manage and Course Content - view must also be enabled. (Teachers, designers, and TAs can set the home page of a course, regardless of their permissions.)

### Course Settings

The Courses - delete permission affects viewing the Permanently Delete this Course button, which only appears for manually created courses.

To cross-list a section, Courses - manage and Manage Course Sections - edit must also be enabled.

To edit the course SIS ID, Courses - manage and SIS Data - manage must also be enabled.

The Courses - Reset permission resets course content for both manually created and SIS-managed courses. (For SIS-managed courses, the SIS Data - manage permission does not apply.)

### Courses - Account Navigations

To access the Courses link in Account Navigation, Courses - manage and Courses - view list must be enabled.

### Grades

To view grades in a course, Courses - manage and Grades - view all grades must also be enabled.

### Modules

The Courses - publish permission allows the user to publish courses that do not contain modules. To publish/unpublish module content, Course Content - add / edit / delete must be enabled.

### Student Context Cards

Student context cards must be enabled for an account by an admin. If Courses - manage is not enabled, users can still view context cards through the Gradebook.

## `manage_data_services` — Data Services - manage

## What it Does

### Data Services

Allows user to access and manage Canvas Data Services.

## `manage_developer_keys` — Developer Keys - manage

## What it Does

### Developer Keys

Allows user to create developer keys for accounts.

## Additional Considerations

### Developer Keys

Required fields include key name, owner email, tool ID, redirect URL, and icon URL.

### Subaccounts

Not available at the subaccount level.

## `manage_differentiation_tags` — Manage Differentiation Tags

## What it Does

### Overview

These permissions control the ability to create, edit, and delete differentiation tags.

### Warning

If any of these permissions are granted to a user role, that role will be able to view and access data about differentiation tags.

## `manage_dsr_requests` — Users - create DSR export

## What it Does

### Users - create DSR export

Allows user to create DSR exports.

Allows user to download completed DSR exports.

## `manage_feature_flags` — Feature Options - enable / disable

## What it Does

### Feature Options (Account Settings)

Allows user to manage Feature Options in Account Settings.

## Additional Considerations

### Feature Options (Account Settings)

To view Feature Options for an account, Feature Options - enable / disable must also be enabled.

## `manage_files` — Manage Course Files

## What it Does

### Course Files - add

Allows user to add course files and folders.

Allows user to import a zip file.

### Course Files - edit

Allows user to edit course files and folders.

### Course Files - delete

Allows user to delete course files and folders.

## Additional Considerations

### Course Files

If one or all permissions are disabled, user can still view and download files into a zip file.

### Course Settings

To import files using the Course Import Tool, Course files - add and Course Content - add / edit / delete must be enabled.

### Blueprint Courses

To edit lock settings for course files, Course files - edit, Blueprint Courses - add / edit / associate / delete, and Courses - manage must also be enabled.

## `manage_grades` — Grades - edit

## What it Does

### Admin Tools (Logging tab)

Allows user to search by course ID or assignment ID in grade change logs in Admin Tools (not available at the subaccount level.)

### Analytics

Allows user to view student-specific data in Analytics.

### Course Settings

Allows user to view the course grading scheme.

### Discussions

Allows user to like discussion posts when the Only Graders Can Like checkbox is selected.

### Gradebook

Allows user to add, edit, and update grades in the Gradebook.

Allows user to access Gradebook History. Allows user to access the Learning Mastery Gradebook (if enabled).

### Grading Schemes

Allows user to create and modify grading schemes.

### Quizzes

Allows user to moderate a quiz and view the quiz statistics page.

### SpeedGrader

Allows user to edit grades and add comments in SpeedGrader.

## Additional Considerations

### Admin Tools (Logging tab)

To search grade change logs, Grades - view change logs must also be enabled.

### Analytics

To view student analytics in course analytics, Analytics - view must also be enabled.

### Course Settings

To edit course grading schemes, Courses - manage must also be enabled.

### Gradebook, SpeedGrader

Gradebook and SpeedGrader will be inaccessible if both Grades - edit and Grades - view all grades are disabled.

### People (Course)

To view student analytics, Users - view list and Analytics - view must also be enabled.

### Quizzes

To moderate a quiz, Assignments and Quizzes - manage / edit must also be enabled.

To view the user SIS ID column in the Quiz Item Analysis CSV file, SIS Data - read must also be enabled.

To view the submission log, Quizzes - view submission log must also be enabled.

### Reports

To access the Student Interactions report, Reports - manage must also be enabled.

## `manage_groups` — Manage Groups

## What it Does

### Groups - add

Allows user to create account or course groups.

Allows user to add group members to account or course groups.

Allows user to add a group for a group assignment in a course.

Allows user to create course groups created by students.

Allows users to import groups in a course.

### Groups - delete

Allows user to delete account or course groups.

Allows user to remove students from account or course groups.

Allows user to move group members to another group in an account or course.

Allows user to assign a student group leader in an account or course.

### Groups - manage

Allows user to edit account and course groups.

Allows user to view the Clone Group Set button for an account or course group.

Allows user to randomly assign users to an account or course group.

Allows user to add users to an account or course group.

Allows user to move group members to another group in an account or course.

Allows user to assign a student group leader in an account or course.

## Additional Considerations

### Groups - add

To add account level groups via CSV, SIS Data - import must also be enabled.

### Groups

If this permission is disabled, at the account level, the user cannot view any existing account groups. At the course level, the user can view, but not access, any existing groups, including groups created by students.

To view account-level groups, Users - view list must also be enabled.

To view all student groups in a course, Groups - view all student groups must also be enabled.

By default, students can always create groups in a course. To restrict students from creating groups, Courses - manage must be enabled, and the Let students organize their own groups checkbox in Course Settings must not be selected.

To access the People page and view course groups, Users - view list must also be enabled.

## `manage_impact` — Impact - Manage

## What it Does

### Impact - Manage

Allows an account administrator to manage the Impact service integration.

## Additional Considerations

### Impact

Impact is an add-on to Canvas LMS. Contact your CSM if interested.

## `manage_institutional_tags` — Manage Institutional Tags

## What it Does

### Overview

These permissions control the ability to view, create, and edit institutional tags.

## `manage_institutional_tags_create` — Institutional Tags - create

## What it Does

### Institutional Tags

Allows user to create institutional tags.

## `manage_institutional_tags_edit` — Institutional Tags - edit

## What it Does

### Institutional Tags

Allows user to edit institutional tags.

## `manage_institutional_tags_view` — Institutional Tags - view

## What it Does

### Institutional Tags

Allows user to view institutional tags.

## `manage_interaction_alerts` — Alerts - add / edit / delete

## What it Does

### Course Settings

Allows user to configure alerts in Course Settings.

## Additional Considerations

### Account Settings

This is an account setting that must be enabled by a Customer Success Manager. Alerts are a seldom-used feature designed to send an alert to students, teachers or admins for specific triggers (e.g., no student-teacher interaction for 7 days). They are checked every day, and notifications will be sent to the student and/or the teacher until the triggering problem is resolved.

## `manage_lti` — Manage LTI

## What it Does

### LTI - add

Allows user to manually add an app in Account Settings.

Allows user to add external app icons to the Rich Content Editor toolbar.

Allows user to manually add an app in Course Settings.

### LTI - delete

Allows user to manually delete an app in Account Settings.

Allows user to manually delete an app in Course Settings.

### LTI - edit

Allows user to edit configurations for manually added external apps.

## Additional Considerations

### External Apps

If LTI - add is disabled, users can still install approved apps through the Canvas App Center (if enabled for your institution). However, if LTI - delete is not enabled, they cannot delete manually added external apps.

## `manage_lti_registrations` — LTI Registrations - Manage

## What it Does

### LTI Registrations - Manage

Allows users to view, add, modify, and delete LTI 1.3 tool registrations on the new Apps page.

## Additional Considerations

### Additional Requirements

The Developer Keys - Manage permission must also be enabled for the Apps link to appear.

## `manage_master_courses` — Blueprint Courses - add / edit / associate / delete

## What it Does

### Blueprint Courses

Allows user to designate a course as a Blueprint Course.

Allows user to manage Blueprint Course settings in Course Settings.

Allows user to add and remove associated courses.

Allows user to edit lock settings on individual assignments, pages, or discussions.

## Additional Considerations

### Blueprint Courses

Course roles can only manage Blueprint Courses if they are added to the Blueprint Course as a teacher, TA, or designer role.

To manage associated courses, Courses - view list and Courses - manage / update must also be enabled.

To edit lock settings on files, Courses - manage and Course Files - edit must also be enabled.

To edit lock settings on quizzes, Courses - manage and Assignments and Quizzes - manage / edit must also be enabled.

To manage lock settings for object types, Courses - manage must also be enabled.

## `manage_nav_menu_links` — Custom Links - manage

## What it Does

### Custom Links (Account)

Allows user to add and remove custom links in Account Navigation, User Navigation, and Course Navigation from the account settings page.

## Additional Considerations

### Custom Links (Account)

Users can still rearrange custom links without this permission.

To access account settings, Account-level settings - manage must also be enabled.

### Feature Flag

This permission requires the Custom Links feature flag to be enabled.

## `manage_outcomes` — Learning Outcomes - add / edit / delete

## What it Does

### Outcomes

Determines visibility and management of the Outcomes link in Account Navigation.

Allows user to view the Outcomes Manage tab at the account and course levels.

Allows user to create, edit, and delete outcomes and outcome groups at the account and course levels.

## Additional Considerations

### Feature Option

If the Account and Course Level Outcome Mastery Scales feature option is enabled, the Manage tab displays an updated interface. Additionally, the Outcomes page will display two additional tabs that decouple mastery scales and proficiency calculations from outcomes management.

Access to these tabs requires the Outcome Proficiency Calculations - add / edit and Outcome Mastery Scales - add / edit permissions.

### Outcomes

To allow the Outcomes page as read-only, this permission can be disabled but Course Content - view must be enabled.

To import learning outcomes, Learning Outcomes - import must also be enabled.

## `manage_proficiency_calculations` — Outcome Proficiency Calculations - add / edit

## What it Does

### Outcomes

Allows user to view the Outcomes Calculations tab and set outcome proficiency calculations at the account and course levels.

## Additional Considerations

### Feature Option

This permission requires the Account and Course Level Outcome Mastery Scales feature option, which must be enabled by a Customer Success Manager.

This feature affects existing data for an entire account.

### Outcomes

If the feature option is enabled, and this permission is enabled, the Outcomes page includes three tabs: Manage, Mastery, and Calculation.

To access the Mastery tab, the Outcome Mastery Scales - add / edit permission must also be enabled. To access the Manage tab, the Learning Outcomes - add / edit / delete permission must also be enabled.

### Rubrics

If this permission is enabled, the Learning Mastery tab displays on the Outcomes page instead of the Rubrics page.

## `manage_proficiency_scales` — Outcome Mastery Scales - add / edit

## What it Does

### Outcomes

Allows user to view the Outcomes Mastery tab and set outcome mastery scales at the account and course levels.

## Additional Considerations

### Feature Option

This permission requires the Account and Course Level Outcome Mastery Scales feature option, which must be enabled by a Customer Success Manager.

This feature affects existing data for an entire account.

### Outcomes

If the feature option is enabled, and this permission is enabled, the Outcomes page includes three tabs: Manage, Mastery, and Calculation.

To access the Calculation tab, the Outcome Proficiency Calculations - add / edit permission must also be enabled. To access the Manage tab, the Learning Outcomes - add / edit / delete permission must also be enabled.

### Rubrics

If this permission is enabled, the Learning Mastery tab displays on the Outcomes page instead of the Rubrics page.

## `manage_rate_limiting` — Site Admin - Rate Limiting

## What it Does

### Rate Limiting - add

Allows user to create new rate limit settings for external tools and integrations.

### Rate Limiting - edit

Allows user to modify existing rate limit settings, including changing rate limit values and comments.

### Rate Limiting - delete

Allows user to remove rate limit settings for external tools and integrations.

### Rate Limiting - view

Allows user to view all rate limit settings and their details.

## Additional Considerations

### Site Admin Only

This permission is only available to Site Admin users.

### External Tools

Rate limiting settings apply to external tools and integrations that use OAuth client configurations with throttling parameters.

### UTID Integration

This feature supports UTID (Unified Tool ID) based rate limiting for partner tools and products.

## `manage_role_overrides` — Permissions - manage

## What it Does

### Permissions

Allows user to view and manage permissions.

## `manage_rubrics` — Rubrics - add / edit / delete

## What it Does

### Rubrics

Determines visibility and management of the Rubrics link in Account Navigation.

Allows user to create, edit, and delete rubrics.

## Additional Considerations

### Assignments

Users can access and create (but not edit) individual assignment rubrics through Assignments when Course Content - view and Assignments and Quizzes - add are enabled.

## `manage_rules` — Automation Rules

## What it Does

### Overview

These permissions control the ability to manage automation rules on the account.

## `manage_rules_add` — Automation Rules - add

## What it Does

### Automation Rules

Allows user to create automation rules on the account.

## `manage_rules_delete` — Automation Rules - delete

## What it Does

### Automation Rules

Allows user to delete automation rules on the account.

## `manage_rules_edit` — Automation Rules - edit

## What it Does

### Automation Rules

Allows user to edit automation rules on the account.

## `manage_rules_view` — Automation Rules - view

## What it Does

### Automation Rules

Allows user to view the account's automation rules.

## `manage_sections` — Manage Course Sections

## What it Does

### Course Sections - add

Allows user to add course sections in Course Settings.

### Course Sections - edit

Allows user to rename course sections.

Allows user to change start and end dates for course sections.

Allows user to cross-list sections.

### Course Sections - delete

Allows user to delete course sections.

Allows user to delete a user from a course section.

## Additional Considerations

### Cross-Listing

To cross-list sections, Course Sections - edit and Courses - manage must also be enabled.

## `manage_sis` — SIS Data - manage

## What it Does

### Account Navigation

Determines visibility of SIS Import link in Account Navigation.

Allows user to view the previous SIS import dates, errors, and imported items.

### Course Settings

Allows user to edit the course SIS ID.

### People (Account)

Allows user to view and edit the SIS ID and Integration ID in a user’s Login Details.

### People (Course)

Allows user to edit the course SIS ID.

### Subaccount Settings

Allows user to view and insert data in the SIS ID field.

## Additional Considerations

### Course Settings

To edit course settings, Courses - manage must be enabled.

### People (Account)

To view or edit a user’s SIS ID or Integration ID, Users - view list and Users - manage login details must also both be enabled.

### People (Course)

If this permission is enabled, users do not need the SIS Data - read permission enabled. The account permission overrides the course permission.

To disallow users from managing SIS IDs at the course level, SIS Data - manage and SIS Data - read must both be disabled.

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

### SIS Import

To import SIS data, SIS Data - import must also be enabled.

### Subaccounts

Not available at the subaccount level.

## `manage_storage_quotas` — Storage Quotas - manage

## What it Does

### Quotas (Account Settings)

Allows user to view and manage Quotas tab in Account Settings. User can set default course, user, and group storage quotes.

## `manage_students` — Users - manage students in courses

## What it Does

### People (Course)

Allows user to view login ID information for students.

Allows user to view prior enrollments.

Allows user to access a user’s settings menu and user details.

Allows user to resend course invitations from the Course People page.

## Additional Considerations

### Courses (Account)

To access the account Courses page, Courses - view list must be enabled.

### People (Course)

To add or remove a student to or from a course, the Users - Student permission must be enabled.

To view the list of users in the course, Users - view list must be enabled.

To view SIS IDs, SIS Data - read must be enabled.

To edit a student’s section, Conversations - send to individual course members must also be enabled.

## `manage_tags_add` — Differentiation Tags - add

## What it Does

### Allows

This permission controls the ability to:

Create new differentiation tags

Add users to differentiation tags

### Warning

This permission does not allow a user to edit a differentiation tag after it has been created.

## `manage_tags_delete` — Differentiation Tags - delete

## What it Does

### What it allows

This permission controls the ability to:

Delete differentiation tags

Remove users from differentiation tags

### Warning

A user who can delete differentiation tags has the ability to remove users from an assignment by deleting the tags assigned to an assignment.

## `manage_tags_manage` — Differentiation Tags - manage

## What it Does

### What it allows

This permission controls the ability to:

Edit differentiation tag names, variants, and members

Remove users from differentiation tags

Add users to differentiation tags

### Warning

A user with this permission has the ability to remove users from an assignment by removing tag variants that are assigned to an assignment

## `manage_temporary_enrollments` — Users - Temporary Enrollments

## What it Does

### Manage Temporary Enrollments

Temporarily enroll a user into a course. This temporary enrollment is paired up with another enrollment within the course.

The temporarily enrolled user can only view and participate in a course between the start and end dates that were chosen when making the temporary enrollment.

### Temporary Enrollments - add

Allows users to add a temporary enrollment with a start date, end date, and role

### Temporary Enrollments - edit

Allows users to edit an existing temporary enrollment

### Temporary Enrollments - delete

Allows users to delete a temporary enrollment

## `manage_user_logins` — Users - manage login details

## What it Does

### People (Account)

Allows user to create accounts for new users.

Allows user to remove and merge users in an account.

Allows user to modify user account details.

Allows user to view and modify login information for a user.

### Admin Tools (Logging tab)

Allows user to generate login/logout activity report in Admin Tools.

## Additional Considerations

### Admin Tools (Logging tab)

If Users - manage login details or Statistics - view is enabled, the user will be able to generate login/logout activity in Admin Tools. To hide the login/logout activity option in Admin Tools, both of these permissions need to be disabled.

### People (Account)

To view users and user account details, Users - view list must be enabled.

To change user passwords, Users - view must also be enabled.

To view a user’s SIS ID, SIS Data - manage or SIS Data - read must also be enabled.

To view a user’s Integration ID, SIS Data - manage must also be enabled.

To merge users, the Self Service User Merge feature option must also be enabled.

### People (Course)

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

### Subaccounts

Not available at the subaccount level.

## `manage_user_observers` — Users - manage observers

## What it Does

### People

Allows user to manage observers associated with students in the account.

## `manage_users_in_bulk` — Bulk actions - people page

## What it Does

### Bulk actions - People page

Allows the user to perform bulk actions (enroll, delete, or suspend) on users listed on the People page.

## `manage_wiki` — Manage Pages

## What it Does

### Pages - create

Allows user to create course pages.

### Pages - delete

Allows user to delete course pages.

### Pages - update

Allows user to edit course pages.

Allows user to define users allowed to edit the page.

Allows user to add page to student to-do list.

Allows user to publish and unpublish pages.

Allows user to view page history and set front page.

Allows user to edit Blueprint Course lock settings in the Pages index page and for an individual page in a Blueprint master course.

## Additional Considerations

### Blueprint Courses

Blueprint courses must be enabled for an account by an admin.

To edit lock settings on the Pages index page, Pages - update, Blueprint Courses - add / edit / associate / delete, and Courses - manage.

However, if these additional permissions are enabled, but the Pages - update permission is not enabled, the user can still adjust content lock settings on individual pages in a Blueprint Master Course.

### Student Page History

Students can edit and view page history if allowed in the options for an individual page.

## `moderate_forum` — Discussions - moderate

## What it Does

### Announcements

Allows user to view the New Announcement button in the Home page.

Allows user to add announcements in the Announcements page.

### Blueprint Courses

Allows user to edit Blueprint lock settings on the Discussions index page in a Blueprint master course.

### Discussions

Allows user to add discussions in the Discussions page.

Allows user to close for comments, move, pin/unpin, edit, and delete discussion topics in the Discussions page.

Allows user to edit discussion topics.

Allows user to view all replies within a discussion topic.

## Additional Considerations

### Announcements

To view announcements, Announcements - view must also be enabled.

### Blueprint Courses

To edit lock settings on the Discussions index page, Courses - manage and Discussions - view must also be enabled.

If the additional permissions are enabled, but this permission is not enabled, lock settings can be edited on individual discussions.

### Discussions

Both Discussions - create and Discussions - moderate allow the user to create a discussion in the Discussions page. If this permission is enabled, Discussions - create is not required.

To view discussions in a course, Discussions - view must be enabled.

To reply to a discussion, Discussions - post must be enabled.

To edit a discussion, Discussions - moderate must also be enabled.

## `moderate_user_content` — Users - moderate content

## What it Does

### ePortfolios

Allows user to view the ePortfolio Moderation page and manage ePortfolio spam content.

## `modify_site_admin_developer_keys` — Developer Keys - modify Site Admin developer keys

## What it Does

### Developer Keys

Allows user to create, modify, and delete global (Site Admin) developer keys and LTI configurations.

This permission controls access to Site Admin developer keys that are inherited by all accounts. Root Account-level keys are unaffected.

## Additional Considerations

### Developer Keys

Developer Keys - manage must also be enabled to access the Developer Keys page.

### Site Admin

This permission is only available in Site Admin and controls access to global developer keys.

## `new_quizzes_multiple_session_detection` — New Quizzes - view multi session information

## What it Does

### New Quizzes

This permission allows users to view multi-session activity information on the activity log and the moderate page.

## Additional Considerations

### Quiz settings

Educators can enable the Detect Multiple Sessions setting on their quizzes to collect multi-session information on student submissions. This permission determines who can view this data in the activity log and moderate page.

## `new_quizzes_view_ip_address` — New Quizzes - view IP address

## What it Does

### New Quizzes

This permission allows users to view IP address information on the activity log.

## `post_to_forum` — Discussions - post

## What it Does

### Discussions

Allows user to reply to a discussion post.

## Additional Considerations

### Discussions

To view discussions in a course, Discussions - view must also be enabled.

If the option requiring users to post before seeing replies is selected in a discussion, users must post a reply to view all posts unless Discussions - moderate is also enabled.

## `proxy_assignment_submission` — Submission - Submit on behalf of student

## What it Does

### Submissions

Allows instructors to submit file attachments on behalf of a student.

## Additional Considerations

### Submissions

Once enabled, this option is visible in gradebook for instructors.

Instructors are not bound by attempt limits, but an instructor's submission WILL count as a student's attempt.

## `read_announcements` — Announcements - view

## What it Does

### Announcements

Allows user to view the Announcements link in Course Navigation.

### Announcements

Allows user to view course announcements.

## Additional Considerations

### Announcements

To view recent announcements on the home page, Course content - view must be enabled, and the Show recent announcements on Course home page checkbox must be selected in Course Settings.

To manage course announcements, Discussions - moderate ​must also be enabled.

### Global Announcements

This permission only affects course announcements; to manage global announcements, Global Announcements - add / edit / delete​ must be enabled.

## `read_course_content` — Course Content - view

## What it Does

### Courses

Allows user to view published and unpublished course content.

## Additional Considerations

### Admin Tools (Undelete Courses)

If Courses - manage and Courses - undelete are also enabled, an account-level user will be able to restore deleted courses in Admin Tools.

### Courses

If disabled, user will still have access to Course Settings.

User cannot manage individual course content without the appropriate permission for that content item.

If course visibility is limited to users enrolled in the course, this permission allows the user to view course content without being enrolled in the course.

### Gradebook

To view the Gradebook, Grades - view all grades must also be enabled.

## `read_course_list` — Courses - view list

## What it Does

### Blueprint Courses

Allows user to filter for Blueprint courses as the account level. Allows user to add associated courses.

### Courses

Allows user to see the list of courses in the account.

## Additional Considerations

### Account Settings

If this permission is disabled and Courses - add is enabled, users can add a new course with the Add a New Course button in Account Settings.

### Blueprint Courses

To add associated courses, Blueprint Courses - add / edit / associate / delete and Courses - add must also be enabled.

### Statistics

Allows user to see the list of recently started and ended courses in account statistics.

## `read_email_addresses` — Users - view primary email address

## What it Does

### People (Account)

Allows user to search for account users via primary email address in the account People page.

Allows user to search for other users via primary email address in a course People page.

## Additional Considerations

### People (Account)

To view the account People page, Users - view list must be enabled.

If this permission is disabled, and Users - view login IDs is enabled, users will still see email addresses used as login IDs.

## `read_forum` — Discussions - view

## What it Does

### Blueprint Courses

Allows user to edit Blueprint content lock settings on individual discussions.

### Discussions

Allows user to view the Discussions link in Course Navigation.

Allows user to view course discussions and all replies within the discussion topics.

## Additional Considerations

### Blueprint Courses

To edit lock settings from the Discussions index page, Blueprint Courses - add / edit / associate / delete and Courses - manage must also be enabled.

### Commons

To share a discussion to Commons, Courses - manage must also be enabled.

### Discussions

To manage discussions, Discussions - moderate must also be enabled.

To reply to a discussion, Discussions - post must also be enabled.

## `read_question_banks` — Question banks - view and link

## What it Does

### Question Banks

Allows user to view and link questions in a quiz to account-level question banks.

## Additional Considerations

### Quizzes and Question Banks

To access the Manage Question Banks link in a course Quizzes Index Page, Course content - view and Assignments and Quizzes - manage / edit must also be enabled.

## `read_reports` — Reports - manage

## What it Does

### Reports

Allows user to view and configure reports in Account Settings.

Allows user to view Access Reports.

Allows user to view last activity and total activity information on the People page.

## Additional Considerations

### People (Course)

To view Last Activity and Total Activity information on the Course People page, Users - view list must also be enabled.

To access a Course People page, Users - view list must also be enabled.

### Reports (Course)

To access the Student Interactions report, Grades - view all grades must also be enabled.

## `read_roster` — Users - view list

## What it Does

### Account Navigation

Allows user to access the People link in Account Navigation.

### Admin Tools (Logging tab)

Allows user to view login/logout activity of users in Admin Tools.

Allows user to search grade change logs by grader or student in Admin Tools.

### Assignments

Allows user to differentiate assignments to individual students.

### Collaborations

Allows user to view and add users in a collaboration.

### Conversations

Allows user to send a message in Conversations without selecting a course.

### Course Navigation

Allows user to view the People link in Course Navigation.

### Groups (Course)

Allows user to view groups in a course.

### People (Account)

Allows user to view list of users in the account.

### People (Course)

Allows user to view list of users in the course People page.

Allows user to view the Prior Enrollments button in the course People page.

## Additional Considerations

### Account Groups

To view account-level groups, Groups - manage must also be enabled.

### Admin Tools (Logging tab)

To generate login/logout activity in Admin Tools, Users - manage login details or Statistics - view must also be enabled.

To generate grade change logs in Admin Tools, Grades - view change logs must also be enabled.

### Courses

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

### Groups

To add groups, Groups - add must also be enabled.

To delete groups, Groups - delete must also be enabled.

To edit groups, Groups - manage must also be enabled.

### People (Account)

To edit user details, modify login details, or change user passwords, Users - manage login details must also be enabled.

To view user page views, Statistics - view must also be enabled.

To act as other users, Users - act as must also be enabled.

### People (Course)

To edit a user’s section, the appropriate Users permission (e.g. Users - Teachers), Users - allow administrative actions in courses, and Conversations - send to individual course members must also be enabled.

## `read_sis` — SIS Data - read

## What it Does

### Course Settings

Allows user to view a course’s SIS ID.

### People (Account)

Allows user to view the SIS ID in a user’s login details.

### People (Course)

Allows user to view user SIS IDs in a course People page.

### Quizzes

Allows user to view the user SIS ID column in the Quiz Item Analysis CSV file.

### SIS

Governs account-related SIS IDs (i.e., subaccount SIS ID).

## Additional Considerations

### Account and Subaccount

Users and terms are located at the account, so the SIS endpoint always confirms the user’s permissions according to account.

Subaccounts only have ownership of courses and sections; they do not own user data. Subaccount admins are not able to view SIS information unless they are also granted an instructor role in a course.

Subaccount admins are not able to view SIS information unless they are also granted an instructor role in a course.

Subaccount admins cannot view SIS information without the course association, as the instructor role has permission to read SIS data at the account level.

### People (Account)

To view a user’s login details, Users - view list and Modify login details for users must also both be enabled.

### People (Course)

To add or remove users to a course, the appropriate Users permission must be enabled (e.g. Users - Teachers).

### SIS Import

To manage SIS data, SIS Data - manage must be enabled.

If SIS Data - manage is enabled and SIS Data - read is disabled, the account permission overrides the course permission.

If SIS Data - manage is disabled and SIS Data - read is enabled, users can only view course, user, and subaccount SIS IDs.

To disallow users from viewing any SIS IDs at the course level, SIS Data - manage and SIS Data - read must both be disabled.

## `select_final_grade` — Grades - select final grade for moderation

## What it Does

### Grades

Allows user to select final grade for moderated assignments.

## Additional Considerations

### Assignments

To add students to a moderation set, Grades - view all grades must also be enabled.

### Grades

To publish final grades for a moderated assignment, Grades - edit must also be enabled.

To post or hide grades for a moderated assignment, Grades - edit must also be enabled.

### SpeedGrader

To review a moderated assignment in SpeedGrader, Grades - edit must also be enabled.

## `send_messages` — Conversations - send messages to individual course members

## What it Does

### Conversations

Allows user to send messages to individual course members.

## Additional Considerations

### Conversations

When disabled, students can still send individual messages to course teachers, course TAs, and students that belong to the same account-level groups.

### People

To edit a user’s section, Users - allow administrative actions in courses and Users - view list must also be enabled.

## `send_messages_all` — Conversations - send messages to entire class

## What it Does

### Conversations

Allows user to send a message to “All in [course name]” or "All in [course group]".

## `share_banks_with_subaccounts` — Item Banks - share with subaccounts

## What it Does

### Item Banks

Allows a user to manage sharing of item banks with subaccounts.

## Additional Considerations

### Item Banks

If this permission is disabled, users cannot share item banks to subaccounts. When a user with an admin role is granted this permission, the user can share item banks to subaccounts they administer.

## `undelete_courses` — Courses - undelete

## What it Does

### Admin Tools (Restore Courses tab)

Allows user to access the Restore Courses tab in Admin Tools.

## Additional Considerations

### Admin Tools (Restore Courses tab)

To search for a course in the Restore Courses tab, Course Content - view must also be enabled.

To restore a deleted course in an account, Manage Courses - delete and Course Content - view must also be enabled.

## `users_manage_access_tokens` — Users - Manage Access Tokens

## What it Does

### Access Tokens - create / update

Allows user to create access tokens on behalf of another user.

Allows user to update access tokens on behalf of another user.

Allows user to regenerate access tokens on behalf of another user.

Allows user to still create access tokens for themself when the Limit Personal Access Token Creation setting is on.

Allows user to still update their access tokens when the Limit Personal Access Token Creation setting is on.

Allows user to still regenerate their access tokens when the Limit Personal Access Token Creation setting is on.

### Access Tokens - delete

Allows user to delete access tokens on behalf of another user.

### Access Tokens - view

Allows user to view access tokens on behalf of another user. This does not include viewing the token string, which is only shown at the time of creation.

## Additional Considerations

### Subaccounts

Not available at the subaccount level

## `view_admin_analytics` — Admin Analytics - view and export data

## What it Does

### Admin Analytics

Allows user to view, drill into, and export Admin Analytics data in the Overview, Course, and Student tabs.

## Additional Considerations

### Account Settings

The Admin Analytics feature must be enabled in Account Settings to view Admin Analytics dashboards.

## `view_all_grades` — Grades - view all grades

## What it Does

### Admin Tools (Logging tab)

Allows user to search by assignment ID in grade change logs.

### Analytics

Allows user to view student-specific data in Analytics.

### Assignments, SpeedGrader

Allows user to view a link to SpeedGrader from assignments.

### Gradebook

Allows user to export the Gradebook to a comma separated values (CSV) file.

Allows user to access the Learning Mastery Gradebook (if enabled).

### Grades

Allows user to view student Grades pages.

### Modules

Allows user to access the Student Progress page.

### People (Course)

Allows user to view analytics link in the user settings menu.

### Quizzes

Allows user to view student results, view quiz statistics, and access a quiz in SpeedGrader.

### Rubrics, SpeedGrader

Allows user to view grader comments on a rubric in SpeedGrader.

### Student Context Card

Adds analytics to a student’s context card.

## Additional Considerations

### Admin Tools (Grade Change Logs)

To search grade change logs, Grades - view change logs must also be enabled.

### Analytics

To view student analytics, Analytics - view must also be enabled.

### Gradebook

To view the Gradebook, Course Content - view must also be enabled.

If both Grades - edit and Grades - view all grades are disabled, Gradebook will be hidden from Course Navigation.

### Grades

To post or hide grades, Grades - edit must also be enabled.

### Modules

To view module progression, Grades - view all grades must also be enabled.

### Reports

To access the Student Interactions report, Reports - manage must also be enabled.

### Student Context Card

Student Context Cards must be enabled for an account by an admin.

## `view_analytics_hub` — Analytics Hub

## What it Does

### Analytics Hub

Allows user to open Analytics Hub, the central library of all things Data, Analytics and Insights.

## `view_ask_questions_analytics` — Ask Your Data - use

## What it Does

### Account Settings

Allows users to access, interact with, and use the Ask Your Data feature of Intelligent Insights.

### Subaccounts

Provides a scoped access to the Ask Your Data feature.

## `view_ask_questions_pinboards` — Pinboards - view

## What it Does

### Account Settings

Allows view access to Ask Your Data's Pinboards feature of Intelligent Insights. Does not include access to Ask Your Data's Chat feature or AI.

### Subaccounts

Provides a scoped access to the Ask Your Data feature.

## `view_audit_trail` — Grades - view audit trail

## What it Does

### Grades

Allows user to review an audit trail in assignments, both moderated and anonymous.

## Additional Considerations

### Grades

To moderate grades, Grades - Select final grade for moderation must also be enabled.

To post or hide grades for an assignment, Grades - edit must also be enabled.

## `view_course_changes` — Courses - view change logs

## What it Does

### Admin Tools (Logging tab)

Determines visibility of the Course Activity option in the Admin Tools Logging tab.

Allows user to view course activity information for the account.

## `view_course_readiness` — Course Readiness

## What it Does

### Course Readiness

Allows an account administrator to access the Course Readiness feature of Intelligent Insights.

## Additional Considerations

### Intelligent Insights

Course Readiness is part of the Intelligent Insights upgrade in Canvas.

## `view_feature_flags` — Feature Options - view

## What it Does

### Feature Options (Account Settings)

Allows user to view Feature Options in Account Settings.

## Additional Considerations

### Feature Options (Account Settings)

To manage Feature Options for an account, Feature Options - enable / disable must also be enabled.

## `view_grade_changes` — Grades - view change logs

## What it Does

### Admin Tools (Logging tab)

Determines visibility of the Grade Change Activity option in the Admin Tools Logging tab.

## Additional Considerations

### Admin Tools (Logging tab)

To search by grader or student ID, Users - view must also be enabled.

To search by course ID or assignment ID, Grades - edit must also be enabled.

To search by assignment ID only, Grades - view all grades must also be enabled.

## `view_group_pages` — Groups - view all student groups

## What it Does

### Groups

Allows user to view the group home pages of all student groups.

Allows students to access other student groups within a group set with a direct link.

## Additional Considerations

### Groups

By default students are able to create groups; to restrict students from creating groups, do not select the Let students organize their own groups checkbox in Course Settings.

## `view_notifications` — Notifications - view

## What it Does

### Admin Tools (Notifications tab)

Allows user to access the View Notifications tab in Admin Tools.

## Additional Considerations

### Admin Tools (Notifications tab)

To search and view notifications for a user, Users - view must also be enabled.

### Subaccounts

Not available at the subaccount level.

## `view_quiz_answer_audits` — Quizzes - view submission log

## What it Does

### Quizzes

Allows user to view student quiz logs.

## Additional Considerations

### Grades

Grades - edit must also be enabled.

### Quizzes

The Quiz Log Auditing feature option must be enabled in Course Settings.

## `view_rsi_report` — Regular and Substantive Interaction

## What it Does

### Account Settings

Allows an account administrator to access the Regular and Substantive Interaction Insights feature of Intelligent Insights.

### Subaccounts

Provides scoped access to the Regular and Substantive Interaction Insights feature.

## Additional Considerations

### Intelligent Insights

Regular and Substantive Interaction Insights is part of the Intelligent Insights upgrade in Canvas.

## `view_statistics` — Statistics - view

## What it Does

### Account Statistics

Allows admin user to view account statistics.

### Admin Tools (Logging tab)

Allows user to generate login/logout activity report in Admin Tools.

## Additional Considerations

### Admin Tools (Logging tab)

If Statistics - view or Users - manage login details is enabled, the user will be able to generate login/logout activity in Admin Tools. To hide the login/logout activity option in Admin Tools, both of these permissions need to be disabled.

### People (Account)

To view user page views, Users - view list must also be enabled.

### Subaccounts

Not available at the subaccount level.

## `view_students_in_need` — Students in Need of Attention

## What it Does

### Students in Need of Attention

Allows an account administrator to access the Students in Need of Attention feature of Intelligent Insights.

## Additional Considerations

### Intelligent Insights

Students in Need of Attention is part of the Intelligent Insights upgrade in Canvas.

## `view_title_iv_financial_aid_report` — Title IV Financial Aid Report

## What it Does

### Account Settings

Allows an account administrator to access the Title IV Financial Aid Report in Intelligent Insights.

### Subaccounts

Provides scoped access to the Title IV Financial Aid Report.

## Additional Considerations

### Intelligent Insights

The Title IV Financial Aid Report is part of the Intelligent Insights upgrade in Canvas.

## `view_user_generated_access_tokens` — Manually Generated Access Tokens - view

## What it Does

### Access Tokens

Allows user to view other user's manually generated access tokens. This does not let them read the actual token value itself, just the information about it.

## Additional Considerations

### Subaccounts

Not available at the subaccount level

## `view_user_logins` — Users - view login IDs

## What it Does

### People (Account, Course)

Allows user to search for other users by Login ID in the account People page.

## Additional Considerations

### People (Account, Course)

To access the People page, Users - view list must be enabled.

If this permission is enabled, and if Users - view primary email address is disabled, users will see email addresses used as login IDs.

To view login IDs, Users - allow administrative actions in courses must also be enabled.
