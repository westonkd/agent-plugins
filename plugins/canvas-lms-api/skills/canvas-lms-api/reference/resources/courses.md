# Courses

> Canvas LMS REST API — `/courses` resource. Base path `/api`.

## GET /v1/courses

**List your courses**  —  `list_your_courses`

Returns the paginated list of active courses for the current user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `enrollment_type` | string | query |  | When set, only return courses where the user is enrolled as this type. For example, set to "teacher" to return only courses where the user is enrolled as a Teacher.  This argument is ignored if enrollment_role is given. Allowed: `teacher`, `student`, `ta`, `observer`, `designer` |
| `enrollment_role` | string | query |  | Deprecated When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. |
| `enrollment_role_id` | integer (int64) | query |  | When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. |
| `enrollment_state` | string | query |  | When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides. Allowed: `active`, `invited_or_pending`, `completed` |
| `exclude_blueprint_courses` | boolean | query |  | When set, only return courses that are not configured as blueprint courses. |
| `include` | array[string] | query |  | - "needs_grading_count": Optional information to include with each Course.   When needs_grading_count is given, and the current user has grading   rights, the total number of submissions needing grading for all   assignments is returned. - "syllabus_body": Optional information to include with each Course.   When syllabus_body is given the user-generated html for the course   syllabus is returned. - "public_description": Optional information to include with each Course.   When public_description is given the user-generated text for the course   public description is returned. - "total_scores": Optional information to include with each Course.   When total_scores is given, any student enrollments will also   include the fields 'computed_current_score', 'computed_final_score',   'computed_current_grade', and 'computed_final_grade', as well as (if   the user has permission) 'unposted_current_score',   'unposted_final_score', 'unposted_current_grade', and   'unposted_final_grade' (see Enrollment documentation for more   information on these fields). This argument is ignored if the course is   configured to hide final grades. - "current_grading_period_scores": Optional information to include with   each Course. When current_grading_period_scores is given and total_scores   is given, any student enrollments will also include the fields   'has_grading_periods',   'totals_for_all_grading_periods_option', 'current_grading_period_title',   'current_grading_period_id', current_period_computed_current_score',   'current_period_computed_final_score',   'current_period_computed_current_grade', and   'current_period_computed_final_grade', as well as (if the user has permission)   'current_period_unposted_current_score',   'current_period_unposted_final_score',   'current_period_unposted_current_grade', and   'current_period_unposted_final_grade' (see Enrollment documentation for   more information on these fields). In addition, when this argument is   passed, the course will have a 'has_grading_periods' attribute   on it. This argument is ignored if the total_scores argument is not   included. If the course is configured to hide final grades, the   following fields are not returned:   'totals_for_all_grading_periods_option',   'current_period_computed_current_score',   'current_period_computed_final_score',   'current_period_computed_current_grade',   'current_period_computed_final_grade',   'current_period_unposted_current_score',   'current_period_unposted_final_score',   'current_period_unposted_current_grade', and   'current_period_unposted_final_grade' - "grading_periods": Optional information to include with each Course. When   grading_periods is given, a list of the grading periods associated with   each course is returned. - "term": Optional information to include with each Course. When   term is given, the information for the enrollment term for each course   is returned. - "account": Optional information to include with each Course. When   account is given, the account json for each course is returned. - "course_progress": Optional information to include with each Course.   When course_progress is given, each course will include a   'course_progress' object with the fields: 'requirement_count', an integer   specifying the total number of requirements in the course,   'requirement_completed_count', an integer specifying the total number of   requirements in this course that have been completed, and   'next_requirement_url', a string url to the next requirement item, and   'completed_at', the date the course was completed (null if incomplete).   'next_requirement_url' will be null if all requirements have been   completed or the current module does not require sequential progress.   "course_progress" will return an error message if the course is not   module based or the user is not enrolled as a student in the course. - "sections": Section enrollment information to include with each Course.   Returns an array of hashes containing the section ID (id), section name   (name), start and end dates (start_at, end_at), as well as the enrollment   type (enrollment_role, e.g. 'StudentEnrollment'). - "storage_quota_used_mb": The amount of storage space used by the files in this course - "total_students": Optional information to include with each Course.   Returns an integer for the total amount of active and invited students. - "passback_status": Include the grade passback_status - "favorites": Optional information to include with each Course.   Indicates if the user has marked the course as a favorite course. - "teachers": Teacher information to include with each Course.   Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information   for each teacher in the course. - "observed_users": Optional information to include with each Course.   Will include data for observed users if the current user has an   observer enrollment. - "tabs": Optional information to include with each Course.   Will include the list of tabs configured for each course.  See the   {api:TabsController#index List available tabs API} for more information. - "course_image": Optional information to include with each Course. Returns course   image url if a course image has been set. - "banner_image": Optional information to include with each Course. Returns course   banner image url if the course is a Canvas for Elementary subject and a banner   image has been set. - "concluded": Optional information to include with each Course. Indicates whether   the course has been concluded, taking course and term dates into account. - "post_manually": Optional information to include with each Course. Returns true if   the course post policy is set to Manually post grades. Returns false if the the course   post policy is set to Automatically post grades. Allowed: `needs_grading_count`, `syllabus_body`, `public_description`, `total_scores`, `current_grading_period_scores`, `grading_periods`, `term`, `account`, `course_progress`, `sections`, `storage_quota_used_mb`, `total_students`, `passback_status`, `favorites`, `teachers`, `observed_users`, `course_image`, `banner_image`, `concluded`, `post_manually` |
| `state` | array[string] | query |  | If set, only return courses that are in the given state(s). By default, "available" is returned for students and observers, and anything except "deleted", for all other enrollment types Allowed: `unpublished`, `available`, `completed`, `deleted` |

**Returns:** `array[Course]`

## GET /v1/users/{user_id}/courses

**List courses for a user**  —  `list_courses_for_user`

Returns a paginated list of active courses for this user. To view the course list for a user other than yourself, you must be either an observer of that user or an administrator.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "needs_grading_count": Optional information to include with each Course.   When needs_grading_count is given, and the current user has grading   rights, the total number of submissions needing grading for all   assignments is returned. - "syllabus_body": Optional information to include with each Course.   When syllabus_body is given the user-generated html for the course   syllabus is returned. - "public_description": Optional information to include with each Course.   When public_description is given the user-generated text for the course   public description is returned. - "total_scores": Optional information to include with each Course.   When total_scores is given, any student enrollments will also   include the fields 'computed_current_score', 'computed_final_score',   'computed_current_grade', and 'computed_final_grade' (see Enrollment   documentation for more information on these fields). This argument   is ignored if the course is configured to hide final grades. - "current_grading_period_scores": Optional information to include with   each Course. When current_grading_period_scores is given and total_scores   is given, any student enrollments will also include the fields   'has_grading_periods',   'totals_for_all_grading_periods_option', 'current_grading_period_title',   'current_grading_period_id', current_period_computed_current_score',   'current_period_computed_final_score',   'current_period_computed_current_grade', and   'current_period_computed_final_grade', as well as (if the user has permission)   'current_period_unposted_current_score',   'current_period_unposted_final_score',   'current_period_unposted_current_grade', and   'current_period_unposted_final_grade' (see Enrollment documentation for   more information on these fields). In addition, when this argument is   passed, the course will have a 'has_grading_periods' attribute   on it. This argument is ignored if the course is configured to hide final   grades or if the total_scores argument is not included. - "grading_periods": Optional information to include with each Course. When   grading_periods is given, a list of the grading periods associated with   each course is returned. - "term": Optional information to include with each Course. When   term is given, the information for the enrollment term for each course   is returned. - "account": Optional information to include with each Course. When   account is given, the account json for each course is returned. - "course_progress": Optional information to include with each Course.   When course_progress is given, each course will include a   'course_progress' object with the fields: 'requirement_count', an integer   specifying the total number of requirements in the course,   'requirement_completed_count', an integer specifying the total number of   requirements in this course that have been completed, and   'next_requirement_url', a string url to the next requirement item, and   'completed_at', the date the course was completed (null if incomplete).   'next_requirement_url' will be null if all requirements have been   completed or the current module does not require sequential progress.   "course_progress" will return an error message if the course is not   module based or the user is not enrolled as a student in the course. - "sections": Section enrollment information to include with each Course.   Returns an array of hashes containing the section ID (id), section name   (name), start and end dates (start_at, end_at), as well as the enrollment   type (enrollment_role, e.g. 'StudentEnrollment'). - "storage_quota_used_mb": The amount of storage space used by the files in this course - "total_students": Optional information to include with each Course.   Returns an integer for the total amount of active and invited students. - "passback_status": Include the grade passback_status - "favorites": Optional information to include with each Course.   Indicates if the user has marked the course as a favorite course. - "teachers": Teacher information to include with each Course.   Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information   for each teacher in the course. - "observed_users": Optional information to include with each Course.   Will include data for observed users if the current user has an   observer enrollment. - "tabs": Optional information to include with each Course.   Will include the list of tabs configured for each course.  See the   {api:TabsController#index List available tabs API} for more information. - "course_image": Optional information to include with each Course. Returns course   image url if a course image has been set. - "banner_image": Optional information to include with each Course. Returns course   banner image url if the course is a Canvas for Elementary subject and a banner   image has been set. - "concluded": Optional information to include with each Course. Indicates whether   the course has been concluded, taking course and term dates into account. - "post_manually": Optional information to include with each Course. Returns true if   the course post policy is set to "Manually". Returns false if the the course post   policy is set to "Automatically". Allowed: `needs_grading_count`, `syllabus_body`, `public_description`, `total_scores`, `current_grading_period_scores`, `grading_periods`, `term`, `account`, `course_progress`, `sections`, `storage_quota_used_mb`, `total_students`, `passback_status`, `favorites`, `teachers`, `observed_users`, `course_image`, `banner_image`, `concluded`, `post_manually` |
| `state` | array[string] | query |  | If set, only return courses that are in the given state(s). By default, "available" is returned for students and observers, and anything except "deleted", for all other enrollment types Allowed: `unpublished`, `available`, `completed`, `deleted` |
| `enrollment_state` | string | query |  | When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides. Allowed: `active`, `invited_or_pending`, `completed` |
| `homeroom` | boolean | query |  | If set, only return homeroom courses. |
| `account_id` | string | query |  | If set, only include courses associated with this account |

**Returns:** `array[Course]`

## GET /v1/courses/{course_id}/users/{user_id}/progress

**Get user progress**  —  `get_user_progress`

Return progress information for the user and course

You can supply +self+ as the user_id to query your own progress in a course. To query another user's progress,
you must be a teacher in the course, an administrator, or a linked observer of the user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `CourseProgress`

## POST /v1/accounts/{account_id}/courses

**Create a new course**  —  `create_new_course`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `course[name]` | string | form |  | The name of the course. If omitted, the course will be named "Unnamed Course." |
| `course[course_code]` | string | form |  | The course code for the course. |
| `course[start_at]` | DateTime | form |  | Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true. |
| `course[end_at]` | DateTime | form |  | Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true. |
| `course[license]` | string | form |  | The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - 'private' (Private Copyrighted) - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives) - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike) - 'cc_by_nc' (CC Attribution Non-Commercial) - 'cc_by_nd' (CC Attribution No Derivatives) - 'cc_by_sa' (CC Attribution Share Alike) - 'cc_by' (CC Attribution) - 'public_domain' (Public Domain). |
| `course[is_public]` | boolean | form |  | Set to true if course is public to both authenticated and unauthenticated users. |
| `course[is_public_to_auth_users]` | boolean | form |  | Set to true if course is public only to authenticated users. |
| `course[public_syllabus]` | boolean | form |  | Set to true to make the course syllabus public. |
| `course[public_syllabus_to_auth]` | boolean | form |  | Set to true to make the course syllabus public for authenticated users. |
| `course[public_description]` | string | form |  | A publicly visible description of the course. |
| `course[allow_student_wiki_edits]` | boolean | form |  | If true, students will be able to modify the course wiki. |
| `course[allow_wiki_comments]` | boolean | form |  | If true, course members will be able to comment on wiki pages. |
| `course[allow_student_forum_attachments]` | boolean | form |  | If true, students can attach files to forum posts. |
| `course[open_enrollment]` | boolean | form |  | Set to true if the course is open enrollment. |
| `course[self_enrollment]` | boolean | form |  | Set to true if the course is self enrollment. |
| `course[restrict_enrollments_to_course_dates]` | boolean | form |  | Set to true to restrict user enrollments to the start and end dates of the course. This value must be set to true in order to specify a course start date and/or end date. |
| `course[term_id]` | string | form |  | The unique ID of the term to create to course in. |
| `course[sis_course_id]` | string | form |  | The unique SIS identifier. |
| `course[integration_id]` | string | form |  | The unique Integration identifier. |
| `course[hide_final_grades]` | boolean | form |  | If this option is set to true, the totals in student grades summary will be hidden. |
| `course[apply_assignment_group_weights]` | boolean | form |  | Set to true to weight final grade based on assignment groups percentages. |
| `course[time_zone]` | string | form |  | The time zone for the course. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `offer` | boolean | form |  | If this option is set to true, the course will be available to students immediately. |
| `enroll_me` | boolean | form |  | Set to true to enroll the current user as the teacher. |
| `skip_course_template` | boolean | form |  | If this option is set to true, the template of the account will not be applied to this course It means copy_from_course_template will not be executed. This option is thought for a course copy. |
| `course[default_view]` | string | form |  | The type of page that users will see when they first visit the course * 'feed' Recent Activity Dashboard * 'modules' Course Modules/Sections Page * 'assignments' Course Assignments List * 'syllabus' Course Syllabus Page other types may be added in the future Allowed: `feed`, `wiki`, `modules`, `syllabus`, `assignments` |
| `course[syllabus_body]` | string | form |  | The syllabus body for the course |
| `course[grading_standard_id]` | integer (int64) | form |  | The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course. |
| `course[grade_passback_setting]` | string | form |  | Optional. The grade_passback_setting for the course. Only 'nightly_sync', 'disabled', and '' are allowed |
| `course[course_format]` | string | form |  | Optional. Specifies the format of the course. (Should be 'on_campus', 'online', or 'blended') |
| `course[post_manually]` | boolean | form |  | Default is false. When true, all grades in the course must be posted manually, and will not be automatically posted. When false, all grades in the course will be automatically posted. |
| `enable_sis_reactivation` | boolean | form |  | When true, will first try to re-activate a deleted course with matching sis_course_id if possible. |

**Returns:** `Course`

## POST /v1/courses/{course_id}/files

**Upload a file**  —  `upload_file`

Upload a file to the course.

This API endpoint is the first step in uploading a file to a course.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Only those with the "Manage Files" permission on a course can upload files
to the course. By default, this is Teachers, TAs and Designers.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/students

**List students**  —  `list_students`

Returns the paginated list of students enrolled in this course.

DEPRECATED: Please use the {api:CoursesController#users course users} endpoint
and pass "student" as the enrollment_type.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[User]`

## GET /v1/courses/{course_id}/users

**List users in course**  —  `list_users_in_course_users`

Returns the paginated list of users in this course. And optionally the user's enrollments in the course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name or full ID of the users to match and return in the results list. |
| `sort` | string | query |  | When set, sort the results of the search based on the given field. Allowed: `username`, `last_login`, `email`, `sis_id` |
| `enrollment_type` | array[string] | query |  | When set, only return users where the user is enrolled as this type. "student_view" implies include[]=test_student. This argument is ignored if enrollment_role is given. Allowed: `teacher`, `student`, `student_view`, `ta`, `observer`, `designer` |
| `enrollment_role` | string | query |  | Deprecated When set, only return users enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. |
| `enrollment_role_id` | integer (int64) | query |  | When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. |
| `section_ids` | array[integer] | query |  | When set, only return users who are enrolled in the given section(s). |
| `include` | array[string] | query |  | - "enrollments": Optionally include with each Course the user's current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a 'grades' key with 'current_score', 'final_score', 'current_grade' and 'final_grade' values. - "locked": Optionally include whether an enrollment is locked. - "avatar_url": Optionally include avatar_url. - "bio": Optionally include each user's bio. - "test_student": Optionally include the course's Test Student, if present. Default is to not include Test Student. - "custom_links": Optionally include plugin-supplied custom links for each student, such as analytics information - "current_grading_period_scores": if enrollments is included as well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A 'grading_period_id' value will also be included with the scores. if grading_period_id is nil there is no current grading period and the score is a total score. - "uuid": Optionally include the users uuid Allowed: `enrollments`, `locked`, `avatar_url`, `test_student`, `bio`, `custom_links`, `current_grading_period_scores`, `uuid` |
| `user_id` | string | query |  | If this parameter is given and it corresponds to a user in the course, the +page+ parameter will be ignored and the page containing the specified user will be returned instead. |
| `user_ids` | array[integer] | query |  | If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the "user_id" argument but multiple user_ids can be included. |
| `enrollment_state` | array[string] | query |  | When set, only return users where the enrollment workflow state is of one of the given types. "active" and "invited" enrollments are returned by default. Allowed: `active`, `invited`, `rejected`, `completed`, `inactive` |

**Returns:** `array[User]`

## GET /v1/courses/{course_id}/search_users

**List users in course**  —  `list_users_in_course_search_users`

Returns the paginated list of users in this course. And optionally the user's enrollments in the course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial name or full ID of the users to match and return in the results list. |
| `sort` | string | query |  | When set, sort the results of the search based on the given field. Allowed: `username`, `last_login`, `email`, `sis_id` |
| `enrollment_type` | array[string] | query |  | When set, only return users where the user is enrolled as this type. "student_view" implies include[]=test_student. This argument is ignored if enrollment_role is given. Allowed: `teacher`, `student`, `student_view`, `ta`, `observer`, `designer` |
| `enrollment_role` | string | query |  | Deprecated When set, only return users enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. |
| `enrollment_role_id` | integer (int64) | query |  | When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'. |
| `section_ids` | array[integer] | query |  | When set, only return users who are enrolled in the given section(s). |
| `include` | array[string] | query |  | - "enrollments": Optionally include with each Course the user's current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a 'grades' key with 'current_score', 'final_score', 'current_grade' and 'final_grade' values. - "locked": Optionally include whether an enrollment is locked. - "avatar_url": Optionally include avatar_url. - "bio": Optionally include each user's bio. - "test_student": Optionally include the course's Test Student, if present. Default is to not include Test Student. - "custom_links": Optionally include plugin-supplied custom links for each student, such as analytics information - "current_grading_period_scores": if enrollments is included as well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A 'grading_period_id' value will also be included with the scores. if grading_period_id is nil there is no current grading period and the score is a total score. - "uuid": Optionally include the users uuid Allowed: `enrollments`, `locked`, `avatar_url`, `test_student`, `bio`, `custom_links`, `current_grading_period_scores`, `uuid` |
| `user_id` | string | query |  | If this parameter is given and it corresponds to a user in the course, the +page+ parameter will be ignored and the page containing the specified user will be returned instead. |
| `user_ids` | array[integer] | query |  | If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the "user_id" argument but multiple user_ids can be included. |
| `enrollment_state` | array[string] | query |  | When set, only return users where the enrollment workflow state is of one of the given types. "active" and "invited" enrollments are returned by default. Allowed: `active`, `invited`, `rejected`, `completed`, `inactive` |

**Returns:** `array[User]`

## GET /v1/courses/{course_id}/recent_students

**List recently logged in students**  —  `list_recently_logged_in_students`

Returns the paginated list of users in this course, ordered by how recently they have
logged in. The records include the 'last_login' field which contains
a timestamp of the last time that user logged into canvas.  The querying
user must have the 'View usage reports' permission.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[User]`

## GET /v1/courses/{course_id}/users/{id}

**Get single user**  —  `get_single_user`

Return information on a single user.

Accepts the same include[] parameters as the :users: action, and returns a
single user with the same fields as that action.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `User`

## GET /v1/courses/{course_id}/content_share_users

**Search for content share users**  —  `search_for_content_share_users`

Returns a paginated list of users you can share content with.  Requires the content share
feature and the user must have the manage content permission for the course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `search_term` | string | query | yes | Term used to find users.  Will search available share users with the search term in their name. |

**Returns:** `array[User]`

## POST /v1/courses/{course_id}/preview_html

**Preview processed html**  —  `preview_processed_html`

Preview html content processed for this course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `html` | string | form |  | The html content to process |

**Returns:** `void`

## GET /v1/courses/{course_id}/activity_stream

**Course activity stream**  —  `course_activity_stream`

Returns the current user's course-specific activity stream, paginated.

For full documentation, see the API documentation for the user activity
stream, in the user api.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/activity_stream/summary

**Course activity stream summary**  —  `course_activity_stream_summary`

Returns a summary of the current user's course-specific activity stream.

For full documentation, see the API documentation for the user activity
stream summary, in the user api.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/todo

**Course TODO items**  —  `course_todo_items`

Returns the current user's course-specific todo items.

For full documentation, see the API documentation for the user todo items, in the user api.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/courses/{id}

**Delete/Conclude a course**  —  `delete_conclude_course`

Delete or conclude an existing course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `event` | string | query | yes | The action to take on the course. Allowed: `delete`, `conclude` |

**Returns:** `void`

## GET /v1/courses/{course_id}/settings

**Get course settings**  —  `get_course_settings`

Returns some of a course's settings.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/settings

**Update course settings**  —  `update_course_settings`

Can update the following course settings:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `allow_final_grade_override` | boolean | form |  | Let student final grades for a grading period or the total grades for the course be overridden |
| `allow_student_discussion_topics` | boolean | form |  | Let students create discussion topics |
| `allow_student_forum_attachments` | boolean | form |  | Let students attach files to discussions |
| `allow_student_discussion_editing` | boolean | form |  | Let students edit or delete their own discussion replies |
| `allow_student_organized_groups` | boolean | form |  | Let students organize their own groups |
| `allow_student_discussion_reporting` | boolean | form |  | Let students report offensive discussion content |
| `allow_student_anonymous_discussion_topics` | boolean | form |  | Let students create anonymous discussion topics |
| `filter_speed_grader_by_student_group` | boolean | form |  | Filter SpeedGrader to only the selected student group |
| `hide_final_grades` | boolean | form |  | Hide totals in student grades summary |
| `hide_distribution_graphs` | boolean | form |  | Hide grade distribution graphs from students |
| `hide_sections_on_course_users_page` | boolean | form |  | Disallow students from viewing students in sections they do not belong to |
| `lock_all_announcements` | boolean | form |  | Disable comments on announcements |
| `usage_rights_required` | boolean | form |  | Copyright and license information must be provided for files before they are published. |
| `restrict_student_past_view` | boolean | form |  | Restrict students from viewing courses after end date |
| `restrict_student_future_view` | boolean | form |  | Restrict students from viewing courses before start date |
| `show_announcements_on_home_page` | boolean | form |  | Show the most recent announcements on the Course home page (if a Wiki, defaults to five announcements, configurable via home_page_announcement_limit). Canvas for Elementary subjects ignore this setting. |
| `home_page_announcement_limit` | integer (int64) | form |  | Limit the number of announcements on the home page if enabled via show_announcements_on_home_page |
| `syllabus_course_summary` | boolean | form |  | Show the course summary (list of assignments and calendar events) on the syllabus page. Default is true. |
| `default_due_time` | string | form |  | Set the default due time for assignments. This is the time that will be pre-selected in the Canvas user interface when setting a due date for an assignment. It does not change when any existing assignment is due. It should be given in 24-hour HH:MM:SS format. The default is "23:59:59". Use "inherit" to inherit the account setting. |
| `conditional_release` | boolean | form |  | Enable or disable individual learning paths for students based on assessment |

**Returns:** `void`

## GET /v1/courses/{course_id}/student_view_student

**Return test student for course**  —  `return_test_student_for_course`

Returns information for a test student in this course. Creates a test
student if one does not already exist for the course. The caller must have
permission to access the course's student view.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `User`

## GET /v1/courses/{id}

**Get a single course**  —  `get_single_course_courses`

Return information on a single course.

Accepts the same include[] parameters as the list action plus:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "all_courses": Also search recently deleted courses. - "permissions": Include permissions the current user has   for the course. - "observed_users": Include observed users in the enrollments - "course_image": Include course image url if a course image has been set - "banner_image": Include course banner image url if the course is a Canvas for   Elementary subject and a banner image has been set - "concluded": Optional information to include with Course. Indicates whether   the course has been concluded, taking course and term dates into account. - "lti_context_id": Include course LTI tool id. - "post_manually": Include course post policy. If the post policy is manually post grades,   the value will be true. If the post policy is automatically post grades, the value will be false. Allowed: `needs_grading_count`, `syllabus_body`, `public_description`, `total_scores`, `current_grading_period_scores`, `term`, `account`, `course_progress`, `sections`, `storage_quota_used_mb`, `total_students`, `passback_status`, `favorites`, `teachers`, `observed_users`, `all_courses`, `permissions`, `course_image`, `banner_image`, `concluded`, `lti_context_id`, `post_manually` |
| `teacher_limit` | integer (int64) | query |  | The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a _teacher_count_ key. |

**Returns:** `Course`

## GET /v1/accounts/{account_id}/courses/{id}

**Get a single course**  —  `get_single_course_accounts`

Return information on a single course.

Accepts the same include[] parameters as the list action plus:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "all_courses": Also search recently deleted courses. - "permissions": Include permissions the current user has   for the course. - "observed_users": Include observed users in the enrollments - "course_image": Include course image url if a course image has been set - "banner_image": Include course banner image url if the course is a Canvas for   Elementary subject and a banner image has been set - "concluded": Optional information to include with Course. Indicates whether   the course has been concluded, taking course and term dates into account. - "lti_context_id": Include course LTI tool id. - "post_manually": Include course post policy. If the post policy is manually post grades,   the value will be true. If the post policy is automatically post grades, the value will be false. Allowed: `needs_grading_count`, `syllabus_body`, `public_description`, `total_scores`, `current_grading_period_scores`, `term`, `account`, `course_progress`, `sections`, `storage_quota_used_mb`, `total_students`, `passback_status`, `favorites`, `teachers`, `observed_users`, `all_courses`, `permissions`, `course_image`, `banner_image`, `concluded`, `lti_context_id`, `post_manually` |
| `teacher_limit` | integer (int64) | query |  | The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a _teacher_count_ key. |

**Returns:** `Course`

## PUT /v1/courses/{id}

**Update a course**  —  `update_course`

Update an existing course.

Arguments are the same as Courses#create, with a few exceptions (enroll_me).

If a user has content management rights, but not full course editing rights, the only attribute
editable through this endpoint will be "syllabus_body"

If an account has set prevent_course_availability_editing_by_teachers, a teacher cannot change
+course[start_at]+, +course[conclude_at]+, or +course[restrict_enrollments_to_course_dates]+ here.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `course[account_id]` | integer (int64) | form |  | The unique ID of the account to move the course to. |
| `course[name]` | string | form |  | The name of the course. If omitted, the course will be named "Unnamed Course." |
| `course[course_code]` | string | form |  | The course code for the course. |
| `course[start_at]` | DateTime | form |  | Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true, or the course is already published. |
| `course[end_at]` | DateTime | form |  | Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true. |
| `course[license]` | string | form |  | The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference): - 'private' (Private Copyrighted) - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives) - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike) - 'cc_by_nc' (CC Attribution Non-Commercial) - 'cc_by_nd' (CC Attribution No Derivatives) - 'cc_by_sa' (CC Attribution Share Alike) - 'cc_by' (CC Attribution) - 'public_domain' (Public Domain). |
| `course[is_public]` | boolean | form |  | Set to true if course is public to both authenticated and unauthenticated users. |
| `course[is_public_to_auth_users]` | boolean | form |  | Set to true if course is public only to authenticated users. |
| `course[public_syllabus]` | boolean | form |  | Set to true to make the course syllabus public. |
| `course[public_syllabus_to_auth]` | boolean | form |  | Set to true to make the course syllabus to public for authenticated users. |
| `course[public_description]` | string | form |  | A publicly visible description of the course. |
| `course[allow_student_wiki_edits]` | boolean | form |  | If true, students will be able to modify the course wiki. |
| `course[allow_wiki_comments]` | boolean | form |  | If true, course members will be able to comment on wiki pages. |
| `course[allow_student_forum_attachments]` | boolean | form |  | If true, students can attach files to forum posts. |
| `course[open_enrollment]` | boolean | form |  | Set to true if the course is open enrollment. |
| `course[self_enrollment]` | boolean | form |  | Set to true if the course is self enrollment. |
| `course[restrict_enrollments_to_course_dates]` | boolean | form |  | Set to true to restrict user enrollments to the start and end dates of the course. Setting this value to false will remove the course end date (if it exists), as well as the course start date (if the course is unpublished). |
| `course[term_id]` | integer (int64) | form |  | The unique ID of the term to create to course in. |
| `course[sis_course_id]` | string | form |  | The unique SIS identifier. |
| `course[integration_id]` | string | form |  | The unique Integration identifier. |
| `course[hide_final_grades]` | boolean | form |  | If this option is set to true, the totals in student grades summary will be hidden. |
| `course[time_zone]` | string | form |  | The time zone for the course. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. |
| `course[apply_assignment_group_weights]` | boolean | form |  | Set to true to weight final grade based on assignment groups percentages. |
| `course[storage_quota_mb]` | integer (int64) | form |  | Set the storage quota for the course, in megabytes. The caller must have the "Manage storage quotas" account permission. |
| `offer` | boolean | form |  | If this option is set to true, the course will be available to students immediately. |
| `course[event]` | string | form |  | The action to take on each course. * 'claim' makes a course no longer visible to students. This action is also called "unpublish" on the web site.   A course cannot be unpublished if students have received graded submissions. * 'offer' makes a course visible to students. This action is also called "publish" on the web site. * 'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears   in prior-enrollment lists. * 'delete' completely removes the course from the web site (including course menus and prior-enrollment lists).   All enrollments are deleted. Course content may be physically deleted at a future date. * 'undelete' attempts to recover a course that has been deleted. This action requires account administrative rights.   (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course   will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered. Allowed: `claim`, `offer`, `conclude`, `delete`, `undelete` |
| `course[default_view]` | string | form |  | The type of page that users will see when they first visit the course * 'feed' Recent Activity Dashboard * 'wiki' Wiki Front Page * 'modules' Course Modules/Sections Page * 'assignments' Course Assignments List * 'syllabus' Course Syllabus Page other types may be added in the future Allowed: `feed`, `wiki`, `modules`, `syllabus`, `assignments` |
| `course[syllabus_body]` | string | form |  | The syllabus body for the course |
| `course[syllabus_course_summary]` | boolean | form |  | Optional. Indicates whether the Course Summary (consisting of the course's assignments and calendar events) is displayed on the syllabus page. Defaults to +true+. |
| `course[grading_standard_id]` | integer (int64) | form |  | The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course. |
| `course[grade_passback_setting]` | string | form |  | Optional. The grade_passback_setting for the course. Only 'nightly_sync' and '' are allowed |
| `course[course_format]` | string | form |  | Optional. Specifies the format of the course. (Should be either 'on_campus' or 'online') |
| `course[image_id]` | integer (int64) | form |  | This is a file ID corresponding to an image file in the course that will be used as the course image. This will clear the course's image_url setting if set.  If you attempt to provide image_url and image_id in a request it will fail. |
| `course[image_url]` | string | form |  | This is a URL to an image to be used as the course image. This will clear the course's image_id setting if set.  If you attempt to provide image_url and image_id in a request it will fail. |
| `course[remove_image]` | boolean | form |  | If this option is set to true, the course image url and course image ID are both set to nil |
| `course[remove_banner_image]` | boolean | form |  | If this option is set to true, the course banner image url and course banner image ID are both set to nil |
| `course[blueprint]` | boolean | form |  | Sets the course as a blueprint course. |
| `course[blueprint_restrictions]` | BlueprintRestriction | form |  | Sets a default set to apply to blueprint course objects when restricted, unless _use_blueprint_restrictions_by_object_type_ is enabled. See the {api:Blueprint_Courses:BlueprintRestriction Blueprint Restriction} documentation |
| `course[use_blueprint_restrictions_by_object_type]` | boolean | form |  | When enabled, the _blueprint_restrictions_ parameter will be ignored in favor of the _blueprint_restrictions_by_object_type_ parameter |
| `course[blueprint_restrictions_by_object_type]` | multiple BlueprintRestrictions | form |  | Allows setting multiple {api:Blueprint_Courses:BlueprintRestriction Blueprint Restriction} to apply to blueprint course objects of the matching type when restricted. The possible object types are "assignment", "attachment", "discussion_topic", "quiz" and "wiki_page". Example usage:   course[blueprint_restrictions_by_object_type][assignment][content]=1 |
| `course[homeroom_course]` | boolean | form |  | Sets the course as a homeroom course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account. |
| `course[sync_enrollments_from_homeroom]` | string | form |  | Syncs enrollments from the homeroom that is set in homeroom_course_id. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled. |
| `course[homeroom_course_id]` | string | form |  | Sets the Homeroom Course id to be used with sync_enrollments_from_homeroom. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled. |
| `course[template]` | boolean | form |  | Enable or disable the course as a template that can be selected by an account |
| `course[course_color]` | string | form |  | Sets a color in hex code format to be associated with the course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account. |
| `course[friendly_name]` | string | form |  | Set a friendly name for the course. If this is provided and the course is associated with a Canvas for Elementary account, it will be shown instead of the course name. This setting takes priority over course nicknames defined by individual users. |
| `course[enable_course_paces]` | boolean | form |  | Enable or disable Course Pacing for the course. This setting only has an effect when the Course Pacing feature flag is enabled for the sub-account. Otherwise, Course Pacing are always disabled. |
| `course[conditional_release]` | boolean | form |  | Enable or disable individual learning paths for students based on assessment |
| `course[post_manually]` | boolean | form |  | When true, all grades in the course will be posted manually. When false, all grades in the course will be automatically posted. Use with caution as this setting will override any assignment level post policy. |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `void`

## PUT /v1/accounts/{account_id}/courses

**Update courses**  —  `update_courses`

Update multiple courses in an account.  Operates asynchronously; use the {api:ProgressController#show progress endpoint}
to query the status of an operation.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `course_ids` | array[string] | form | yes | List of ids of courses to update. At most 500 courses may be updated in one call. |
| `event` | string | form | yes | The action to take on each course.  Must be one of 'offer', 'conclude', 'delete', or 'undelete'. * 'offer' makes a course visible to students. This action is also called "publish" on the web site. * 'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears   in prior-enrollment lists. * 'delete' completely removes the course from the web site (including course menus and prior-enrollment lists).   All enrollments are deleted. Course content may be physically deleted at a future date. * 'undelete' attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude   rather than delete a course if there is any possibility the course will be used again.) The recovered course   will be unpublished. Deleted enrollments will not be recovered. Allowed: `offer`, `conclude`, `delete`, `undelete` |

**Returns:** `Progress`

## POST /v1/courses/{course_id}/reset_content

**Reset a course**  —  `reset_course`

Deletes the current course, and creates a new equivalent course with
no content, but all sections and users moved over.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `Course`

## GET /v1/courses/{course_id}/effective_due_dates

**Get effective due dates**  —  `get_effective_due_dates`

For each assignment in the course, returns each assigned student's ID
and their corresponding due date along with some grading period data.
Returns a collection with keys representing assignment IDs and values as a
collection containing keys representing student IDs and values representing
the student's effective due_at, the grading_period_id of which the due_at falls
in, and whether or not the grading period is closed (in_closed_grading_period)

The list of assignment IDs for which effective student due dates are
requested. If not provided, all assignments in the course will be used.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_ids` | array[string] | query |  | no description |

**Returns:** `void`

## GET /v1/courses/{course_id}/permissions

**Permissions**  —  `permissions`

Returns permission information for the calling user in the given course.
See also the {api:AccountsController#permissions Account} and
{api:GroupsController#permissions Group} counterparts.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `permissions` | array[string] | query |  | List of permissions to check against the authenticated user. Permission names are documented in the {api:RoleOverridesController#manageable_permissions List assignable permissions} endpoint. |

**Returns:** `void`

## GET /v1/courses/{course_id}/bulk_user_progress

**Get bulk user progress**  —  `get_bulk_user_progress`

Returns progress information for all users enrolled in the given course.

You must be a user who has permission to view all grades in the course (such as a teacher or administrator).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{id}/dismiss_migration_limitation_message

**Remove quiz migration alert**  —  `remove_quiz_migration_alert`

Remove alert about the limitations of quiz migrations that is displayed
to a user in a course

you must be logged in to use this endpoint

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/restore/{version_id}

**Restore course version**  —  `restore_course_version`

Restore a course to a prior version.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `version_id` | integer (int64) | path | yes | The version to restore to (use the syllabus_versions include parameter in the course show API to see available versions) |

**Returns:** `Course`

## GET /v1/courses/{course_id}/course_copy/{id}

**Get course copy status**  —  `get_course_copy_status`

DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}

Retrieve the status of a course copy

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/course_copy

**Copy course content**  —  `copy_course_content`

DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}

Copies content from one course into another. The default is to copy all course
content. You can control specific types to copy by using either the 'except' option
or the 'only' option.

The response is the same as the course copy status endpoint

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `source_course` | string | form |  | ID or SIS-ID of the course to copy the content from |
| `except` | array[string] | form |  | A list of the course content types to exclude, all areas not listed will be copied. Allowed: `course_settings`, `assignments`, `external_tools`, `files`, `topics`, `calendar_events`, `quizzes`, `wiki_pages`, `modules`, `outcomes` |
| `only` | array[string] | form |  | A list of the course content types to copy, all areas not listed will not be copied. Allowed: `course_settings`, `assignments`, `external_tools`, `files`, `topics`, `calendar_events`, `quizzes`, `wiki_pages`, `modules`, `outcomes` |

**Returns:** `void`


---

# Models


## Term

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | e.g. `1` |
| `name` | string |  | e.g. `Default Term` |
| `start_at` | datetime |  | e.g. `2012-06-01T00:00:00-06:00` |
| `end_at` | datetime |  |  |


## CourseProgress

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `requirement_count` | integer |  | total number of requirements from all modules e.g. `10` |
| `requirement_completed_count` | integer |  | total number of requirements the user has completed from all modules e.g. `1` |
| `next_requirement_url` | string |  | url to next module item that has an unmet requirement. null if the user has completed the course or the current module does not require sequential progress e.g. `http://localhost/courses/1/modules/items/2` |
| `completed_at` | datetime |  | date the course was completed. null if the course has not been completed by this user e.g. `2013-06-01T00:00:00-06:00` |


## Course

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the unique identifier for the course e.g. `370663` |
| `sis_course_id` | string |  | the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information. |
| `uuid` | string |  | the UUID of the course e.g. `WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5` |
| `integration_id` | string |  | the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information. |
| `sis_import_id` | integer |  | the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. e.g. `34` |
| `name` | string |  | the full name of the course. If the requesting user has set a nickname for the course, the nickname will be shown here. e.g. `InstructureCon 2012` |
| `course_code` | string |  | the course code e.g. `INSTCON12` |
| `original_name` | string |  | the actual course name. This field is returned only if the requesting user has set a nickname for the course. e.g. `InstructureCon-2012-01` |
| `workflow_state` | string |  | the current state of the course, also known as ‘status’.  The value will be one of the following values: 'unpublished', 'available', 'completed', or 'deleted'.  NOTE: When fetching a singular course that has a 'deleted' workflow state value, an error will be returned with a message of 'The specified resource does not exist.' e.g. `available` |
| `account_id` | integer |  | the account associated with the course e.g. `81259` |
| `root_account_id` | integer |  | the root account associated with the course e.g. `81259` |
| `enrollment_term_id` | integer |  | the enrollment term associated with the course e.g. `34` |
| `grading_periods` | array[GradingPeriod] |  | A list of grading periods associated with the course |
| `grading_standard_id` | integer |  | the grading standard associated with the course e.g. `25` |
| `grade_passback_setting` | string |  | the grade_passback_setting set on the course e.g. `nightly_sync` |
| `created_at` | datetime |  | the date the course was created. e.g. `2012-05-01T00:00:00-06:00` |
| `start_at` | datetime |  | the start date for the course, if applicable e.g. `2012-06-01T00:00:00-06:00` |
| `end_at` | datetime |  | the end date for the course, if applicable e.g. `2012-09-01T00:00:00-06:00` |
| `locale` | string |  | the course-set locale, if applicable e.g. `en` |
| `enrollments` | array[Enrollment] |  | A list of enrollments linking the current user to the course. for student enrollments, grading information may be included if include[]=total_scores |
| `total_students` | integer |  | optional: the total number of active and invited students in the course e.g. `32` |
| `calendar` | CalendarLink |  | course calendar |
| `default_view` | string |  | the type of page that users will see when they first visit the course - 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules': Course Modules/Sections Page - 'assignments': Course Assignments List - 'syllabus': Course Syllabus Page other types may be added in the future e.g. `feed` |
| `syllabus_body` | string |  | optional: user-generated HTML for the course syllabus e.g. `<p>syllabus html goes here</p>` |
| `needs_grading_count` | integer |  | optional: the number of submissions needing grading returned only if the current user has grading rights and include[]=needs_grading_count e.g. `17` |
| `term` | Term |  | optional: the enrollment term object for the course returned only if include[]=term |
| `course_progress` | CourseProgress |  | optional: information on progress through the course returned only if include[]=course_progress |
| `apply_assignment_group_weights` | boolean |  | weight final grade based on assignment group percentages e.g. `True` |
| `permissions` | object |  | optional: the permissions the user has for the course. returned only for a single course and include[]=permissions e.g. `{'create_discussion_topic': True, 'create_announcement': True}` |
| `is_public` | boolean |  | e.g. `True` |
| `is_public_to_auth_users` | boolean |  | e.g. `True` |
| `public_syllabus` | boolean |  | e.g. `True` |
| `public_syllabus_to_auth` | boolean |  | e.g. `True` |
| `public_description` | string |  | optional: the public description of the course e.g. `Come one, come all to InstructureCon 2012!` |
| `storage_quota_mb` | integer |  | e.g. `5` |
| `storage_quota_used_mb` | number |  | e.g. `5` |
| `hide_final_grades` | boolean |  | e.g. `False` |
| `license` | string |  | e.g. `Creative Commons` |
| `allow_student_assignment_edits` | boolean |  | e.g. `False` |
| `allow_wiki_comments` | boolean |  | e.g. `False` |
| `allow_student_forum_attachments` | boolean |  | e.g. `False` |
| `open_enrollment` | boolean |  | e.g. `True` |
| `self_enrollment` | boolean |  | e.g. `False` |
| `restrict_enrollments_to_course_dates` | boolean |  | e.g. `False` |
| `course_format` | string |  | e.g. `online` |
| `access_restricted_by_date` | boolean |  | optional: this will be true if this user is currently prevented from viewing the course because of date restriction settings e.g. `False` |
| `time_zone` | string |  | The course's IANA time zone name. e.g. `America/Denver` |
| `blueprint` | boolean |  | optional: whether the course is set as a Blueprint Course (blueprint fields require the Blueprint Courses feature) e.g. `True` |
| `blueprint_restrictions` | object |  | optional: Set of restrictions applied to all locked course objects e.g. `{'content': True, 'points': True, 'due_dates': False, 'availability_dates': False}` |
| `blueprint_restrictions_by_object_type` | object |  | optional: Sets of restrictions differentiated by object type applied to locked course objects e.g. `{'assignment': {'content': True, 'points': True}, 'wiki_page': {'content': True}}` |
| `template` | boolean |  | optional: whether the course is set as a template (requires the Course Templates feature) e.g. `True` |


## CalendarLink

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `ics` | string |  | The URL of the calendar in ICS format e.g. `https://canvas.instructure.com/feeds/calendars/course_abcdef.ics` |
