# Enrollments

> Canvas LMS REST API — `/enrollments` resource. Base path `/api`.

## GET /v1/courses/{course_id}/enrollments

**List enrollments**  —  `list_enrollments_courses`

Depending on the URL given, return a paginated list of either (1) all of
the enrollments in a course, (2) all of the enrollments in a section or (3)
all of a user's enrollments. This includes student, teacher, TA, and
observer enrollments.

If a user has multiple enrollments in a context (e.g. as a teacher
and a student or in multiple course sections), each enrollment will be
listed separately.

note: Currently, only a root level admin user can return other users' enrollments.
A user can, however, return his/her own enrollments.

Enrollments scoped to a course context will include inactive states by default
if the caller has account admin authorization and the state[] parameter is omitted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `type` | array[string] | query |  | A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given. |
| `role` | array[string] | query |  | A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above. |
| `state` | array[string] | query |  | Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. The following synthetic states are supported only when querying a user's enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ Allowed: `active`, `invited`, `creation_pending`, `deleted`, `rejected`, `completed`, `inactive`, `current_and_invited`, `current_and_future`, `current_future_and_restricted`, `current_and_concluded` |
| `include` | array[string] | query |  | Array of additional information to include on the enrollment or user records. "avatar_url" and "group_ids" will be returned on the user record. If "current_points" is specified, the fields "current_points" and (if the caller has permissions to manage grades) "unposted_current_points" will be included in the "grades" hash for student enrollments. Allowed: `avatar_url`, `group_ids`, `locked`, `observed_users`, `can_be_removed`, `uuid`, `current_points` |
| `user_id` | string | query |  | Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. |
| `grading_period_id` | integer (int64) | query |  | Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. |
| `enrollment_term_id` | integer (int64) | query |  | Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with 'sis_term_id:'. |
| `sis_account_id` | array[string] | query |  | Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. |
| `sis_course_id` | array[string] | query |  | Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. |
| `sis_section_id` | array[string] | query |  | Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. |
| `sis_user_id` | array[string] | query |  | Returns only enrollments for the specified SIS user ID(s). May pass in array or string. |
| `created_for_sis_id` | array[boolean] | query |  | If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id's, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id |

**Returns:** `array[Enrollment]`

## GET /v1/sections/{section_id}/enrollments

**List enrollments**  —  `list_enrollments_sections`

Depending on the URL given, return a paginated list of either (1) all of
the enrollments in a course, (2) all of the enrollments in a section or (3)
all of a user's enrollments. This includes student, teacher, TA, and
observer enrollments.

If a user has multiple enrollments in a context (e.g. as a teacher
and a student or in multiple course sections), each enrollment will be
listed separately.

note: Currently, only a root level admin user can return other users' enrollments.
A user can, however, return his/her own enrollments.

Enrollments scoped to a course context will include inactive states by default
if the caller has account admin authorization and the state[] parameter is omitted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `type` | array[string] | query |  | A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given. |
| `role` | array[string] | query |  | A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above. |
| `state` | array[string] | query |  | Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. The following synthetic states are supported only when querying a user's enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ Allowed: `active`, `invited`, `creation_pending`, `deleted`, `rejected`, `completed`, `inactive`, `current_and_invited`, `current_and_future`, `current_future_and_restricted`, `current_and_concluded` |
| `include` | array[string] | query |  | Array of additional information to include on the enrollment or user records. "avatar_url" and "group_ids" will be returned on the user record. If "current_points" is specified, the fields "current_points" and (if the caller has permissions to manage grades) "unposted_current_points" will be included in the "grades" hash for student enrollments. Allowed: `avatar_url`, `group_ids`, `locked`, `observed_users`, `can_be_removed`, `uuid`, `current_points` |
| `user_id` | string | query |  | Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. |
| `grading_period_id` | integer (int64) | query |  | Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. |
| `enrollment_term_id` | integer (int64) | query |  | Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with 'sis_term_id:'. |
| `sis_account_id` | array[string] | query |  | Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. |
| `sis_course_id` | array[string] | query |  | Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. |
| `sis_section_id` | array[string] | query |  | Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. |
| `sis_user_id` | array[string] | query |  | Returns only enrollments for the specified SIS user ID(s). May pass in array or string. |
| `created_for_sis_id` | array[boolean] | query |  | If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id's, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id |

**Returns:** `array[Enrollment]`

## GET /v1/users/{user_id}/enrollments

**List enrollments**  —  `list_enrollments_users`

Depending on the URL given, return a paginated list of either (1) all of
the enrollments in a course, (2) all of the enrollments in a section or (3)
all of a user's enrollments. This includes student, teacher, TA, and
observer enrollments.

If a user has multiple enrollments in a context (e.g. as a teacher
and a student or in multiple course sections), each enrollment will be
listed separately.

note: Currently, only a root level admin user can return other users' enrollments.
A user can, however, return his/her own enrollments.

Enrollments scoped to a course context will include inactive states by default
if the caller has account admin authorization and the state[] parameter is omitted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `type` | array[string] | query |  | A list of enrollment types to return. Accepted values are 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', and 'ObserverEnrollment.' If omitted, all enrollment types are returned. This argument is ignored if `role` is given. |
| `role` | array[string] | query |  | A list of enrollment roles to return. Accepted values include course-level roles created by the {api:RoleOverridesController#add_role Add Role API} as well as the base enrollment types accepted by the `type` argument above. |
| `state` | array[string] | query |  | Filter by enrollment state. If omitted, 'active' and 'invited' enrollments are returned. The following synthetic states are supported only when querying a user's enrollments (either via user_id argument or via user enrollments endpoint): +current_and_invited+, +current_and_future+, +current_future_and_restricted+, +current_and_concluded+ Allowed: `active`, `invited`, `creation_pending`, `deleted`, `rejected`, `completed`, `inactive`, `current_and_invited`, `current_and_future`, `current_future_and_restricted`, `current_and_concluded` |
| `include` | array[string] | query |  | Array of additional information to include on the enrollment or user records. "avatar_url" and "group_ids" will be returned on the user record. If "current_points" is specified, the fields "current_points" and (if the caller has permissions to manage grades) "unposted_current_points" will be included in the "grades" hash for student enrollments. Allowed: `avatar_url`, `group_ids`, `locked`, `observed_users`, `can_be_removed`, `uuid`, `current_points` |
| `user_id` | string | path | yes | Filter by user_id (only valid for course or section enrollment queries). If set to the current user's id, this is a way to determine if the user has any enrollments in the course or section, independent of whether the user has permission to view other people on the roster. |
| `grading_period_id` | integer (int64) | query |  | Return grades for the given grading_period.  If this parameter is not specified, the returned grades will be for the whole course. |
| `enrollment_term_id` | integer (int64) | query |  | Returns only enrollments for the specified enrollment term. This parameter only applies to the user enrollments path. May pass the ID from the enrollment terms api or the SIS id prepended with 'sis_term_id:'. |
| `sis_account_id` | array[string] | query |  | Returns only enrollments for the specified SIS account ID(s). Does not look into sub_accounts. May pass in array or string. |
| `sis_course_id` | array[string] | query |  | Returns only enrollments matching the specified SIS course ID(s). May pass in array or string. |
| `sis_section_id` | array[string] | query |  | Returns only section enrollments matching the specified SIS section ID(s). May pass in array or string. |
| `sis_user_id` | array[string] | query |  | Returns only enrollments for the specified SIS user ID(s). May pass in array or string. |
| `created_for_sis_id` | array[boolean] | query |  | If sis_user_id is present and created_for_sis_id is true, Returns only enrollments for the specified SIS ID(s). If a user has two sis_id's, one enrollment may be created using one of the two ids. This would limit the enrollments returned from the endpoint to enrollments that were created from a sis_import with that sis_user_id |

**Returns:** `array[Enrollment]`

## GET /v1/accounts/{account_id}/enrollments/{id}

**Enrollment by ID**  —  `enrollment_by_id`

Get an Enrollment object by Enrollment ID

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | integer (int64) | path | yes | The ID of the enrollment object |

**Returns:** `Enrollment`

## POST /v1/courses/{course_id}/enrollments

**Enroll a user**  —  `enroll_user_courses`

Create a new user enrollment for a course or section.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `enrollment[start_at]` | DateTime | form |  | The start time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z |
| `enrollment[end_at]` | DateTime | form |  | The end time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z |
| `enrollment[user_id]` | string | form | yes | The ID of the user to be enrolled in the course. |
| `enrollment[type]` | string | form | yes | Enroll the user as a student, teacher, TA, observer, or designer. If no value is given, the type will be inferred by +enrollment[role]+ if supplied, otherwise 'StudentEnrollment' will be used. Allowed: `StudentEnrollment`, `TeacherEnrollment`, `TaEnrollment`, `ObserverEnrollment`, `DesignerEnrollment` |
| `enrollment[role]` | Deprecated | form |  | Assigns a custom course-level role to the user. |
| `enrollment[role_id]` | integer (int64) | form |  | Assigns a custom course-level role to the user. |
| `enrollment[enrollment_state]` | string | form |  | If set to 'active,' student will be immediately enrolled in the course. Otherwise they will be required to accept a course invitation. Default is 'invited.'.  If set to 'inactive', student will be listed in the course roster for teachers, but will not be able to participate in the course until their enrollment is activated. Allowed: `active`, `invited`, `inactive` |
| `enrollment[course_section_id]` | integer (int64) | form |  | The ID of the course section to enroll the student in. If the section-specific URL is used, this argument is redundant and will be ignored. |
| `enrollment[limit_privileges_to_course_section]` | boolean | form |  | If set, the enrollment will only allow the user to see and interact with users enrolled in the section given by course_section_id. * For teachers and TAs, this includes grading privileges. * Section-limited students will not see any users (including teachers   and TAs) not enrolled in their sections. * Users may have other enrollments that grant privileges to   multiple sections in the same course. |
| `enrollment[notify]` | boolean | form |  | If true, a notification will be sent to the enrolled user. Notifications are not sent by default. |
| `enrollment[self_enrollment_code]` | string | form |  | If the current user is not allowed to manage enrollments in this course, but the course allows self-enrollment, the user can self- enroll as a student in the default section by passing in a valid code. When self-enrolling, the user_id must be 'self'. The enrollment_state will be set to 'active' and all other arguments will be ignored. |
| `enrollment[self_enrolled]` | boolean | form |  | If true, marks the enrollment as a self-enrollment, which gives students the ability to drop the course if desired. Defaults to false. |
| `enrollment[associated_user_id]` | integer (int64) | form |  | For an observer enrollment, the ID of a student to observe. This is a one-off operation; to automatically observe all a student's enrollments (for example, as a parent), please use the {api:UserObserveesController#create User Observees API}. |
| `enrollment[sis_user_id]` | string | form |  | Required if the user is being enrolled from another trusted account. The unique identifier for the user (sis_user_id) must also be accompanied by the root_account parameter. The user_id will be ignored. |
| `enrollment[integration_id]` | string | form |  | Required if the user is being enrolled from another trusted account. The unique identifier for the user (integration_id) must also be accompanied by the root_account parameter. The user_id will be ignored. |
| `root_account` | string | form |  | The domain of the account to search for the user. Will be a no-op unless the sis_user_id or integration_id parameter is also included. |

**Returns:** `Enrollment`

## POST /v1/sections/{section_id}/enrollments

**Enroll a user**  —  `enroll_user_sections`

Create a new user enrollment for a course or section.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `enrollment[start_at]` | DateTime | form |  | The start time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z |
| `enrollment[end_at]` | DateTime | form |  | The end time of the enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z |
| `enrollment[user_id]` | string | form | yes | The ID of the user to be enrolled in the course. |
| `enrollment[type]` | string | form | yes | Enroll the user as a student, teacher, TA, observer, or designer. If no value is given, the type will be inferred by +enrollment[role]+ if supplied, otherwise 'StudentEnrollment' will be used. Allowed: `StudentEnrollment`, `TeacherEnrollment`, `TaEnrollment`, `ObserverEnrollment`, `DesignerEnrollment` |
| `enrollment[role]` | Deprecated | form |  | Assigns a custom course-level role to the user. |
| `enrollment[role_id]` | integer (int64) | form |  | Assigns a custom course-level role to the user. |
| `enrollment[enrollment_state]` | string | form |  | If set to 'active,' student will be immediately enrolled in the course. Otherwise they will be required to accept a course invitation. Default is 'invited.'.  If set to 'inactive', student will be listed in the course roster for teachers, but will not be able to participate in the course until their enrollment is activated. Allowed: `active`, `invited`, `inactive` |
| `enrollment[course_section_id]` | integer (int64) | form |  | The ID of the course section to enroll the student in. If the section-specific URL is used, this argument is redundant and will be ignored. |
| `enrollment[limit_privileges_to_course_section]` | boolean | form |  | If set, the enrollment will only allow the user to see and interact with users enrolled in the section given by course_section_id. * For teachers and TAs, this includes grading privileges. * Section-limited students will not see any users (including teachers   and TAs) not enrolled in their sections. * Users may have other enrollments that grant privileges to   multiple sections in the same course. |
| `enrollment[notify]` | boolean | form |  | If true, a notification will be sent to the enrolled user. Notifications are not sent by default. |
| `enrollment[self_enrollment_code]` | string | form |  | If the current user is not allowed to manage enrollments in this course, but the course allows self-enrollment, the user can self- enroll as a student in the default section by passing in a valid code. When self-enrolling, the user_id must be 'self'. The enrollment_state will be set to 'active' and all other arguments will be ignored. |
| `enrollment[self_enrolled]` | boolean | form |  | If true, marks the enrollment as a self-enrollment, which gives students the ability to drop the course if desired. Defaults to false. |
| `enrollment[associated_user_id]` | integer (int64) | form |  | For an observer enrollment, the ID of a student to observe. This is a one-off operation; to automatically observe all a student's enrollments (for example, as a parent), please use the {api:UserObserveesController#create User Observees API}. |
| `enrollment[sis_user_id]` | string | form |  | Required if the user is being enrolled from another trusted account. The unique identifier for the user (sis_user_id) must also be accompanied by the root_account parameter. The user_id will be ignored. |
| `enrollment[integration_id]` | string | form |  | Required if the user is being enrolled from another trusted account. The unique identifier for the user (integration_id) must also be accompanied by the root_account parameter. The user_id will be ignored. |
| `root_account` | string | form |  | The domain of the account to search for the user. Will be a no-op unless the sis_user_id or integration_id parameter is also included. |

**Returns:** `Enrollment`

## POST /v1/accounts/{account_id}/bulk_enrollment

**Enroll multiple users to one or more courses**  —  `enroll_multiple_users_to_one_or_more_courses`

Enrolls multiple users in one or more courses in a single operation.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user_ids` | array[integer] | form | yes | The user IDs to enroll in the courses. |
| `course_ids` | array[integer] | form | yes | The course IDs to enroll each user in. |
| `enrollment_type` | string | form |  | Enroll each user as a student, teacher, TA, observer, or designer. If no value is given, the type will be 'StudentEnrollment'. Allowed: `StudentEnrollment`, `TeacherEnrollment`, `TaEnrollment`, `ObserverEnrollment`, `DesignerEnrollment` |
| `enrollment_role_id` | integer (int64) | form |  | Optional custom course-level role id to apply to created enrollments. |
| `start_at` | DateTime | form |  | The start time of every created enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z. When provided, applies to all enrollments in the bulk creation. |
| `end_at` | DateTime | form |  | The end time of every created enrollment, in ISO8601 format. e.g. 2012-04-18T23:08:51Z. When provided, applies to all enrollments in the bulk creation. |

**Returns:** `Progress`

## DELETE /v1/courses/{course_id}/enrollments/{id}

**Conclude, deactivate, or delete an enrollment**  —  `conclude_deactivate_or_delete_enrollment`

Conclude, deactivate, or delete an enrollment. If the +task+ argument isn't given, the enrollment
will be concluded.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `task` | string | query |  | The action to take on the enrollment. When inactive, a user will still appear in the course roster to admins, but be unable to participate. ("inactivate" and "deactivate" are equivalent tasks) Allowed: `conclude`, `delete`, `inactivate`, `deactivate` |

**Returns:** `Enrollment`

## POST /v1/courses/{course_id}/enrollments/{id}/accept

**Accept Course Invitation**  —  `accept_course_invitation`

accepts a pending course invitation for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/enrollments/{id}/reject

**Reject Course Invitation**  —  `reject_course_invitation`

rejects a pending course invitation for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/enrollments/{id}/reactivate

**Re-activate an enrollment**  —  `re_activate_enrollment`

Activates an inactive enrollment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Enrollment`

## PUT /v1/courses/{course_id}/users/{user_id}/last_attended

**Add last attended date**  —  `add_last_attended_date`

Add last attended date to student enrollment in course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `date` | Date | form |  | The last attended date of a student enrollment in a course. |

**Returns:** `Enrollment`

## GET /v1/users/{user_id}/temporary_enrollment_status

**Show Temporary Enrollment recipient and provider status**  —  `show_temporary_enrollment_recipient_and_provider_status`

Returns a JSON Object containing the temporary enrollment status for a user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `account_id` | string | query |  | The ID of the account to check for temporary enrollment status. Defaults to the domain root account if not provided. |

**Returns:** `void`

## GET /v1/temporary_enrollment_status

**Bulk Temporary Enrollment Status**  —  `bulk_temporary_enrollment_status`

Returns temporary enrollment statuses for multiple users at once.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_ids` | array[string] | query | yes | The IDs of the users to check temporary enrollment status for. |
| `account_id` | string | query |  | The ID of the account to scope the check to. |
| `limit` | integer (int64) | query |  | The maximum number of user IDs to process. Defaults to 10, max 100. |

**Returns:** `void`


---

# Models


## Grade

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `html_url` | string |  | The URL to the Canvas web UI page for the user's grades, if this is a student enrollment. |
| `current_grade` | string |  | The user's current grade in the class. Only included if user has permissions to view this grade. |
| `final_grade` | string |  | The user's final grade for the class. Only included if user has permissions to view this grade. |
| `current_score` | string |  | The user's current score in the class. Only included if user has permissions to view this score. |
| `final_score` | string |  | The user's final score for the class. Only included if user has permissions to view this score. |
| `current_points` | integer |  | The total points the user has earned in the class. Only included if user has permissions to view this score and 'current_points' is passed in the request's 'include' parameter. e.g. `150` |
| `unposted_current_grade` | string |  | The user's current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. |
| `unposted_final_grade` | string |  | The user's final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. |
| `unposted_current_score` | string |  | The user's current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. |
| `unposted_final_score` | string |  | The user's final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. |
| `unposted_current_points` | integer |  | The total points the user has earned in the class, including muted/unposted assignments. Only included if user has permissions to view this score (typically teachers, TAs, and admins) and 'current_points' is passed in the request's 'include' parameter. e.g. `150` |


## Enrollment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the enrollment. e.g. `1` |
| `course_id` | integer |  | The unique id of the course. e.g. `1` |
| `sis_course_id` | string |  | The SIS Course ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. e.g. `SHEL93921` |
| `course_integration_id` | string |  | The Course Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. e.g. `SHEL93921` |
| `course_section_id` | integer |  | The unique id of the user's section. e.g. `1` |
| `section_integration_id` | string |  | The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. e.g. `SHEL93921` |
| `sis_account_id` | string |  | The SIS Account ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. e.g. `SHEL93921` |
| `sis_section_id` | string |  | The SIS Section ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. e.g. `SHEL93921` |
| `sis_user_id` | string |  | The SIS User ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. e.g. `SHEL93921` |
| `enrollment_state` | string |  | The state of the user's enrollment in the course. e.g. `active` |
| `limit_privileges_to_course_section` | boolean |  | User can only access his or her own course section. e.g. `True` |
| `sis_import_id` | integer |  | The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. e.g. `83` |
| `root_account_id` | integer |  | The unique id of the user's account. e.g. `1` |
| `type` | string |  | The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'. e.g. `StudentEnrollment` |
| `user_id` | integer |  | The unique id of the user. e.g. `1` |
| `associated_user_id` | integer |  | The unique id of the associated user. Will be null unless type is ObserverEnrollment. |
| `role` | string |  | The enrollment role, for course-level permissions. This field will match `type` if the enrollment role has not been customized. e.g. `StudentEnrollment` |
| `role_id` | integer |  | The id of the enrollment role. e.g. `1` |
| `created_at` | datetime |  | The created time of the enrollment, in ISO8601 format. e.g. `2012-04-18T23:08:51Z` |
| `updated_at` | datetime |  | The updated time of the enrollment, in ISO8601 format. e.g. `2012-04-18T23:08:51Z` |
| `start_at` | datetime |  | The start time of the enrollment, in ISO8601 format. e.g. `2012-04-18T23:08:51Z` |
| `end_at` | datetime |  | The end time of the enrollment, in ISO8601 format. e.g. `2012-04-18T23:08:51Z` |
| `last_activity_at` | datetime |  | The last activity time of the user for the enrollment, in ISO8601 format. e.g. `2012-04-18T23:08:51Z` |
| `last_attended_at` | datetime |  | The last attended date of the user for the enrollment in a course, in ISO8601 format. e.g. `2012-04-18T23:08:51Z` |
| `total_activity_time` | integer |  | The total activity time of the user for the enrollment, in seconds. e.g. `260` |
| `html_url` | string |  | The URL to the Canvas web UI page for this course enrollment. e.g. `https://...` |
| `grades` | Grade |  | The URL to the Canvas web UI page containing the grades associated with this enrollment. e.g. `{'html_url': 'https://...', 'current_score': 35, 'current_grade': None, 'final_score': 6.67, 'final_grade': None}` |
| `user` | User |  | A description of the user. e.g. `{'id': 3, 'name': 'Student 1', 'sortable_name': '1, Student', 'short_name': 'Stud 1'}` |
| `override_grade` | string |  | The user's override grade for the course. e.g. `A` |
| `override_score` | number |  | The user's override score for the course. e.g. `99.99` |
| `unposted_current_grade` | string |  | The user's current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. |
| `unposted_final_grade` | string |  | The user's final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. |
| `unposted_current_score` | string |  | The user's current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. |
| `unposted_final_score` | string |  | The user's final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. |
| `has_grading_periods` | boolean |  | optional: Indicates whether the course the enrollment belongs to has grading periods set up. (applies only to student enrollments, and only available in course endpoints) e.g. `True` |
| `totals_for_all_grading_periods_option` | boolean |  | optional: Indicates whether the course the enrollment belongs to has the Display Totals for 'All Grading Periods' feature enabled. (applies only to student enrollments, and only available in course endpoints) e.g. `True` |
| `current_grading_period_title` | string |  | optional: The name of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) e.g. `Fall Grading Period` |
| `current_grading_period_id` | integer |  | optional: The id of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) e.g. `5` |
| `current_period_override_grade` | string |  | The user's override grade for the current grading period. e.g. `A` |
| `current_period_override_score` | number |  | The user's override score for the current grading period. e.g. `99.99` |
| `current_period_unposted_current_score` | number |  | optional: The student's score in the course for the current grading period, including muted/unposted assignments. Only included if user has permission to view this score, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) e.g. `95.8` |
| `current_period_unposted_final_score` | number |  | optional: The student's score in the course for the current grading period, including muted/unposted assignments and including ungraded assignments with a score of 0. Only included if user has permission to view this score, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) e.g. `85.25` |
| `current_period_unposted_current_grade` | string |  | optional: The letter grade equivalent of current_period_unposted_current_score, if available. Only included if user has permission to view this grade, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) e.g. `A` |
| `current_period_unposted_final_grade` | string |  | optional: The letter grade equivalent of current_period_unposted_final_score, if available. Only included if user has permission to view this grade, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) e.g. `B` |
