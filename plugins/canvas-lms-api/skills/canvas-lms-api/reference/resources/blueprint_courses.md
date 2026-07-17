# Blueprint Courses

> Canvas LMS REST API — `/blueprint_courses` resource. Base path `/api`.

## GET /v1/courses/{course_id}/blueprint_templates/{template_id}

**Get blueprint information**  —  `get_blueprint_information`

Using 'default' as the template_id should suffice for the current implmentation (as there should be only one template per course).
However, using specific template ids may become necessary in the future

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |

**Returns:** `BlueprintTemplate`

## GET /v1/courses/{course_id}/blueprint_templates/{template_id}/associated_courses

**Get associated course information**  —  `get_associated_course_information`

Returns a list of courses that are configured to receive updates from this blueprint

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |

**Returns:** `array[Course]`

## PUT /v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations

**Update associated courses**  —  `update_associated_courses`

Send a list of course ids to add or remove new associations for the template.
Cannot add courses that do not belong to the blueprint course's account. Also cannot add
other blueprint courses or courses that already have an association with another blueprint course.

After associating new courses, {api:MasterCourses::MasterTemplatesController#queue_migration start a sync} to populate their contents from the blueprint.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |
| `course_ids_to_add` | Array | form |  | Courses to add as associated courses |
| `course_ids_to_remove` | Array | form |  | Courses to remove as associated courses |

**Returns:** `void`

## POST /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations

**Begin a migration to push to associated courses**  —  `begin_migration_to_push_to_associated_courses`

Begins a migration to push recently updated content to all associated courses.
Only one migration can be running at a time.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |
| `comment` | string | form |  | An optional comment to be included in the sync history. |
| `send_notification` | boolean | form |  | Send a notification to the calling user when the sync completes. |
| `copy_settings` | boolean | form |  | Whether course settings should be copied over to associated courses. Defaults to true for newly associated courses. |
| `send_item_notifications` | boolean | form |  | By default, new-item notifications are suppressed in blueprint syncs. If this option is set, teachers and students may receive notifications for items such as announcements and assignments that are created in associated courses (subject to the usual notification settings). This option requires the Blueprint Item Notifications feature to be enabled. |
| `publish_after_initial_sync` | boolean | form |  | If set, newly associated courses will be automatically published after the sync completes |

**Returns:** `BlueprintMigration`

## PUT /v1/courses/{course_id}/blueprint_templates/{template_id}/restrict_item

**Set or remove restrictions on a blueprint course object**  —  `set_or_remove_restrictions_on_blueprint_course_object`

If a blueprint course object is restricted, editing will be limited for copies in associated courses.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |
| `content_type` | string | form |  | [String, "assignment"\|"attachment"\|"discussion_topic"\|"external_tool"\|"lti-quiz"\|"quiz"\|"wiki_page"] The type of the object. |
| `content_id` | integer (int64) | form |  | The ID of the object. |
| `restricted` | boolean | form |  | Whether to apply restrictions. |
| `restrictions` | BlueprintRestriction | form |  | (Optional) If the object is restricted, this specifies a set of restrictions. If not specified, the course-level restrictions will be used. See {api:CoursesController#update Course API update documentation} |

**Returns:** `void`

## GET /v1/courses/{course_id}/blueprint_templates/{template_id}/unsynced_changes

**Get unsynced changes**  —  `get_unsynced_changes`

Retrieve a list of learning objects that have changed since the last blueprint sync operation.
If no syncs have been completed, a ChangeRecord with a change_type of +initial_sync+ is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |

**Returns:** `array[ChangeRecord]`

## GET /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations

**List blueprint migrations**  —  `list_blueprint_migrations`

Shows a paginated list of migrations for the template, starting with the most recent. This endpoint can be called on a
blueprint course. See also {api:MasterCourses::MasterTemplatesController#imports_index the associated course side}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |

**Returns:** `array[BlueprintMigration]`

## GET /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}

**Show a blueprint migration**  —  `show_blueprint_migration`

Shows the status of a migration. This endpoint can be called on a blueprint course. See also
{api:MasterCourses::MasterTemplatesController#imports_show the associated course side}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `BlueprintMigration`

## GET /v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}/details

**Get migration details**  —  `get_migration_details`

Show the changes that were propagated in a blueprint migration. This endpoint can be called on a
blueprint course. See also {api:MasterCourses::MasterTemplatesController#import_details the associated course side}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `template_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array[ChangeRecord]`

## GET /v1/courses/{course_id}/blueprint_subscriptions

**List blueprint subscriptions**  —  `list_blueprint_subscriptions`

Returns a list of blueprint subscriptions for the given course. (Currently a course may have no more than one.)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[BlueprintSubscription]`

## GET /v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations

**List blueprint imports**  —  `list_blueprint_imports`

Shows a paginated list of migrations imported into a course associated with a blueprint, starting with the most recent. See also
{api:MasterCourses::MasterTemplatesController#migrations_index the blueprint course side}.

Use 'default' as the subscription_id to use the currently active blueprint subscription.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `subscription_id` | string | path | yes | ID |

**Returns:** `array[BlueprintMigration]`

## GET /v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}

**Show a blueprint import**  —  `show_blueprint_import`

Shows the status of an import into a course associated with a blueprint. See also
{api:MasterCourses::MasterTemplatesController#migrations_show the blueprint course side}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `subscription_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `BlueprintMigration`

## GET /v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}/details

**Get import details**  —  `get_import_details`

Show the changes that were propagated to a course associated with a blueprint.  See also
{api:MasterCourses::MasterTemplatesController#migration_details the blueprint course side}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `subscription_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array[ChangeRecord]`


---

# Models


## BlueprintTemplate

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | The ID of the template. e.g. `1` |
| `course_id` | integer (int64) |  | The ID of the Course the template belongs to. e.g. `2` |
| `last_export_completed_at` | datetime |  | Time when the last export was completed e.g. `2013-08-28T23:59:00-06:00` |
| `associated_course_count` | integer |  | Number of associated courses for the template e.g. `3` |
| `latest_migration` | BlueprintMigration |  | Details of the latest migration |


## BlueprintMigration

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | The ID of the migration. e.g. `1` |
| `template_id` | integer (int64) |  | The ID of the template the migration belongs to. Only present when querying a blueprint course. e.g. `2` |
| `subscription_id` | integer (int64) |  | The ID of the associated course's blueprint subscription. Only present when querying a course associated with a blueprint. e.g. `101` |
| `user_id` | integer (int64) |  | The ID of the user who queued the migration. e.g. `3` |
| `workflow_state` | string |  | Current state of the content migration: queued, exporting, imports_queued, completed, exports_failed, imports_failed e.g. `running` |
| `created_at` | datetime |  | Time when the migration was queued e.g. `2013-08-28T23:59:00-06:00` |
| `exports_started_at` | datetime |  | Time when the exports begun e.g. `2013-08-28T23:59:00-06:00` |
| `imports_queued_at` | datetime |  | Time when the exports were completed and imports were queued e.g. `2013-08-28T23:59:00-06:00` |
| `imports_completed_at` | datetime |  | Time when the imports were completed e.g. `2013-08-28T23:59:00-06:00` |
| `comment` | string |  | User-specified comment describing changes made in this operation e.g. `Fixed spelling in question 3 of midterm exam` |


## BlueprintRestriction

A set of restrictions on editing for copied objects in associated courses

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `content` | boolean |  | Restriction on main content (e.g. title, description). e.g. `True` |
| `points` | boolean |  | Restriction on points possible for assignments and graded learning objects e.g. `True` |
| `due_dates` | boolean |  | Restriction on due dates for assignments and graded learning objects e.g. `False` |
| `availability_dates` | boolean |  | Restriction on availability dates for an object e.g. `True` |


## ChangeRecord

Describes a learning object change propagated to associated courses from a blueprint course

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `asset_id` | integer (int64) |  | The ID of the learning object that was changed in the blueprint course. e.g. `2` |
| `asset_type` | string |  | The type of the learning object that was changed in the blueprint course.  One of 'assignment', 'attachment', 'discussion_topic', 'external_tool', 'quiz', 'wiki_page', 'syllabus', or 'settings'.  For 'syllabus' or 'settings', the asset_id is the course id. e.g. `assignment` |
| `asset_name` | string |  | The name of the learning object that was changed in the blueprint course. e.g. `Some Assignment` |
| `change_type` | string |  | The type of change; one of 'created', 'updated', 'deleted' e.g. `created` |
| `html_url` | string |  | The URL of the changed object e.g. `https://canvas.example.com/courses/101/assignments/2` |
| `locked` | boolean |  | Whether the object is locked in the blueprint e.g. `False` |
| `exceptions` | array[object] |  | A list of ExceptionRecords for linked courses that did not receive this update. e.g. `[{'course_id': 101, 'conflicting_changes': ['points']}]` |


## ExceptionRecord

Lists associated courses that did not receive a change propagated from a blueprint

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `course_id` | integer (int64) |  | The ID of the associated course e.g. `101` |
| `conflicting_changes` | array[object] |  | A list of change classes in the associated course's copy of the item that prevented a blueprint change from being applied. One or more of ['content', 'points', 'due_dates', 'availability_dates']. e.g. `['points']` |


## BlueprintSubscription

Associates a course with a blueprint

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | The ID of the blueprint course subscription e.g. `101` |
| `template_id` | integer (int64) |  | The ID of the blueprint template the associated course is subscribed to e.g. `1` |
| `blueprint_course` | object |  | The blueprint course subscribed to e.g. `{'id': 2, 'name': 'Biology 100 Blueprint', 'course_code': 'BIOL 100 BP', 'term_name': 'Default term'}` |
