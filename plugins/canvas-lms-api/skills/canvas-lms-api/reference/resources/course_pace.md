# Course Pace

> Canvas LMS REST API — `/course_pace` resource. Base path `/api`.

## GET /v1/courses/{course_id}/course_pacing/{id}

**Show a Course pace**  —  `show_course_pace`

Returns a course pace for the course and pace id provided

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `course_id` | integer (int64) | path | yes | The id of the course |
| `course_pace_id` | integer (int64) | query | yes | The id of the course_pace |

**Returns:** `CoursePace`

## POST /v1/courses/{course_id}/course_pacing

**Create a Course pace**  —  `create_course_pace`

Creates a new course pace with specified parameters.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the course |
| `end_date` | Datetime | form |  | End date of the course pace |
| `end_date_context` | string | form |  | End date context (course, section, hupothetical) |
| `start_date` | Datetime | form |  | Start date of the course pace |
| `start_date_context` | string | form |  | Start date context (course, section, hupothetical) |
| `exclude_weekends` | boolean | form |  | Course pace dates excludes weekends if true |
| `selected_days_to_skip` | string | form |  | [Array<String>] Course pace dates excludes weekends if true |
| `hard_end_dates` | boolean | form |  | Course pace uess hard end dates if true |
| `workflow_state` | string | form |  | The state of the course pace |
| `course_pace_module_item_attributes` | array[string] | form |  | Module Items attributes |
| `context_id` | integer (int64) | form |  | Pace Context ID |
| `context_type` | string | form |  | Pace Context Type (Course, Section, User) |

**Returns:** `CoursePace`

## PUT /v1/courses/{course_id}/course_pacing/{id}

**Update a Course pace**  —  `update_course_pace`

Returns the updated course pace

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `course_id` | integer (int64) | path | yes | The id of the course |
| `course_pace_id` | integer (int64) | form | yes | The id of the course pace |
| `end_date` | Datetime | form |  | End date of the course pace |
| `exclude_weekends` | boolean | form |  | Course pace dates excludes weekends if true |
| `selected_days_to_skip` | string | form |  | [Array<String>] Course pace dates excludes weekends if true |
| `hard_end_dates` | boolean | form |  | Course pace uess hard end dates if true |
| `workflow_state` | string | form |  | The state of the course pace |
| `course_pace_module_item_attributes` | array[string] | form |  | Module Items attributes |

**Returns:** `CoursePace`

## DELETE /v1/courses/{course_id}/course_pacing/{id}

**Delete a Course pace**  —  `delete_course_pace`

Returns the updated course pace

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `course_id` | integer (int64) | path | yes | The id of the course |
| `course_pace_id` | integer (int64) | query | yes | The id of the course_pace |

**Returns:** `CoursePace`


---

# Models


## CoursePace

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the course pace e.g. `5` |
| `course_id` | integer |  | the ID of the course e.g. `5` |
| `user_id` | integer |  | the ID of the user for this course pace e.g. `10` |
| `workflow_state` | string |  | the state of the course pace e.g. `active` |
| `exclude_weekends` | boolean |  | boolean value depending on exclude weekends setting e.g. `True` |
| `selected_days_to_skip` | array[integer] |  | array of strings representing the days of the work week e.g. `['fri', 'sat']` |
| `hard_end_dates` | boolean |  | set if the end date is set from course e.g. `True` |
| `created_at` | datetime |  | date when course pace is created e.g. `2013-01-23T23:59:00-07:00` |
| `end_date` | datetime |  | course end date e.g. `2013-01-23T23:59:00-07:00` |
| `updated_at` | datetime |  | date when course pace is updated e.g. `2013-01-23T23:59:00-07:00` |
| `published_at` | datetime |  | date when course pace is published e.g. `2013-01-23T23:59:00-07:00` |
| `root_account_id` | integer |  | the root account ID for this course pace e.g. `10` |
| `start_date` | datetime |  | course start date e.g. `2013-01-23T23:59:00-07:00` |
| `modules` | array |  | list of modules and items for this course pace |
| `progress` | Progress |  | progress of pace publishing |


## Module

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the module e.g. `5` |
| `name` | string |  | the name of the module e.g. `Module 1` |
| `position` | integer |  | the position of the module e.g. `5` |
| `items` | array[ModuleItem] |  | list of module items |
| `context_id` | integer |  | the ID of the context for this course pace e.g. `10` |
| `context_type` | string |  | The given context for the course pace e.g. `Course` Allowed: `Course`, `Section`, `User` |


## ModuleItem

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the module item e.g. `5` |
| `duration` | integer |  | the duration of the module item e.g. `5` |
| `course_pace_id` | integer |  | the course pace id of the module item e.g. `5` |
| `root_account_id` | integer |  | the root account id of the module item e.g. `5` |
| `module_item_id` | integer |  | the module item id of the module item e.g. `5` |
| `assignment_title` | string |  | The title of the item assignment e.g. `Assignment 9` |
| `points_possible` | number |  | The points of the item e.g. `10.0` |
| `assignment_link` | string |  | The link of the item assignment e.g. `/courses/105/modules/items/264` |
| `position` | integer |  | the current position of the module item e.g. `5` |
| `module_item_type` | string |  | The module item type of the item assignment e.g. `Assignment` |
| `published` | boolean |  | published boolean value for course pace e.g. `True` |


## Progress

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the Progress object e.g. `1` |
| `context_id` | integer |  | the context owning the job. e.g. `1` |
| `context_type` | string |  | e.g. `Account` |
| `user_id` | integer |  | the id of the user who started the job e.g. `123` |
| `tag` | string |  | the type of operation e.g. `course_batch_update` |
| `completion` | integer |  | percent completed e.g. `100` |
| `workflow_state` | string |  | the state of the job one of 'queued', 'running', 'completed', 'failed' e.g. `completed` |
| `created_at` | datetime |  | the time the job was created e.g. `2013-01-15T15:00:00Z` |
| `updated_at` | datetime |  | the time the job was last updated e.g. `2013-01-15T15:04:00Z` |
| `message` | string |  | optional details about the job e.g. `17 courses processed` |
| `results` | object |  | optional results of the job. omitted when job is still pending e.g. `{'id': '123'}` |
| `url` | string |  | url where a progress update can be retrieved e.g. `https://canvas.example.edu/api/v1/progress/1` |
