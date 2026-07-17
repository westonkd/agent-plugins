# Sections

> Canvas LMS REST API — `/sections` resource. Base path `/api`.

## GET /v1/courses/{course_id}/sections

**List course sections**  —  `list_course_sections`

A paginated list of the list of sections for this course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "students": Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - "avatar_url": Include the avatar URLs for students returned. - "enrollments": If 'students' is also included, return the section   enrollment for each student - "total_students": Returns the total amount of active and invited students   for the course section - "passback_status": Include the grade passback status. - "permissions": Include whether section grants :manage_calendar permission   to the caller Allowed: `students`, `avatar_url`, `enrollments`, `total_students`, `passback_status`, `permissions` |
| `search_term` | string | query |  | When included, searches course sections for the term. Returns only matching results. Term must be at least 2 characters. |

**Returns:** `array[Section]`

## POST /v1/courses/{course_id}/sections

**Create course section**  —  `create_course_section`

Creates a new section for this course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `course_section[name]` | string | form |  | The name of the section |
| `course_section[sis_section_id]` | string | form |  | The sis ID of the section. Must have manage_sis permission to set. This is ignored if caller does not have permission to set. |
| `course_section[integration_id]` | string | form |  | The integration_id of the section. Must have manage_sis permission to set. This is ignored if caller does not have permission to set. |
| `course_section[start_at]` | DateTime | form |  | Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z |
| `course_section[end_at]` | DateTime | form |  | Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z |
| `course_section[restrict_enrollments_to_section_dates]` | boolean | form |  | Set to true to restrict user enrollments to the start and end dates of the section. |
| `enable_sis_reactivation` | boolean | form |  | When true, will first try to re-activate a deleted section with matching sis_section_id if possible. |

**Returns:** `Section`

## POST /v1/sections/{id}/crosslist/{new_course_id}

**Cross-list a Section**  —  `cross_list_section`

Move the Section to another course.  The new course may be in a different account (department),
but must belong to the same root account (institution).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `new_course_id` | string | path | yes | ID |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `Section`

## DELETE /v1/sections/{id}/crosslist

**De-cross-list a Section**  —  `de_cross_list_section`

Undo cross-listing of a Section, returning it to its original course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `override_sis_stickiness` | boolean | query |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `Section`

## PUT /v1/sections/{id}

**Edit a section**  —  `edit_section`

Modify an existing section.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `course_section[name]` | string | form |  | The name of the section |
| `course_section[sis_section_id]` | string | form |  | The sis ID of the section. Must have manage_sis permission to set. |
| `course_section[integration_id]` | string | form |  | The integration_id of the section. Must have manage_sis permission to set. |
| `course_section[start_at]` | DateTime | form |  | Section start date in ISO8601 format, e.g. 2011-01-01T01:00Z |
| `course_section[end_at]` | DateTime | form |  | Section end date in ISO8601 format. e.g. 2011-01-01T01:00Z |
| `course_section[restrict_enrollments_to_section_dates]` | boolean | form |  | Set to true to restrict user enrollments to the start and end dates of the section. |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `Section`

## GET /v1/courses/{course_id}/sections/{id}

**Get section information**  —  `get_section_information_courses`

Gets details about a specific section

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "students": Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - "avatar_url": Include the avatar URLs for students returned. - "enrollments": If 'students' is also included, return the section   enrollment for each student - "total_students": Returns the total amount of active and invited students   for the course section - "passback_status": Include the grade passback status. - "permissions": Include whether section grants :manage_calendar permission   to the caller Allowed: `students`, `avatar_url`, `enrollments`, `total_students`, `passback_status`, `permissions` |

**Returns:** `Section`

## GET /v1/sections/{id}

**Get section information**  —  `get_section_information_sections`

Gets details about a specific section

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "students": Associations to include with the group. Note: this is only   available if you have permission to view users or grades in the course - "avatar_url": Include the avatar URLs for students returned. - "enrollments": If 'students' is also included, return the section   enrollment for each student - "total_students": Returns the total amount of active and invited students   for the course section - "passback_status": Include the grade passback status. - "permissions": Include whether section grants :manage_calendar permission   to the caller Allowed: `students`, `avatar_url`, `enrollments`, `total_students`, `passback_status`, `permissions` |

**Returns:** `Section`

## DELETE /v1/sections/{id}

**Delete a section**  —  `delete_section`

Delete an existing section.  Returns the former Section.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `Section`

## GET /v1/sections/{id}/users

**List section's users**  —  `list_section_s_users`

Returns a paginated list of users in the section.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name or full ID of the users to match and return in the results list. Must be at least 2 characters. |
| `include` | array[string] | query |  | "avatar_url": Include users' avatar_urls. Allowed: `avatar_url` |
| `exclude_inactive` | boolean | query |  | Whether to filter out inactive users from the results. Defaults to false unless explicitly provided. |
| `enrollment_type` | string | query |  | When set, only return users with the specified enrollment type for the given section. Allowed: `teacher`, `student`, `ta`, `observer`, `designer` |

**Returns:** `array[User]`


---

# Models


## Section

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the section. e.g. `1` |
| `name` | string |  | The name of the section. e.g. `Section A` |
| `sis_section_id` | string |  | The sis id of the section. This field is only included if the user has permission to view SIS information. e.g. `s34643` |
| `integration_id` | string |  | Optional: The integration ID of the section. This field is only included if the user has permission to view SIS information. e.g. `3452342345` |
| `sis_import_id` | integer |  | The unique identifier for the SIS import if created through SIS. This field is only included if the user has permission to manage SIS information. e.g. `47` |
| `course_id` | integer |  | The unique Canvas identifier for the course in which the section belongs e.g. `7` |
| `sis_course_id` | string |  | The unique SIS identifier for the course in which the section belongs. This field is only included if the user has permission to view SIS information. e.g. `7` |
| `start_at` | datetime |  | the start date for the section, if applicable e.g. `2012-06-01T00:00:00-06:00` |
| `end_at` | datetime |  | the end date for the section, if applicable |
| `restrict_enrollments_to_section_dates` | boolean |  | Restrict user enrollments to the start and end dates of the section |
| `nonxlist_course_id` | integer |  | The unique identifier of the original course of a cross-listed section |
| `total_students` | integer |  | optional: the total number of active and invited students in the section e.g. `13` |
| `students` | array[User] |  | optional: A list of students that are included in the section. Returned only if include[]=students. WARNING: this collection's size is capped (if there are an extremely large number of users in the section (thousands) not all of them will be returned). If you need to capture all the users in a section with certainty or experiencing slow response consider using the paginated /api/v1/sections/<section_id>/users endpoint. |
