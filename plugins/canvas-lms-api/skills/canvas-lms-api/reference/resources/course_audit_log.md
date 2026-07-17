# Course Audit log

> Canvas LMS REST API — `/course_audit_log` resource. Base path `/api`.

## GET /v1/audit/course/courses/{course_id}

**Query by course.**  —  `query_by_course`

List course change events for a given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `array[CourseEvent]`

## GET /v1/audit/course/accounts/{account_id}

**Query by account.**  —  `query_by_account`

List course change events for a given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `start_time` | DateTime | query |  | The beginning of the time range from which you want events. |
| `end_time` | DateTime | query |  | The end of the time range from which you want events. |

**Returns:** `array[CourseEvent]`


---

# Models


## CourseEventLink

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `course` | integer |  | ID of the course for the event. e.g. `12345` |
| `user` | integer |  | ID of the user for the event (who made the change). e.g. `12345` |
| `page_view` | string |  | ID of the page view during the event if it exists. e.g. `e2b76430-27a5-0131-3ca1-48e0eb13f29b` |
| `copied_from` | integer |  | ID of the course that this course was copied from. This is only included if the event_type is copied_from. e.g. `12345` |
| `copied_to` | integer |  | ID of the course that this course was copied to. This is only included if the event_type is copied_to. e.g. `12345` |
| `sis_batch` | integer |  | ID of the SIS batch that triggered the event. e.g. `12345` |


## CourseEvent

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | ID of the event. e.g. `e2b76430-27a5-0131-3ca1-48e0eb13f29b` |
| `created_at` | datetime |  | timestamp of the event e.g. `2012-07-19T15:00:00-06:00` |
| `event_type` | string |  | Course event type The event type defines the type and schema of the event_data object. e.g. `updated` |
| `event_data` | string |  | Course event data depending on the event type.  This will return an object containing the relevant event data.  An updated event type will return an UpdatedEventData object. e.g. `{}` |
| `event_source` | string |  | Course event source depending on the event type.  This will return a string containing the source of the event. e.g. `manual\|sis\|api` |
| `links` | CourseEventLink |  | Jsonapi.org links e.g. `{'course': '12345', 'user': '12345', 'page_view': 'e2b76430-27a5-0131-3ca1-48e0eb13f29b'}` |


## CreatedEventData

The created event data object returns all the fields that were set in the format of the following example.  If a field does not exist it was not set. The value of each field changed is in the format of [:old_value, :new_value].  The created event type also includes a created_source field to specify what triggered the creation of the course.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `name` | array[string] |  | e.g. `[None, 'Course 1']` |
| `start_at` | array[datetime] |  | e.g. `[None, '2012-01-19T15:00:00-06:00']` |
| `conclude_at` | array[datetime] |  | e.g. `[None, '2012-01-19T15:00:00-08:00']` |
| `is_public` | array[boolean] |  | e.g. `[None, False]` |
| `created_source` | string |  | The type of action that triggered the creation of the course. e.g. `manual\|sis\|api` |


## UpdatedEventData

The updated event data object returns all the fields that have changed in the format of the following example.  If a field does not exist it was not changed.  The value is an array that contains the before and after values for the change as in [:old_value, :new_value].

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `name` | array[string] |  | e.g. `['Course 1', 'Course 2']` |
| `start_at` | array[datetime] |  | e.g. `['2012-01-19T15:00:00-06:00', '2012-07-19T15:00:00-06:00']` |
| `conclude_at` | array[datetime] |  | e.g. `['2012-01-19T15:00:00-08:00', '2012-07-19T15:00:00-08:00']` |
| `is_public` | array[boolean] |  | e.g. `[True, False]` |
