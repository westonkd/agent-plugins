# Calendar Events

> Canvas LMS REST API — `/calendar_events` resource. Base path `/api`.

## GET /v1/calendar_events

**List calendar events**  —  `list_calendar_events`

Retrieve the paginated list of calendar events or assignments for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `type` | string | query |  | Defaults to "event" Allowed: `event`, `assignment`, `sub_assignment` |
| `start_date` | Date | query |  | Only return events since the start_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `end_date` | Date | query |  | Only return events before the end_date (inclusive). Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date is the same as start_date, then only events on that day are returned. |
| `undated` | boolean | query |  | Defaults to false (dated events only). If true, only return undated events and ignore start_date and end_date. |
| `all_events` | boolean | query |  | Defaults to false (uses start_date, end_date, and undated criteria). If true, all events are returned, ignoring start_date, end_date, and undated criteria. |
| `context_codes` | array[string] | query |  | List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 |
| `excludes` | array[Array] | query |  | Array of attributes to exclude. Possible values are "description", "child_events" and "assignment" |
| `includes` | array[Array] | query |  | Array of optional attributes to include. Possible values are "web_conference" and "series_natural_language" |
| `important_dates` | boolean | query |  | Defaults to false. If true, only events with important dates set to true will be returned. |
| `blackout_date` | boolean | query |  | Defaults to false. If true, only events with blackout date set to true will be returned. |

**Returns:** `array[CalendarEvent]`

## GET /v1/users/{user_id}/calendar_events

**List calendar events for a user**  —  `list_calendar_events_for_user`

Retrieve the paginated list of calendar events or assignments for the specified user.
To view calendar events for a user other than yourself,
you must either be an observer of that user or an administrator.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `type` | string | query |  | Defaults to "event" Allowed: `event`, `assignment` |
| `start_date` | Date | query |  | Only return events since the start_date (inclusive). Defaults to today. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `end_date` | Date | query |  | Only return events before the end_date (inclusive). Defaults to start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ. If end_date is the same as start_date, then only events on that day are returned. |
| `undated` | boolean | query |  | Defaults to false (dated events only). If true, only return undated events and ignore start_date and end_date. |
| `all_events` | boolean | query |  | Defaults to false (uses start_date, end_date, and undated criteria). If true, all events are returned, ignoring start_date, end_date, and undated criteria. |
| `context_codes` | array[string] | query |  | List of context codes of courses, groups, users, or accounts whose events you want to see. If not specified, defaults to the current user (i.e personal calendar, no course/group events). Limited to 10 context codes, additional ones are ignored. The format of this field is the context type, followed by an underscore, followed by the context id. For example: course_42 |
| `excludes` | array[Array] | query |  | Array of attributes to exclude. Possible values are "description", "child_events" and "assignment" |
| `submission_types` | array[Array] | query |  | When type is "assignment", specifies the allowable submission types for returned assignments. Ignored if type is not "assignment" or if exclude_submission_types is provided. |
| `exclude_submission_types` | array[Array] | query |  | When type is "assignment", specifies the submission types to be excluded from the returned assignments. Ignored if type is not "assignment". |
| `includes` | array[Array] | query |  | Array of optional attributes to include. Possible values are "web_conference" and "series_natural_language" |
| `important_dates` | boolean | query |  | Defaults to false If true, only events with important dates set to true will be returned. |
| `blackout_date` | boolean | query |  | Defaults to false If true, only events with blackout date set to true will be returned. |

**Returns:** `array[CalendarEvent]`

## POST /v1/calendar_events

**Create a calendar event**  —  `create_calendar_event`

Create and return a new calendar event

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `calendar_event[context_code]` | string | form | yes | Context code of the course, group, user, or account whose calendar this event should be added to. |
| `calendar_event[title]` | string | form |  | Short title for the calendar event. |
| `calendar_event[description]` | string | form |  | Longer HTML description of the event. |
| `calendar_event[start_at]` | DateTime | form |  | Start date/time of the event. |
| `calendar_event[end_at]` | DateTime | form |  | End date/time of the event. |
| `calendar_event[location_name]` | string | form |  | Location name of the event. |
| `calendar_event[location_address]` | string | form |  | Location address |
| `calendar_event[time_zone_edited]` | string | form |  | Time zone of the user editing the event. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `calendar_event[all_day]` | boolean | form |  | When true event is considered to span the whole day and times are ignored. |
| `calendar_event[child_event_data][X][start_at]` | DateTime | form |  | Section-level start time(s) if this is a course event. X can be any identifier, provided that it is consistent across the start_at, end_at and context_code |
| `calendar_event[child_event_data][X][end_at]` | DateTime | form |  | Section-level end time(s) if this is a course event. |
| `calendar_event[child_event_data][X][context_code]` | string | form |  | Context code(s) corresponding to the section-level start and end time(s). |
| `calendar_event[duplicate][count]` | number | form |  | Number of times to copy/duplicate the event.  Count cannot exceed 200. |
| `calendar_event[duplicate][interval]` | number | form |  | Defaults to 1 if duplicate `count` is set.  The interval between the duplicated events. |
| `calendar_event[duplicate][frequency]` | string | form |  | Defaults to "weekly".  The frequency at which to duplicate the event Allowed: `daily`, `weekly`, `monthly` |
| `calendar_event[duplicate][append_iterator]` | boolean | form |  | Defaults to false.  If set to `true`, an increasing counter number will be appended to the event title when the event is duplicated.  (e.g. Event 1, Event 2, Event 3, etc) |
| `calendar_event[rrule]` | string | form |  | The recurrence rule to create a series of recurring events. Its value is the {https://icalendar.org/iCalendar-RFC-5545/3-8-5-3-recurrence-rule.html iCalendar RRULE} defining how the event repeats. Unending series not supported. |
| `calendar_event[blackout_date]` | boolean | form |  | If the blackout_date is true, this event represents a holiday or some other special day that does not count in course pacing. |

**Returns:** `void`

## GET /v1/calendar_events/{id}

**Get a single calendar event or assignment**  —  `get_single_calendar_event_or_assignment`

Returns detailed information about a specific calendar event or assignment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `CalendarEvent`

## POST /v1/calendar_events/{id}/reservations

**Reserve a time slot**  —  `reserve_time_slot`

Reserves a particular time slot and return the new reservation

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `participant_id` | string | form |  | User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user's candidate group). |
| `comments` | string | form |  | Comments to associate with this reservation |
| `cancel_existing` | boolean | form |  | Defaults to false. If true, cancel any previous reservation(s) for this participant and appointment group. |

**Returns:** `void`

## POST /v1/calendar_events/{id}/reservations/{participant_id}

**Reserve a time slot**  —  `reserve_time_slot_participant_id`

Reserves a particular time slot and return the new reservation

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `participant_id` | string | path | yes | User or group id for whom you are making the reservation (depends on the participant type). Defaults to the current user (or user's candidate group). |
| `comments` | string | form |  | Comments to associate with this reservation |
| `cancel_existing` | boolean | form |  | Defaults to false. If true, cancel any previous reservation(s) for this participant and appointment group. |

**Returns:** `void`

## PUT /v1/calendar_events/{id}

**Update a calendar event**  —  `update_calendar_event`

Update and return a calendar event

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `calendar_event[context_code]` | string | form |  | Context code of the course, group, user, or account to move this event to. Scheduler appointments and events with section-specific times cannot be moved between calendars. |
| `calendar_event[title]` | string | form |  | Short title for the calendar event. |
| `calendar_event[description]` | string | form |  | Longer HTML description of the event. |
| `calendar_event[start_at]` | DateTime | form |  | Start date/time of the event. |
| `calendar_event[end_at]` | DateTime | form |  | End date/time of the event. |
| `calendar_event[location_name]` | string | form |  | Location name of the event. |
| `calendar_event[location_address]` | string | form |  | Location address |
| `calendar_event[time_zone_edited]` | string | form |  | Time zone of the user editing the event. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `calendar_event[all_day]` | boolean | form |  | When true event is considered to span the whole day and times are ignored. |
| `calendar_event[child_event_data][X][start_at]` | DateTime | form |  | Section-level start time(s) if this is a course event. X can be any identifier, provided that it is consistent across the start_at, end_at and context_code |
| `calendar_event[child_event_data][X][end_at]` | DateTime | form |  | Section-level end time(s) if this is a course event. |
| `calendar_event[child_event_data][X][context_code]` | string | form |  | Context code(s) corresponding to the section-level start and end time(s). |
| `calendar_event[rrule]` | string | form |  | Valid if the event whose ID is in the URL is part of a series. This defines the shape of the recurring event series after it's updated. Its value is the iCalendar RRULE. Unending series are not supported. |
| `which` | string | form |  | Valid if the event whose ID is in the URL is part of a series. Update just the event whose ID is in in the URL, all events in the series, or the given event and all those following. Some updates may create a new series. For example, changing the start time of this and all following events from the middle of a series. Allowed: `one`, `all`, `following` |
| `calendar_event[blackout_date]` | boolean | form |  | If the blackout_date is true, this event represents a holiday or some other special day that does not count in course pacing. |

**Returns:** `void`

## DELETE /v1/calendar_events/{id}

**Delete a calendar event**  —  `delete_calendar_event`

Delete an event from the calendar and return the deleted event

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `cancel_reason` | string | query |  | Reason for deleting/canceling the event. |
| `which` | string | query |  | Valid if the event whose ID is in the URL is part of a series. Delete just the event whose ID is in in the URL, all events in the series, or the given event and all those following. Allowed: `one`, `all`, `following` |

**Returns:** `void`

## POST /v1/calendar_events/save_enabled_account_calendars

**Save enabled account calendars**  —  `save_enabled_account_calendars`

Creates and updates the enabled_account_calendars and mark_feature_as_seen user preferences

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `mark_feature_as_seen` | boolean | form |  | Flag to mark account calendars feature as seen |
| `enabled_account_calendars` | array[Array] | form |  | An array of account Ids to remember in the calendars list of the user |

**Returns:** `void`

## POST /v1/courses/{course_id}/calendar_events/timetable

**Set a course timetable**  —  `set_course_timetable`

Creates and updates "timetable" events for a course.
Can automaticaly generate a series of calendar events based on simple schedules
(e.g. "Monday and Wednesday at 2:00pm" )

Existing timetable events for the course and course sections
will be updated if they still are part of the timetable.
Otherwise, they will be deleted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `timetables[course_section_id]` | array[Array] | form |  | An array of timetable objects for the course section specified by course_section_id. If course_section_id is set to "all", events will be created for the entire course. |
| `timetables[course_section_id][weekdays]` | array[string] | form |  | A comma-separated list of abbreviated weekdays (Mon-Monday, Tue-Tuesday, Wed-Wednesday, Thu-Thursday, Fri-Friday, Sat-Saturday, Sun-Sunday) |
| `timetables[course_section_id][start_time]` | array[string] | form |  | Time to start each event at (e.g. "9:00 am") |
| `timetables[course_section_id][end_time]` | array[string] | form |  | Time to end each event at (e.g. "9:00 am") |
| `timetables[course_section_id][location_name]` | array[string] | form |  | A location name to set for each event |

**Returns:** `void`

## GET /v1/courses/{course_id}/calendar_events/timetable

**Get course timetable**  —  `get_course_timetable`

Returns the last timetable set by the
{api:CalendarEventsApiController#set_course_timetable Set a course timetable} endpoint

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/calendar_events/timetable_events

**Create or update events directly for a course timetable**  —  `create_or_update_events_directly_for_course_timetable`

Creates and updates "timetable" events for a course or course section.
Similar to {api:CalendarEventsApiController#set_course_timetable setting a course timetable},
but instead of generating a list of events based on a timetable schedule,
this endpoint expects a complete list of events.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `course_section_id` | string | form |  | Events will be created for the course section specified by course_section_id. If not present, events will be created for the entire course. |
| `events` | array[Array] | form |  | An array of event objects to use. |
| `events[start_at]` | array[DateTime] | form |  | Start time for the event |
| `events[end_at]` | array[DateTime] | form |  | End time for the event |
| `events[location_name]` | array[string] | form |  | Location name for the event |
| `events[code]` | array[string] | form |  | A unique identifier that can be used to update the event at a later time If one is not specified, an identifier will be generated based on the start and end times |
| `events[title]` | array[string] | form |  | Title for the meeting. If not present, will default to the associated course's name |

**Returns:** `void`


---

# Models


## CalendarEvent

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the calendar event e.g. `234` |
| `title` | string |  | The title of the calendar event e.g. `Paintball Fight!` |
| `start_at` | datetime |  | The start timestamp of the event e.g. `2012-07-19T15:00:00-06:00` |
| `end_at` | datetime |  | The end timestamp of the event e.g. `2012-07-19T16:00:00-06:00` |
| `description` | string |  | The HTML description of the event e.g. `<b>It's that time again!</b>` |
| `location_name` | string |  | The location name of the event e.g. `Greendale Community College` |
| `location_address` | string |  | The address where the event is taking place e.g. `Greendale, Colorado` |
| `context_code` | string |  | the context code of the calendar this event belongs to (course, group, user, or account) e.g. `course_123` |
| `effective_context_code` | string |  | if specified, it indicates which calendar this event should be displayed on. for example, a section-level event would have the course's context code here, while the section's context code would be returned above) |
| `context_name` | string |  | the context name of the calendar this event belongs to (course, user or group) e.g. `Chemistry 101` |
| `all_context_codes` | string |  | a comma-separated list of all calendar contexts this event is part of e.g. `course_123,course_456` |
| `workflow_state` | string |  | Current state of the event ('active', 'locked' or 'deleted') 'locked' indicates that start_at/end_at cannot be changed (though the event could be deleted). Normally only reservations or time slots with reservations are locked (see the Appointment Groups API) e.g. `active` |
| `hidden` | boolean |  | Whether this event should be displayed on the calendar. Only true for course-level events with section-level child events. e.g. `False` |
| `parent_event_id` | integer |  | Normally null. If this is a reservation (see the Appointment Groups API), the id will indicate the time slot it is for. If this is a section-level event, this will be the course-level parent event. |
| `child_events_count` | integer |  | The number of child_events. See child_events (and parent_event_id) e.g. `0` |
| `child_events` | array[integer] |  | Included by default, but may be excluded (see include[] option). If this is a time slot (see the Appointment Groups API) this will be a list of any reservations. If this is a course-level event, this will be a list of section-level events (if any) |
| `url` | string |  | URL for this calendar event (to update, delete, etc.) e.g. `https://example.com/api/v1/calendar_events/234` |
| `html_url` | string |  | URL for a user to view this event e.g. `https://example.com/calendar?event_id=234&include_contexts=course_123` |
| `all_day_date` | datetime |  | The date of this event e.g. `2012-07-19` |
| `all_day` | boolean |  | Boolean indicating whether this is an all-day event (midnight to midnight) e.g. `False` |
| `created_at` | datetime |  | When the calendar event was created e.g. `2012-07-12T10:55:20-06:00` |
| `updated_at` | datetime |  | When the calendar event was last updated e.g. `2012-07-12T10:55:20-06:00` |
| `appointment_group_id` | integer |  | Various Appointment-Group-related fields.These fields are only pertinent to time slots (appointments) and reservations of those time slots. See the Appointment Groups API. The id of the appointment group |
| `appointment_group_url` | string |  | The API URL of the appointment group |
| `own_reservation` | boolean |  | If the event is a reservation, this a boolean indicating whether it is the current user's reservation, or someone else's e.g. `False` |
| `reserve_url` | string |  | If the event is a time slot, the API URL for reserving it |
| `reserved` | boolean |  | If the event is a time slot, a boolean indicating whether the user has already made a reservation for it e.g. `False` |
| `participant_type` | string |  | The type of participant to sign up for a slot: 'User' or 'Group' e.g. `User` |
| `participants_per_appointment` | integer |  | If the event is a time slot, this is the participant limit |
| `available_slots` | integer |  | If the event is a time slot and it has a participant limit, an integer indicating how many slots are available |
| `user` | string |  | If the event is a user-level reservation, this will contain the user participant JSON (refer to the Users API). |
| `group` | string |  | If the event is a group-level reservation, this will contain the group participant JSON (refer to the Groups API). |
| `important_dates` | boolean |  | Boolean indicating whether this has important dates. e.g. `True` |
| `series_uuid` | uuid |  | Identifies the recurring event series this event may belong to. |
| `rrule` | string |  | An iCalendar RRULE for defining how events in a recurring event series repeat. |
| `series_head` | boolean |  | Boolean indicating if is the first event in the series of recurring events. |
| `series_natural_language` | string |  | A natural language expression of how events occur in the series. e.g. `Daily 5 times` |
| `blackout_date` | boolean |  | Boolean indicating whether this has blackout date. e.g. `True` |


## AssignmentEvent

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | A synthetic ID for the assignment e.g. `assignment_987` |
| `title` | string |  | The title of the assignment e.g. `Essay` |
| `start_at` | datetime |  | The due_at timestamp of the assignment e.g. `2012-07-19T23:59:00-06:00` |
| `end_at` | datetime |  | The due_at timestamp of the assignment e.g. `2012-07-19T23:59:00-06:00` |
| `description` | string |  | The HTML description of the assignment e.g. `<b>Write an essay. Whatever you want.</b>` |
| `context_code` | string |  | the context code of the (course) calendar this assignment belongs to e.g. `course_123` |
| `workflow_state` | string |  | Current state of the assignment ('published' or 'deleted') e.g. `published` |
| `url` | string |  | URL for this assignment (note that updating/deleting should be done via the Assignments API) e.g. `https://example.com/api/v1/calendar_events/assignment_987` |
| `html_url` | string |  | URL for a user to view this assignment e.g. `http://example.com/courses/123/assignments/987` |
| `all_day_date` | datetime |  | The due date of this assignment e.g. `2012-07-19` |
| `all_day` | boolean |  | Boolean indicating whether this is an all-day event (e.g. assignment due at midnight) e.g. `True` |
| `created_at` | datetime |  | When the assignment was created e.g. `2012-07-12T10:55:20-06:00` |
| `updated_at` | datetime |  | When the assignment was last updated e.g. `2012-07-12T10:55:20-06:00` |
| `assignment` | Assignment |  | The full assignment JSON data (See the Assignments API) |
| `assignment_overrides` | AssignmentOverride |  | The list of AssignmentOverrides that apply to this event (See the Assignments API). This information is useful for determining which students or sections this assignment-due event applies to. |
| `important_dates` | boolean |  | Boolean indicating whether this has important dates. e.g. `True` |
| `rrule` | string |  | An iCalendar RRULE for defining how events in a recurring event series repeat. e.g. `FREQ=DAILY;INTERVAL=1;COUNT=5` |
| `series_head` | boolean |  | Trueif this is the first event in the series of recurring events. |
| `series_natural_language` | string |  | A natural language expression of how events occur in the series. e.g. `Daily 5 times` |
