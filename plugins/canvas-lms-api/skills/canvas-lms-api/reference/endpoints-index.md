# Canvas LMS API — Endpoint Index

One line per endpoint. `grep -i <keyword>` this file to locate an endpoint, then open the matching `resources/<slug>.md` for full parameters.

Format: `METHOD` path — summary [nickname]


### Access Tokens  —  resources/access_tokens.md

`GET` /v1/users/{user_id}/user_generated_tokens — List access tokens for a user [list_access_tokens_for_user]
`GET` /v1/users/{user_id}/tokens/{id} — Show an access token [show_access_token]
`POST` /v1/users/{user_id}/tokens — Create an access token [create_access_token]
`PUT` /v1/users/{user_id}/tokens/{id} — Update an access token [update_access_token]
`DELETE` /v1/users/{user_id}/tokens/{id} — Delete an access token [delete_access_token]

### Accessibility Course Scans  —  resources/accessibility_course_scans.md

`POST` /v1/users/{user_id}/educator_accessibility_course_scan — Trigger accessibility course scan [trigger_accessibility_course_scan]

### Accessibility Course Statistics  —  resources/accessibility_course_statistics.md

`GET` /v1/users/{user_id}/educator_accessibility_course_statistics — List accessibility course statistics [list_accessibility_course_statistics]

### Account Calendars  —  resources/account_calendars.md

`GET` /v1/account_calendars — List available account calendars [list_available_account_calendars]
`GET` /v1/account_calendars/{account_id} — Get a single account calendar [get_single_account_calendar]
`PUT` /v1/account_calendars/{account_id} — Update a calendar [update_calendar]
`PUT` /v1/accounts/{account_id}/account_calendars — Update several calendars [update_several_calendars]
`GET` /v1/accounts/{account_id}/account_calendars — List all account calendars [list_all_account_calendars]
`GET` /v1/accounts/{account_id}/visible_calendars_count — Count of all visible account calendars [count_of_all_visible_account_calendars]

### Account Notifications  —  resources/account_notifications.md

`GET` /v1/accounts/{account_id}/account_notifications — Index of active global notification for the user [index_of_active_global_notification_for_user]
`GET` /v1/accounts/{account_id}/account_notifications/{id} — Show a global notification [show_global_notification]
`POST` /v1/accounts/{account_id}/account_notifications — Create a global notification [create_global_notification]
`PUT` /v1/accounts/{account_id}/account_notifications/{id} — Update a global notification [update_global_notification]
`DELETE` /v1/accounts/{account_id}/account_notifications/{id} — Close notification for user. Destroy notification for admin [close_notification_for_user_destroy_notification_for_admin]

### Account Reports  —  resources/account_reports.md

`GET` /v1/accounts/{account_id}/reports — List Available Reports [list_available_reports]
`POST` /v1/accounts/{account_id}/reports/{report} — Start a Report [start_report]
`GET` /v1/accounts/{account_id}/reports/{report} — Index of Reports [index_of_reports]
`GET` /v1/accounts/{account_id}/reports/{report}/{id} — Status of a Report [status_of_report]
`DELETE` /v1/accounts/{account_id}/reports/{report}/{id} — Delete a Report [delete_report]
`PUT` /v1/accounts/{account_id}/reports/{report}/{id}/abort — Abort a Report [abort_report]

### Accounts  —  resources/accounts.md

`GET` /v1/accounts — List accounts [list_accounts]
`GET` /v1/horizon_accounts — List horizon accounts [list_horizon_accounts]
`GET` /v1/manageable_accounts — Get accounts that admins can manage [get_accounts_that_admins_can_manage]
`GET` /v1/course_creation_accounts — Get accounts that users can create courses in [get_accounts_that_users_can_create_courses_in]
`GET` /v1/course_accounts — List accounts for course admins [list_accounts_for_course_admins]
`GET` /v1/accounts/{id} — Get a single account [get_single_account]
`GET` /v1/accounts/{account_id}/settings — Settings [settings]
`GET` /v1/settings/environment — List environment settings [list_environment_settings]
`GET` /v1/accounts/{account_id}/permissions — Permissions [permissions]
`GET` /v1/accounts/{account_id}/sub_accounts — Get the sub-accounts of an account [get_sub_accounts_of_account]
`GET` /v1/accounts/{account_id}/terms_of_service — Get the Terms of Service [get_terms_of_service]
`GET` /v1/accounts/{account_id}/help_links — Get help links [get_help_links]
`GET` /v1/manually_created_courses_account — Get the manually-created courses sub-account for the domain root account [get_manually_created_courses_sub_account_for_domain_root_account]
`GET` /v1/accounts/{account_id}/courses — List active courses in an account [list_active_courses_in_account]
`PUT` /v1/accounts/{id} — Update an account [update_account]
`DELETE` /v1/accounts/{account_id}/users/{user_id} — Delete a user from the root account [delete_user_from_root_account]
`DELETE` /v1/accounts/{account_id}/users — Delete multiple users from the root account [delete_multiple_users_from_root_account]
`PUT` /v1/accounts/{account_id}/users/bulk_update — Update multiple users [update_multiple_users]
`PUT` /v1/accounts/{account_id}/users/{user_id}/restore — Restore a deleted user from a root account [restore_deleted_user_from_root_account]
`POST` /v1/accounts/{account_id}/sub_accounts — Create a new sub-account [create_new_sub_account]
`DELETE` /v1/accounts/{account_id}/sub_accounts/{id} — Delete a sub-account [delete_sub_account]

### Accounts (LTI)  —  resources/accounts_(lti).md

`GET` /lti/accounts/{account_id} — Get account [get_account]

### Admins  —  resources/admins.md

`GET` /v1/accounts/{account_id}/admins — List account admins [list_account_admins]
`POST` /v1/accounts/{account_id}/admins — Make an account admin [make_account_admin]
`DELETE` /v1/accounts/{account_id}/admins/{user_id} — Remove account admin [remove_account_admin]
`GET` /v1/accounts/{account_id}/admins/self — List my admin roles [list_my_admin_roles]

### AI Conversations  —  resources/ai_conversations.md

`GET` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id} — Show conversation [show_conversation]
`GET` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations — Get active conversation [get_active_conversation]
`POST` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations — Create AI conversation [create_ai_conversation]
`POST` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages — Post message to conversation [post_message_to_conversation]
`DELETE` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id} — Delete AI conversation [delete_ai_conversation]
`GET` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/evaluation — Get conversation evaluation [get_conversation_evaluation]
`POST` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages/{message_id}/feedback — Create feedback on a conversation message [create_feedback_on_conversation_message]
`DELETE` /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages/{message_id}/feedback/{feedback_id} — Delete feedback on a conversation message [delete_feedback_on_conversation_message]

### AI Experiences  —  resources/ai_experiences.md

`GET` /v1/courses/{course_id}/ai_experiences — List AI experiences [list_ai_experiences]
`GET` /v1/courses/{course_id}/ai_experiences/{id} — Show an AI experience [show_ai_experience]
`GET` /v1/courses/{course_id}/ai_experiences/new — Show new AI experience form [show_new_ai_experience_form]
`GET` /v1/courses/{course_id}/ai_experiences/{id}/edit — Show edit AI experience form [show_edit_ai_experience_form]
`POST` /v1/courses/{course_id}/ai_experiences — Create an AI experience [create_ai_experience]
`PUT` /v1/courses/{course_id}/ai_experiences/{id} — Update an AI experience [update_ai_experience]
`DELETE` /v1/courses/{course_id}/ai_experiences/{id} — Delete an AI experience [delete_ai_experience]
`GET` /v1/courses/{course_id}/ai_experiences/{id}/ai_conversations — List student AI conversations [list_student_ai_conversations]
`GET` /v1/courses/{course_id}/ai_experiences/{id}/ai_conversations/{conversation_id} — Show student AI conversation [show_student_ai_conversation]

### Announcement External Feeds  —  resources/announcement_external_feeds.md

`GET` /v1/courses/{course_id}/external_feeds — List external feeds [list_external_feeds_courses]
`GET` /v1/groups/{group_id}/external_feeds — List external feeds [list_external_feeds_groups]
`POST` /v1/courses/{course_id}/external_feeds — Create an external feed [create_external_feed_courses]
`POST` /v1/groups/{group_id}/external_feeds — Create an external feed [create_external_feed_groups]
`DELETE` /v1/courses/{course_id}/external_feeds/{external_feed_id} — Delete an external feed [delete_external_feed_courses]
`DELETE` /v1/groups/{group_id}/external_feeds/{external_feed_id} — Delete an external feed [delete_external_feed_groups]

### Announcements  —  resources/announcements.md

`GET` /v1/announcements — List announcements [list_announcements]

### API Token Scopes  —  resources/api_token_scopes.md

`GET` /v1/accounts/{account_id}/scopes — List scopes [list_scopes]

### Appointment Groups  —  resources/appointment_groups.md

`GET` /v1/appointment_groups — List appointment groups [list_appointment_groups]
`POST` /v1/appointment_groups — Create an appointment group [create_appointment_group]
`GET` /v1/appointment_groups/{id} — Get a single appointment group [get_single_appointment_group]
`PUT` /v1/appointment_groups/{id} — Update an appointment group [update_appointment_group]
`DELETE` /v1/appointment_groups/{id} — Delete an appointment group [delete_appointment_group]
`GET` /v1/appointment_groups/{id}/users — List user participants [list_user_participants]
`GET` /v1/appointment_groups/{id}/groups — List student group participants [list_student_group_participants]
`GET` /v1/appointment_groups/next_appointment — Get next appointment [get_next_appointment]

### Assessment Question Banks  —  resources/assessment_question_banks.md

`GET` /v1/question_banks — List question banks [list_question_banks]
`GET` /v1/question_banks/{id} — Get a single question bank [get_single_question_bank]
`GET` /v1/question_banks/{id}/questions — List assessment questions for a question bank [list_assessment_questions_for_question_bank]

### Asset Processor  —  resources/asset_processor.md

`POST` /lti/asset_processors/{asset_processor_id}/reports — Create an Asset Report [create_asset_report]
`PUT` /lti/asset_processor_eulas/{context_external_tool_id}/deployment — Update Eula Deployment Configuration [update_eula_deployment_configuration]
`POST` /lti/asset_processor_eulas/{context_external_tool_id}/user — Create an Eula Acceptance [create_eula_acceptance]
`DELETE` /lti/asset_processor_eulas/{context_external_tool_id}/user — Delete Eula Acceptances for deployment [delete_eula_acceptances_for_deployment]

### Assignment Extensions  —  resources/assignment_extensions.md

`POST` /v1/courses/{course_id}/assignments/{assignment_id}/extensions — Set extensions for student assignment submissions [set_extensions_for_student_assignment_submissions]

### Assignment Groups  —  resources/assignment_groups.md

`GET` /v1/courses/{course_id}/assignment_groups — List assignment groups [list_assignment_groups]
`GET` /v1/courses/{course_id}/assignment_groups/{assignment_group_id} — Get an Assignment Group [get_assignment_group]
`POST` /v1/courses/{course_id}/assignment_groups — Create an Assignment Group [create_assignment_group]
`PUT` /v1/courses/{course_id}/assignment_groups/{assignment_group_id} — Edit an Assignment Group [edit_assignment_group]
`DELETE` /v1/courses/{course_id}/assignment_groups/{assignment_group_id} — Destroy an Assignment Group [destroy_assignment_group]

### Assignments  —  resources/assignments.md

`DELETE` /v1/courses/{course_id}/assignments/{id} — Delete an assignment [delete_assignment]
`GET` /v1/courses/{course_id}/assignments — List assignments [list_assignments_assignments]
`GET` /v1/courses/{course_id}/assignment_groups/{assignment_group_id}/assignments — List assignments [list_assignments_assignment_groups]
`GET` /v1/users/{user_id}/courses/{course_id}/assignments — List assignments for user [list_assignments_for_user]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/duplicate — Duplicate assignment [duplicate_assignment]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/users/{user_id}/group_members — List group members for a student on an assignment [list_group_members_for_student_on_assignment]
`GET` /v1/courses/{course_id}/assignments/{id} — Get a single assignment [get_single_assignment]
`POST` /v1/courses/{course_id}/assignments — Create an assignment [create_assignment]
`PUT` /v1/courses/{course_id}/assignments/{id} — Edit an assignment [edit_assignment]
`PUT` /v1/courses/{course_id}/assignments/bulk_update — Bulk update assignment dates [bulk_update_assignment_dates]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/overrides — List assignment overrides [list_assignment_overrides]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} — Get a single assignment override [get_single_assignment_override]
`GET` /v1/groups/{group_id}/assignments/{assignment_id}/override — Redirect to the assignment override for a group [redirect_to_assignment_override_for_group]
`GET` /v1/sections/{course_section_id}/assignments/{assignment_id}/override — Redirect to the assignment override for a section [redirect_to_assignment_override_for_section]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/overrides — Create an assignment override [create_assignment_override]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} — Update an assignment override [update_assignment_override]
`DELETE` /v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} — Delete an assignment override [delete_assignment_override]
`GET` /v1/courses/{course_id}/assignments/overrides — Batch retrieve overrides in a course [batch_retrieve_overrides_in_course]
`POST` /v1/courses/{course_id}/assignments/overrides — Batch create overrides in a course [batch_create_overrides_in_course]
`PUT` /v1/courses/{course_id}/assignments/overrides — Batch update overrides in a course [batch_update_overrides_in_course]

### Authentication Providers  —  resources/authentication_providers.md

`GET` /v1/accounts/{account_id}/authentication_providers — List authentication providers [list_authentication_providers]
`GET` /v1/accounts/{account_id}/authentication_providers/{id} — Get authentication provider [get_authentication_provider]
`POST` /v1/accounts/{account_id}/authentication_providers — Add authentication provider [add_authentication_provider]
`PUT` /v1/accounts/{account_id}/authentication_providers/{id} — Update authentication provider [update_authentication_provider]
`DELETE` /v1/accounts/{account_id}/authentication_providers/{id} — Delete authentication provider [delete_authentication_provider]
`PUT` /v1/accounts/{account_id}/authentication_providers/{id}/restore — Restore a deleted authentication provider [restore_deleted_authentication_provider]
`GET` /v1/accounts/{account_id}/sso_settings — Show account auth settings [show_account_auth_settings]
`PUT` /v1/accounts/{account_id}/sso_settings — Update account auth settings [update_account_auth_settings]

### Authentications Log  —  resources/authentications_log.md

`GET` /v1/audit/authentication/logins/{login_id} — Query by login. [query_by_login]
`GET` /v1/audit/authentication/accounts/{account_id} — Query by account. [query_by_account]
`GET` /v1/audit/authentication/users/{user_id} — Query by user. [query_by_user]

### Blackout Dates  —  resources/blackout_dates.md

`GET` /v1/courses/{course_id}/blackout_dates — List blackout dates [list_blackout_dates_courses]
`GET` /v1/accounts/{account_id}/blackout_dates — List blackout dates [list_blackout_dates_accounts]
`GET` /v1/courses/{course_id}/blackout_dates/{id} — Get a single blackout date [get_single_blackout_date_courses]
`GET` /v1/accounts/{account_id}/blackout_dates/{id} — Get a single blackout date [get_single_blackout_date_accounts]
`GET` /v1/courses/{course_id}/blackout_dates/new — New Blackout Date [new_blackout_date_courses]
`GET` /v1/accounts/{account_id}/blackout_dates/new — New Blackout Date [new_blackout_date_accounts]
`POST` /v1/courses/{course_id}/blackout_dates — Create Blackout Date [create_blackout_date_courses]
`POST` /v1/accounts/{account_id}/blackout_dates — Create Blackout Date [create_blackout_date_accounts]
`PUT` /v1/courses/{course_id}/blackout_dates/{id} — Update Blackout Date [update_blackout_date_courses]
`PUT` /v1/accounts/{account_id}/blackout_dates/{id} — Update Blackout Date [update_blackout_date_accounts]
`DELETE` /v1/courses/{course_id}/blackout_dates/{id} — Delete Blackout Date [delete_blackout_date_courses]
`DELETE` /v1/accounts/{account_id}/blackout_dates/{id} — Delete Blackout Date [delete_blackout_date_accounts]
`PUT` /v1/courses/{course_id}/blackout_dates — Update a list of Blackout Dates [update_list_of_blackout_dates]

### BlockEditorTemplate  —  resources/block_editor_template.md

`GET` /v1/courses/{course_id}/block_editor_templates — List block templates [list_block_templates]

### Blueprint Courses  —  resources/blueprint_courses.md

`GET` /v1/courses/{course_id}/blueprint_templates/{template_id} — Get blueprint information [get_blueprint_information]
`GET` /v1/courses/{course_id}/blueprint_templates/{template_id}/associated_courses — Get associated course information [get_associated_course_information]
`PUT` /v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations — Update associated courses [update_associated_courses]
`POST` /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations — Begin a migration to push to associated courses [begin_migration_to_push_to_associated_courses]
`PUT` /v1/courses/{course_id}/blueprint_templates/{template_id}/restrict_item — Set or remove restrictions on a blueprint course object [set_or_remove_restrictions_on_blueprint_course_object]
`GET` /v1/courses/{course_id}/blueprint_templates/{template_id}/unsynced_changes — Get unsynced changes [get_unsynced_changes]
`GET` /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations — List blueprint migrations [list_blueprint_migrations]
`GET` /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id} — Show a blueprint migration [show_blueprint_migration]
`GET` /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}/details — Get migration details [get_migration_details]
`GET` /v1/courses/{course_id}/blueprint_subscriptions — List blueprint subscriptions [list_blueprint_subscriptions]
`GET` /v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations — List blueprint imports [list_blueprint_imports]
`GET` /v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id} — Show a blueprint import [show_blueprint_import]
`GET` /v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}/details — Get import details [get_import_details]

### Bookmarks  —  resources/bookmarks.md

`GET` /v1/users/self/bookmarks — List bookmarks [list_bookmarks]
`POST` /v1/users/self/bookmarks — Create bookmark [create_bookmark]
`GET` /v1/users/self/bookmarks/{id} — Get bookmark [get_bookmark]
`PUT` /v1/users/self/bookmarks/{id} — Update bookmark [update_bookmark]
`DELETE` /v1/users/self/bookmarks/{id} — Delete bookmark [delete_bookmark]

### Brand Configs  —  resources/brand_configs.md

`GET` /v1/brand_variables — Get the brand config variables that should be used for this domain [get_brand_config_variables_that_should_be_used_for_this_domain]
`GET` /v1/accounts/{account_id}/brand_variables — Get the brand config variables for a sub-account or course [get_brand_config_variables_for_sub_account_or_course_accounts]
`GET` /v1/courses/{course_id}/brand_variables — Get the brand config variables for a sub-account or course [get_brand_config_variables_for_sub_account_or_course_courses]

### Calendar Events  —  resources/calendar_events.md

`GET` /v1/calendar_events — List calendar events [list_calendar_events]
`GET` /v1/users/{user_id}/calendar_events — List calendar events for a user [list_calendar_events_for_user]
`POST` /v1/calendar_events — Create a calendar event [create_calendar_event]
`GET` /v1/calendar_events/{id} — Get a single calendar event or assignment [get_single_calendar_event_or_assignment]
`POST` /v1/calendar_events/{id}/reservations — Reserve a time slot [reserve_time_slot]
`POST` /v1/calendar_events/{id}/reservations/{participant_id} — Reserve a time slot [reserve_time_slot_participant_id]
`PUT` /v1/calendar_events/{id} — Update a calendar event [update_calendar_event]
`DELETE` /v1/calendar_events/{id} — Delete a calendar event [delete_calendar_event]
`POST` /v1/calendar_events/save_enabled_account_calendars — Save enabled account calendars [save_enabled_account_calendars]
`POST` /v1/courses/{course_id}/calendar_events/timetable — Set a course timetable [set_course_timetable]
`GET` /v1/courses/{course_id}/calendar_events/timetable — Get course timetable [get_course_timetable]
`POST` /v1/courses/{course_id}/calendar_events/timetable_events — Create or update events directly for a course timetable [create_or_update_events_directly_for_course_timetable]

### Canvas Career Experiences  —  resources/canvas_career_experiences.md

`GET` /v1/career/enabled — Check if Canvas Career is enabled [check_if_canvas_career_is_enabled]
`GET` /v1/career/experience_summary — Get current and available experiences [get_current_and_available_experiences]
`POST` /v1/career/switch_experience — Switch experience [switch_experience]
`POST` /v1/career/switch_role — Switch role [switch_role]

### Collaborations  —  resources/collaborations.md

`GET` /v1/courses/{course_id}/collaborations — List collaborations [list_collaborations_courses]
`GET` /v1/groups/{group_id}/collaborations — List collaborations [list_collaborations_groups]
`GET` /v1/collaborations/{id}/members — List members of a collaboration. [list_members_of_collaboration]
`GET` /v1/courses/{course_id}/potential_collaborators — List potential members [list_potential_members_courses]
`GET` /v1/groups/{group_id}/potential_collaborators — List potential members [list_potential_members_groups]

### CommMessages  —  resources/comm_messages.md

`GET` /v1/comm_messages — List of CommMessages for a user [list_of_commmessages_for_user]

### Communication Channels  —  resources/communication_channels.md

`GET` /v1/users/{user_id}/communication_channels — List user communication channels [list_user_communication_channels]
`POST` /v1/users/{user_id}/communication_channels — Create a communication channel [create_communication_channel]
`DELETE` /v1/users/{user_id}/communication_channels/{id} — Delete a communication channel [delete_communication_channel_id]
`DELETE` /v1/users/{user_id}/communication_channels/{type}/{address} — Delete a communication channel [delete_communication_channel_type]
`DELETE` /v1/users/self/communication_channels/push — Delete a push notification endpoint [delete_push_notification_endpoint]

### Conferences  —  resources/conferences.md

`GET` /v1/courses/{course_id}/conferences — List conferences [list_conferences_courses]
`GET` /v1/groups/{group_id}/conferences — List conferences [list_conferences_groups]
`GET` /v1/conferences — List conferences for the current user [list_conferences_for_current_user]

### Content Exports  —  resources/content_exports.md

`GET` /v1/courses/{course_id}/content_exports — List content exports [list_content_exports_courses]
`GET` /v1/groups/{group_id}/content_exports — List content exports [list_content_exports_groups]
`GET` /v1/users/{user_id}/content_exports — List content exports [list_content_exports_users]
`GET` /v1/courses/{course_id}/content_exports/{id} — Show content export [show_content_export_courses]
`GET` /v1/groups/{group_id}/content_exports/{id} — Show content export [show_content_export_groups]
`GET` /v1/users/{user_id}/content_exports/{id} — Show content export [show_content_export_users]
`POST` /v1/courses/{course_id}/content_exports — Export content [export_content_courses]
`POST` /v1/groups/{group_id}/content_exports — Export content [export_content_groups]
`POST` /v1/users/{user_id}/content_exports — Export content [export_content_users]

### Content Migrations  —  resources/content_migrations.md

`GET` /v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues — List migration issues [list_migration_issues_accounts]
`GET` /v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues — List migration issues [list_migration_issues_courses]
`GET` /v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues — List migration issues [list_migration_issues_groups]
`GET` /v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues — List migration issues [list_migration_issues_users]
`GET` /v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Get a migration issue [get_migration_issue_accounts]
`GET` /v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Get a migration issue [get_migration_issue_courses]
`GET` /v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Get a migration issue [get_migration_issue_groups]
`GET` /v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Get a migration issue [get_migration_issue_users]
`PUT` /v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Update a migration issue [update_migration_issue_accounts]
`PUT` /v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Update a migration issue [update_migration_issue_courses]
`PUT` /v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Update a migration issue [update_migration_issue_groups]
`PUT` /v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} — Update a migration issue [update_migration_issue_users]
`GET` /v1/accounts/{account_id}/content_migrations — List content migrations [list_content_migrations_accounts]
`GET` /v1/courses/{course_id}/content_migrations — List content migrations [list_content_migrations_courses]
`GET` /v1/groups/{group_id}/content_migrations — List content migrations [list_content_migrations_groups]
`GET` /v1/users/{user_id}/content_migrations — List content migrations [list_content_migrations_users]
`GET` /v1/accounts/{account_id}/content_migrations/{id} — Get a content migration [get_content_migration_accounts]
`GET` /v1/courses/{course_id}/content_migrations/{id} — Get a content migration [get_content_migration_courses]
`GET` /v1/groups/{group_id}/content_migrations/{id} — Get a content migration [get_content_migration_groups]
`GET` /v1/users/{user_id}/content_migrations/{id} — Get a content migration [get_content_migration_users]
`POST` /v1/accounts/{account_id}/content_migrations — Create a content migration [create_content_migration_accounts]
`POST` /v1/courses/{course_id}/content_migrations — Create a content migration [create_content_migration_courses]
`POST` /v1/groups/{group_id}/content_migrations — Create a content migration [create_content_migration_groups]
`POST` /v1/users/{user_id}/content_migrations — Create a content migration [create_content_migration_users]
`PUT` /v1/accounts/{account_id}/content_migrations/{id} — Update a content migration [update_content_migration_accounts]
`PUT` /v1/courses/{course_id}/content_migrations/{id} — Update a content migration [update_content_migration_courses]
`PUT` /v1/groups/{group_id}/content_migrations/{id} — Update a content migration [update_content_migration_groups]
`PUT` /v1/users/{user_id}/content_migrations/{id} — Update a content migration [update_content_migration_users]
`GET` /v1/accounts/{account_id}/content_migrations/migrators — List Migration Systems [list_migration_systems_accounts]
`GET` /v1/courses/{course_id}/content_migrations/migrators — List Migration Systems [list_migration_systems_courses]
`GET` /v1/groups/{group_id}/content_migrations/migrators — List Migration Systems [list_migration_systems_groups]
`GET` /v1/users/{user_id}/content_migrations/migrators — List Migration Systems [list_migration_systems_users]
`GET` /v1/accounts/{account_id}/content_migrations/{id}/selective_data — List items for selective import [list_items_for_selective_import_accounts]
`GET` /v1/courses/{course_id}/content_migrations/{id}/selective_data — List items for selective import [list_items_for_selective_import_courses]
`GET` /v1/groups/{group_id}/content_migrations/{id}/selective_data — List items for selective import [list_items_for_selective_import_groups]
`GET` /v1/users/{user_id}/content_migrations/{id}/selective_data — List items for selective import [list_items_for_selective_import_users]
`GET` /v1/courses/{course_id}/content_migrations/{id}/asset_id_mapping — Get asset id mapping [get_asset_id_mapping]

### Content Security Policy Settings  —  resources/content_security_policy_settings.md

`GET` /v1/courses/{course_id}/csp_settings — Get current settings for account or course [get_current_settings_for_account_or_course_courses]
`GET` /v1/accounts/{account_id}/csp_settings — Get current settings for account or course [get_current_settings_for_account_or_course_accounts]
`PUT` /v1/courses/{course_id}/csp_settings — Enable, disable, or clear explicit CSP setting [enable_disable_or_clear_explicit_csp_setting_courses]
`PUT` /v1/accounts/{account_id}/csp_settings — Enable, disable, or clear explicit CSP setting [enable_disable_or_clear_explicit_csp_setting_accounts]
`PUT` /v1/accounts/{account_id}/csp_settings/lock — Lock or unlock current CSP settings for sub-accounts and courses [lock_or_unlock_current_csp_settings_for_sub_accounts_and_courses]
`POST` /v1/accounts/{account_id}/csp_settings/domains — Add an allowed domain to account [add_allowed_domain_to_account]
`POST` /v1/accounts/{account_id}/csp_settings/domains/batch_create — Add multiple allowed domains to an account [add_multiple_allowed_domains_to_account]
`DELETE` /v1/accounts/{account_id}/csp_settings/domains — Remove a domain from account [remove_domain_from_account]

### Content Shares  —  resources/content_shares.md

`POST` /v1/users/{user_id}/content_shares — Create a content share [create_content_share]
`GET` /v1/users/{user_id}/content_shares/sent — List content shares [list_content_shares_sent]
`GET` /v1/users/{user_id}/content_shares/received — List content shares [list_content_shares_received]
`GET` /v1/users/{user_id}/content_shares/unread_count — Get unread shares count [get_unread_shares_count]
`GET` /v1/users/{user_id}/content_shares/{id} — Get content share [get_content_share]
`DELETE` /v1/users/{user_id}/content_shares/{id} — Remove content share [remove_content_share]
`POST` /v1/users/{user_id}/content_shares/{id}/add_users — Add users to content share [add_users_to_content_share]
`PUT` /v1/users/{user_id}/content_shares/{id} — Update a content share [update_content_share]

### Conversations  —  resources/conversations.md

`GET` /v1/conversations — List conversations [list_conversations]
`POST` /v1/conversations — Create a conversation [create_conversation]
`GET` /v1/conversations/batches — Get running batches [get_running_batches]
`GET` /v1/conversations/{id} — Get a single conversation [get_single_conversation]
`PUT` /v1/conversations/{id} — Edit a conversation [edit_conversation]
`POST` /v1/conversations/mark_all_as_read — Mark all as read [mark_all_as_read]
`DELETE` /v1/conversations/{id} — Delete a conversation [delete_conversation]
`POST` /v1/conversations/{id}/add_recipients — Add recipients [add_recipients]
`POST` /v1/conversations/{id}/add_message — Add a message [add_message]
`POST` /v1/conversations/{id}/remove_messages — Delete a message [delete_message]
`PUT` /v1/conversations — Batch update conversations [batch_update_conversations]
`GET` /v1/conversations/find_recipients — Find recipients [find_recipients]
`GET` /v1/conversations/unread_count — Unread count [unread_count]

### Course Audit log  —  resources/course_audit_log.md

`GET` /v1/audit/course/courses/{course_id} — Query by course. [query_by_course]
`GET` /v1/audit/course/accounts/{account_id} — Query by account. [query_by_account]

### Course Pace  —  resources/course_pace.md

`GET` /v1/courses/{course_id}/course_pacing/{id} — Show a Course pace [show_course_pace]
`POST` /v1/courses/{course_id}/course_pacing — Create a Course pace [create_course_pace]
`PUT` /v1/courses/{course_id}/course_pacing/{id} — Update a Course pace [update_course_pace]
`DELETE` /v1/courses/{course_id}/course_pacing/{id} — Delete a Course pace [delete_course_pace]

### Course Quiz Extensions  —  resources/course_quiz_extensions.md

`POST` /v1/courses/{course_id}/quiz_extensions — Set extensions for student quiz submissions [set_extensions_for_student_quiz_submissions]

### Course Reports  —  resources/course_reports.md

`GET` /v1/courses/{course_id}/reports/{report_type}/{id} — Status of a Report [status_of_report]
`POST` /v1/courses/{course_id}/reports/{report_type} — Start a Report [start_report]
`GET` /v1/courses/{course_id}/reports/{report_type} — Status of last Report [status_of_last_report]

### Courses  —  resources/courses.md

`GET` /v1/courses — List your courses [list_your_courses]
`GET` /v1/users/{user_id}/courses — List courses for a user [list_courses_for_user]
`GET` /v1/courses/{course_id}/users/{user_id}/progress — Get user progress [get_user_progress]
`POST` /v1/accounts/{account_id}/courses — Create a new course [create_new_course]
`POST` /v1/courses/{course_id}/files — Upload a file [upload_file]
`GET` /v1/courses/{course_id}/students — List students [list_students]
`GET` /v1/courses/{course_id}/users — List users in course [list_users_in_course_users]
`GET` /v1/courses/{course_id}/search_users — List users in course [list_users_in_course_search_users]
`GET` /v1/courses/{course_id}/recent_students — List recently logged in students [list_recently_logged_in_students]
`GET` /v1/courses/{course_id}/users/{id} — Get single user [get_single_user]
`GET` /v1/courses/{course_id}/content_share_users — Search for content share users [search_for_content_share_users]
`POST` /v1/courses/{course_id}/preview_html — Preview processed html [preview_processed_html]
`GET` /v1/courses/{course_id}/activity_stream — Course activity stream [course_activity_stream]
`GET` /v1/courses/{course_id}/activity_stream/summary — Course activity stream summary [course_activity_stream_summary]
`GET` /v1/courses/{course_id}/todo — Course TODO items [course_todo_items]
`DELETE` /v1/courses/{id} — Delete/Conclude a course [delete_conclude_course]
`GET` /v1/courses/{course_id}/settings — Get course settings [get_course_settings]
`PUT` /v1/courses/{course_id}/settings — Update course settings [update_course_settings]
`GET` /v1/courses/{course_id}/student_view_student — Return test student for course [return_test_student_for_course]
`GET` /v1/courses/{id} — Get a single course [get_single_course_courses]
`GET` /v1/accounts/{account_id}/courses/{id} — Get a single course [get_single_course_accounts]
`PUT` /v1/courses/{id} — Update a course [update_course]
`PUT` /v1/accounts/{account_id}/courses — Update courses [update_courses]
`POST` /v1/courses/{course_id}/reset_content — Reset a course [reset_course]
`GET` /v1/courses/{course_id}/effective_due_dates — Get effective due dates [get_effective_due_dates]
`GET` /v1/courses/{course_id}/permissions — Permissions [permissions]
`GET` /v1/courses/{course_id}/bulk_user_progress — Get bulk user progress [get_bulk_user_progress]
`POST` /v1/courses/{id}/dismiss_migration_limitation_message — Remove quiz migration alert [remove_quiz_migration_alert]
`POST` /v1/courses/{course_id}/restore/{version_id} — Restore course version [restore_course_version]
`GET` /v1/courses/{course_id}/course_copy/{id} — Get course copy status [get_course_copy_status]
`POST` /v1/courses/{course_id}/course_copy — Copy course content [copy_course_content]

### Custom Gradebook Columns  —  resources/custom_gradebook_columns.md

`GET` /v1/courses/{course_id}/custom_gradebook_columns — List custom gradebook columns [list_custom_gradebook_columns]
`POST` /v1/courses/{course_id}/custom_gradebook_columns — Create a custom gradebook column [create_custom_gradebook_column]
`PUT` /v1/courses/{course_id}/custom_gradebook_columns/{id} — Update a custom gradebook column [update_custom_gradebook_column]
`DELETE` /v1/courses/{course_id}/custom_gradebook_columns/{id} — Delete a custom gradebook column [delete_custom_gradebook_column]
`POST` /v1/courses/{course_id}/custom_gradebook_columns/reorder — Reorder custom columns [reorder_custom_columns]
`GET` /v1/courses/{course_id}/custom_gradebook_columns/{id}/data — List entries for a column [list_entries_for_column]
`PUT` /v1/courses/{course_id}/custom_gradebook_columns/{id}/data/{user_id} — Update column data [update_column_data]
`PUT` /v1/courses/{course_id}/custom_gradebook_column_data — Bulk update column data [bulk_update_column_data]

### Data Services  —  resources/data_services.md

`POST` /lti/accounts/{account_id}/data_services — Create a Data Services Event Subscription [create_data_services_event_subscription]
`PUT` /lti/accounts/{account_id}/data_services/{id} — Update a Data Services Event Subscription [update_data_services_event_subscription]
`GET` /lti/accounts/{account_id}/data_services/{id} — Show a Data Services Event Subscription [show_data_services_event_subscription]
`GET` /lti/accounts/{account_id}/data_services — List all Data Services Event Subscriptions [list_all_data_services_event_subscriptions]
`DELETE` /lti/accounts/{account_id}/data_services/{id} — Destroy a Data Services Event Subscription [destroy_data_services_event_subscription]

### Developer Key Account Bindings  —  resources/developer_key_account_bindings.md

`POST` /v1/accounts/{account_id}/developer_keys/{developer_key_id}/developer_key_account_bindings — Create a Developer Key Account Binding [create_developer_key_account_binding]

### Developer Keys  —  resources/developer_keys.md

`GET` /v1/accounts/{account_id}/developer_keys — List Developer Keys [list_developer_keys]
`POST` /v1/accounts/{account_id}/developer_keys — Create a Developer Key [create_developer_key]
`PUT` /v1/developer_keys/{id} — Update a Developer Key [update_developer_key]
`DELETE` /v1/developer_keys/{id} — Delete a Developer Key [delete_developer_key]

### Discovery Pages  —  resources/discovery_pages.md

`GET` /v1/discovery_pages — Get Discovery Page [get_discovery_page]
`PUT` /v1/discovery_pages — Update Discovery Page [update_discovery_page]
`POST` /v1/discovery_pages/token — Generate Discovery Page Preview Token [generate_discovery_page_preview_token]

### Discussion Topics  —  resources/discussion_topics.md

`GET` /v1/courses/{course_id}/discussion_topics — List discussion topics [list_discussion_topics_courses]
`GET` /v1/groups/{group_id}/discussion_topics — List discussion topics [list_discussion_topics_groups]
`POST` /v1/courses/{course_id}/discussion_topics — Create a new discussion topic [create_new_discussion_topic_courses]
`POST` /v1/groups/{group_id}/discussion_topics — Create a new discussion topic [create_new_discussion_topic_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/{topic_id} — Update a topic [update_topic_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/{topic_id} — Update a topic [update_topic_groups]
`DELETE` /v1/courses/{course_id}/discussion_topics/{topic_id} — Delete a topic [delete_topic_courses]
`DELETE` /v1/groups/{group_id}/discussion_topics/{topic_id} — Delete a topic [delete_topic_groups]
`POST` /v1/courses/{course_id}/discussion_topics/reorder — Reorder pinned topics [reorder_pinned_topics_courses]
`POST` /v1/groups/{group_id}/discussion_topics/reorder — Reorder pinned topics [reorder_pinned_topics_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id} — Update an entry [update_entry_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id} — Update an entry [update_entry_groups]
`DELETE` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id} — Delete an entry [delete_entry_courses]
`DELETE` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id} — Delete an entry [delete_entry_groups]
`GET` /v1/courses/{course_id}/discussion_topics/{topic_id} — Get a single topic [get_single_topic_courses]
`GET` /v1/groups/{group_id}/discussion_topics/{topic_id} — Get a single topic [get_single_topic_groups]
`GET` /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries — Find Last Summary [find_last_summary_courses]
`GET` /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries — Find Last Summary [find_last_summary_groups]
`POST` /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries — Find or Create Summary [find_or_create_summary_courses]
`POST` /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries — Find or Create Summary [find_or_create_summary_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries/disable — Disable summary [disable_summary_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries/disable — Disable summary [disable_summary_groups]
`POST` /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries/{summary_id}/feedback — Summary Feedback [summary_feedback_courses]
`POST` /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries/{summary_id}/feedback — Summary Feedback [summary_feedback_groups]
`GET` /v1/courses/{course_id}/discussion_topics/{topic_id}/view — Get the full topic [get_full_topic_courses]
`GET` /v1/groups/{group_id}/discussion_topics/{topic_id}/view — Get the full topic [get_full_topic_groups]
`POST` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries — Post an entry [post_entry_courses]
`POST` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries — Post an entry [post_entry_groups]
`POST` /v1/courses/{course_id}/discussion_topics/{topic_id}/duplicate — Duplicate discussion topic [duplicate_discussion_topic_courses]
`POST` /v1/groups/{group_id}/discussion_topics/{topic_id}/duplicate — Duplicate discussion topic [duplicate_discussion_topic_groups]
`GET` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries — List topic entries [list_topic_entries_courses]
`GET` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries — List topic entries [list_topic_entries_groups]
`POST` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies — Post a reply [post_reply_courses]
`POST` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies — Post a reply [post_reply_groups]
`GET` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies — List entry replies [list_entry_replies_courses]
`GET` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies — List entry replies [list_entry_replies_groups]
`GET` /v1/courses/{course_id}/discussion_topics/{topic_id}/entry_list — List entries [list_entries_courses]
`GET` /v1/groups/{group_id}/discussion_topics/{topic_id}/entry_list — List entries [list_entries_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/{topic_id}/read — Mark topic as read [mark_topic_as_read_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/{topic_id}/read — Mark topic as read [mark_topic_as_read_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/read_all — Mark all topic as read [mark_all_topic_as_read_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/read_all — Mark all topic as read [mark_all_topic_as_read_groups]
`DELETE` /v1/courses/{course_id}/discussion_topics/{topic_id}/read — Mark topic as unread [mark_topic_as_unread_courses]
`DELETE` /v1/groups/{group_id}/discussion_topics/{topic_id}/read — Mark topic as unread [mark_topic_as_unread_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/{topic_id}/read_all — Mark all entries as read [mark_all_entries_as_read_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/{topic_id}/read_all — Mark all entries as read [mark_all_entries_as_read_groups]
`DELETE` /v1/courses/{course_id}/discussion_topics/{topic_id}/read_all — Mark all entries as unread [mark_all_entries_as_unread_courses]
`DELETE` /v1/groups/{group_id}/discussion_topics/{topic_id}/read_all — Mark all entries as unread [mark_all_entries_as_unread_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read — Mark entry as read [mark_entry_as_read_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read — Mark entry as read [mark_entry_as_read_groups]
`DELETE` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read — Mark entry as unread [mark_entry_as_unread_courses]
`DELETE` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read — Mark entry as unread [mark_entry_as_unread_groups]
`POST` /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating — Rate entry [rate_entry_courses]
`POST` /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating — Rate entry [rate_entry_groups]
`PUT` /v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed — Subscribe to a topic [subscribe_to_topic_courses]
`PUT` /v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed — Subscribe to a topic [subscribe_to_topic_groups]
`DELETE` /v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed — Unsubscribe from a topic [unsubscribe_from_topic_courses]
`DELETE` /v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed — Unsubscribe from a topic [unsubscribe_from_topic_groups]

### Enrollment Terms  —  resources/enrollment_terms.md

`POST` /v1/accounts/{account_id}/terms — Create enrollment term [create_enrollment_term]
`PUT` /v1/accounts/{account_id}/terms/{id} — Update enrollment term [update_enrollment_term]
`DELETE` /v1/accounts/{account_id}/terms/{id} — Delete enrollment term [delete_enrollment_term]
`GET` /v1/accounts/{account_id}/terms — List enrollment terms [list_enrollment_terms]
`GET` /v1/accounts/{account_id}/terms/{id} — Retrieve enrollment term [retrieve_enrollment_term]

### Enrollments  —  resources/enrollments.md

`GET` /v1/courses/{course_id}/enrollments — List enrollments [list_enrollments_courses]
`GET` /v1/sections/{section_id}/enrollments — List enrollments [list_enrollments_sections]
`GET` /v1/users/{user_id}/enrollments — List enrollments [list_enrollments_users]
`GET` /v1/accounts/{account_id}/enrollments/{id} — Enrollment by ID [enrollment_by_id]
`POST` /v1/courses/{course_id}/enrollments — Enroll a user [enroll_user_courses]
`POST` /v1/sections/{section_id}/enrollments — Enroll a user [enroll_user_sections]
`POST` /v1/accounts/{account_id}/bulk_enrollment — Enroll multiple users to one or more courses [enroll_multiple_users_to_one_or_more_courses]
`DELETE` /v1/courses/{course_id}/enrollments/{id} — Conclude, deactivate, or delete an enrollment [conclude_deactivate_or_delete_enrollment]
`POST` /v1/courses/{course_id}/enrollments/{id}/accept — Accept Course Invitation [accept_course_invitation]
`POST` /v1/courses/{course_id}/enrollments/{id}/reject — Reject Course Invitation [reject_course_invitation]
`PUT` /v1/courses/{course_id}/enrollments/{id}/reactivate — Re-activate an enrollment [re_activate_enrollment]
`PUT` /v1/courses/{course_id}/users/{user_id}/last_attended — Add last attended date [add_last_attended_date]
`GET` /v1/users/{user_id}/temporary_enrollment_status — Show Temporary Enrollment recipient and provider status [show_temporary_enrollment_recipient_and_provider_status]
`GET` /v1/temporary_enrollment_status — Bulk Temporary Enrollment Status [bulk_temporary_enrollment_status]

### ePortfolios  —  resources/e_portfolios.md

`GET` /v1/users/{user_id}/eportfolios — Get all ePortfolios for a User [get_all_eportfolios_for_user]
`GET` /v1/eportfolios/{id} — Get an ePortfolio [get_eportfolio]
`DELETE` /v1/eportfolios/{id} — Delete an ePortfolio [delete_eportfolio]
`GET` /v1/eportfolios/{eportfolio_id}/pages — Get ePortfolio Pages [get_eportfolio_pages]
`PUT` /v1/eportfolios/{eportfolio_id}/moderate — Moderate an ePortfolio [moderate_eportfolio]
`PUT` /v1/users/{user_id}/eportfolios — Moderate all ePortfolios for a User [moderate_all_eportfolios_for_user]
`PUT` /v1/eportfolios/{eportfolio_id}/restore — Restore a deleted ePortfolio [restore_deleted_eportfolio]

### ePub Exports  —  resources/e_pub_exports.md

`GET` /v1/epub_exports — List courses with their latest ePub export [list_courses_with_their_latest_epub_export]
`POST` /v1/courses/{course_id}/epub_exports — Create ePub Export [create_epub_export]
`GET` /v1/courses/{course_id}/epub_exports/{id} — Show ePub export [show_epub_export]

### Error Reports  —  resources/error_reports.md

`POST` /v1/error_reports — Create Error Report [create_error_report]

### External Tools  —  resources/external_tools.md

`GET` /v1/courses/{course_id}/external_tools — List external tools [list_external_tools_courses]
`GET` /v1/accounts/{account_id}/external_tools — List external tools [list_external_tools_accounts]
`GET` /v1/groups/{group_id}/external_tools — List external tools [list_external_tools_groups]
`GET` /v1/courses/{course_id}/external_tools/sessionless_launch — Get a sessionless launch url for an external tool. [get_sessionless_launch_url_for_external_tool_courses]
`GET` /v1/accounts/{account_id}/external_tools/sessionless_launch — Get a sessionless launch url for an external tool. [get_sessionless_launch_url_for_external_tool_accounts]
`GET` /v1/courses/{course_id}/external_tools/{external_tool_id} — Get a single external tool [get_single_external_tool_courses]
`GET` /v1/accounts/{account_id}/external_tools/{external_tool_id} — Get a single external tool [get_single_external_tool_accounts]
`POST` /v1/courses/{course_id}/external_tools — Create an external tool [create_external_tool_courses]
`POST` /v1/accounts/{account_id}/external_tools — Create an external tool [create_external_tool_accounts]
`PUT` /v1/courses/{course_id}/external_tools/{external_tool_id} — Edit an external tool [edit_external_tool_courses]
`PUT` /v1/accounts/{account_id}/external_tools/{external_tool_id} — Edit an external tool [edit_external_tool_accounts]
`DELETE` /v1/courses/{course_id}/external_tools/{external_tool_id} — Delete an external tool [delete_external_tool_courses]
`DELETE` /v1/accounts/{account_id}/external_tools/{external_tool_id} — Delete an external tool [delete_external_tool_accounts]
`POST` /v1/accounts/{account_id}/external_tools/rce_favorites/{id} — Mark tool as RCE Favorite [mark_tool_as_rce_favorite]
`DELETE` /v1/accounts/{account_id}/external_tools/rce_favorites/{id} — Unmark tool as RCE Favorite [unmark_tool_as_rce_favorite]
`POST` /v1/accounts/{account_id}/external_tools/top_nav_favorites/{id} — Add tool to Top Navigation Favorites [add_tool_to_top_navigation_favorites]
`DELETE` /v1/accounts/{account_id}/external_tools/top_nav_favorites/{id} — Remove tool from Top Navigation Favorites [remove_tool_from_top_navigation_favorites]
`GET` /v1/external_tools/visible_course_nav_tools — Get visible course navigation tools [get_visible_course_navigation_tools]
`GET` /v1/courses/{course_id}/external_tools/visible_course_nav_tools — Get visible course navigation tools for a single course [get_visible_course_navigation_tools_for_single_course]

### Favorites  —  resources/favorites.md

`GET` /v1/users/self/favorites/courses — List favorite courses [list_favorite_courses]
`GET` /v1/users/self/favorites/groups — List favorite groups [list_favorite_groups]
`POST` /v1/users/self/favorites/courses/{id} — Add course to favorites [add_course_to_favorites]
`POST` /v1/users/self/favorites/groups/{id} — Add group to favorites [add_group_to_favorites]
`DELETE` /v1/users/self/favorites/courses/{id} — Remove course from favorites [remove_course_from_favorites]
`DELETE` /v1/users/self/favorites/groups/{id} — Remove group from favorites [remove_group_from_favorites]
`DELETE` /v1/users/self/favorites/courses — Reset course favorites [reset_course_favorites]
`DELETE` /v1/users/self/favorites/groups — Reset group favorites [reset_group_favorites]

### Feature Flags  —  resources/feature_flags.md

`GET` /v1/courses/{course_id}/features — List features [list_features_courses]
`GET` /v1/accounts/{account_id}/features — List features [list_features_accounts]
`GET` /v1/users/{user_id}/features — List features [list_features_users]
`GET` /v1/courses/{course_id}/features/enabled — List enabled features [list_enabled_features_courses]
`GET` /v1/accounts/{account_id}/features/enabled — List enabled features [list_enabled_features_accounts]
`GET` /v1/users/{user_id}/features/enabled — List enabled features [list_enabled_features_users]
`GET` /v1/features/environment — List environment features [list_environment_features]
`GET` /v1/courses/{course_id}/features/flags/{feature} — Get feature flag [get_feature_flag_courses]
`GET` /v1/accounts/{account_id}/features/flags/{feature} — Get feature flag [get_feature_flag_accounts]
`GET` /v1/users/{user_id}/features/flags/{feature} — Get feature flag [get_feature_flag_users]
`PUT` /v1/courses/{course_id}/features/flags/{feature} — Set feature flag [set_feature_flag_courses]
`PUT` /v1/accounts/{account_id}/features/flags/{feature} — Set feature flag [set_feature_flag_accounts]
`PUT` /v1/users/{user_id}/features/flags/{feature} — Set feature flag [set_feature_flag_users]
`DELETE` /v1/courses/{course_id}/features/flags/{feature} — Remove feature flag [remove_feature_flag_courses]
`DELETE` /v1/accounts/{account_id}/features/flags/{feature} — Remove feature flag [remove_feature_flag_accounts]
`DELETE` /v1/users/{user_id}/features/flags/{feature} — Remove feature flag [remove_feature_flag_users]

### Files  —  resources/files.md

`GET` /v1/courses/{course_id}/files/quota — Get quota information [get_quota_information_courses]
`GET` /v1/groups/{group_id}/files/quota — Get quota information [get_quota_information_groups]
`GET` /v1/users/{user_id}/files/quota — Get quota information [get_quota_information_users]
`GET` /v1/courses/{course_id}/files — List files [list_files_courses]
`GET` /v1/users/{user_id}/files — List files [list_files_users]
`GET` /v1/groups/{group_id}/files — List files [list_files_groups]
`GET` /v1/folders/{id}/files — List files [list_files_folders]
`GET` /v1/files/{id}/public_url — Get public inline preview url [get_public_inline_preview_url]
`GET` /v1/files/{id} — Get file [get_file_files]
`GET` /v1/courses/{course_id}/files/{id} — Get file [get_file_courses]
`GET` /v1/groups/{group_id}/files/{id} — Get file [get_file_groups]
`GET` /v1/users/{user_id}/files/{id} — Get file [get_file_users]
`GET` /v1/courses/{course_id}/files/file_ref/{migration_id} — Translate file reference [translate_file_reference]
`PUT` /v1/files/{id} — Update file [update_file]
`DELETE` /v1/files/{id} — Delete file [delete_file]
`GET` /v1/files/{id}/icon_metadata — Get icon metadata [get_icon_metadata]
`POST` /v1/files/{id}/reset_verifier — Reset link verifier [reset_link_verifier] (deprecated)
`GET` /v1/folders/{id}/folders — List folders [list_folders]
`GET` /v1/courses/{course_id}/folders — List all folders [list_all_folders_courses]
`GET` /v1/users/{user_id}/folders — List all folders [list_all_folders_users]
`GET` /v1/groups/{group_id}/folders — List all folders [list_all_folders_groups]
`GET` /v1/courses/{course_id}/folders/by_path/*full_path — Resolve path [resolve_path_courses_full_path]
`GET` /v1/courses/{course_id}/folders/by_path — Resolve path [resolve_path_courses]
`GET` /v1/users/{user_id}/folders/by_path/*full_path — Resolve path [resolve_path_users_full_path]
`GET` /v1/users/{user_id}/folders/by_path — Resolve path [resolve_path_users]
`GET` /v1/groups/{group_id}/folders/by_path/*full_path — Resolve path [resolve_path_groups_full_path]
`GET` /v1/groups/{group_id}/folders/by_path — Resolve path [resolve_path_groups]
`GET` /v1/courses/{course_id}/folders/{id} — Get folder [get_folder_courses]
`GET` /v1/users/{user_id}/folders/{id} — Get folder [get_folder_users]
`GET` /v1/groups/{group_id}/folders/{id} — Get folder [get_folder_groups]
`GET` /v1/folders/{id} — Get folder [get_folder_folders]
`PUT` /v1/folders/{id} — Update folder [update_folder]
`POST` /v1/courses/{course_id}/folders — Create folder [create_folder_courses]
`POST` /v1/users/{user_id}/folders — Create folder [create_folder_users]
`POST` /v1/groups/{group_id}/folders — Create folder [create_folder_groups]
`POST` /v1/folders/{folder_id}/folders — Create folder [create_folder_folders]
`POST` /v1/accounts/{account_id}/folders — Create folder [create_folder_accounts]
`DELETE` /v1/folders/{id} — Delete folder [delete_folder]
`POST` /v1/folders/{folder_id}/files — Upload a file [upload_file]
`POST` /v1/folders/{dest_folder_id}/copy_file — Copy a file [copy_file]
`POST` /v1/folders/{dest_folder_id}/copy_folder — Copy a folder [copy_folder]
`GET` /v1/courses/{course_id}/folders/media — Get uploaded media folder for user [get_uploaded_media_folder_for_user_courses]
`GET` /v1/groups/{group_id}/folders/media — Get uploaded media folder for user [get_uploaded_media_folder_for_user_groups]
`PUT` /v1/courses/{course_id}/usage_rights — Set usage rights [set_usage_rights_courses]
`PUT` /v1/groups/{group_id}/usage_rights — Set usage rights [set_usage_rights_groups]
`PUT` /v1/users/{user_id}/usage_rights — Set usage rights [set_usage_rights_users]
`DELETE` /v1/courses/{course_id}/usage_rights — Remove usage rights [remove_usage_rights_courses]
`DELETE` /v1/groups/{group_id}/usage_rights — Remove usage rights [remove_usage_rights_groups]
`DELETE` /v1/users/{user_id}/usage_rights — Remove usage rights [remove_usage_rights_users]
`GET` /v1/courses/{course_id}/content_licenses — List licenses [list_licenses_courses]
`GET` /v1/groups/{group_id}/content_licenses — List licenses [list_licenses_groups]
`GET` /v1/users/{user_id}/content_licenses — List licenses [list_licenses_users]

### Grade Change Log  —  resources/grade_change_log.md

`GET` /v1/audit/grade_change/assignments/{assignment_id} — Query by assignment [query_by_assignment]
`GET` /v1/audit/grade_change/courses/{course_id} — Query by course [query_by_course]
`GET` /v1/audit/grade_change/students/{student_id} — Query by student [query_by_student]
`GET` /v1/audit/grade_change/graders/{grader_id} — Query by grader [query_by_grader]
`GET` /v1/audit/grade_change — Advanced query [advanced_query]

### Gradebook History  —  resources/gradebook_history.md

`GET` /v1/courses/{course_id}/gradebook_history/days — Days in gradebook history for this course [days_in_gradebook_history_for_this_course]
`GET` /v1/courses/{course_id}/gradebook_history/{date} — Details for a given date in gradebook history for this course [details_for_given_date_in_gradebook_history_for_this_course]
`GET` /v1/courses/{course_id}/gradebook_history/{date}/graders/{grader_id}/assignments/{assignment_id}/submissions — Lists submissions [lists_submissions]
`GET` /v1/courses/{course_id}/gradebook_history/feed — List uncollated submission versions [list_uncollated_submission_versions]

### Grading Period Sets  —  resources/grading_period_sets.md

`GET` /v1/accounts/{account_id}/grading_period_sets — List grading period sets [list_grading_period_sets]
`POST` /v1/accounts/{account_id}/grading_period_sets — Create a grading period set [create_grading_period_set]
`PATCH` /v1/accounts/{account_id}/grading_period_sets/{id} — Update a grading period set [update_grading_period_set]
`DELETE` /v1/accounts/{account_id}/grading_period_sets/{id} — Delete a grading period set [delete_grading_period_set]

### Grading Periods  —  resources/grading_periods.md

`GET` /v1/accounts/{account_id}/grading_periods — List grading periods [list_grading_periods_accounts]
`GET` /v1/courses/{course_id}/grading_periods — List grading periods [list_grading_periods_courses]
`GET` /v1/courses/{course_id}/grading_periods/{id} — Get a single grading period [get_single_grading_period]
`PUT` /v1/courses/{course_id}/grading_periods/{id} — Update a single grading period [update_single_grading_period]
`DELETE` /v1/courses/{course_id}/grading_periods/{id} — Delete a grading period [delete_grading_period_courses]
`DELETE` /v1/accounts/{account_id}/grading_periods/{id} — Delete a grading period [delete_grading_period_accounts]
`PATCH` /v1/courses/{course_id}/grading_periods/batch_update — Batch update grading periods [batch_update_grading_periods_courses]
`PATCH` /v1/grading_period_sets/{set_id}/grading_periods/batch_update — Batch update grading periods [batch_update_grading_periods_grading_period_sets]

### Grading Standards  —  resources/grading_standards.md

`POST` /v1/accounts/{account_id}/grading_standards — Create a new grading standard [create_new_grading_standard_accounts]
`POST` /v1/courses/{course_id}/grading_standards — Create a new grading standard [create_new_grading_standard_courses]
`GET` /v1/courses/{course_id}/grading_standards — List the grading standards available in a context. [list_grading_standards_available_in_context_courses]
`GET` /v1/accounts/{account_id}/grading_standards — List the grading standards available in a context. [list_grading_standards_available_in_context_accounts]
`GET` /v1/courses/{course_id}/grading_standards/{grading_standard_id} — Get a single grading standard in a context. [get_single_grading_standard_in_context_courses]
`GET` /v1/accounts/{account_id}/grading_standards/{grading_standard_id} — Get a single grading standard in a context. [get_single_grading_standard_in_context_accounts]
`PUT` /v1/courses/{course_id}/grading_standards/{grading_standard_id} — Update a grading standard [update_grading_standard_courses]
`PUT` /v1/accounts/{account_id}/grading_standards/{grading_standard_id} — Update a grading standard [update_grading_standard_accounts]
`DELETE` /v1/courses/{course_id}/grading_standards/{grading_standard_id} — Delete a grading standard [delete_grading_standard_courses]
`DELETE` /v1/accounts/{account_id}/grading_standards/{grading_standard_id} — Delete a grading standard [delete_grading_standard_accounts]

### Group Categories  —  resources/group_categories.md

`GET` /v1/accounts/{account_id}/group_categories — List group categories for a context [list_group_categories_for_context_accounts]
`GET` /v1/courses/{course_id}/group_categories — List group categories for a context [list_group_categories_for_context_courses]
`GET` /v1/group_categories/{group_category_id} — Get a single group category [get_single_group_category]
`POST` /v1/accounts/{account_id}/group_categories — Create a Group Category [create_group_category_accounts]
`POST` /v1/courses/{course_id}/group_categories — Create a Group Category [create_group_category_courses]
`POST` /v1/courses/{course_id}/group_categories/bulk_manage_differentiation_tag — Bulk manage differentiation tags [bulk_manage_differentiation_tags]
`POST` /v1/courses/{course_id}/group_categories/import_tags — Import differentiation tags [import_differentiation_tags]
`POST` /v1/group_categories/{group_category_id}/import — Import category groups [import_category_groups]
`PUT` /v1/group_categories/{group_category_id} — Update a Group Category [update_group_category]
`DELETE` /v1/group_categories/{group_category_id} — Delete a Group Category [delete_group_category]
`GET` /v1/group_categories/{group_category_id}/groups — List groups in group category [list_groups_in_group_category]
`GET` /v1/group_categories/{group_category_id}/export — export groups in and users in category [export_groups_in_and_users_in_category]
`GET` /v1/courses/{course_id}/group_categories/export_tags — export tags and users in course [export_tags_and_users_in_course]
`GET` /v1/group_categories/{group_category_id}/users — List users in group category [list_users_in_group_category]
`POST` /v1/group_categories/{group_category_id}/assign_unassigned_members — Assign unassigned members [assign_unassigned_members]

### Groups  —  resources/groups.md

`GET` /v1/users/self/groups — List your groups [list_your_groups]
`GET` /v1/accounts/{account_id}/groups — List the groups available in a context. [list_groups_available_in_context_accounts]
`GET` /v1/courses/{course_id}/groups — List the groups available in a context. [list_groups_available_in_context_courses]
`GET` /v1/courses/{course_id}/bulk_user_tags — Bulk fetch user tags for multiple users in a course [bulk_fetch_user_tags_for_multiple_users_in_course]
`GET` /v1/groups/{group_id} — Get a single group [get_single_group]
`POST` /v1/groups — Create a group [create_group_groups]
`POST` /v1/group_categories/{group_category_id}/groups — Create a group [create_group_group_categories]
`PUT` /v1/groups/{group_id} — Edit a group [edit_group]
`DELETE` /v1/groups/{group_id} — Delete a group [delete_group]
`POST` /v1/groups/{group_id}/invite — Invite others to a group [invite_others_to_group]
`GET` /v1/groups/{group_id}/users — List group's users [list_group_s_users]
`POST` /v1/groups/{group_id}/files — Upload a file [upload_file]
`POST` /v1/groups/{group_id}/preview_html — Preview processed html [preview_processed_html]
`GET` /v1/groups/{group_id}/activity_stream — Group activity stream [group_activity_stream]
`GET` /v1/groups/{group_id}/activity_stream/summary — Group activity stream summary [group_activity_stream_summary]
`GET` /v1/groups/{group_id}/permissions — Permissions [permissions]
`GET` /v1/groups/{group_id}/memberships — List group memberships [list_group_memberships]
`GET` /v1/groups/{group_id}/memberships/{membership_id} — Get a single group membership [get_single_group_membership_memberships]
`GET` /v1/groups/{group_id}/users/{user_id} — Get a single group membership [get_single_group_membership_users]
`POST` /v1/groups/{group_id}/memberships — Create a membership [create_membership]
`PUT` /v1/groups/{group_id}/memberships/{membership_id} — Update a membership [update_membership_memberships]
`PUT` /v1/groups/{group_id}/users/{user_id} — Update a membership [update_membership_users]
`DELETE` /v1/groups/{group_id}/memberships/{membership_id} — Leave a group [leave_group_memberships]
`DELETE` /v1/groups/{group_id}/users/{user_id} — Leave a group [leave_group_users]
`DELETE` /v1/groups/{group_id}/users — Bulk delete memberships
Bulk deletes memberships by providing an array of user IDs. [bulk_delete_memberships_bulk_deletes_memberships_by_providing_array_of_user_ids]

### History  —  resources/history.md

`GET` /v1/users/{user_id}/history — List recent history for a user [list_recent_history_for_user]

### InstAccess tokens  —  resources/inst_access_tokens.md

`POST` /v1/inst_access_tokens — Create InstAccess token [create_instaccess_token]

### JWTs  —  resources/jw_ts.md

`POST` /v1/jwts — Create JWT [create_jwt]
`POST` /v1/jwts/refresh — Refresh JWT [refresh_jwt]

### Late Policy  —  resources/late_policy.md

`GET` /v1/courses/{id}/late_policy — Get a late policy [get_late_policy]
`POST` /v1/courses/{id}/late_policy — Create a late policy [create_late_policy]
`PATCH` /v1/courses/{id}/late_policy — Patch a late policy [patch_late_policy]

### Learning Object Dates  —  resources/learning_object_dates.md

`GET` /v1/courses/{course_id}/modules/{context_module_id}/date_details — Get a learning object's date information [get_learning_object_s_date_information_modules]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/date_details — Get a learning object's date information [get_learning_object_s_date_information_assignments]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/date_details — Get a learning object's date information [get_learning_object_s_date_information_quizzes]
`GET` /v1/courses/{course_id}/discussion_topics/{discussion_topic_id}/date_details — Get a learning object's date information [get_learning_object_s_date_information_discussion_topics]
`GET` /v1/courses/{course_id}/pages/{url_or_id}/date_details — Get a learning object's date information [get_learning_object_s_date_information_pages]
`GET` /v1/courses/{course_id}/files/{attachment_id}/date_details — Get a learning object's date information [get_learning_object_s_date_information_files]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/date_details — Update a learning object's date information [update_learning_object_s_date_information_assignments]
`PUT` /v1/courses/{course_id}/quizzes/{quiz_id}/date_details — Update a learning object's date information [update_learning_object_s_date_information_quizzes]
`PUT` /v1/courses/{course_id}/discussion_topics/{discussion_topic_id}/date_details — Update a learning object's date information [update_learning_object_s_date_information_discussion_topics]
`PUT` /v1/courses/{course_id}/pages/{url_or_id}/date_details — Update a learning object's date information [update_learning_object_s_date_information_pages]
`PUT` /v1/courses/{course_id}/files/{attachment_id}/date_details — Update a learning object's date information [update_learning_object_s_date_information_files]

### Line Items  —  resources/line_items.md

`POST` /lti/courses/{course_id}/line_items — Create a Line Item [create_line_item]
`PUT` /lti/courses/{course_id}/line_items/{id} — Update a Line Item [update_line_item]
`GET` /lti/courses/{course_id}/line_items/{id} — Show a Line Item [show_line_item]
`GET` /lti/courses/{course_id}/line_items — List line Items [list_line_items]
`DELETE` /lti/courses/{course_id}/line_items/{id} — Delete a Line Item [delete_line_item]

### LiveAssessments  —  resources/live_assessments.md

`POST` /v1/courses/{course_id}/live_assessments/{assessment_id}/results — Create live assessment results [create_live_assessment_results]
`GET` /v1/courses/{course_id}/live_assessments/{assessment_id}/results — List live assessment results [list_live_assessment_results]
`POST` /v1/courses/{course_id}/live_assessments — Create or find a live assessment [create_or_find_live_assessment]
`GET` /v1/courses/{course_id}/live_assessments — List live assessments [list_live_assessments]

### Logins  —  resources/logins.md

`GET` /v1/accounts/{account_id}/logins — List user logins [list_user_logins_accounts]
`GET` /v1/users/{user_id}/logins — List user logins [list_user_logins_users]
`POST` /v1/users/reset_password — Kickoff password recovery flow [kickoff_password_recovery_flow]
`POST` /v1/accounts/{account_id}/logins — Create a user login [create_user_login]
`PUT` /v1/accounts/{account_id}/logins/{id} — Edit a user login [edit_user_login]
`DELETE` /v1/users/{user_id}/logins/{id} — Delete a user login [delete_user_login]

### LTI 2 Authorization  —  resources/lti_2_authorization.md

`POST` /lti/courses/{course_id}/authorize — authorize [authorize_courses]
`POST` /lti/accounts/{account_id}/authorize — authorize [authorize_accounts]

### LTI Advantage Feature Flags  —  resources/lti_advantage_feature_flags.md

`GET` /lti/courses/{course_id}/feature_flags/{feature} — Show the specified feature flag [show_specified_feature_flag_courses]
`GET` /lti/accounts/{account_id}/feature_flags/{feature} — Show the specified feature flag [show_specified_feature_flag_accounts]

### LTI ContextControls  —  resources/lti_context_controls.md

`GET` /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls — List All Context Controls [list_all_context_controls]
`GET` /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id} — Show LTI Context Control [show_lti_context_control]
`POST` /v1/accounts/{current_account_id}/lti_registrations/{registration_id}/controls — Create LTI Context Control [create_lti_context_control]
`POST` /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/bulk — Bulk Create LTI Context Controls [bulk_create_lti_context_controls]
`PUT` /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id} — Modify a Context Control [modify_context_control]
`DELETE` /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id} — Delete a Context Control [delete_context_control]

### LTI Deployments  —  resources/lti_deployments.md

`GET` /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id} — Show LTI Deployment [show_lti_deployment]
`POST` /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments — Create LTI Deployment [create_lti_deployment]
`DELETE` /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id} — Delete LTI Deployment [delete_lti_deployment]
`GET` /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments — List LTI Deployments [list_lti_deployments]
`GET` /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id}/controls — List LTI Context Controls [list_lti_context_controls]

### LTI Dynamic Registrations  —  resources/lti_dynamic_registrations.md

`GET` /lti/registrations/{registration_id} — Get Dynamic Registration Configuration [get_dynamic_registration_configuration]
`POST` /lti/registrations — Create a Dynamic Registration [create_dynamic_registration]

### LTI Launch Definitions  —  resources/lti_launch_definitions.md

`GET` /v1/courses/{course_id}/lti_apps/launch_definitions — List LTI Launch Definitions [list_lti_launch_definitions_courses]
`GET` /v1/accounts/{account_id}/lti_apps/launch_definitions — List LTI Launch Definitions [list_lti_launch_definitions_accounts]

### LTI Registrations  —  resources/lti_registrations.md

`GET` /v1/accounts/{account_id}/lti_registrations — List LTI Registrations in an account [list_lti_registrations_in_account]
`GET` /v1/accounts/{account_id}/lti_registrations/{id} — Show an LTI Registration [show_lti_registration]
`POST` /v1/accounts/{account_id}/lti_registrations — Create an LTI Registration [create_lti_registration]
`GET` /v1/accounts/{account_id}/lti_registration_by_client_id/{client_id} — Show an LTI Registration (via the client_id) [show_lti_registration_via_client_id]
`GET` /v1/accounts/{account_id}/lti_registrations/by_utid/{utid} — Get LTI Registration by Unified Tool ID [get_lti_registration_by_unified_tool_id]
`GET` /v1/accounts/{account_id}/lti_registrations/install_status/{client_id} — Check LTI Registration Install Status [check_lti_registration_install_status]
`PUT` /v1/accounts/{account_id}/lti_registrations/{id} — Update an LTI Registration [update_lti_registration]
`PUT` /v1/accounts/{account_id}/lti_registrations/{id}/reset — Reset an LTI Registration to Defaults [reset_lti_registration_to_defaults]
`DELETE` /v1/accounts/{account_id}/lti_registrations/{id} — Delete an LTI Registration [delete_lti_registration]
`POST` /v1/accounts/{account_id}/lti_registrations/{id}/bind — Bind an LTI Registration to a Root Account [bind_lti_registration_to_root_account]
`DELETE` /v1/accounts/{account_id}/lti_registrations/{id}/bind — Remove an Inherited LTI Registration [remove_inherited_lti_registration]
`POST` /v1/accounts/{account_id}/lti_registrations/{id}/install_from_template — Install an LTI Registration from a Template [install_lti_registration_from_template]
`GET` /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{deployment_id}/context_search — Search for Accounts and Courses [search_for_accounts_and_courses]
`GET` /v1/accounts/{account_id}/lti_registrations/{id}/overlay_history — Get LTI Registration Overlay History [get_lti_registration_overlay_history]
`GET` /v1/accounts/{account_id}/lti_registrations/{id}/history — Get LTI Registration History [get_lti_registration_history]
`GET` /v1/accounts/{account_id}/lti_registrations/{id}/update_requests/{update_request_id} — Get LTI Registration Update Request [get_lti_registration_update_request]
`GET` /v1/accounts/{account_id}/lti_registrations/{id}/latest_update_request — Get Latest LTI Registration Update Request [get_latest_lti_registration_update_request]
`PUT` /v1/accounts/{account_id}/lti_registrations/{id}/update_requests/{update_request_id}/apply — Apply LTI Registration Update Requst [apply_lti_registration_update_requst]

### LTI Resource Links  —  resources/lti_resource_links.md

`GET` /v1/courses/{course_id}/lti_resource_links — List LTI Resource Links [list_lti_resource_links]
`GET` /v1/courses/{course_id}/lti_resource_links/{id} — Show an LTI Resource Link [show_lti_resource_link]
`POST` /v1/courses/{course_id}/lti_resource_links — Create an LTI Resource Link [create_lti_resource_link]
`POST` /v1/courses/{course_id}/lti_resource_links/bulk — Bulk Create LTI Resource Links [bulk_create_lti_resource_links]
`PUT` /v1/courses/{course_id}/lti_resource_links/{id} — Update an LTI Resource Link [update_lti_resource_link]
`DELETE` /v1/courses/{course_id}/lti_resource_links/{id} — Delete an LTI Resource Link [delete_lti_resource_link]

### Media Objects  —  resources/media_objects.md

`GET` /v1/media_objects/{media_object_id}/media_tracks — List media tracks for a Media Object or Attachment [list_media_tracks_for_media_object_or_attachment_media_objects]
`GET` /v1/media_attachments/{attachment_id}/media_tracks — List media tracks for a Media Object or Attachment [list_media_tracks_for_media_object_or_attachment_media_attachments]
`PUT` /v1/media_objects/{media_object_id}/media_tracks — Update Media Tracks [update_media_tracks_media_objects]
`PUT` /v1/media_attachments/{attachment_id}/media_tracks — Update Media Tracks [update_media_tracks_media_attachments]
`GET` /v1/media_objects — List Media Objects [list_media_objects_media_objects]
`GET` /v1/courses/{course_id}/media_objects — List Media Objects [list_media_objects_courses_media_objects]
`GET` /v1/groups/{group_id}/media_objects — List Media Objects [list_media_objects_groups_media_objects]
`GET` /v1/media_attachments — List Media Objects [list_media_objects_media_attachments]
`GET` /v1/courses/{course_id}/media_attachments — List Media Objects [list_media_objects_courses_media_attachments]
`GET` /v1/groups/{group_id}/media_attachments — List Media Objects [list_media_objects_groups_media_attachments]
`PUT` /v1/media_objects/{media_object_id} — Update Media Object [update_media_object_media_objects]
`PUT` /v1/media_attachments/{attachment_id} — Update Media Object [update_media_object_media_attachments]

### Microsoft Sync - Groups  —  resources/microsoft_sync___groups.md


### Moderated Grading  —  resources/moderated_grading.md

`GET` /v1/courses/{course_id}/assignments/{assignment_id}/moderated_students — List students selected for moderation [list_students_selected_for_moderation]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/moderated_students — Select students for moderation [select_students_for_moderation]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/bulk_select — Bulk select provisional grades [bulk_select_provisional_grades]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/status — Show provisional grade status for a student [show_provisional_grade_status_for_student]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/select — Select provisional grade [select_provisional_grade]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/publish — Publish provisional grades for an assignment [publish_provisional_grades_for_assignment]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/anonymous_provisional_grades/status — Show provisional grade status for a student [show_provisional_grade_status_for_student]

### Modules  —  resources/modules.md

`GET` /v1/courses/{course_id}/modules — List modules [list_modules]
`GET` /v1/courses/{course_id}/modules/{id} — Show module [show_module]
`POST` /v1/courses/{course_id}/modules — Create a module [create_module]
`PUT` /v1/courses/{course_id}/modules/{id} — Update a module [update_module]
`DELETE` /v1/courses/{course_id}/modules/{id} — Delete module [delete_module]
`PUT` /v1/courses/{course_id}/modules/{id}/relock — Re-lock module progressions [re_lock_module_progressions]
`GET` /v1/courses/{course_id}/modules/{module_id}/items — List module items [list_module_items]
`GET` /v1/courses/{course_id}/modules/{module_id}/items/{id} — Show module item [show_module_item]
`POST` /v1/courses/{course_id}/modules/{module_id}/items — Create a module item [create_module_item]
`PUT` /v1/courses/{course_id}/modules/{module_id}/items/{id} — Update a module item [update_module_item]
`POST` /v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path — Select a mastery path [select_mastery_path]
`DELETE` /v1/courses/{course_id}/modules/{module_id}/items/{id} — Delete module item [delete_module_item]
`PUT` /v1/courses/{course_id}/modules/{module_id}/items/{id}/done — Mark module item as done/not done [mark_module_item_as_done_not_done]
`GET` /v1/courses/{course_id}/module_item_sequence — Get module item sequence [get_module_item_sequence]
`POST` /v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read — Mark module item read [mark_module_item_read]
`GET` /v1/courses/{course_id}/modules/{context_module_id}/assignment_overrides — List a module's overrides [list_module_s_overrides]
`PUT` /v1/courses/{course_id}/modules/{context_module_id}/assignment_overrides — Update a module's overrides [update_module_s_overrides]

### Names and Role  —  resources/names_and_role.md

`GET` /lti/courses/{course_id}/names_and_roles — List Course Memberships [list_course_memberships]
`GET` /lti/groups/{group_id}/names_and_roles — List Group Memberships [list_group_memberships]

### Notice Handlers  —  resources/notice_handlers.md

`GET` /lti/notice-handlers/{context_external_tool_id} — Show notice handlers [show_notice_handlers]
`PUT` /lti/notice-handlers/{context_external_tool_id} — Set notice handler [set_notice_handler]

### Notification Preferences  —  resources/notification_preferences.md

`GET` /v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences — List preferences [list_preferences_communication_channel_id]
`GET` /v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences — List preferences [list_preferences_type]
`GET` /v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories — List of preference categories [list_of_preference_categories]
`GET` /v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences/{notification} — Get a preference [get_preference_communication_channel_id]
`GET` /v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences/{notification} — Get a preference [get_preference_type]
`PUT` /v1/users/self/communication_channels/{communication_channel_id}/notification_preferences/{notification} — Update a preference [update_preference_communication_channel_id]
`PUT` /v1/users/self/communication_channels/{type}/{address}/notification_preferences/{notification} — Update a preference [update_preference_type]
`PUT` /v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category} — Update preferences by category [update_preferences_by_category]
`PUT` /v1/users/self/communication_channels/{communication_channel_id}/notification_preferences — Update multiple preferences [update_multiple_preferences_communication_channel_id]
`PUT` /v1/users/self/communication_channels/{type}/{address}/notification_preferences — Update multiple preferences [update_multiple_preferences_type]

### Originality Reports  —  resources/originality_reports.md

`POST` /lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report — Create an Originality Report [create_originality_report]
`PUT` /lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id} — Edit an Originality Report [edit_originality_report_submissions]
`PUT` /lti/assignments/{assignment_id}/files/{file_id}/originality_report — Edit an Originality Report [edit_originality_report_files]
`GET` /lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id} — Show an Originality Report [show_originality_report_submissions]
`GET` /lti/assignments/{assignment_id}/files/{file_id}/originality_report — Show an Originality Report [show_originality_report_files]

### Outcome Groups  —  resources/outcome_groups.md

`GET` /v1/global/root_outcome_group — Redirect to root outcome group for context [redirect_to_root_outcome_group_for_context_global]
`GET` /v1/accounts/{account_id}/root_outcome_group — Redirect to root outcome group for context [redirect_to_root_outcome_group_for_context_accounts]
`GET` /v1/courses/{course_id}/root_outcome_group — Redirect to root outcome group for context [redirect_to_root_outcome_group_for_context_courses]
`GET` /v1/accounts/{account_id}/outcome_groups — Get all outcome groups for context [get_all_outcome_groups_for_context_accounts]
`GET` /v1/courses/{course_id}/outcome_groups — Get all outcome groups for context [get_all_outcome_groups_for_context_courses]
`GET` /v1/accounts/{account_id}/outcome_group_links — Get all outcome links for context [get_all_outcome_links_for_context_accounts]
`GET` /v1/courses/{course_id}/outcome_group_links — Get all outcome links for context [get_all_outcome_links_for_context_courses]
`GET` /v1/global/outcome_groups/{id} — Show an outcome group [show_outcome_group_global]
`GET` /v1/accounts/{account_id}/outcome_groups/{id} — Show an outcome group [show_outcome_group_accounts]
`GET` /v1/courses/{course_id}/outcome_groups/{id} — Show an outcome group [show_outcome_group_courses]
`PUT` /v1/global/outcome_groups/{id} — Update an outcome group [update_outcome_group_global]
`PUT` /v1/accounts/{account_id}/outcome_groups/{id} — Update an outcome group [update_outcome_group_accounts]
`PUT` /v1/courses/{course_id}/outcome_groups/{id} — Update an outcome group [update_outcome_group_courses]
`DELETE` /v1/global/outcome_groups/{id} — Delete an outcome group [delete_outcome_group_global]
`DELETE` /v1/accounts/{account_id}/outcome_groups/{id} — Delete an outcome group [delete_outcome_group_accounts]
`DELETE` /v1/courses/{course_id}/outcome_groups/{id} — Delete an outcome group [delete_outcome_group_courses]
`GET` /v1/global/outcome_groups/{id}/outcomes — List linked outcomes [list_linked_outcomes_global]
`GET` /v1/accounts/{account_id}/outcome_groups/{id}/outcomes — List linked outcomes [list_linked_outcomes_accounts]
`GET` /v1/courses/{course_id}/outcome_groups/{id}/outcomes — List linked outcomes [list_linked_outcomes_courses]
`POST` /v1/global/outcome_groups/{id}/outcomes — Create/link an outcome [create_link_outcome_global]
`PUT` /v1/global/outcome_groups/{id}/outcomes/{outcome_id} — Create/link an outcome [create_link_outcome_global_outcome_id]
`POST` /v1/accounts/{account_id}/outcome_groups/{id}/outcomes — Create/link an outcome [create_link_outcome_accounts]
`PUT` /v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id} — Create/link an outcome [create_link_outcome_accounts_outcome_id]
`POST` /v1/courses/{course_id}/outcome_groups/{id}/outcomes — Create/link an outcome [create_link_outcome_courses]
`PUT` /v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id} — Create/link an outcome [create_link_outcome_courses_outcome_id]
`DELETE` /v1/global/outcome_groups/{id}/outcomes/{outcome_id} — Unlink an outcome [unlink_outcome_global]
`DELETE` /v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id} — Unlink an outcome [unlink_outcome_accounts]
`DELETE` /v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id} — Unlink an outcome [unlink_outcome_courses]
`GET` /v1/global/outcome_groups/{id}/subgroups — List subgroups [list_subgroups_global]
`GET` /v1/accounts/{account_id}/outcome_groups/{id}/subgroups — List subgroups [list_subgroups_accounts]
`GET` /v1/courses/{course_id}/outcome_groups/{id}/subgroups — List subgroups [list_subgroups_courses]
`POST` /v1/global/outcome_groups/{id}/subgroups — Create a subgroup [create_subgroup_global]
`POST` /v1/accounts/{account_id}/outcome_groups/{id}/subgroups — Create a subgroup [create_subgroup_accounts]
`POST` /v1/courses/{course_id}/outcome_groups/{id}/subgroups — Create a subgroup [create_subgroup_courses]
`POST` /v1/global/outcome_groups/{id}/import — Import an outcome group [import_outcome_group_global]
`POST` /v1/accounts/{account_id}/outcome_groups/{id}/import — Import an outcome group [import_outcome_group_accounts]
`POST` /v1/courses/{course_id}/outcome_groups/{id}/import — Import an outcome group [import_outcome_group_courses]

### Outcome Imports  —  resources/outcome_imports.md

`POST` /v1/accounts/{account_id}/outcome_imports — Import Outcomes [import_outcomes_accounts]
`POST` /v1/courses/{course_id}/outcome_imports — Import Outcomes [import_outcomes_courses]
`GET` /v1/accounts/{account_id}/outcome_imports/{id} — Get Outcome import status [get_outcome_import_status_accounts]
`GET` /v1/courses/{course_id}/outcome_imports/{id} — Get Outcome import status [get_outcome_import_status_courses]
`GET` /v1/accounts/{account_id}/outcome_imports/{id}/created_group_ids — Get IDs of outcome groups created after successful import [get_ids_of_outcome_groups_created_after_successful_import_accounts]
`GET` /v1/courses/{course_id}/outcome_imports/{id}/created_group_ids — Get IDs of outcome groups created after successful import [get_ids_of_outcome_groups_created_after_successful_import_courses]

### Outcome Results  —  resources/outcome_results.md

`GET` /v1/courses/{course_id}/outcome_results — Get outcome results [get_outcome_results]
`POST` /v1/courses/{course_id}/assign_outcome_order — Set outcome ordering for LMGB [set_outcome_ordering_for_lmgb]
`GET` /v1/courses/{course_id}/outcome_rollups — Get outcome result rollups [get_outcome_result_rollups]
`GET` /v1/courses/{course_id}/outcomes/{outcome_id}/contributing_scores — Get contributing scores [get_contributing_scores]
`GET` /v1/courses/{course_id}/outcome_mastery_distribution — Get mastery distribution [get_mastery_distribution]
`POST` /v1/enqueue_outcome_rollup_calculation — Enqueue a delayed Outcome Rollup Calculation Job [enqueue_delayed_outcome_rollup_calculation_job]

### Outcomes  —  resources/outcomes.md

`GET` /v1/outcomes/{id} — Show an outcome [show_outcome]
`PUT` /v1/outcomes/{id} — Update an outcome [update_outcome]
`GET` /v1/courses/{course_id}/outcome_alignments — Get outcome alignments for a student or assignment [get_outcome_alignments_for_student_or_assignment]

### Pages  —  resources/pages.md

`GET` /v1/courses/{course_id}/front_page — Show front page [show_front_page_courses]
`GET` /v1/groups/{group_id}/front_page — Show front page [show_front_page_groups]
`POST` /v1/courses/{course_id}/pages/{url_or_id}/duplicate — Duplicate page [duplicate_page]
`PUT` /v1/courses/{course_id}/front_page — Update/create front page [update_create_front_page_courses]
`PUT` /v1/groups/{group_id}/front_page — Update/create front page [update_create_front_page_groups]
`GET` /v1/courses/{course_id}/pages — List pages [list_pages_courses]
`GET` /v1/groups/{group_id}/pages — List pages [list_pages_groups]
`POST` /v1/courses/{course_id}/pages — Create page [create_page_courses]
`POST` /v1/groups/{group_id}/pages — Create page [create_page_groups]
`GET` /v1/courses/{course_id}/pages/{url_or_id} — Show page [show_page_courses]
`GET` /v1/groups/{group_id}/pages/{url_or_id} — Show page [show_page_groups]
`PUT` /v1/courses/{course_id}/pages/{url_or_id} — Update/create page [update_create_page_courses]
`PUT` /v1/groups/{group_id}/pages/{url_or_id} — Update/create page [update_create_page_groups]
`DELETE` /v1/courses/{course_id}/pages/{url_or_id} — Delete page [delete_page_courses]
`DELETE` /v1/groups/{group_id}/pages/{url_or_id} — Delete page [delete_page_groups]
`GET` /v1/courses/{course_id}/pages/{url_or_id}/revisions — List revisions [list_revisions_courses]
`GET` /v1/groups/{group_id}/pages/{url_or_id}/revisions — List revisions [list_revisions_groups]
`GET` /v1/courses/{course_id}/pages/{url_or_id}/revisions/latest — Show revision [show_revision_courses_latest]
`GET` /v1/groups/{group_id}/pages/{url_or_id}/revisions/latest — Show revision [show_revision_groups_latest]
`GET` /v1/courses/{course_id}/pages/{url_or_id}/revisions/{revision_id} — Show revision [show_revision_courses_revision_id]
`GET` /v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id} — Show revision [show_revision_groups_revision_id]
`POST` /v1/courses/{course_id}/pages/{url_or_id}/revisions/{revision_id} — Revert to revision [revert_to_revision_courses]
`POST` /v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id} — Revert to revision [revert_to_revision_groups]

### Peer Reviews  —  resources/peer_reviews.md

`GET` /v1/courses/{course_id}/assignments/{assignment_id}/peer_reviews — Get all Peer Reviews [get_all_peer_reviews_courses_peer_reviews]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/peer_reviews — Get all Peer Reviews [get_all_peer_reviews_sections_peer_reviews]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews — Get all Peer Reviews [get_all_peer_reviews_courses_submissions]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews — Get all Peer Reviews [get_all_peer_reviews_sections_submissions]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews — Create Peer Review [create_peer_review_courses]
`POST` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews — Create Peer Review [create_peer_review_sections]
`DELETE` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews — Delete Peer Review [delete_peer_review_courses]
`DELETE` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews — Delete Peer Review [delete_peer_review_sections]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/allocate — Allocate Peer Review [allocate_peer_review]

### Plagiarism Detection Platform Assignments  —  resources/plagiarism_detection_platform_assignments.md

`GET` /lti/assignments/{assignment_id} — Get a single assignment (lti) [get_single_assignment_lti]

### Plagiarism Detection Platform Users  —  resources/plagiarism_detection_platform_users.md

`GET` /lti/users/{id} — Get a single user (lti) [get_single_user_lti]
`GET` /lti/groups/{group_id}/users — Get all users in a group (lti) [get_all_users_in_group_lti]

### Plagiarism Detection Submissions  —  resources/plagiarism_detection_submissions.md

`GET` /lti/assignments/{assignment_id}/submissions/{submission_id} — Get a single submission [get_single_submission]
`GET` /lti/assignments/{assignment_id}/submissions/{submission_id}/history — Get the history of a single submission [get_history_of_single_submission]

### Planner  —  resources/planner.md

`GET` /v1/planner/items — List planner items [list_planner_items_planner]
`GET` /v1/users/{user_id}/planner/items — List planner items [list_planner_items_users]
`GET` /v1/planner_notes — List planner notes [list_planner_notes]
`GET` /v1/planner_notes/{id} — Show a planner note [show_planner_note]
`PUT` /v1/planner_notes/{id} — Update a planner note [update_planner_note]
`POST` /v1/planner_notes — Create a planner note [create_planner_note]
`DELETE` /v1/planner_notes/{id} — Delete a planner note [delete_planner_note]
`GET` /v1/planner/overrides — List planner overrides [list_planner_overrides]
`GET` /v1/planner/overrides/{id} — Show a planner override [show_planner_override]
`PUT` /v1/planner/overrides/{id} — Update a planner override [update_planner_override]
`POST` /v1/planner/overrides — Create a planner override [create_planner_override]
`DELETE` /v1/planner/overrides/{id} — Delete a planner override [delete_planner_override]

### Poll Sessions  —  resources/poll_sessions.md

`GET` /v1/polls/{poll_id}/poll_sessions — List poll sessions for a poll [list_poll_sessions_for_poll]
`GET` /v1/polls/{poll_id}/poll_sessions/{id} — Get the results for a single poll session [get_results_for_single_poll_session]
`POST` /v1/polls/{poll_id}/poll_sessions — Create a single poll session [create_single_poll_session]
`PUT` /v1/polls/{poll_id}/poll_sessions/{id} — Update a single poll session [update_single_poll_session]
`DELETE` /v1/polls/{poll_id}/poll_sessions/{id} — Delete a poll session [delete_poll_session]
`GET` /v1/polls/{poll_id}/poll_sessions/{id}/open — Open a poll session [open_poll_session]
`GET` /v1/polls/{poll_id}/poll_sessions/{id}/close — Close an opened poll session [close_opened_poll_session]
`GET` /v1/poll_sessions/opened — List opened poll sessions [list_opened_poll_sessions]
`GET` /v1/poll_sessions/closed — List closed poll sessions [list_closed_poll_sessions]

### PollChoices  —  resources/poll_choices.md

`GET` /v1/polls/{poll_id}/poll_choices — List poll choices in a poll [list_poll_choices_in_poll]
`GET` /v1/polls/{poll_id}/poll_choices/{id} — Get a single poll choice [get_single_poll_choice]
`POST` /v1/polls/{poll_id}/poll_choices — Create a single poll choice [create_single_poll_choice]
`PUT` /v1/polls/{poll_id}/poll_choices/{id} — Update a single poll choice [update_single_poll_choice]
`DELETE` /v1/polls/{poll_id}/poll_choices/{id} — Delete a poll choice [delete_poll_choice]

### Polls  —  resources/polls.md

`GET` /v1/polls — List polls [list_polls]
`GET` /v1/polls/{id} — Get a single poll [get_single_poll]
`POST` /v1/polls — Create a single poll [create_single_poll]
`PUT` /v1/polls/{id} — Update a single poll [update_single_poll]
`DELETE` /v1/polls/{id} — Delete a poll [delete_poll]

### PollSubmissions  —  resources/poll_submissions.md

`GET` /v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions/{id} — Get a single poll submission [get_single_poll_submission]
`POST` /v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions — Create a single poll submission [create_single_poll_submission]

### Proficiency Ratings  —  resources/proficiency_ratings.md

`POST` /v1/accounts/{account_id}/outcome_proficiency — Create/update proficiency ratings [create_update_proficiency_ratings_accounts]
`POST` /v1/courses/{course_id}/outcome_proficiency — Create/update proficiency ratings [create_update_proficiency_ratings_courses]
`GET` /v1/accounts/{account_id}/outcome_proficiency — Get proficiency ratings [get_proficiency_ratings_accounts]
`GET` /v1/courses/{course_id}/outcome_proficiency — Get proficiency ratings [get_proficiency_ratings_courses]

### Progress  —  resources/progress.md

`GET` /v1/progress/{id} — Query progress [query_progress]
`POST` /v1/progress/{id}/cancel — Cancel progress [cancel_progress]
`GET` /lti/courses/{course_id}/progress/{id} — Query progress [query_progress]

### Public JWK  —  resources/public_jwk.md

`PUT` /lti/developer_key/update_public_jwk — Update Public JWK [update_public_jwk]

### Quiz Assignment Overrides  —  resources/quiz_assignment_overrides.md

`GET` /v1/courses/{course_id}/quizzes/assignment_overrides — Retrieve assignment-overridden dates for Classic Quizzes [retrieve_assignment_overridden_dates_for_classic_quizzes]
`GET` /v1/courses/{course_id}/new_quizzes/assignment_overrides — Retrieve assignment-overridden dates for New Quizzes [retrieve_assignment_overridden_dates_for_new_quizzes]

### Quiz Extensions  —  resources/quiz_extensions.md

`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/extensions — Set extensions for student quiz submissions [set_extensions_for_student_quiz_submissions]

### Quiz IP Filters  —  resources/quiz_ip_filters.md

`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/ip_filters — Get available quiz IP filters. [get_available_quiz_ip_filters]

### Quiz Question Groups  —  resources/quiz_question_groups.md

`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/groups — List question groups in a quiz [list_question_groups_in_quiz]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} — Get a single quiz group [get_single_quiz_group]
`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/groups — Create a question group [create_question_group]
`PUT` /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} — Update a question group [update_question_group]
`DELETE` /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id} — Delete a question group [delete_question_group]
`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder — Reorder question groups [reorder_question_groups]

### Quiz Questions  —  resources/quiz_questions.md

`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/questions — List questions in a quiz or a submission [list_questions_in_quiz_or_submission]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} — Get a single quiz question [get_single_quiz_question]
`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/questions — Create a single quiz question [create_single_quiz_question]
`PUT` /v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} — Update an existing quiz question [update_existing_quiz_question]
`DELETE` /v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id} — Delete a quiz question [delete_quiz_question]

### Quiz Reports  —  resources/quiz_reports.md

`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/reports — Retrieve all quiz reports [retrieve_all_quiz_reports]
`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/reports — Create a quiz report [create_quiz_report]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id} — Get a quiz report [get_quiz_report]
`DELETE` /v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id} — Abort the generation of a report, or remove a previously generated one [abort_generation_of_report_or_remove_previously_generated_one]

### Quiz Statistics  —  resources/quiz_statistics.md

`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/statistics — Fetching the latest quiz statistics [fetching_latest_quiz_statistics]

### Quiz Submission Events  —  resources/quiz_submission_events.md

`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events — Submit captured events [submit_captured_events]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events — Retrieve captured events [retrieve_captured_events]

### Quiz Submission Files  —  resources/quiz_submission_files.md

`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files — Upload a file [upload_file]

### Quiz Submission Questions  —  resources/quiz_submission_questions.md

`GET` /v1/quiz_submissions/{quiz_submission_id}/questions — Get all quiz submission questions. [get_all_quiz_submission_questions]
`POST` /v1/quiz_submissions/{quiz_submission_id}/questions — Answering questions [answering_questions]
`GET` /v1/quiz_submissions/{quiz_submission_id}/questions/{id}/formatted_answer — Get a formatted student numerical answer. [get_formatted_student_numerical_answer]
`PUT` /v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag — Flagging a question. [flagging_question]
`PUT` /v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag — Unflagging a question. [unflagging_question]

### Quiz Submission User List  —  resources/quiz_submission_user_list.md

`POST` /v1/courses/{course_id}/quizzes/{id}/submission_users/message — Send a message to unsubmitted or submitted users for the quiz [send_message_to_unsubmitted_or_submitted_users_for_quiz]

### Quiz Submissions  —  resources/quiz_submissions.md

`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions — Get all quiz submissions. [get_all_quiz_submissions]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/submission — Get the quiz submission. [get_quiz_submission]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id} — Get a single quiz submission. [get_single_quiz_submission]
`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions — Create the quiz submission (start a quiz-taking session) [create_quiz_submission_start_quiz_taking_session]
`PUT` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id} — Update student question scores and comments. [update_student_question_scores_and_comments]
`POST` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete — Complete the quiz submission (turn it in). [complete_quiz_submission_turn_it_in]
`GET` /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/time — Get current quiz submission times. [get_current_quiz_submission_times]

### Quizzes  —  resources/quizzes.md

`GET` /v1/courses/{course_id}/quizzes — List quizzes in a course [list_quizzes_in_course]
`GET` /v1/courses/{course_id}/quizzes/{id} — Get a single quiz [get_single_quiz]
`POST` /v1/courses/{course_id}/quizzes — Create a quiz [create_quiz]
`PUT` /v1/courses/{course_id}/quizzes/{id} — Edit a quiz [edit_quiz]
`DELETE` /v1/courses/{course_id}/quizzes/{id} — Delete a quiz [delete_quiz]
`POST` /v1/courses/{course_id}/quizzes/{id}/reorder — Reorder quiz items [reorder_quiz_items]
`POST` /v1/courses/{course_id}/quizzes/{id}/validate_access_code — Validate quiz access code [validate_quiz_access_code]

### Result  —  resources/result.md

`GET` /lti/courses/{course_id}/line_items/{line_item_id}/results — Show a collection of Results [show_collection_of_results]
`GET` /lti/courses/{course_id}/line_items/{line_item_id}/results/{id} — Show a Result [show_result]

### Roles  —  resources/roles.md

`GET` /v1/accounts/{account_id}/roles — List roles [list_roles]
`GET` /v1/accounts/{account_id}/roles/{id} — Get a single role [get_single_role]
`POST` /v1/accounts/{account_id}/roles — Create a new role [create_new_role]
`DELETE` /v1/accounts/{account_id}/roles/{id} — Deactivate a role [deactivate_role]
`POST` /v1/accounts/{account_id}/roles/{id}/activate — Activate a role [activate_role]
`PUT` /v1/accounts/{account_id}/roles/{id} — Update a role [update_role]
`GET` /v1/accounts/{account_id}/roles/permissions — List assignable permissions [list_assignable_permissions]
`GET` /v1/permissions/{context_type}/{permission}/help — Get help text for permissions [get_help_text_for_permissions]
`GET` /v1/permissions/groups — Retrieve permission groups [retrieve_permission_groups]

### Rubrics  —  resources/rubrics.md

`POST` /v1/courses/{course_id}/rubrics — Create a single rubric [create_single_rubric]
`PUT` /v1/courses/{course_id}/rubrics/{id} — Update a single rubric [update_single_rubric]
`DELETE` /v1/courses/{course_id}/rubrics/{id} — Delete a single [delete_single]
`GET` /v1/accounts/{account_id}/rubrics — List rubrics [list_rubrics_accounts]
`GET` /v1/courses/{course_id}/rubrics — List rubrics [list_rubrics_courses]
`GET` /v1/accounts/{account_id}/rubrics/{id} — Get a single rubric [get_single_rubric_accounts]
`GET` /v1/courses/{course_id}/rubrics/{id} — Get a single rubric [get_single_rubric_courses]
`GET` /v1/courses/{course_id}/rubrics/{id}/used_locations — Get the courses and assignments for a rubric [get_courses_and_assignments_for_rubric_courses]
`GET` /v1/accounts/{account_id}/rubrics/{id}/used_locations — Get the courses and assignments for a rubric [get_courses_and_assignments_for_rubric_accounts]
`POST` /v1/courses/{course_id}/rubrics/upload — Creates a rubric using a CSV file [creates_rubric_using_csv_file_courses]
`POST` /v1/accounts/{account_id}/rubrics/upload — Creates a rubric using a CSV file [creates_rubric_using_csv_file_accounts]
`GET` /v1/rubrics/upload_template — Templated file for importing a rubric [templated_file_for_importing_rubric]
`GET` /v1/courses/{course_id}/rubrics/upload/{id} — Get the status of a rubric import [get_status_of_rubric_import_courses]
`GET` /v1/accounts/{account_id}/rubrics/upload/{id} — Get the status of a rubric import [get_status_of_rubric_import_accounts]
`POST` /v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments — Create a single rubric assessment [create_single_rubric_assessment]
`PUT` /v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id} — Update a single rubric assessment [update_single_rubric_assessment]
`DELETE` /v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id} — Delete a single rubric assessment [delete_single_rubric_assessment]
`POST` /v1/courses/{course_id}/rubric_associations — Create a RubricAssociation [create_rubricassociation]
`PUT` /v1/courses/{course_id}/rubric_associations/{id} — Update a RubricAssociation [update_rubricassociation]
`DELETE` /v1/courses/{course_id}/rubric_associations/{id} — Delete a RubricAssociation [delete_rubricassociation]

### Score  —  resources/score.md

`POST` /lti/courses/{course_id}/line_items/{line_item_id}/scores — Create a Score [create_score]

### Search  —  resources/search.md

`GET` /v1/conversations/find_recipients — Find recipients [find_recipients_conversations]
`GET` /v1/search/recipients — Find recipients [find_recipients_search]
`GET` /v1/search/all_courses — List all courses [list_all_courses]

### Sections  —  resources/sections.md

`GET` /v1/courses/{course_id}/sections — List course sections [list_course_sections]
`POST` /v1/courses/{course_id}/sections — Create course section [create_course_section]
`POST` /v1/sections/{id}/crosslist/{new_course_id} — Cross-list a Section [cross_list_section]
`DELETE` /v1/sections/{id}/crosslist — De-cross-list a Section [de_cross_list_section]
`PUT` /v1/sections/{id} — Edit a section [edit_section]
`GET` /v1/courses/{course_id}/sections/{id} — Get section information [get_section_information_courses]
`GET` /v1/sections/{id} — Get section information [get_section_information_sections]
`DELETE` /v1/sections/{id} — Delete a section [delete_section]
`GET` /v1/sections/{id}/users — List section's users [list_section_s_users]

### Security  —  resources/security.md

`GET` /lti/security/jwks — Show all available JWKs used by Canvas for signing. [show_all_available_jwks_used_by_canvas_for_signing]

### Services  —  resources/services.md

`GET` /v1/services/kaltura — Get Kaltura config [get_kaltura_config]
`POST` /v1/services/kaltura_session — Start Kaltura session [start_kaltura_session]

### Shared Brand Configs  —  resources/shared_brand_configs.md

`POST` /v1/accounts/{account_id}/shared_brand_configs — Share a BrandConfig (Theme) [share_brandconfig_theme]
`PUT` /v1/accounts/{account_id}/shared_brand_configs/{id} — Update a shared theme [update_shared_theme]
`DELETE` /v1/shared_brand_configs/{id} — Un-share a BrandConfig (Theme) [un_share_brandconfig_theme]

### SIS Import Errors  —  resources/sis_import_errors.md

`GET` /v1/accounts/{account_id}/sis_imports/{id}/errors — Get SIS import error list [get_sis_import_error_list_sis_imports]
`GET` /v1/accounts/{account_id}/sis_import_errors — Get SIS import error list [get_sis_import_error_list_sis_import_errors]

### SIS Imports  —  resources/sis_imports.md

`GET` /v1/accounts/{account_id}/sis_imports — Get SIS import list [get_sis_import_list]
`GET` /v1/accounts/{account_id}/sis_imports/importing — Get the current importing SIS import [get_current_importing_sis_import]
`POST` /v1/accounts/{account_id}/sis_imports — Import SIS data [import_sis_data]
`GET` /v1/accounts/{account_id}/sis_imports/{id} — Get SIS import status [get_sis_import_status]
`PUT` /v1/accounts/{account_id}/sis_imports/{id}/restore_states — Restore workflow_states of SIS imported items [restore_workflow_states_of_sis_imported_items]
`PUT` /v1/accounts/{account_id}/sis_imports/{id}/abort — Abort SIS import [abort_sis_import]
`PUT` /v1/accounts/{account_id}/sis_imports/abort_all_pending — Abort all pending SIS imports [abort_all_pending_sis_imports]

### SIS Integration  —  resources/sis_integration.md

`GET` /sis/accounts/{account_id}/assignments — Retrieve assignments enabled for grade export to SIS [retrieve_assignments_enabled_for_grade_export_to_sis_accounts]
`GET` /sis/courses/{course_id}/assignments — Retrieve assignments enabled for grade export to SIS [retrieve_assignments_enabled_for_grade_export_to_sis_courses]
`PUT` /sis/courses/{course_id}/disable_post_to_sis — Disable assignments currently enabled for grade export to SIS [disable_assignments_currently_enabled_for_grade_export_to_sis]

### Smart Search  —  resources/smart_search.md

`GET` /v1/courses/{course_id}/smartsearch — Search course content [search_course_content]

### Study Assist  —  resources/study_assist.md

`POST` /v1/courses/{course_id}/study_assist — Request a study assist response [request_study_assist_response]

### Submission Comments  —  resources/submission_comments.md

`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id} — Edit a submission comment [edit_submission_comment]
`DELETE` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id} — Delete a submission comment [delete_submission_comment]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files — Upload a file [upload_file]

### Submissions  —  resources/submissions.md

`POST` /v1/courses/{course_id}/assignments/{assignment_id}/submissions — Submit an assignment [submit_assignment_courses]
`POST` /v1/sections/{section_id}/assignments/{assignment_id}/submissions — Submit an assignment [submit_assignment_sections]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/submissions — List assignment submissions [list_assignment_submissions_courses]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/submissions — List assignment submissions [list_assignment_submissions_sections]
`GET` /v1/courses/{course_id}/students/submissions — List submissions for multiple assignments [list_submissions_for_multiple_assignments_courses]
`GET` /v1/sections/{section_id}/students/submissions — List submissions for multiple assignments [list_submissions_for_multiple_assignments_sections]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} — Get a single submission [get_single_submission_courses]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} — Get a single submission [get_single_submission_sections]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} — Get a single submission by anonymous id [get_single_submission_by_anonymous_id_courses]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} — Get a single submission by anonymous id [get_single_submission_by_anonymous_id_sections]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files — Upload a file [upload_file_courses]
`POST` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files — Upload a file [upload_file_sections]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} — Grade or comment on a submission [grade_or_comment_on_submission_courses]
`PUT` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} — Grade or comment on a submission [grade_or_comment_on_submission_sections]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} — Grade or comment on a submission by anonymous id [grade_or_comment_on_submission_by_anonymous_id_courses]
`PUT` /v1/sections/{section_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id} — Grade or comment on a submission by anonymous id [grade_or_comment_on_submission_by_anonymous_id_sections]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students — List gradeable students [list_gradeable_students]
`GET` /v1/courses/{course_id}/assignments/gradeable_students — List multiple assignments gradeable students [list_multiple_assignments_gradeable_students]
`POST` /v1/courses/{course_id}/submissions/update_grades — Grade or comment on multiple submissions [grade_or_comment_on_multiple_submissions_courses_submissions]
`POST` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades — Grade or comment on multiple submissions [grade_or_comment_on_multiple_submissions_courses_assignments]
`POST` /v1/sections/{section_id}/submissions/update_grades — Grade or comment on multiple submissions [grade_or_comment_on_multiple_submissions_sections_submissions]
`POST` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades — Grade or comment on multiple submissions [grade_or_comment_on_multiple_submissions_sections_assignments]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read — Mark submission as read [mark_submission_as_read_courses]
`PUT` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read — Mark submission as read [mark_submission_as_read_sections]
`DELETE` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read — Mark submission as unread [mark_submission_as_unread_courses]
`DELETE` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read — Mark submission as unread [mark_submission_as_unread_sections]
`PUT` /v1/courses/{course_id}/submissions/bulk_mark_read — Mark bulk submissions as read [mark_bulk_submissions_as_read_courses]
`PUT` /v1/sections/{section_id}/submissions/bulk_mark_read — Mark bulk submissions as read [mark_bulk_submissions_as_read_sections]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read/{item} — Mark submission item as read [mark_submission_item_as_read_courses]
`PUT` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read/{item} — Mark submission item as read [mark_submission_item_as_read_sections]
`PUT` /v1/courses/{course_id}/submissions/{user_id}/clear_unread — Clear unread status for all submissions. [clear_unread_status_for_all_submissions_courses]
`PUT` /v1/sections/{section_id}/submissions/{user_id}/clear_unread — Clear unread status for all submissions. [clear_unread_status_for_all_submissions_sections]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read — Get rubric assessments read state [get_rubric_assessments_read_state_courses_rubric_comments]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read — Get rubric assessments read state [get_rubric_assessments_read_state_courses_rubric_assessments]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read — Get rubric assessments read state [get_rubric_assessments_read_state_sections_rubric_comments]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read — Get rubric assessments read state [get_rubric_assessments_read_state_sections_rubric_assessments]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read — Mark rubric assessments as read [mark_rubric_assessments_as_read_courses_rubric_comments]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read — Mark rubric assessments as read [mark_rubric_assessments_as_read_courses_rubric_assessments]
`PUT` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read — Mark rubric assessments as read [mark_rubric_assessments_as_read_sections_rubric_comments]
`PUT` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read — Mark rubric assessments as read [mark_rubric_assessments_as_read_sections_rubric_assessments]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read — Get document annotations read state [get_document_annotations_read_state_courses]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read — Get document annotations read state [get_document_annotations_read_state_sections]
`PUT` /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read — Mark document annotations as read [mark_document_annotations_as_read_courses]
`PUT` /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read — Mark document annotations as read [mark_document_annotations_as_read_sections]
`GET` /v1/courses/{course_id}/assignments/{assignment_id}/submission_summary — Submission Summary [submission_summary_courses]
`GET` /v1/sections/{section_id}/assignments/{assignment_id}/submission_summary — Submission Summary [submission_summary_sections]

### Tabs  —  resources/tabs.md

`GET` /v1/accounts/{account_id}/tabs — List available tabs for a course or group [list_available_tabs_for_course_or_group_accounts]
`GET` /v1/courses/{course_id}/tabs — List available tabs for a course or group [list_available_tabs_for_course_or_group_courses]
`GET` /v1/groups/{group_id}/tabs — List available tabs for a course or group [list_available_tabs_for_course_or_group_groups]
`GET` /v1/users/{user_id}/tabs — List available tabs for a course or group [list_available_tabs_for_course_or_group_users]
`PUT` /v1/courses/{course_id}/tabs/{tab_id} — Update a tab for a course [update_tab_for_course]

### Temporary Enrollment Pairings  —  resources/temporary_enrollment_pairings.md

`GET` /v1/accounts/{account_id}/temporary_enrollment_pairings — List temporary enrollment pairings [list_temporary_enrollment_pairings]
`GET` /v1/accounts/{account_id}/temporary_enrollment_pairings/{id} — Get a single temporary enrollment pairing [get_single_temporary_enrollment_pairing]
`GET` /v1/accounts/{account_id}/temporary_enrollment_pairings/new — New TemporaryEnrollmentPairing [new_temporaryenrollmentpairing]
`POST` /v1/accounts/{account_id}/temporary_enrollment_pairings — Create Temporary Enrollment Pairing [create_temporary_enrollment_pairing]
`DELETE` /v1/accounts/{account_id}/temporary_enrollment_pairings/{id} — Delete Temporary Enrollment Pairing [delete_temporary_enrollment_pairing]

### Tool Configuration API  —  resources/tool_configuration_api.md

`POST` /lti/accounts/{account_id}/developer_keys/tool_configuration — Create Tool configuration [create_tool_configuration]
`PUT` /lti/developer_keys/{developer_key_id}/tool_configuration — Update Tool configuration [update_tool_configuration]
`GET` /lti/accounts/{account_id}/developer_keys/{developer_key_id}/tool_configuration — Show Tool configuration [show_tool_configuration_accounts]
`GET` /lti/courses/{course_id}/developer_keys/{developer_key_id}/tool_configuration — Show Tool configuration [show_tool_configuration_courses]
`DELETE` /lti/developer_keys/{developer_key_id}/tool_configuration — Show Tool configuration [show_tool_configuration]

### User Observees  —  resources/user_observees.md

`GET` /v1/users/{user_id}/observees — List linked observees [list_linked_observees]
`GET` /v1/users/{user_id}/observers — List linked observers [list_linked_observers]
`POST` /v1/users/{user_id}/observees — Add an observee with credentials [add_observee_with_credentials]
`GET` /v1/users/{user_id}/observees/{observee_id} — Show an observee [show_observee]
`GET` /v1/users/{user_id}/observers/{observer_id} — Show an observer [show_observer]
`PUT` /v1/users/{user_id}/observees/{observee_id} — Add an observee [add_observee]
`DELETE` /v1/users/{user_id}/observees/{observee_id} — Remove an observee [remove_observee]
`POST` /v1/users/{user_id}/observer_pairing_codes — Create observer pairing code [create_observer_pairing_code]

### Users  —  resources/users.md

`GET` /v1/accounts/{account_id}/users — List users in account [list_users_in_account]
`GET` /v1/users/self/activity_stream — List the activity stream [list_activity_stream_self]
`GET` /v1/users/activity_stream — List the activity stream [list_activity_stream_activity_stream]
`GET` /v1/users/self/activity_stream/summary — Activity stream summary [activity_stream_summary]
`GET` /v1/users/self/todo — List the TODO items [list_todo_items]
`GET` /v1/users/self/todo_item_count — List counts for todo items [list_counts_for_todo_items]
`GET` /v1/users/self/upcoming_events — List upcoming assignments, calendar events [list_upcoming_assignments_calendar_events]
`GET` /v1/users/{user_id}/missing_submissions — List Missing Submissions [list_missing_submissions]
`DELETE` /v1/users/self/activity_stream/{id} — Hide a stream item [hide_stream_item]
`DELETE` /v1/users/self/activity_stream — Hide all stream items [hide_all_stream_items]
`POST` /v1/users/{user_id}/files — Upload a file [upload_file]
`GET` /v1/users/{id} — Show user details [show_user_details]
`POST` /v1/accounts/{account_id}/users — Create a user [create_user]
`POST` /v1/accounts/{account_id}/self_registration — [DEPRECATED] Self register a user [deprecated_self_register_user]
`GET` /v1/users/{id}/settings — Update user settings. [update_user_settings]
`GET` /v1/users/{id}/colors — Get custom colors [get_custom_colors]
`GET` /v1/users/{id}/colors/{asset_string} — Get custom color [get_custom_color]
`PUT` /v1/users/{id}/colors/{asset_string} — Update custom color [update_custom_color]
`PUT` /v1/users/{id}/text_editor_preference — Update text editor preference [update_text_editor_preference]
`PUT` /v1/users/{id}/files_ui_version_preference — Update files UI version preference [update_files_ui_version_preference]
`GET` /v1/users/{id}/dashboard_positions — Get dashboard positions [get_dashboard_positions]
`PUT` /v1/users/{id}/dashboard_positions — Update dashboard positions [update_dashboard_positions]
`PUT` /v1/users/{id} — Edit a user [edit_user]
`DELETE` /v1/users/{id}/sessions — Terminate all user sessions [terminate_all_user_sessions]
`DELETE` /v1/users/mobile_sessions — Log users out of all mobile apps [log_users_out_of_all_mobile_apps_mobile_sessions]
`DELETE` /v1/users/{id}/mobile_sessions — Log users out of all mobile apps [log_users_out_of_all_mobile_apps_id]
`PUT` /v1/users/{id}/merge_into/{destination_user_id} — Merge user into another user [merge_user_into_another_user_destination_user_id]
`PUT` /v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id} — Merge user into another user [merge_user_into_another_user_accounts]
`POST` /v1/users/{id}/split — Split merged users into separate users [split_merged_users_into_separate_users]
`POST` /v1/users/self/pandata_events_token — Get a Pandata Events jwt token and its expiration date [get_pandata_events_jwt_token_and_its_expiration_date]
`GET` /v1/users/{id}/graded_submissions — Get a users most recently graded submissions [get_users_most_recently_graded_submissions]
`GET` /v1/users/{user_id}/profile — Get user profile [get_user_profile]
`GET` /v1/users/{user_id}/avatars — List avatar options [list_avatar_options]
`GET` /v1/users/{user_id}/page_views — List user page views [list_user_page_views]
`POST` /v1/users/{user_id}/page_views/query — BETA - Initiate page views query [beta_initiate_page_views_query]
`GET` /v1/users/{user_id}/page_views/query/{query_id} — BETA - Poll query status [beta_poll_query_status]
`GET` /v1/users/{user_id}/page_views/query/{query_id}/results — BETA - Get query results [beta_get_query_results]
`POST` /v1/users/page_views/query — BETA - Initiate batch page views query [beta_initiate_batch_page_views_query]
`GET` /v1/users/page_views/query/{query_id} — BETA - Poll batch query status [beta_poll_batch_query_status]
`GET` /v1/users/page_views/query/{query_id}/results — BETA - Get batch query results [beta_get_batch_query_results]
`PUT` /v1/users/{user_id}/custom_data — Store custom data [store_custom_data]
`GET` /v1/users/{user_id}/custom_data — Load custom data [load_custom_data]
`DELETE` /v1/users/{user_id}/custom_data — Delete custom data [delete_custom_data]
`GET` /v1/users/self/course_nicknames — List course nicknames [list_course_nicknames]
`GET` /v1/users/self/course_nicknames/{course_id} — Get course nickname [get_course_nickname]
`PUT` /v1/users/self/course_nicknames/{course_id} — Set course nickname [set_course_nickname]
`DELETE` /v1/users/self/course_nicknames/{course_id} — Remove course nickname [remove_course_nickname]
`DELETE` /v1/users/self/course_nicknames — Clear course nicknames [clear_course_nicknames]

### Webhooks Subscriptions for Plagiarism Platform  —  resources/webhooks_subscriptions_for_plagiarism_platform.md

`POST` /lti/subscriptions — Create a Webhook Subscription [create_webhook_subscription]
`DELETE` /lti/subscriptions/{id} — Delete a Webhook Subscription [delete_webhook_subscription]
`GET` /lti/subscriptions/{id} — Show a single Webhook Subscription [show_single_webhook_subscription]
`PUT` /lti/subscriptions/{id} — Update a Webhook Subscription [update_webhook_subscription]
`GET` /lti/subscriptions — List all Webhook Subscription for a tool proxy [list_all_webhook_subscription_for_tool_proxy]

### What If Grades  —  resources/what_if_grades.md

`PUT` /v1/submissions/{id}/what_if_grades — Update a submission's what-if score and calculate grades [update_submission_s_what_if_score_and_calculate_grades]
`PUT` /v1/courses/{course_id}/what_if_grades/reset — Reset the what-if scores for the current user for an entire course and recalculate grades [reset_what_if_scores_for_current_user_for_entire_course_and_recalculate_grades]

