# Content Migrations

> Canvas LMS REST API — `/content_migrations` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues

**List migration issues**  —  `list_migration_issues_accounts`

Returns paginated migration issues

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |

**Returns:** `array[MigrationIssue]`

## GET /v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues

**List migration issues**  —  `list_migration_issues_courses`

Returns paginated migration issues

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |

**Returns:** `array[MigrationIssue]`

## GET /v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues

**List migration issues**  —  `list_migration_issues_groups`

Returns paginated migration issues

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |

**Returns:** `array[MigrationIssue]`

## GET /v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues

**List migration issues**  —  `list_migration_issues_users`

Returns paginated migration issues

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |

**Returns:** `array[MigrationIssue]`

## GET /v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Get a migration issue**  —  `get_migration_issue_accounts`

Returns data on an individual migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `MigrationIssue`

## GET /v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Get a migration issue**  —  `get_migration_issue_courses`

Returns data on an individual migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `MigrationIssue`

## GET /v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Get a migration issue**  —  `get_migration_issue_groups`

Returns data on an individual migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `MigrationIssue`

## GET /v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Get a migration issue**  —  `get_migration_issue_users`

Returns data on an individual migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `MigrationIssue`

## PUT /v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Update a migration issue**  —  `update_migration_issue_accounts`

Update the workflow_state of a migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `workflow_state` | string | form | yes | Set the workflow_state of the issue. Allowed: `active`, `resolved` |

**Returns:** `MigrationIssue`

## PUT /v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Update a migration issue**  —  `update_migration_issue_courses`

Update the workflow_state of a migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `workflow_state` | string | form | yes | Set the workflow_state of the issue. Allowed: `active`, `resolved` |

**Returns:** `MigrationIssue`

## PUT /v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Update a migration issue**  —  `update_migration_issue_groups`

Update the workflow_state of a migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `workflow_state` | string | form | yes | Set the workflow_state of the issue. Allowed: `active`, `resolved` |

**Returns:** `MigrationIssue`

## PUT /v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}

**Update a migration issue**  —  `update_migration_issue_users`

Update the workflow_state of a migration issue

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `content_migration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `workflow_state` | string | form | yes | Set the workflow_state of the issue. Allowed: `active`, `resolved` |

**Returns:** `MigrationIssue`

## GET /v1/accounts/{account_id}/content_migrations

**List content migrations**  —  `list_content_migrations_accounts`

Returns paginated content migrations

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[ContentMigration]`

## GET /v1/courses/{course_id}/content_migrations

**List content migrations**  —  `list_content_migrations_courses`

Returns paginated content migrations

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[ContentMigration]`

## GET /v1/groups/{group_id}/content_migrations

**List content migrations**  —  `list_content_migrations_groups`

Returns paginated content migrations

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[ContentMigration]`

## GET /v1/users/{user_id}/content_migrations

**List content migrations**  —  `list_content_migrations_users`

Returns paginated content migrations

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[ContentMigration]`

## GET /v1/accounts/{account_id}/content_migrations/{id}

**Get a content migration**  —  `get_content_migration_accounts`

Returns data on an individual content migration

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## GET /v1/courses/{course_id}/content_migrations/{id}

**Get a content migration**  —  `get_content_migration_courses`

Returns data on an individual content migration

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## GET /v1/groups/{group_id}/content_migrations/{id}

**Get a content migration**  —  `get_content_migration_groups`

Returns data on an individual content migration

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## GET /v1/users/{user_id}/content_migrations/{id}

**Get a content migration**  —  `get_content_migration_users`

Returns data on an individual content migration

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## POST /v1/accounts/{account_id}/content_migrations

**Create a content migration**  —  `create_content_migration_accounts`

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `migration_type` | string | form | yes | The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter |
| `pre_attachment[name]` | string | form |  | Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow. |
| `pre_attachment[*]` | string | form |  | Other file upload properties, See {file:file.file_uploads.html File Upload Documentation} |
| `settings[file_url]` | string | form |  | A URL to download the file from. Must not require authentication. |
| `settings[content_export_id]` | string | form |  | The id of a ContentExport to import. This allows you to import content previously exported from Canvas without needing to download and re-upload it. |
| `settings[source_course_id]` | string | form |  | The course to copy from for a course copy migration. (required if doing course copy) |
| `settings[folder_id]` | string | form |  | The folder to unzip the .zip file into for a zip_file_import. |
| `settings[overwrite_quizzes]` | boolean | form |  | Whether to overwrite quizzes with the same identifiers between content packages. |
| `settings[question_bank_id]` | integer (int64) | form |  | The existing question bank ID to import questions into if not specified in the content package. |
| `settings[question_bank_name]` | string | form |  | The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence. |
| `settings[insert_into_module_id]` | integer (int64) | form |  | The id of a module in the target course. This will add all imported items (that can be added to a module) to the given module. |
| `settings[insert_into_module_type]` | string | form |  | If provided (and +insert_into_module_id+ is supplied), only add objects of the specified type to the module. Allowed: `assignment`, `discussion_topic`, `file`, `page`, `quiz` |
| `settings[insert_into_module_position]` | integer (int64) | form |  | The (1-based) position to insert the imported items into the course (if +insert_into_module_id+ is supplied). If this parameter is omitted, items will be added to the end of the module. |
| `settings[move_to_assignment_group_id]` | integer (int64) | form |  | The id of an assignment group in the target course. If provided, all imported assignments will be moved to the given assignment group. |
| `settings[importer_skips]` | Array | form |  | Set of importers to skip, even if otherwise selected by migration settings. Allowed: `all_course_settings`, `visibility_settings` |
| `settings[import_blueprint_settings]` | boolean | form |  | Import the "use as blueprint course" setting as well as the list of locked items from the source course or package. The destination course must not be associated with an existing blueprint course and cannot have any student or observer enrollments. |
| `date_shift_options[shift_dates]` | boolean | form |  | Whether to shift dates in the copied course |
| `date_shift_options[old_start_date]` | Date | form |  | The original start date of the source content/course |
| `date_shift_options[old_end_date]` | Date | form |  | The original end date of the source content/course |
| `date_shift_options[new_start_date]` | Date | form |  | The new start date for the content/course |
| `date_shift_options[new_end_date]` | Date | form |  | The new end date for the source content/course |
| `date_shift_options[day_substitutions][X]` | integer (int64) | form |  | Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday) |
| `date_shift_options[remove_dates]` | boolean | form |  | Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*. |
| `selective_import` | boolean | form |  | If set, perform a selective import instead of importing all content. The migration will identify the contents of the package and then stop in the +waiting_for_select+ workflow state. At this point, use the {api:ContentMigrationsController#content_list List items endpoint} to enumerate the contents of the package, identifying the copy parameters for the desired content. Then call the {api:ContentMigrationsController#update Update endpoint} and provide these copy parameters to start the import. |
| `select` | Hash | form |  | For +course_copy_importer+ migrations, this parameter allows you to select the objects to copy without using the +selective_import+ argument and +waiting_for_select+ state as is required for uploaded imports (though that workflow is also supported for course copy migrations). The keys are object types like 'files', 'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an integer or a string. Multiple object types can be selected in the same call. Allowed: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics` |

**Returns:** `ContentMigration`

## POST /v1/courses/{course_id}/content_migrations

**Create a content migration**  —  `create_content_migration_courses`

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `migration_type` | string | form | yes | The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter |
| `pre_attachment[name]` | string | form |  | Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow. |
| `pre_attachment[*]` | string | form |  | Other file upload properties, See {file:file.file_uploads.html File Upload Documentation} |
| `settings[file_url]` | string | form |  | A URL to download the file from. Must not require authentication. |
| `settings[content_export_id]` | string | form |  | The id of a ContentExport to import. This allows you to import content previously exported from Canvas without needing to download and re-upload it. |
| `settings[source_course_id]` | string | form |  | The course to copy from for a course copy migration. (required if doing course copy) |
| `settings[folder_id]` | string | form |  | The folder to unzip the .zip file into for a zip_file_import. |
| `settings[overwrite_quizzes]` | boolean | form |  | Whether to overwrite quizzes with the same identifiers between content packages. |
| `settings[question_bank_id]` | integer (int64) | form |  | The existing question bank ID to import questions into if not specified in the content package. |
| `settings[question_bank_name]` | string | form |  | The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence. |
| `settings[insert_into_module_id]` | integer (int64) | form |  | The id of a module in the target course. This will add all imported items (that can be added to a module) to the given module. |
| `settings[insert_into_module_type]` | string | form |  | If provided (and +insert_into_module_id+ is supplied), only add objects of the specified type to the module. Allowed: `assignment`, `discussion_topic`, `file`, `page`, `quiz` |
| `settings[insert_into_module_position]` | integer (int64) | form |  | The (1-based) position to insert the imported items into the course (if +insert_into_module_id+ is supplied). If this parameter is omitted, items will be added to the end of the module. |
| `settings[move_to_assignment_group_id]` | integer (int64) | form |  | The id of an assignment group in the target course. If provided, all imported assignments will be moved to the given assignment group. |
| `settings[importer_skips]` | Array | form |  | Set of importers to skip, even if otherwise selected by migration settings. Allowed: `all_course_settings`, `visibility_settings` |
| `settings[import_blueprint_settings]` | boolean | form |  | Import the "use as blueprint course" setting as well as the list of locked items from the source course or package. The destination course must not be associated with an existing blueprint course and cannot have any student or observer enrollments. |
| `date_shift_options[shift_dates]` | boolean | form |  | Whether to shift dates in the copied course |
| `date_shift_options[old_start_date]` | Date | form |  | The original start date of the source content/course |
| `date_shift_options[old_end_date]` | Date | form |  | The original end date of the source content/course |
| `date_shift_options[new_start_date]` | Date | form |  | The new start date for the content/course |
| `date_shift_options[new_end_date]` | Date | form |  | The new end date for the source content/course |
| `date_shift_options[day_substitutions][X]` | integer (int64) | form |  | Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday) |
| `date_shift_options[remove_dates]` | boolean | form |  | Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*. |
| `selective_import` | boolean | form |  | If set, perform a selective import instead of importing all content. The migration will identify the contents of the package and then stop in the +waiting_for_select+ workflow state. At this point, use the {api:ContentMigrationsController#content_list List items endpoint} to enumerate the contents of the package, identifying the copy parameters for the desired content. Then call the {api:ContentMigrationsController#update Update endpoint} and provide these copy parameters to start the import. |
| `select` | Hash | form |  | For +course_copy_importer+ migrations, this parameter allows you to select the objects to copy without using the +selective_import+ argument and +waiting_for_select+ state as is required for uploaded imports (though that workflow is also supported for course copy migrations). The keys are object types like 'files', 'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an integer or a string. Multiple object types can be selected in the same call. Allowed: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics` |

**Returns:** `ContentMigration`

## POST /v1/groups/{group_id}/content_migrations

**Create a content migration**  —  `create_content_migration_groups`

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `migration_type` | string | form | yes | The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter |
| `pre_attachment[name]` | string | form |  | Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow. |
| `pre_attachment[*]` | string | form |  | Other file upload properties, See {file:file.file_uploads.html File Upload Documentation} |
| `settings[file_url]` | string | form |  | A URL to download the file from. Must not require authentication. |
| `settings[content_export_id]` | string | form |  | The id of a ContentExport to import. This allows you to import content previously exported from Canvas without needing to download and re-upload it. |
| `settings[source_course_id]` | string | form |  | The course to copy from for a course copy migration. (required if doing course copy) |
| `settings[folder_id]` | string | form |  | The folder to unzip the .zip file into for a zip_file_import. |
| `settings[overwrite_quizzes]` | boolean | form |  | Whether to overwrite quizzes with the same identifiers between content packages. |
| `settings[question_bank_id]` | integer (int64) | form |  | The existing question bank ID to import questions into if not specified in the content package. |
| `settings[question_bank_name]` | string | form |  | The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence. |
| `settings[insert_into_module_id]` | integer (int64) | form |  | The id of a module in the target course. This will add all imported items (that can be added to a module) to the given module. |
| `settings[insert_into_module_type]` | string | form |  | If provided (and +insert_into_module_id+ is supplied), only add objects of the specified type to the module. Allowed: `assignment`, `discussion_topic`, `file`, `page`, `quiz` |
| `settings[insert_into_module_position]` | integer (int64) | form |  | The (1-based) position to insert the imported items into the course (if +insert_into_module_id+ is supplied). If this parameter is omitted, items will be added to the end of the module. |
| `settings[move_to_assignment_group_id]` | integer (int64) | form |  | The id of an assignment group in the target course. If provided, all imported assignments will be moved to the given assignment group. |
| `settings[importer_skips]` | Array | form |  | Set of importers to skip, even if otherwise selected by migration settings. Allowed: `all_course_settings`, `visibility_settings` |
| `settings[import_blueprint_settings]` | boolean | form |  | Import the "use as blueprint course" setting as well as the list of locked items from the source course or package. The destination course must not be associated with an existing blueprint course and cannot have any student or observer enrollments. |
| `date_shift_options[shift_dates]` | boolean | form |  | Whether to shift dates in the copied course |
| `date_shift_options[old_start_date]` | Date | form |  | The original start date of the source content/course |
| `date_shift_options[old_end_date]` | Date | form |  | The original end date of the source content/course |
| `date_shift_options[new_start_date]` | Date | form |  | The new start date for the content/course |
| `date_shift_options[new_end_date]` | Date | form |  | The new end date for the source content/course |
| `date_shift_options[day_substitutions][X]` | integer (int64) | form |  | Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday) |
| `date_shift_options[remove_dates]` | boolean | form |  | Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*. |
| `selective_import` | boolean | form |  | If set, perform a selective import instead of importing all content. The migration will identify the contents of the package and then stop in the +waiting_for_select+ workflow state. At this point, use the {api:ContentMigrationsController#content_list List items endpoint} to enumerate the contents of the package, identifying the copy parameters for the desired content. Then call the {api:ContentMigrationsController#update Update endpoint} and provide these copy parameters to start the import. |
| `select` | Hash | form |  | For +course_copy_importer+ migrations, this parameter allows you to select the objects to copy without using the +selective_import+ argument and +waiting_for_select+ state as is required for uploaded imports (though that workflow is also supported for course copy migrations). The keys are object types like 'files', 'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an integer or a string. Multiple object types can be selected in the same call. Allowed: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics` |

**Returns:** `ContentMigration`

## POST /v1/users/{user_id}/content_migrations

**Create a content migration**  —  `create_content_migration_users`

Create a content migration. If the migration requires a file to be uploaded
the actual processing of the file will start once the file upload process is completed.
File uploading works as described in the {file:file.file_uploads.html File Upload Documentation}
except that the values are set on a *pre_attachment* sub-hash.

For migrations that don't require a file to be uploaded, like course copy, the
processing will begin as soon as the migration is created.

You can use the {api:ProgressController#show Progress API} to track the
progress of the migration. The migration's progress is linked to with the
_progress_url_ value.

The two general workflows are:

If no file upload is needed:

1. POST to create
2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

For file uploading:

1. POST to create with file info in *pre_attachment*
2. Do {file:file.file_uploads.html file upload processing} using the data in the *pre_attachment* data
3. {api:ContentMigrationsController#show GET} the ContentMigration
4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress

 (required if doing .zip file upload)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `migration_type` | string | form | yes | The type of the migration. Use the {api:ContentMigrationsController#available_migrators Migrator} endpoint to see all available migrators. Default allowed values: canvas_cartridge_importer, common_cartridge_importer, course_copy_importer, zip_file_importer, qti_converter, moodle_converter |
| `pre_attachment[name]` | string | form |  | Required if uploading a file. This is the first step in uploading a file to the content migration. See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow. |
| `pre_attachment[*]` | string | form |  | Other file upload properties, See {file:file.file_uploads.html File Upload Documentation} |
| `settings[file_url]` | string | form |  | A URL to download the file from. Must not require authentication. |
| `settings[content_export_id]` | string | form |  | The id of a ContentExport to import. This allows you to import content previously exported from Canvas without needing to download and re-upload it. |
| `settings[source_course_id]` | string | form |  | The course to copy from for a course copy migration. (required if doing course copy) |
| `settings[folder_id]` | string | form |  | The folder to unzip the .zip file into for a zip_file_import. |
| `settings[overwrite_quizzes]` | boolean | form |  | Whether to overwrite quizzes with the same identifiers between content packages. |
| `settings[question_bank_id]` | integer (int64) | form |  | The existing question bank ID to import questions into if not specified in the content package. |
| `settings[question_bank_name]` | string | form |  | The question bank to import questions into if not specified in the content package, if both bank id and name are set, id will take precedence. |
| `settings[insert_into_module_id]` | integer (int64) | form |  | The id of a module in the target course. This will add all imported items (that can be added to a module) to the given module. |
| `settings[insert_into_module_type]` | string | form |  | If provided (and +insert_into_module_id+ is supplied), only add objects of the specified type to the module. Allowed: `assignment`, `discussion_topic`, `file`, `page`, `quiz` |
| `settings[insert_into_module_position]` | integer (int64) | form |  | The (1-based) position to insert the imported items into the course (if +insert_into_module_id+ is supplied). If this parameter is omitted, items will be added to the end of the module. |
| `settings[move_to_assignment_group_id]` | integer (int64) | form |  | The id of an assignment group in the target course. If provided, all imported assignments will be moved to the given assignment group. |
| `settings[importer_skips]` | Array | form |  | Set of importers to skip, even if otherwise selected by migration settings. Allowed: `all_course_settings`, `visibility_settings` |
| `settings[import_blueprint_settings]` | boolean | form |  | Import the "use as blueprint course" setting as well as the list of locked items from the source course or package. The destination course must not be associated with an existing blueprint course and cannot have any student or observer enrollments. |
| `date_shift_options[shift_dates]` | boolean | form |  | Whether to shift dates in the copied course |
| `date_shift_options[old_start_date]` | Date | form |  | The original start date of the source content/course |
| `date_shift_options[old_end_date]` | Date | form |  | The original end date of the source content/course |
| `date_shift_options[new_start_date]` | Date | form |  | The new start date for the content/course |
| `date_shift_options[new_end_date]` | Date | form |  | The new end date for the source content/course |
| `date_shift_options[day_substitutions][X]` | integer (int64) | form |  | Move anything scheduled for day 'X' to the specified day. (0-Sunday, 1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday) |
| `date_shift_options[remove_dates]` | boolean | form |  | Whether to remove dates in the copied course. Cannot be used in conjunction with *shift_dates*. |
| `selective_import` | boolean | form |  | If set, perform a selective import instead of importing all content. The migration will identify the contents of the package and then stop in the +waiting_for_select+ workflow state. At this point, use the {api:ContentMigrationsController#content_list List items endpoint} to enumerate the contents of the package, identifying the copy parameters for the desired content. Then call the {api:ContentMigrationsController#update Update endpoint} and provide these copy parameters to start the import. |
| `select` | Hash | form |  | For +course_copy_importer+ migrations, this parameter allows you to select the objects to copy without using the +selective_import+ argument and +waiting_for_select+ state as is required for uploaded imports (though that workflow is also supported for course copy migrations). The keys are object types like 'files', 'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an integer or a string. Multiple object types can be selected in the same call. Allowed: `folders`, `files`, `attachments`, `quizzes`, `assignments`, `announcements`, `calendar_events`, `discussion_topics`, `modules`, `module_items`, `pages`, `rubrics` |

**Returns:** `ContentMigration`

## PUT /v1/accounts/{account_id}/content_migrations/{id}

**Update a content migration**  —  `update_content_migration_accounts`

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## PUT /v1/courses/{course_id}/content_migrations/{id}

**Update a content migration**  —  `update_content_migration_courses`

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## PUT /v1/groups/{group_id}/content_migrations/{id}

**Update a content migration**  —  `update_content_migration_groups`

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## PUT /v1/users/{user_id}/content_migrations/{id}

**Update a content migration**  —  `update_content_migration_users`

Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
can't change the migration type. However, changing most settings after the
migration process has started will not do anything. Generally updating the
content migration will be used when there is a file upload problem, or when
importing content selectively. If the first upload has a problem you can
supply new _pre_attachment_ values to start the process again.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentMigration`

## GET /v1/accounts/{account_id}/content_migrations/migrators

**List Migration Systems**  —  `list_migration_systems_accounts`

Lists the currently available migration types. These values may change.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[Migrator]`

## GET /v1/courses/{course_id}/content_migrations/migrators

**List Migration Systems**  —  `list_migration_systems_courses`

Lists the currently available migration types. These values may change.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[Migrator]`

## GET /v1/groups/{group_id}/content_migrations/migrators

**List Migration Systems**  —  `list_migration_systems_groups`

Lists the currently available migration types. These values may change.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[Migrator]`

## GET /v1/users/{user_id}/content_migrations/migrators

**List Migration Systems**  —  `list_migration_systems_users`

Lists the currently available migration types. These values may change.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[Migrator]`

## GET /v1/accounts/{account_id}/content_migrations/{id}/selective_data

**List items for selective import**  —  `list_items_for_selective_import_accounts`

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `type` | string | query |  | The type of content to enumerate. Allowed: `context_modules`, `assignments`, `quizzes`, `assessment_question_banks`, `discussion_topics`, `wiki_pages`, `context_external_tools`, `tool_profiles`, `announcements`, `calendar_events`, `rubrics`, `groups`, `learning_outcomes`, `attachments` |

**Returns:** `list of content items`

## GET /v1/courses/{course_id}/content_migrations/{id}/selective_data

**List items for selective import**  —  `list_items_for_selective_import_courses`

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `type` | string | query |  | The type of content to enumerate. Allowed: `context_modules`, `assignments`, `quizzes`, `assessment_question_banks`, `discussion_topics`, `wiki_pages`, `context_external_tools`, `tool_profiles`, `announcements`, `calendar_events`, `rubrics`, `groups`, `learning_outcomes`, `attachments` |

**Returns:** `list of content items`

## GET /v1/groups/{group_id}/content_migrations/{id}/selective_data

**List items for selective import**  —  `list_items_for_selective_import_groups`

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `type` | string | query |  | The type of content to enumerate. Allowed: `context_modules`, `assignments`, `quizzes`, `assessment_question_banks`, `discussion_topics`, `wiki_pages`, `context_external_tools`, `tool_profiles`, `announcements`, `calendar_events`, `rubrics`, `groups`, `learning_outcomes`, `attachments` |

**Returns:** `list of content items`

## GET /v1/users/{user_id}/content_migrations/{id}/selective_data

**List items for selective import**  —  `list_items_for_selective_import_users`

Enumerates the content available for selective import in a tree structure. Each node provides
a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
to selectively copy the content associated with that tree node and its children. Each node may also
provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
for a subset of the resources in a given node.

If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:

  [{
    "type": "course_settings",
    "property": "copy[all_course_settings]",
    "title": "Course Settings"
  },
  {
    "type": "context_modules",
    "property": "copy[all_context_modules]",
    "title": "Modules",
    "count": 5,
    "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
  },
  {
    "type": "assignments",
    "property": "copy[all_assignments]",
    "title": "Assignments",
    "count": 2,
    "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
  }]

When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
results in a node for each assignment group and a sub_item for each assignment, like this:

  [{
    "type": "assignment_groups",
    "title": "An Assignment Group",
    "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
    "sub_items": [{
        "type": "assignments",
        "title": "Assignment 1",
        "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
    }, {
        "type": "assignments",
        "title": "Assignment 2",
        "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
    }]
  }]


To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
{api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:

  copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1

You can include multiple copy parameters to selectively import multiple items or groups of items.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `type` | string | query |  | The type of content to enumerate. Allowed: `context_modules`, `assignments`, `quizzes`, `assessment_question_banks`, `discussion_topics`, `wiki_pages`, `context_external_tools`, `tool_profiles`, `announcements`, `calendar_events`, `rubrics`, `groups`, `learning_outcomes`, `attachments` |

**Returns:** `list of content items`

## GET /v1/courses/{course_id}/content_migrations/{id}/asset_id_mapping

**Get asset id mapping**  —  `get_asset_id_mapping`

Given a complete course copy or blueprint import content migration, return a mapping of asset ids
from the source course to the destination course that were copied in this migration or an earlier one
with the same course pair and migration_type (course copy or blueprint).

The returned object's keys are asset types as they appear in API URLs (+announcements+, +assignments+,
+discussion_topics+, +files+, +module_items+, +modules+, +pages+, and +quizzes+). The values are a mapping
from id in source course to id in destination course for objects of this type.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## MigrationIssue

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the issue e.g. `370663` |
| `content_migration_url` | string |  | API url to the content migration e.g. `https://example.com/api/v1/courses/1/content_migrations/1` |
| `description` | string |  | Description of the issue for the end-user e.g. `Questions in this quiz couldn't be converted` |
| `workflow_state` | string |  | Current state of the issue: active, resolved e.g. `active` |
| `fix_issue_html_url` | string |  | HTML Url to the Canvas page to investigate the issue e.g. `https://example.com/courses/1/quizzes/2` |
| `issue_type` | string |  | Severity of the issue: todo, warning, error e.g. `warning` |
| `error_report_html_url` | string |  | Link to a Canvas error report if present (If the requesting user has permissions) e.g. `https://example.com/error_reports/3` |
| `error_message` | string |  | Site administrator error message (If the requesting user has permissions) e.g. `admin only message` |
| `created_at` | datetime |  | timestamp e.g. `2012-06-01T00:00:00-06:00` |
| `updated_at` | datetime |  | timestamp e.g. `2012-06-01T00:00:00-06:00` |


## ContentMigration

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the migration e.g. `370663` |
| `migration_type` | string |  | the type of content migration e.g. `common_cartridge_importer` |
| `migration_type_title` | string |  | the name of the content migration type e.g. `Canvas Cartridge Importer` |
| `migration_issues_url` | string |  | API url to the content migration's issues e.g. `https://example.com/api/v1/courses/1/content_migrations/1/migration_issues` |
| `attachment` | string |  | attachment api object for the uploaded file may not be present for all migrations e.g. `{"url"=>"https://example.com/api/v1/courses/1/content_migrations/1/download_archive"}` |
| `progress_url` | string |  | The api endpoint for polling the current progress e.g. `https://example.com/api/v1/progress/4` |
| `user_id` | integer |  | The user who started the migration e.g. `4` |
| `workflow_state` | string |  | Current state of the content migration: pre_processing, pre_processed, running, waiting_for_select, completed, failed e.g. `running` |
| `started_at` | datetime |  | timestamp e.g. `2012-06-01T00:00:00-06:00` |
| `finished_at` | datetime |  | timestamp e.g. `2012-06-01T00:00:00-06:00` |
| `pre_attachment` | string |  | file uploading data, see {file:file.file_uploads.html File Upload Documentation} for file upload workflow This works a little differently in that all the file data is in the pre_attachment hash if there is no upload_url then there was an attachment pre-processing error, the error message will be in the message key This data will only be here after a create or update call e.g. `{"upload_url"=>"", "message"=>"file exceeded quota", "upload_params"=>{}}` |


## Migrator

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `type` | string |  | The value to pass to the create endpoint e.g. `common_cartridge_importer` |
| `requires_file_upload` | boolean |  | Whether this endpoint requires a file upload e.g. `True` |
| `name` | string |  | Description of the package type expected e.g. `Common Cartridge 1.0/1.1/1.2 Package` |
| `required_settings` | array[string] |  | A list of fields this system requires e.g. `['source_course_id']` |
