# Modules

> Canvas LMS REST API — `/modules` resource. Base path `/api`.

## GET /v1/courses/{course_id}/modules

**List modules**  —  `list_modules`

A paginated list of the modules in a course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "items": Return module items inline if possible.   This parameter suggests that Canvas return module items directly   in the Module object JSON, to avoid having to make separate API   requests for each module when enumerating modules and items. Canvas   is free to omit 'items' for any particular module if it deems them   too numerous to return inline. Callers must be prepared to use the   {api:ContextModuleItemsApiController#index List Module Items API}   if items are not returned. - "content_details": Requires 'items'. Returns additional   details with module items specific to their associated content items.   Includes standard lock information for each item. Allowed: `items`, `content_details` |
| `search_term` | string | query |  | The partial name of the modules (and module items, if 'items' is specified with include[]) to match and return. |
| `student_id` | string | query |  | Returns module completion information for the student with this id. |

**Returns:** `array[Module]`

## GET /v1/courses/{course_id}/modules/{id}

**Show module**  —  `show_module`

Get information about a single module

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "items": Return module items inline if possible.   This parameter suggests that Canvas return module items directly   in the Module object JSON, to avoid having to make separate API   requests for each module when enumerating modules and items. Canvas   is free to omit 'items' for any particular module if it deems them   too numerous to return inline. Callers must be prepared to use the   {api:ContextModuleItemsApiController#index List Module Items API}   if items are not returned. - "content_details": Requires 'items'. Returns additional   details with module items specific to their associated content items.   Includes standard lock information for each item. Allowed: `items`, `content_details` |
| `student_id` | string | query |  | Returns module completion information for the student with this id. |

**Returns:** `Module`

## POST /v1/courses/{course_id}/modules

**Create a module**  —  `create_module`

Create and return a new module

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module[name]` | string | form | yes | The name of the module |
| `module[unlock_at]` | DateTime | form |  | The date the module will unlock |
| `module[position]` | integer (int64) | form |  | The position of this module in the course (1-based) |
| `module[require_sequential_progress]` | boolean | form |  | Whether module items must be unlocked in order |
| `module[prerequisite_module_ids]` | array[string] | form |  | IDs of Modules that must be completed before this one is unlocked. Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored |
| `module[publish_final_grade]` | boolean | form |  | Whether to publish the student's final grade for the course upon completion of this module. |

**Returns:** `Module`

## PUT /v1/courses/{course_id}/modules/{id}

**Update a module**  —  `update_module`

Update and return an existing module

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `module[name]` | string | form |  | The name of the module |
| `module[unlock_at]` | DateTime | form |  | The date the module will unlock |
| `module[position]` | integer (int64) | form |  | The position of the module in the course (1-based) |
| `module[require_sequential_progress]` | boolean | form |  | Whether module items must be unlocked in order |
| `module[prerequisite_module_ids]` | array[string] | form |  | IDs of Modules that must be completed before this one is unlocked Prerequisite modules must precede this module (i.e. have a lower position value), otherwise they will be ignored |
| `module[publish_final_grade]` | boolean | form |  | Whether to publish the student's final grade for the course upon completion of this module. |
| `module[published]` | boolean | form |  | Whether the module is published and visible to students |

**Returns:** `Module`

## DELETE /v1/courses/{course_id}/modules/{id}

**Delete module**  —  `delete_module`

Delete a module

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Module`

## PUT /v1/courses/{course_id}/modules/{id}/relock

**Re-lock module progressions**  —  `re_lock_module_progressions`

Resets module progressions to their default locked state and
recalculates them based on the current requirements.

Adding progression requirements to an active course will not lock students
out of modules they have already unlocked unless this action is called.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Module`

## GET /v1/courses/{course_id}/modules/{module_id}/items

**List module items**  —  `list_module_items`

A paginated list of the items in a module

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `include` | array[string] | query |  | If included, will return additional details specific to the content associated with each item. Refer to the {api:Modules:Module%20Item Module Item specification} for more details. Includes standard lock information for each item. Allowed: `content_details` |
| `search_term` | string | query |  | The partial title of the items to match and return. |
| `student_id` | string | query |  | Returns module completion information for the student with this id. |

**Returns:** `array[ModuleItem]`

## GET /v1/courses/{course_id}/modules/{module_id}/items/{id}

**Show module item**  —  `show_module_item`

Get information about a single module item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | If included, will return additional details specific to the content associated with this item. Refer to the {api:Modules:Module%20Item Module Item specification} for more details. Includes standard lock information for each item. Allowed: `content_details` |
| `student_id` | string | query |  | Returns module completion information for the student with this id. |

**Returns:** `ModuleItem`

## POST /v1/courses/{course_id}/modules/{module_id}/items

**Create a module item**  —  `create_module_item`

Create and return a new module item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `module_item[title]` | string | form |  | The name of the module item and associated content |
| `module_item[type]` | string | form | yes | The type of content linked to the item Allowed: `File`, `Page`, `Discussion`, `Assignment`, `Quiz`, `SubHeader`, `ExternalUrl`, `ExternalTool` |
| `module_item[content_id]` | string | form | yes | The id of the content to link to the module item. Required, except for 'ExternalUrl', 'Page', and 'SubHeader' types. |
| `module_item[position]` | integer (int64) | form |  | The position of this item in the module (1-based). |
| `module_item[indent]` | integer (int64) | form |  | 0-based indent level; module items may be indented to show a hierarchy |
| `module_item[page_url]` | string | form |  | Suffix for the linked wiki page (e.g. 'front-page'). Required for 'Page' type. |
| `module_item[external_url]` | string | form |  | External url that the item points to. [Required for 'ExternalUrl' and 'ExternalTool' types. |
| `module_item[new_tab]` | boolean | form |  | Whether the external tool opens in a new tab. Only applies to 'ExternalTool' type. |
| `module_item[completion_requirement][type]` | string | form |  | Completion requirement for this module item. "must_view": Applies to all item types "must_contribute": Only applies to "Assignment", "Discussion", and "Page" types "must_submit", "min_score": Only apply to "Assignment" and "Quiz" types "must_mark_done": Only applies to "Assignment" and "Page" types Inapplicable types will be ignored Allowed: `must_view`, `must_contribute`, `must_submit`, `must_mark_done` |
| `module_item[completion_requirement][min_score]` | integer (int64) | form |  | Minimum score required to complete. Required for completion_requirement type 'min_score'. |
| `module_item[iframe][width]` | integer (int64) | form |  | Width of the ExternalTool on launch |
| `module_item[iframe][height]` | integer (int64) | form |  | Height of the ExternalTool on launch |

**Returns:** `ModuleItem`

## PUT /v1/courses/{course_id}/modules/{module_id}/items/{id}

**Update a module item**  —  `update_module_item`

Update and return an existing module item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `module_item[title]` | string | form |  | The name of the module item |
| `module_item[position]` | integer (int64) | form |  | The position of this item in the module (1-based) |
| `module_item[indent]` | integer (int64) | form |  | 0-based indent level; module items may be indented to show a hierarchy |
| `module_item[external_url]` | string | form |  | External url that the item points to. Only applies to 'ExternalUrl' type. |
| `module_item[new_tab]` | boolean | form |  | Whether the external tool opens in a new tab. Only applies to 'ExternalTool' type. |
| `module_item[completion_requirement][type]` | string | form |  | Completion requirement for this module item. "must_view": Applies to all item types "must_contribute": Only applies to "Assignment", "Discussion", and "Page" types "must_submit", "min_score": Only apply to "Assignment" and "Quiz" types "must_mark_done": Only applies to "Assignment" and "Page" types Inapplicable types will be ignored Allowed: `must_view`, `must_contribute`, `must_submit`, `must_mark_done` |
| `module_item[completion_requirement][min_score]` | integer (int64) | form |  | Minimum score required to complete, Required for completion_requirement type 'min_score'. |
| `module_item[published]` | boolean | form |  | Whether the module item is published and visible to students. |
| `module_item[module_id]` | string | form |  | Move this item to another module by specifying the target module id here. The target module must be in the same course. |

**Returns:** `ModuleItem`

## POST /v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path

**Select a mastery path**  —  `select_mastery_path`

Select a mastery path when module item includes several possible paths.
Requires Mastery Paths feature to be enabled.  Returns a compound document
with the assignments included in the given path and any module items
related to those assignments

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `assignment_set_id` | string | form |  | Assignment set chosen, as specified in the mastery_paths portion of the context module item response |
| `student_id` | string | form |  | Which student the selection applies to.  If not specified, current user is implied. |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/modules/{module_id}/items/{id}

**Delete module item**  —  `delete_module_item`

Delete a module item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ModuleItem`

## PUT /v1/courses/{course_id}/modules/{module_id}/items/{id}/done

**Mark module item as done/not done**  —  `mark_module_item_as_done_not_done`

Mark a module item as done/not done. Use HTTP method PUT to mark as done,
and DELETE to mark as not done.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/module_item_sequence

**Get module item sequence**  —  `get_module_item_sequence`

Given an asset in a course, find the ModuleItem it belongs to, the previous and next Module Items
in the course sequence, and also any applicable mastery path rules

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `asset_type` | string | query |  | The type of asset to find module sequence information for. Use the ModuleItem if it is known (e.g., the user navigated from a module item), since this will avoid ambiguity if the asset appears more than once in the module sequence. Allowed: `ModuleItem`, `File`, `Page`, `Discussion`, `Assignment`, `Quiz`, `ExternalTool` |
| `asset_id` | integer (int64) | query |  | The id of the asset (or the url in the case of a Page) |

**Returns:** `ModuleItemSequence`

## POST /v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read

**Mark module item read**  —  `mark_module_item_read`

Fulfills "must view" requirement for a module item. It is generally not necessary to do this explicitly,
but it is provided for applications that need to access external content directly (bypassing the html_url
redirect that normally allows Canvas to fulfill "must view" requirements).

This endpoint cannot be used to complete requirements on locked or unpublished module items.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `module_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/modules/{context_module_id}/assignment_overrides

**List a module's overrides**  —  `list_module_s_overrides`

Returns a paginated list of AssignmentOverrides that apply to the ContextModule.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `context_module_id` | string | path | yes | ID |

**Returns:** `array[ModuleAssignmentOverride]`

## PUT /v1/courses/{course_id}/modules/{context_module_id}/assignment_overrides

**Update a module's overrides**  —  `update_module_s_overrides`

Accepts a list of overrides and applies them to the ContextModule. Returns 204 No Content response
code if successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `context_module_id` | string | path | yes | ID |
| `overrides` | array[Array] | form | yes | List of overrides to apply to the module. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the module's overrides. Keys for each override object can include: 'id', 'title', 'student_ids', and 'course_section_id'. 'group_id' is accepted if the Differentiation Tags account setting is enabled. |

**Returns:** `void`


---

# Models


## Module

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the module e.g. `123` |
| `workflow_state` | string |  | the state of the module: 'active', 'deleted' e.g. `active` |
| `position` | integer |  | the position of this module in the course (1-based) e.g. `2` |
| `name` | string |  | the name of this module e.g. `Imaginary Numbers and You` |
| `unlock_at` | datetime |  | (Optional) the date this module will unlock e.g. `2012-12-31T06:00:00-06:00` |
| `require_sequential_progress` | boolean |  | Whether module items must be unlocked in order e.g. `True` |
| `requirement_type` | string |  | Whether module requires all required items or one required item to be considered complete (one of 'all' or 'one') e.g. `all` |
| `prerequisite_module_ids` | array[integer] |  | IDs of Modules that must be completed before this one is unlocked e.g. `[121, 122]` |
| `items_count` | integer |  | The number of items in the module e.g. `10` |
| `items_url` | string |  | The API URL to retrive this module's items e.g. `https://canvas.example.com/api/v1/modules/123/items` |
| `items` | array[ModuleItem] |  | The contents of this module, as an array of Module Items. (Present only if requested via include[]=items AND the module is not deemed too large by Canvas.) |
| `state` | string |  | The state of this Module for the calling user one of 'locked', 'unlocked', 'started', 'completed' (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) e.g. `started` |
| `completed_at` | datetime |  | the date the calling user completed the module (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) |
| `publish_final_grade` | boolean |  | if the student's final grade for the course should be published to the SIS upon completion of this module |
| `published` | boolean |  | (Optional) Whether this module is published. This field is present only if the caller has permission to view unpublished modules. e.g. `True` |


## CompletionRequirement

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `type` | string |  | one of 'must_view', 'must_submit', 'must_contribute', 'min_score', 'min_percentage', 'must_mark_done' e.g. `min_score` |
| `min_score` | integer |  | minimum score required to complete (only present when type == 'min_score') e.g. `10` |
| `min_percentage` | integer |  | minimum percentage required to complete (only present when type == 'min_percentage') e.g. `70` |
| `completed` | boolean |  | whether the calling user has met this requirement (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) e.g. `True` |


## ContentDetails

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `points_possible` | integer |  | e.g. `20` |
| `due_at` | datetime |  | e.g. `2012-12-31T06:00:00-06:00` |
| `unlock_at` | datetime |  | e.g. `2012-12-31T06:00:00-06:00` |
| `lock_at` | datetime |  | e.g. `2012-12-31T06:00:00-06:00` |
| `locked_for_user` | boolean |  | e.g. `True` |
| `lock_explanation` | string |  | e.g. `This quiz is part of an unpublished module and is not available yet.` |
| `lock_info` | LockInfo |  | e.g. `{'asset_string': 'assignment_4', 'unlock_at': '2012-12-31T06:00:00-06:00', 'lock_at': '2012-12-31T06:00:00-06:00', 'context_module': {}}` |


## ModuleItem

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the module item e.g. `768` |
| `module_id` | integer |  | the id of the Module this item appears in e.g. `123` |
| `position` | integer |  | the position of this item in the module (1-based) e.g. `1` |
| `title` | string |  | the title of this item e.g. `Square Roots: Irrational numbers or boxy vegetables?` |
| `indent` | integer |  | 0-based indent level; module items may be indented to show a hierarchy e.g. `0` |
| `type` | string |  | the type of object referred to one of 'File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool' e.g. `Assignment` |
| `content_id` | integer |  | the id of the object referred to applies to 'File', 'Discussion', 'Assignment', 'Quiz', 'ExternalTool' types e.g. `1337` |
| `html_url` | string |  | link to the item in Canvas e.g. `https://canvas.example.edu/courses/222/modules/items/768` |
| `url` | string |  | (Optional) link to the Canvas API object, if applicable e.g. `https://canvas.example.edu/api/v1/courses/222/assignments/987` |
| `page_url` | string |  | (only for 'Page' type) unique locator for the linked wiki page e.g. `my-page-title` |
| `external_url` | string |  | (only for 'ExternalUrl' and 'ExternalTool' types) external url that the item points to e.g. `https://www.example.com/externalurl` |
| `new_tab` | boolean |  | (only for 'ExternalTool' type) whether the external tool opens in a new tab e.g. `False` |
| `completion_requirement` | CompletionRequirement |  | Completion requirement for this module item e.g. `{'type': 'min_score', 'min_score': 10, 'completed': True}` |
| `content_details` | ContentDetails |  | (Present only if requested through include[]=content_details) If applicable, returns additional details specific to the associated object e.g. `{'points_possible': 20, 'due_at': '2012-12-31T06:00:00-06:00', 'unlock_at': '2012-12-31T06:00:00-06:00', 'lock_at': '2012-12-31T06:00:00-06:00'}` |
| `published` | boolean |  | (Optional) Whether this module item is published. This field is present only if the caller has permission to view unpublished items. e.g. `True` |


## ModuleItemSequenceNode

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `prev` | ModuleItem |  | The previous ModuleItem in the sequence |
| `current` | ModuleItem |  | The ModuleItem being queried e.g. `{'id': 768, 'module_id': 123, 'title': 'A lonely page', 'type': 'Page'}` |
| `next` | ModuleItem |  | The next ModuleItem in the sequence e.g. `{'id': 769, 'module_id': 127, 'title': 'Project 1', 'type': 'Assignment'}` |
| `mastery_path` | object |  | The conditional release rule for the module item, if applicable e.g. `{'locked': True, 'assignment_sets': [], 'selected_set_id': None, 'awaiting_choice': False, 'still_processing': False, 'modules_url': '/courses/11/modules', 'choose_url': '/courses/11/modules/items/9/choose', 'modules_tab_disabled': False}` |


## ModuleItemSequence

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `items` | array[ModuleItemSequenceNode] |  | an array containing one ModuleItemSequenceNode for each appearence of the asset in the module sequence (up to 10 total) e.g. `[{'prev': None, 'current': {'id': 768, 'module_id': 123, 'title': 'A lonely page', 'type': 'Page'}, 'next': {'id': 769, 'module_id': 127, 'title': 'Project 1', 'type': 'Assignment'}, 'mastery_path': {'locked': True, 'assignment_sets': [], 'selected_set_id': None, 'awaiting_choice': False, 'still_processing': False, 'modules_url': '/courses/11/modules', 'choose_url': '/courses/11/modules/items/9/choose', 'modules_tab_disabled': False}}]` |
| `modules` | array[Module] |  | an array containing each Module referenced above e.g. `[{'id': 123, 'name': 'Overview'}, {'id': 127, 'name': 'Imaginary Numbers'}]` |


## ModuleAssignmentOverride

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the assignment override e.g. `4355` |
| `context_module_id` | integer |  | the ID of the module the override applies to e.g. `567` |
| `title` | string |  | the title of the override e.g. `Section 6` |
| `students` | OverrideTarget |  | an array of the override's target students (present only if the override targets an adhoc set of students) |
| `course_section` | OverrideTarget |  | the override's target section (present only if the override targets a section) |


## OverrideTarget

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the user or section that the override is targeting e.g. `7` |
| `name` | string |  | the name of the user or section that the override is targeting e.g. `Section 6` |
