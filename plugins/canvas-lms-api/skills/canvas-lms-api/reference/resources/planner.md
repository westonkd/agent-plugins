# Planner

> Canvas LMS REST API — `/planner` resource. Base path `/api`.

## GET /v1/planner/items

**List planner items**  —  `list_planner_items_planner`

Retrieve the paginated list of objects to be shown on the planner for the
current user with the associated planner override to override an item's
visibility if set.

Planner items for a student may also be retrieved by a linked observer. Use
the path that accepts a user_id and supply the student's id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `start_date` | Date | query |  | Only return items starting from the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `end_date` | Date | query |  | Only return items up to the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `context_codes` | array[string] | query |  | List of context codes of courses and/or groups whose items you want to see. If not specified, defaults to all contexts associated to the current user. Note that concluded courses will be ignored unless specified in the includes[] parameter. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42, group_123 |
| `observed_user_id` | string | query |  | Return planner items for the given observed user. Must be accompanied by context_codes[]. The user making the request must be observing the observed user in all the courses specified by context_codes[]. |
| `filter` | string | query |  | Only return items that have new or unread activity Allowed: `new_activity` |
| `filter` | string | query |  | Only return items that are not completed (excludes items with planner_override.marked_complete = true or submitted assignments) Allowed: `incomplete_items` |
| `filter` | string | query |  | Only return items that are completed (includes items with planner_override.marked_complete = true or submitted assignments) Allowed: `complete_items` |

**Returns:** `void`

## GET /v1/users/{user_id}/planner/items

**List planner items**  —  `list_planner_items_users`

Retrieve the paginated list of objects to be shown on the planner for the
current user with the associated planner override to override an item's
visibility if set.

Planner items for a student may also be retrieved by a linked observer. Use
the path that accepts a user_id and supply the student's id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `start_date` | Date | query |  | Only return items starting from the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `end_date` | Date | query |  | Only return items up to the given date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `context_codes` | array[string] | query |  | List of context codes of courses and/or groups whose items you want to see. If not specified, defaults to all contexts associated to the current user. Note that concluded courses will be ignored unless specified in the includes[] parameter. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42, group_123 |
| `observed_user_id` | string | query |  | Return planner items for the given observed user. Must be accompanied by context_codes[]. The user making the request must be observing the observed user in all the courses specified by context_codes[]. |
| `filter` | string | query |  | Only return items that have new or unread activity Allowed: `new_activity` |
| `filter` | string | query |  | Only return items that are not completed (excludes items with planner_override.marked_complete = true or submitted assignments) Allowed: `incomplete_items` |
| `filter` | string | query |  | Only return items that are completed (includes items with planner_override.marked_complete = true or submitted assignments) Allowed: `complete_items` |

**Returns:** `void`

## GET /v1/planner_notes

**List planner notes**  —  `list_planner_notes`

Retrieve the paginated list of planner notes

Retrieve planner note for a user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `start_date` | DateTime | query |  | Only return notes with todo dates since the start_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `end_date` | DateTime | query |  | Only return notes with todo dates before the end_date (inclusive). No default. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date and start_date are both specified and equivalent, then only notes with todo dates on that day are returned. |
| `context_codes` | array[string] | query |  | List of context codes of courses whose notes you want to see. If not specified, defaults to all contexts that the user belongs to. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 Including a code matching the user's own context code (e.g. user_1) will include notes that are not associated with any particular course. |

**Returns:** `array[PlannerNote]`

## GET /v1/planner_notes/{id}

**Show a planner note**  —  `show_planner_note`

Retrieve a planner note for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `PlannerNote`

## PUT /v1/planner_notes/{id}

**Update a planner note**  —  `update_planner_note`

Update a planner note for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `title` | string | form |  | The title of the planner note. |
| `details` | string | form |  | Text of the planner note. |
| `todo_date` | Date | form |  | The date where this planner note should appear in the planner. The value should be formatted as: yyyy-mm-dd. |
| `course_id` | integer (int64) | form |  | The ID of the course to associate with the planner note. The caller must be able to view the course in order to associate it with a planner note. Use a null or empty value to remove a planner note from a course. Note that if the planner note is linked to a learning object, its course_id cannot be changed. |

**Returns:** `PlannerNote`

## POST /v1/planner_notes

**Create a planner note**  —  `create_planner_note`

Create a planner note for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `title` | string | form |  | The title of the planner note. |
| `details` | string | form |  | Text of the planner note. |
| `todo_date` | Date | form |  | The date where this planner note should appear in the planner. The value should be formatted as: yyyy-mm-dd. |
| `course_id` | integer (int64) | form |  | The ID of the course to associate with the planner note. The caller must be able to view the course in order to associate it with a planner note. |
| `linked_object_type` | string | form |  | The type of a learning object to link to this planner note. Must be used in conjunction wtih linked_object_id and course_id. Valid linked_object_type values are: 'announcement', 'assignment', 'discussion_topic', 'wiki_page', 'quiz' |
| `linked_object_id` | integer (int64) | form |  | The id of a learning object to link to this planner note. Must be used in conjunction with linked_object_type and course_id. The object must be in the same course as specified by course_id. If the title argument is not provided, the planner note will use the learning object's title as its title. Only one planner note may be linked to a specific learning object. |

**Returns:** `PlannerNote`

## DELETE /v1/planner_notes/{id}

**Delete a planner note**  —  `delete_planner_note`

Delete a planner note for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `PlannerNote`

## GET /v1/planner/overrides

**List planner overrides**  —  `list_planner_overrides`

Retrieve a planner override for the current user

**Returns:** `array[PlannerOverride]`

## GET /v1/planner/overrides/{id}

**Show a planner override**  —  `show_planner_override`

Retrieve a planner override for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `PlannerOverride`

## PUT /v1/planner/overrides/{id}

**Update a planner override**  —  `update_planner_override`

Update a planner override's visibilty for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `marked_complete` | string | form |  | determines whether the planner item is marked as completed |
| `dismissed` | string | form |  | determines whether the planner item shows in the opportunities list |

**Returns:** `PlannerOverride`

## POST /v1/planner/overrides

**Create a planner override**  —  `create_planner_override`

Create a planner override for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `plannable_type` | string | form | yes | Type of the item that you are overriding in the planner Allowed: `announcement`, `assignment`, `discussion_topic`, `quiz`, `wiki_page`, `planner_note`, `calendar_event`, `assessment_request`, `sub_assignment`, `peer_review_sub_assignment` |
| `plannable_id` | integer (int64) | form | yes | ID of the item that you are overriding in the planner |
| `marked_complete` | boolean | form |  | If this is true, the item will show in the planner as completed |
| `dismissed` | boolean | form |  | If this is true, the item will not show in the opportunities list |

**Returns:** `PlannerOverride`

## DELETE /v1/planner/overrides/{id}

**Delete a planner override**  —  `delete_planner_override`

Delete a planner override for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `PlannerOverride`


---

# Models


## PlannerNote

A planner note

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the planner note e.g. `234` |
| `title` | string |  | The title for a planner note e.g. `Bring books tomorrow` |
| `description` | string |  | The description of the planner note e.g. `I need to bring books tomorrow for my course on biology` |
| `user_id` | integer |  | The id of the associated user creating the planner note e.g. `1578941` |
| `workflow_state` | string |  | The current published state of the planner note e.g. `active` |
| `course_id` | integer |  | The course that the note is in relation too, if applicable e.g. `1578941` |
| `todo_date` | datetime |  | The datetime of when the planner note should show up on their planner e.g. `2017-05-09T10:12:00Z` |
| `linked_object_type` | string |  | the type of the linked learning object e.g. `assignment` |
| `linked_object_id` | integer |  | the id of the linked learning object e.g. `131072` |
| `linked_object_html_url` | string |  | the Canvas web URL of the linked learning object e.g. `https://canvas.example.com/courses/1578941/assignments/131072` |
| `linked_object_url` | string |  | the API URL of the linked learning object e.g. `https://canvas.example.com/api/v1/courses/1578941/assignments/131072` |


## PlannerOverride

User-controlled setting for whether an item should be displayed on the planner or not

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the planner override e.g. `234` |
| `plannable_type` | string |  | The type of the associated object for the planner override e.g. `Assignment` |
| `plannable_id` | integer |  | The id of the associated object for the planner override e.g. `1578941` |
| `user_id` | integer |  | The id of the associated user for the planner override e.g. `1578941` |
| `assignment_id` | integer |  | The id of the plannable's associated assignment, if it has one e.g. `1578941` |
| `workflow_state` | string |  | The current published state of the item, synced with the associated object e.g. `published` |
| `marked_complete` | boolean |  | Controls whether or not the associated plannable item is marked complete on the planner e.g. `False` |
| `dismissed` | boolean |  | Controls whether or not the associated plannable item shows up in the opportunities list e.g. `False` |
| `created_at` | datetime |  | The datetime of when the planner override was created e.g. `2017-05-09T10:12:00Z` |
| `updated_at` | datetime |  | The datetime of when the planner override was updated e.g. `2017-05-09T10:12:00Z` |
| `deleted_at` | datetime |  | The datetime of when the planner override was deleted, if applicable e.g. `2017-05-15T12:12:00Z` |
