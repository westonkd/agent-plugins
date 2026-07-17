# Appointment Groups

> Canvas LMS REST API — `/appointment_groups` resource. Base path `/api`.

## GET /v1/appointment_groups

**List appointment groups**  —  `list_appointment_groups`

Retrieve the paginated list of appointment groups that can be reserved or
managed by the current user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `scope` | string | query |  | Defaults to "reservable" Allowed: `reservable`, `manageable` |
| `context_codes` | array[string] | query |  | Array of context codes used to limit returned results. |
| `include_past_appointments` | boolean | query |  | Defaults to false. If true, includes past appointment groups |
| `include` | array[string] | query |  | Array of additional information to include.  "appointments":: calendar event time slots for this appointment group "child_events":: reservations of those time slots "participant_count":: number of reservations "reserved_times":: the event id, start time and end time of reservations                    the current user has made) "all_context_codes":: all context codes associated with this appointment group Allowed: `appointments`, `child_events`, `participant_count`, `reserved_times`, `all_context_codes` |

**Returns:** `void`

## POST /v1/appointment_groups

**Create an appointment group**  —  `create_appointment_group`

Create and return a new appointment group. If new_appointments are
specified, the response will return a new_appointments array (same format
as appointments array, see "List appointment groups" action)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `appointment_group[context_codes]` | array[string] | form | yes | Array of context codes (courses, e.g. course_1) this group should be linked to (1 or more). Users in the course(s) with appropriate permissions will be able to sign up for this appointment group. |
| `appointment_group[sub_context_codes]` | array[string] | form |  | Array of sub context codes (course sections or a single group category) this group should be linked to. Used to limit the appointment group to particular sections. If a group category is specified, students will sign up in groups and the participant_type will be "Group" instead of "User". |
| `appointment_group[title]` | string | form | yes | Short title for the appointment group. |
| `appointment_group[description]` | string | form |  | Longer text description of the appointment group. |
| `appointment_group[location_name]` | string | form |  | Location name of the appointment group. |
| `appointment_group[location_address]` | string | form |  | Location address. |
| `appointment_group[publish]` | boolean | form |  | Indicates whether this appointment group should be published (i.e. made available for signup). Once published, an appointment group cannot be unpublished. Defaults to false. |
| `appointment_group[participants_per_appointment]` | integer (int64) | form |  | Maximum number of participants that may register for each time slot. Defaults to null (no limit). |
| `appointment_group[min_appointments_per_participant]` | integer (int64) | form |  | Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots. |
| `appointment_group[max_appointments_per_participant]` | integer (int64) | form |  | Maximum number of time slots a user may register for. |
| `appointment_group[new_appointments][X]` | array[string] | form |  | Nested array of start time/end time pairs indicating time slots for this appointment group. Refer to the example request. |
| `appointment_group[participant_visibility]` | string | form |  | "private":: participants cannot see who has signed up for a particular             time slot "protected":: participants can see who has signed up.  Defaults to               "private". Allowed: `private`, `protected` |
| `appointment_group[allow_observer_signup]` | boolean | form |  | Whether observer users can sign-up for an appointment. Defaults to false. |

**Returns:** `void`

## GET /v1/appointment_groups/{id}

**Get a single appointment group**  —  `get_single_appointment_group`

Returns information for a single appointment group

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include. See include[] argument of "List appointment groups" action.  "child_events":: reservations of time slots time slots "appointments":: will always be returned "all_context_codes":: all context codes associated with this appointment group Allowed: `child_events`, `appointments`, `all_context_codes` |

**Returns:** `void`

## PUT /v1/appointment_groups/{id}

**Update an appointment group**  —  `update_appointment_group`

Update and return an appointment group. If new_appointments are specified,
the response will return a new_appointments array (same format as
appointments array, see "List appointment groups" action).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `appointment_group[context_codes]` | array[string] | form | yes | Array of context codes (courses, e.g. course_1) this group should be linked to (1 or more). Users in the course(s) with appropriate permissions will be able to sign up for this appointment group. |
| `appointment_group[sub_context_codes]` | array[string] | form |  | Array of sub context codes (course sections or a single group category) this group should be linked to. Used to limit the appointment group to particular sections. If a group category is specified, students will sign up in groups and the participant_type will be "Group" instead of "User". |
| `appointment_group[title]` | string | form |  | Short title for the appointment group. |
| `appointment_group[description]` | string | form |  | Longer text description of the appointment group. |
| `appointment_group[location_name]` | string | form |  | Location name of the appointment group. |
| `appointment_group[location_address]` | string | form |  | Location address. |
| `appointment_group[publish]` | boolean | form |  | Indicates whether this appointment group should be published (i.e. made available for signup). Once published, an appointment group cannot be unpublished. Defaults to false. |
| `appointment_group[participants_per_appointment]` | integer (int64) | form |  | Maximum number of participants that may register for each time slot. Defaults to null (no limit). |
| `appointment_group[min_appointments_per_participant]` | integer (int64) | form |  | Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots. |
| `appointment_group[max_appointments_per_participant]` | integer (int64) | form |  | Maximum number of time slots a user may register for. |
| `appointment_group[new_appointments][X]` | array[string] | form |  | Nested array of start time/end time pairs indicating time slots for this appointment group. Refer to the example request. |
| `appointment_group[participant_visibility]` | string | form |  | "private":: participants cannot see who has signed up for a particular             time slot "protected":: participants can see who has signed up. Defaults to "private". Allowed: `private`, `protected` |
| `appointment_group[allow_observer_signup]` | boolean | form |  | Whether observer users can sign-up for an appointment. |

**Returns:** `void`

## DELETE /v1/appointment_groups/{id}

**Delete an appointment group**  —  `delete_appointment_group`

Delete an appointment group (and associated time slots and reservations)
and return the deleted group

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `cancel_reason` | string | query |  | Reason for deleting/canceling the appointment group. |

**Returns:** `void`

## GET /v1/appointment_groups/{id}/users

**List user participants**  —  `list_user_participants`

A paginated list of users that are (or may be) participating in this
appointment group.  Refer to the Users API for the response fields. Returns
no results for appointment groups with the "Group" participant_type.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `registration_status` | string | query |  | Limits results to the a given participation status, defaults to "all" Allowed: `all`, `registered`, `registered` |

**Returns:** `void`

## GET /v1/appointment_groups/{id}/groups

**List student group participants**  —  `list_student_group_participants`

A paginated list of student groups that are (or may be) participating in
this appointment group. Refer to the Groups API for the response fields.
Returns no results for appointment groups with the "User" participant_type.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `registration_status` | string | query |  | Limits results to the a given participation status, defaults to "all" Allowed: `all`, `registered`, `registered` |

**Returns:** `void`

## GET /v1/appointment_groups/next_appointment

**Get next appointment**  —  `get_next_appointment`

Return the next appointment available to sign up for. The appointment
is returned in a one-element array. If no future appointments are
available, an empty array is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `appointment_group_ids` | array[string] | query |  | List of ids of appointment groups to search. |

**Returns:** `array[CalendarEvent]`


---

# Models


## Appointment

Date and time for an appointment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The appointment identifier. e.g. `987` |
| `start_at` | datetime |  | Start time for the appointment e.g. `2012-07-20T15:00:00-06:00` |
| `end_at` | datetime |  | End time for the appointment e.g. `2012-07-20T15:00:00-06:00` |


## AppointmentGroup

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the appointment group e.g. `543` |
| `title` | string |  | The title of the appointment group e.g. `Final Presentation` |
| `start_at` | datetime |  | The start of the first time slot in the appointment group e.g. `2012-07-20T15:00:00-06:00` |
| `end_at` | datetime |  | The end of the last time slot in the appointment group e.g. `2012-07-20T17:00:00-06:00` |
| `description` | string |  | The text description of the appointment group e.g. `Es muy importante` |
| `location_name` | string |  | The location name of the appointment group e.g. `El Tigre Chino's office` |
| `location_address` | string |  | The address of the appointment group's location e.g. `Room 234` |
| `participant_count` | integer |  | The number of participant who have reserved slots (see include[] argument) e.g. `2` |
| `reserved_times` | array[Appointment] |  | The start and end times of slots reserved by the current user as well as the id of the calendar event for the reservation (see include[] argument) e.g. `[{'id': 987, 'start_at': '2012-07-20T15:00:00-06:00', 'end_at': '2012-07-20T15:00:00-06:00'}]` |
| `allow_observer_signup` | boolean |  | Boolean indicating whether observer users should be able to sign-up for an appointment e.g. `False` |
| `context_codes` | array[string] |  | The context codes (i.e. courses) this appointment group belongs to. Only people in these courses will be eligible to sign up. e.g. `['course_123']` |
| `sub_context_codes` | array[integer] |  | The sub-context codes (i.e. course sections and group categories) this appointment group is restricted to e.g. `['course_section_234']` |
| `workflow_state` | string |  | Current state of the appointment group ('pending', 'active' or 'deleted'). 'pending' indicates that it has not been published yet and is invisible to participants. e.g. `active` |
| `requiring_action` | boolean |  | Boolean indicating whether the current user needs to sign up for this appointment group (i.e. it's reservable and the min_appointments_per_participant limit has not been met by this user). e.g. `True` |
| `appointments_count` | integer |  | Number of time slots in this appointment group e.g. `2` |
| `appointments` | array[CalendarEvent] |  | Calendar Events representing the time slots (see include[] argument) Refer to the Calendar Events API for more information e.g. `[]` |
| `new_appointments` | array[CalendarEvent] |  | Newly created time slots (same format as appointments above). Only returned in Create/Update responses where new time slots have been added e.g. `[]` |
| `max_appointments_per_participant` | integer |  | Maximum number of time slots a user may register for, or null if no limit e.g. `1` |
| `min_appointments_per_participant` | integer |  | Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots e.g. `1` |
| `participants_per_appointment` | integer |  | Maximum number of participants that may register for each time slot, or null if no limit e.g. `1` |
| `participant_visibility` | string |  | 'private' means participants cannot see who has signed up for a particular time slot, 'protected' means that they can e.g. `private` |
| `participant_type` | string |  | Indicates how participants sign up for the appointment group, either as individuals ('User') or in student groups ('Group'). Related to sub_context_codes (i.e. 'Group' signups always have a single group category) e.g. `User` |
| `url` | string |  | URL for this appointment group (to update, delete, etc.) e.g. `https://example.com/api/v1/appointment_groups/543` |
| `html_url` | string |  | URL for a user to view this appointment group e.g. `http://example.com/appointment_groups/1` |
| `created_at` | datetime |  | When the appointment group was created e.g. `2012-07-13T10:55:20-06:00` |
| `updated_at` | datetime |  | When the appointment group was last updated e.g. `2012-07-13T10:55:20-06:00` |
