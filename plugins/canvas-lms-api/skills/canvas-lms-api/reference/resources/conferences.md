# Conferences

> Canvas LMS REST API — `/conferences` resource. Base path `/api`.

## GET /v1/courses/{course_id}/conferences

**List conferences**  —  `list_conferences_courses`

Retrieve the paginated list of conferences for this context

This API returns a JSON object containing the list of conferences,
the key for the list of conferences is "conferences"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[Conference]`

## GET /v1/groups/{group_id}/conferences

**List conferences**  —  `list_conferences_groups`

Retrieve the paginated list of conferences for this context

This API returns a JSON object containing the list of conferences,
the key for the list of conferences is "conferences"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[Conference]`

## GET /v1/conferences

**List conferences for the current user**  —  `list_conferences_for_current_user`

Retrieve the paginated list of conferences for all courses and groups
the current user belongs to

This API returns a JSON object containing the list of conferences.
The key for the list of conferences is "conferences".

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `state` | string | query |  | If set to "live", returns only conferences that are live (i.e., have started and not finished yet). If omitted, returns all conferences for this user's groups and courses. |

**Returns:** `array[Conference]`


---

# Models


## ConferenceRecording

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `duration_minutes` | integer |  | e.g. `0` |
| `title` | string |  | e.g. `course2: Test conference 3 [170]_0` |
| `updated_at` | datetime |  | e.g. `2013-12-12T16:09:33.903-07:00` |
| `created_at` | datetime |  | e.g. `2013-12-12T16:09:09.960-07:00` |
| `playback_url` | string |  | e.g. `http://example.com/recording_url` |


## Conference

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The id of the conference e.g. `170` |
| `conference_type` | string |  | The type of conference e.g. `AdobeConnect` |
| `conference_key` | string |  | The 3rd party's ID for the conference e.g. `abcdjoelisgreatxyz` |
| `description` | string |  | The description for the conference e.g. `Conference Description` |
| `duration` | integer |  | The expected duration the conference is supposed to last e.g. `60` |
| `ended_at` | datetime |  | The date that the conference ended at, null if it hasn't ended e.g. `2013-12-13T17:23:26Z` |
| `started_at` | datetime |  | The date the conference started at, null if it hasn't started e.g. `2013-12-12T23:02:17Z` |
| `title` | string |  | The title of the conference e.g. `Test conference` |
| `users` | array[integer] |  | Array of user ids that are participants in the conference e.g. `[1, 7, 8, 9, 10]` |
| `invitees` | array[integer] |  | Array of user ids that are invitees in the conference e.g. `[1, 7, 8, 9, 10]` |
| `attendees` | array[integer] |  | Array of user ids that are attendees in the conference e.g. `[1, 7, 8, 9, 10]` |
| `has_advanced_settings` | boolean |  | True if the conference type has advanced settings. e.g. `False` |
| `long_running` | boolean |  | If true the conference is long running and has no expected end time e.g. `False` |
| `user_settings` | object |  | A collection of settings specific to the conference type e.g. `{'record': True}` |
| `recordings` | array[ConferenceRecording] |  | A List of recordings for the conference |
| `url` | string |  | URL for the conference, may be null if the conference type doesn't set it |
| `join_url` | string |  | URL to join the conference, may be null if the conference type doesn't set it |
| `context_type` | string |  | The type of this conference's context, typically 'Course' or 'Group'. |
| `context_id` | integer |  | The ID of this conference's context. |
