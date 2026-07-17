# Assignments

> Canvas LMS REST API — `/assignments` resource. Base path `/api`.

## DELETE /v1/courses/{course_id}/assignments/{id}

**Delete an assignment**  —  `delete_assignment`

Delete the given assignment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Assignment`

## GET /v1/courses/{course_id}/assignments

**List assignments**  —  `list_assignments_assignments`

Returns the paginated list of assignments for the current course or assignment group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Optional information to include with each assignment: submission:: The current user's current +Submission+ assignment_visibility:: An array of ids of students who can see the assignment all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an "Everyone" / "Everyone Else" date overrides:: An array of +AssignmentOverride+ structures observed_users:: An array of submissions for observed users can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment. score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if 'submission' is also included. ab_guid:: An array of guid strings for academic benchmarks Allowed: `submission`, `assignment_visibility`, `all_dates`, `overrides`, `observed_users`, `can_edit`, `score_statistics`, `ab_guid` |
| `search_term` | string | query |  | The partial title of the assignments to match and return. |
| `override_assignment_dates` | boolean | query |  | Apply assignment overrides for each assignment, defaults to true. |
| `needs_grading_count_by_section` | boolean | query |  | Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false |
| `bucket` | string | query |  | If included, only return certain assignments depending on due date and submission status. Allowed: `past`, `overdue`, `undated`, `ungraded`, `unsubmitted`, `upcoming`, `future` |
| `assignment_ids` | array[string] | query |  | if set, return only assignments specified |
| `order_by` | string | query |  | Determines the order of the assignments. Defaults to "position". Allowed: `position`, `name`, `due_at` |
| `post_to_sis` | boolean | query |  | Return only assignments that have post_to_sis set or not set. |
| `new_quizzes` | boolean | query |  | Return only New Quizzes assignments |

**Returns:** `array[Assignment]`

## GET /v1/courses/{course_id}/assignment_groups/{assignment_group_id}/assignments

**List assignments**  —  `list_assignments_assignment_groups`

Returns the paginated list of assignments for the current course or assignment group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_group_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Optional information to include with each assignment: submission:: The current user's current +Submission+ assignment_visibility:: An array of ids of students who can see the assignment all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an "Everyone" / "Everyone Else" date overrides:: An array of +AssignmentOverride+ structures observed_users:: An array of submissions for observed users can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment. score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if 'submission' is also included. ab_guid:: An array of guid strings for academic benchmarks Allowed: `submission`, `assignment_visibility`, `all_dates`, `overrides`, `observed_users`, `can_edit`, `score_statistics`, `ab_guid` |
| `search_term` | string | query |  | The partial title of the assignments to match and return. |
| `override_assignment_dates` | boolean | query |  | Apply assignment overrides for each assignment, defaults to true. |
| `needs_grading_count_by_section` | boolean | query |  | Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false |
| `bucket` | string | query |  | If included, only return certain assignments depending on due date and submission status. Allowed: `past`, `overdue`, `undated`, `ungraded`, `unsubmitted`, `upcoming`, `future` |
| `assignment_ids` | array[string] | query |  | if set, return only assignments specified |
| `order_by` | string | query |  | Determines the order of the assignments. Defaults to "position". Allowed: `position`, `name`, `due_at` |
| `post_to_sis` | boolean | query |  | Return only assignments that have post_to_sis set or not set. |
| `new_quizzes` | boolean | query |  | Return only New Quizzes assignments |

**Returns:** `array[Assignment]`

## GET /v1/users/{user_id}/courses/{course_id}/assignments

**List assignments for user**  —  `list_assignments_for_user`

Returns the paginated list of assignments for the specified user if the current user has rights to view.
See {api:AssignmentsApiController#index List assignments} for valid arguments.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/duplicate

**Duplicate assignment**  —  `duplicate_assignment`

Duplicate an assignment and return a json based on result_type argument.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `result_type` | string | form |  | Optional information: When the root account has the feature `newquizzes_on_quiz_page` enabled and this argument is set to "Quiz" the response will be serialized into a {file:quizzes.html#Quiz quiz format}; When this argument isn't specified the response will be serialized into an assignment format; Allowed: `Quiz` |

**Returns:** `Assignment`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/users/{user_id}/group_members

**List group members for a student on an assignment**  —  `list_group_members_for_student_on_assignment`

Returns student ids and names for the group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `array[BasicUser]`

## GET /v1/courses/{course_id}/assignments/{id}

**Get a single assignment**  —  `get_single_assignment`

Returns the assignment with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the assignment. The "assignment_visibility" option requires that the Differentiated Assignments course feature be turned on. If "observed_users" is passed, submissions for observed users will also be included. For "score_statistics" to be included, the "submission" option must also be set. The "peer_review" option returns peer review sub assignment data if it exists, regardless of the Peer Review Allocation and Grading feature state. If no peer review sub assignment exists, the feature must be enabled to receive a null value; otherwise the key is omitted. Allowed: `submission`, `assignment_visibility`, `overrides`, `observed_users`, `can_edit`, `score_statistics`, `ab_guid`, `peer_review` |
| `override_assignment_dates` | boolean | query |  | Apply assignment overrides to the assignment, defaults to true. |
| `needs_grading_count_by_section` | boolean | query |  | Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false |
| `all_dates` | boolean | query |  | All dates associated with the assignment, if applicable |

**Returns:** `Assignment`

## POST /v1/courses/{course_id}/assignments

**Create an assignment**  —  `create_assignment`

Create a new assignment for this course. The assignment is created in the
active state.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment[name]` | string | form | yes | The assignment name. |
| `assignment[position]` | integer (int64) | form |  | The position of this assignment in the group when displaying assignment lists. |
| `assignment[submission_types]` | array[string] | form |  | List of supported submission types for the assignment. Unless the assignment is allowing online submissions, the array should only have one element.  If not allowing online submissions, your options are:   "online_quiz"   "none"   "on_paper"   "discussion_topic"   "external_tool"  If you are allowing online submissions, you can have one or many allowed submission types:    "online_upload"   "online_text_entry"   "online_url"   "media_recording" (Only valid when the Kaltura plugin is enabled)   "student_annotation" Allowed: `online_quiz`, `none`, `on_paper`, `discussion_topic`, `external_tool`, `online_upload`, `online_text_entry`, `online_url`, `media_recording`, `student_annotation` |
| `assignment[allowed_extensions]` | array[string] | form |  | Allowed extensions if submission_types includes "online_upload"  Example:   allowed_extensions: ["docx","ppt"] |
| `assignment[turnitin_enabled]` | boolean | form |  | Only applies when the Turnitin plugin is enabled for a course and the submission_types array includes "online_upload". Toggles Turnitin submissions for the assignment. Will be ignored if Turnitin is not available for the course. |
| `assignment[vericite_enabled]` | boolean | form |  | Only applies when the VeriCite plugin is enabled for a course and the submission_types array includes "online_upload". Toggles VeriCite submissions for the assignment. Will be ignored if VeriCite is not available for the course. |
| `assignment[turnitin_settings]` | string | form |  | Settings to send along to turnitin. See Assignment object definition for format. |
| `assignment[integration_data]` | string | form |  | Data used for SIS integrations. Requires admin-level token with the "Manage SIS" permission. JSON string required. |
| `assignment[integration_id]` | string | form |  | Unique ID from third party integrations |
| `assignment[peer_reviews]` | boolean | form |  | If submission_types does not include external_tool,discussion_topic, online_quiz, or on_paper, determines whether or not peer reviews will be turned on for the assignment. |
| `assignment[automatic_peer_reviews]` | boolean | form |  | Whether peer reviews will be assigned automatically by Canvas or if teachers must manually assign peer reviews. Does not apply if peer reviews are not enabled. |
| `assignment[notify_of_update]` | boolean | form |  | If true, Canvas will send a notification to students in the class notifying them that the content has changed. |
| `assignment[group_category_id]` | integer (int64) | form |  | If present, the assignment will become a group assignment assigned to the group. |
| `assignment[grade_group_students_individually]` | integer (int64) | form |  | If this is a group assignment, teachers have the options to grade students individually. If false, Canvas will apply the assignment's score to each member of the group. If true, the teacher can manually assign scores to each member of the group. |
| `assignment[external_tool_tag_attributes]` | string | form |  | Hash of external tool parameters if submission_types is ["external_tool"]. See Assignment object definition for format. |
| `assignment[points_possible]` | number (float) | form |  | The maximum points possible on the assignment. |
| `assignment[grading_type]` | string | form |  | The strategy used for grading the assignment. The assignment defaults to "points" if this field is omitted. Allowed: `pass_fail`, `percent`, `letter_grade`, `gpa_scale`, `points`, `not_graded` |
| `assignment[due_at]` | DateTime | form |  | The day/time the assignment is due. Must be between the lock dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. |
| `assignment[lock_at]` | DateTime | form |  | The day/time the assignment is locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. |
| `assignment[unlock_at]` | DateTime | form |  | The day/time the assignment is unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. |
| `assignment[description]` | string | form |  | The assignment's description, supports HTML. |
| `assignment[assignment_group_id]` | integer (int64) | form |  | The assignment group id to put the assignment in. Defaults to the top assignment group in the course. |
| `assignment[assignment_overrides]` | array[AssignmentOverride] | form |  | List of overrides for the assignment. |
| `assignment[only_visible_to_overrides]` | boolean | form |  | Whether this assignment is only visible to overrides (Only useful if 'differentiated assignments' account setting is on) |
| `assignment[published]` | boolean | form |  | Whether this assignment is published. (Only useful if 'draft state' account setting is on) Unpublished assignments are not visible to students. |
| `assignment[grading_standard_id]` | integer (int64) | form |  | The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course. This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'. |
| `assignment[omit_from_final_grade]` | boolean | form |  | Whether this assignment is counted towards a student's final grade. |
| `assignment[hide_in_gradebook]` | boolean | form |  | Whether this assignment is shown in the gradebook. |
| `assignment[quiz_lti]` | boolean | form |  | Whether this assignment should use the Quizzes 2 LTI tool. Sets the submission type to 'external_tool' and configures the external tool attributes to use the Quizzes 2 LTI tool configured for this course. Has no effect if no Quizzes 2 LTI tool is configured. |
| `assignment[moderated_grading]` | boolean | form |  | Whether this assignment is moderated. |
| `assignment[grader_count]` | integer (int64) | form |  | The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors. |
| `assignment[final_grader_id]` | integer (int64) | form |  | The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments. |
| `assignment[grader_comments_visible_to_graders]` | boolean | form |  | Boolean indicating if provisional graders' comments are visible to other provisional graders. Only relevant for moderated assignments. |
| `assignment[graders_anonymous_to_graders]` | boolean | form |  | Boolean indicating if provisional graders' identities are hidden from other provisional graders. Only relevant for moderated assignments. |
| `assignment[graders_names_visible_to_final_grader]` | boolean | form |  | Boolean indicating if provisional grader identities are visible to the the final grader. Only relevant for moderated assignments. |
| `assignment[anonymous_grading]` | boolean | form |  | Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities. |
| `assignment[allowed_attempts]` | integer (int64) | form |  | The number of submission attempts allowed for this assignment. Set to -1 for unlimited attempts. |
| `assignment[annotatable_attachment_id]` | integer (int64) | form |  | The Attachment ID of the document being annotated.  Only applies when submission_types includes "student_annotation". |
| `assignment[asset_processors]` | array[Array] | form |  | Document processors for this assignment. New document processors can only be added via the interactive LTI Deep Linking flow (in a browser), not via API token or JWT authentication. Deletion of document processors (passing an empty array) is allowed via API. |
| `assignment[peer_review][points_possible]` | number (float) | form |  | The maximum points possible for peer reviews. |
| `assignment[peer_review][grading_type]` | string | form |  | The strategy used for grading peer reviews. Defaults to "points" if this field is omitted. Allowed: `pass_fail`, `percent`, `letter_grade`, `gpa_scale`, `points` |
| `assignment[peer_review][due_at]` | DateTime | form |  | The day/time the peer reviews are due. Must be between the lock dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2025-08-20T12:10:00Z. |
| `assignment[peer_review][lock_at]` | DateTime | form |  | The day/time the peer reviews are locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-25T12:10:00Z. |
| `assignment[peer_review][unlock_at]` | DateTime | form |  | The day/time the peer reviews are unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-15T12:10:00Z. |
| `assignment[peer_review][peer_review_overrides]` | array[AssignmentOverride] | form |  | List of overrides for the peer reviews. |

**Returns:** `Assignment`

## PUT /v1/courses/{course_id}/assignments/{id}

**Edit an assignment**  —  `edit_assignment`

Modify an existing assignment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `assignment[name]` | string | form |  | The assignment name. |
| `assignment[position]` | integer (int64) | form |  | The position of this assignment in the group when displaying assignment lists. |
| `assignment[submission_types]` | array[string] | form |  | Only applies if the assignment doesn't have student submissions.  List of supported submission types for the assignment. Unless the assignment is allowing online submissions, the array should only have one element.  If not allowing online submissions, your options are:   "online_quiz"   "none"   "on_paper"   "discussion_topic"   "external_tool"  If you are allowing online submissions, you can have one or many allowed submission types:    "online_upload"   "online_text_entry"   "online_url"   "media_recording" (Only valid when the Kaltura plugin is enabled)   "student_annotation" Allowed: `online_quiz`, `none`, `on_paper`, `discussion_topic`, `external_tool`, `online_upload`, `online_text_entry`, `online_url`, `media_recording`, `student_annotation` |
| `assignment[allowed_extensions]` | array[string] | form |  | Allowed extensions if submission_types includes "online_upload"  Example:   allowed_extensions: ["docx","ppt"] |
| `assignment[turnitin_enabled]` | boolean | form |  | Only applies when the Turnitin plugin is enabled for a course and the submission_types array includes "online_upload". Toggles Turnitin submissions for the assignment. Will be ignored if Turnitin is not available for the course. |
| `assignment[vericite_enabled]` | boolean | form |  | Only applies when the VeriCite plugin is enabled for a course and the submission_types array includes "online_upload". Toggles VeriCite submissions for the assignment. Will be ignored if VeriCite is not available for the course. |
| `assignment[turnitin_settings]` | string | form |  | Settings to send along to turnitin. See Assignment object definition for format. |
| `assignment[sis_assignment_id]` | string | form |  | The sis id of the Assignment |
| `assignment[integration_data]` | string | form |  | Data used for SIS integrations. Requires admin-level token with the "Manage SIS" permission. JSON string required. |
| `assignment[integration_id]` | string | form |  | Unique ID from third party integrations |
| `assignment[peer_reviews]` | boolean | form |  | If submission_types does not include external_tool,discussion_topic, online_quiz, or on_paper, determines whether or not peer reviews will be turned on for the assignment. |
| `assignment[automatic_peer_reviews]` | boolean | form |  | Whether peer reviews will be assigned automatically by Canvas or if teachers must manually assign peer reviews. Does not apply if peer reviews are not enabled. |
| `assignment[notify_of_update]` | boolean | form |  | If true, Canvas will send a notification to students in the class notifying them that the content has changed. |
| `assignment[group_category_id]` | integer (int64) | form |  | If present, the assignment will become a group assignment assigned to the group. |
| `assignment[grade_group_students_individually]` | integer (int64) | form |  | If this is a group assignment, teachers have the options to grade students individually. If false, Canvas will apply the assignment's score to each member of the group. If true, the teacher can manually assign scores to each member of the group. |
| `assignment[external_tool_tag_attributes]` | string | form |  | Hash of external tool parameters if submission_types is ["external_tool"]. See Assignment object definition for format. |
| `assignment[points_possible]` | number (float) | form |  | The maximum points possible on the assignment. |
| `assignment[grading_type]` | string | form |  | The strategy used for grading the assignment. The assignment defaults to "points" if this field is omitted. Allowed: `pass_fail`, `percent`, `letter_grade`, `gpa_scale`, `points`, `not_graded` |
| `assignment[due_at]` | DateTime | form |  | The day/time the assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. |
| `assignment[lock_at]` | DateTime | form |  | The day/time the assignment is locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. |
| `assignment[unlock_at]` | DateTime | form |  | The day/time the assignment is unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. |
| `assignment[description]` | string | form |  | The assignment's description, supports HTML. |
| `assignment[assignment_group_id]` | integer (int64) | form |  | The assignment group id to put the assignment in. Defaults to the top assignment group in the course. |
| `assignment[assignment_overrides]` | array[AssignmentOverride] | form |  | List of overrides for the assignment. If the +assignment[assignment_overrides]+ key is absent, any existing overrides are kept as is. If the +assignment[assignment_overrides]+ key is present, existing overrides are updated or deleted (and new ones created, as necessary) to match the provided list. |
| `assignment[only_visible_to_overrides]` | boolean | form |  | Whether this assignment is only visible to overrides (Only useful if 'differentiated assignments' account setting is on) |
| `assignment[published]` | boolean | form |  | Whether this assignment is published. (Only useful if 'draft state' account setting is on) Unpublished assignments are not visible to students. |
| `assignment[grading_standard_id]` | integer (int64) | form |  | The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course. This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'. |
| `assignment[omit_from_final_grade]` | boolean | form |  | Whether this assignment is counted towards a student's final grade. |
| `assignment[hide_in_gradebook]` | boolean | form |  | Whether this assignment is shown in the gradebook. |
| `assignment[moderated_grading]` | boolean | form |  | Whether this assignment is moderated. |
| `assignment[grader_count]` | integer (int64) | form |  | The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors. |
| `assignment[final_grader_id]` | integer (int64) | form |  | The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments. |
| `assignment[grader_comments_visible_to_graders]` | boolean | form |  | Boolean indicating if provisional graders' comments are visible to other provisional graders. Only relevant for moderated assignments. |
| `assignment[graders_anonymous_to_graders]` | boolean | form |  | Boolean indicating if provisional graders' identities are hidden from other provisional graders. Only relevant for moderated assignments. |
| `assignment[graders_names_visible_to_final_grader]` | boolean | form |  | Boolean indicating if provisional grader identities are visible to the the final grader. Only relevant for moderated assignments. |
| `assignment[anonymous_grading]` | boolean | form |  | Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities. |
| `assignment[allowed_attempts]` | integer (int64) | form |  | The number of submission attempts allowed for this assignment. Set to -1 or null for unlimited attempts. |
| `assignment[annotatable_attachment_id]` | integer (int64) | form |  | The Attachment ID of the document being annotated.  Only applies when submission_types includes "student_annotation". |
| `assignment[asset_processors]` | array[Array] | form |  | Document processors for this assignment. New document processors can only be added via the interactive LTI Deep Linking flow (in a browser), not via API token or JWT authentication. Deletion of document processors (passing an empty array) is allowed via API. |
| `assignment[force_updated_at]` | boolean | form |  | If true, updated_at will be set even if no changes were made. |
| `assignment[peer_review][points_possible]` | number (float) | form |  | The maximum points possible for peer reviews. |
| `assignment[peer_review][grading_type]` | string | form |  | The strategy used for grading peer reviews. Defaults to "points" if this field is omitted. Allowed: `pass_fail`, `percent`, `letter_grade`, `gpa_scale`, `points` |
| `assignment[peer_review][due_at]` | DateTime | form |  | The day/time the peer reviews are due. Must be between the lock dates if there are lock dates. Accepts times in ISO 8601 format, e.g. 2025-08-20T12:10:00Z. |
| `assignment[peer_review][lock_at]` | DateTime | form |  | The day/time the peer reviews are locked after. Must be after the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-25T12:10:00Z. |
| `assignment[peer_review][unlock_at]` | DateTime | form |  | The day/time the peer reviews are unlocked. Must be before the due date if there is a due date. Accepts times in ISO 8601 format, e.g. 2025-08-15T12:10:00Z. |
| `assignment[peer_review][peer_review_overrides]` | array[AssignmentOverride] | form |  | List of overrides for the peer reviews. When updating overrides: - Include "id" to update an existing override - Omit "id" to create a new override - Omit an override from the list to delete it |
| `assignment[submission_types] *(dep)*` | array[string] | form |  | Only applies if the assignment doesn't have student submissions. |

**Returns:** `Assignment`

## PUT /v1/courses/{course_id}/assignments/bulk_update

**Bulk update assignment dates**  —  `bulk_update_assignment_dates`

Update due dates and availability dates for multiple assignments in a course.

Accepts a JSON array of objects containing two keys each: +id+, the assignment id,
and +all_dates+, an array of +AssignmentDate+ structures containing the base and/or override
dates for the assignment, as returned from the {api:AssignmentsApiController#index List assignments}
endpoint with +include[]=all_dates+.

This endpoint cannot create or destroy assignment overrides; any existing assignment overrides
that are not referenced in the arguments will be left alone. If an override is given, any dates
that are not supplied with it will be defaulted. To clear a date, specify null explicitly.

All referenced assignments will be validated before any are saved. A list of errors will
be returned if any provided dates are invalid, and no changes will be saved.

The bulk update is performed in a background job, use the {api:ProgressController#show Progress API}
to check its status.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `Progress`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/overrides

**List assignment overrides**  —  `list_assignment_overrides`

Returns the paginated list of overrides for this assignment that target
sections/groups/students visible to the current user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |

**Returns:** `array[AssignmentOverride]`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}

**Get a single assignment override**  —  `get_single_assignment_override`

Returns details of the the override with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AssignmentOverride`

## GET /v1/groups/{group_id}/assignments/{assignment_id}/override

**Redirect to the assignment override for a group**  —  `redirect_to_assignment_override_for_group`

Responds with a redirect to the override for the given group, if any
(404 otherwise).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/sections/{course_section_id}/assignments/{assignment_id}/override

**Redirect to the assignment override for a section**  —  `redirect_to_assignment_override_for_section`

Responds with a redirect to the override for the given section, if any
(404 otherwise).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/overrides

**Create an assignment override**  —  `create_assignment_override`

One of student_ids, group_id, or course_section_id must be present. At most
one should be present; if multiple are present only the most specific
(student_ids first, then group_id, then course_section_id) is used and any
others are ignored.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `assignment_override[student_ids]` | array[integer] | form |  | The IDs of the override's target students. If present, the IDs must each identify a user with an active student enrollment in the course that is not already targetted by a different adhoc override. |
| `assignment_override[title]` | string | form |  | The title of the adhoc assignment override. Required if student_ids is present, ignored otherwise (the title is set to the name of the targetted group or section instead). |
| `assignment_override[group_id]` | integer (int64) | form |  | The ID of the override's target group. If present, the following conditions must be met for the override to be successful:  1. the assignment MUST be a group assignment (a group_category_id is assigned to it) 2. the ID must identify an active group in the group set the assignment is in 3. the ID must not be targetted by a different override  See {Appendix: Group assignments} for more info. |
| `assignment_override[course_section_id]` | integer (int64) | form |  | The ID of the override's target section. If present, must identify an active section of the assignment's course not already targetted by a different override. |
| `assignment_override[due_at]` | DateTime | form |  | The day/time the overridden assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect due date. May be present but null to indicate the override removes any previous due date. |
| `assignment_override[unlock_at]` | DateTime | form |  | The day/time the overridden assignment becomes unlocked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the unlock date. May be present but null to indicate the override removes any previous unlock date. |
| `assignment_override[lock_at]` | DateTime | form |  | The day/time the overridden assignment becomes locked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the lock date. May be present but null to indicate the override removes any previous lock date. |

**Returns:** `AssignmentOverride`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}

**Update an assignment override**  —  `update_assignment_override`

All current overridden values must be supplied if they are to be retained;
e.g. if due_at was overridden, but this PUT omits a value for due_at,
due_at will no longer be overridden. If the override is adhoc and
student_ids is not supplied, the target override set is unchanged. Target
override sets cannot be changed for group or section overrides.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `assignment_override[student_ids]` | array[integer] | form |  | The IDs of the override's target students. If present, the IDs must each identify a user with an active student enrollment in the course that is not already targetted by a different adhoc override. Ignored unless the override being updated is adhoc. |
| `assignment_override[title]` | string | form |  | The title of an adhoc assignment override. Ignored unless the override being updated is adhoc. |
| `assignment_override[due_at]` | DateTime | form |  | The day/time the overridden assignment is due. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect due date. May be present but null to indicate the override removes any previous due date. |
| `assignment_override[unlock_at]` | DateTime | form |  | The day/time the overridden assignment becomes unlocked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the unlock date. May be present but null to indicate the override removes any previous unlock date. |
| `assignment_override[lock_at]` | DateTime | form |  | The day/time the overridden assignment becomes locked. Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not affect the lock date. May be present but null to indicate the override removes any previous lock date. |

**Returns:** `AssignmentOverride`

## DELETE /v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}

**Delete an assignment override**  —  `delete_assignment_override`

Deletes an override and returns its former details.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AssignmentOverride`

## GET /v1/courses/{course_id}/assignments/overrides

**Batch retrieve overrides in a course**  —  `batch_retrieve_overrides_in_course`

Returns a list of specified overrides in this course, providing
they target sections/groups/students visible to the current user.
Returns null elements in the list for requests that were not found.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_overrides[id]` | array[string] | query | yes | Ids of overrides to retrieve |
| `assignment_overrides[assignment_id]` | array[string] | query | yes | Ids of assignments for each override |

**Returns:** `array[AssignmentOverride]`

## POST /v1/courses/{course_id}/assignments/overrides

**Batch create overrides in a course**  —  `batch_create_overrides_in_course`

Creates the specified overrides for each assignment.  Handles creation in a
transaction, so all records are created or none are.

One of student_ids, group_id, or course_section_id must be present. At most
one should be present; if multiple are present only the most specific
(student_ids first, then group_id, then course_section_id) is used and any
others are ignored.

Errors are reported in an errors attribute, an array of errors corresponding
to inputs.  Global errors will be reported as a single element errors array

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_overrides` | array[AssignmentOverride] | form | yes | Attributes for the new assignment overrides. See {api:AssignmentOverridesController#create Create an assignment override} for available attributes |

**Returns:** `array[AssignmentOverride]`

## PUT /v1/courses/{course_id}/assignments/overrides

**Batch update overrides in a course**  —  `batch_update_overrides_in_course`

Updates a list of specified overrides for each assignment.  Handles overrides
in a transaction, so either all updates are applied or none.
See {api:AssignmentOverridesController#update Update an assignment override} for
available attributes.

All current overridden values must be supplied if they are to be retained;
e.g. if due_at was overridden, but this PUT omits a value for due_at,
due_at will no longer be overridden. If the override is adhoc and
student_ids is not supplied, the target override set is unchanged. Target
override sets cannot be changed for group or section overrides.

Errors are reported in an errors attribute, an array of errors corresponding
to inputs.  Global errors will be reported as a single element errors array

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_overrides` | array[AssignmentOverride] | form | yes | Attributes for the updated overrides. |

**Returns:** `array[AssignmentOverride]`


---

# Models


## ExternalToolTagAttributes

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `url` | string |  | URL to the external tool e.g. `http://instructure.com` |
| `new_tab` | boolean |  | Whether or not there is a new tab for the external tool e.g. `False` |
| `resource_link_id` | string |  | the identifier for this tool_tag e.g. `ab81173af98b8c33e66a` |


## LockInfo

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `asset_string` | string |  | Asset string for the object causing the lock e.g. `assignment_4` |
| `unlock_at` | datetime |  | (Optional) Time at which this was/will be unlocked. Must be before the due date. e.g. `2013-01-01T00:00:00-06:00` |
| `lock_at` | datetime |  | (Optional) Time at which this was/will be locked. Must be after the due date. e.g. `2013-02-01T00:00:00-06:00` |
| `context_module` | string |  | (Optional) Context module causing the lock. e.g. `{}` |
| `manually_locked` | boolean |  | e.g. `True` |


## RubricRating

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `points` | integer |  | e.g. `10` |
| `id` | string |  | e.g. `rat1` |
| `description` | string |  | e.g. `Full marks` |
| `long_description` | string |  | e.g. `Student completed the assignment flawlessly.` |


## RubricCriteria

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `points` | integer |  | e.g. `10` |
| `id` | string |  | The id of rubric criteria. e.g. `crit1` |
| `learning_outcome_id` | string |  | (Optional) The id of the learning outcome this criteria uses, if any. e.g. `1234` |
| `vendor_guid` | string |  | (Optional) The 3rd party vendor's GUID for the outcome this criteria references, if any. e.g. `abdsfjasdfne3jsdfn2` |
| `description` | string |  | e.g. `Criterion 1` |
| `long_description` | string |  | e.g. `Criterion 1 more details` |
| `criterion_use_range` | boolean |  | e.g. `True` |
| `ratings` | array[RubricRating] |  |  |
| `ignore_for_scoring` | boolean |  | e.g. `True` |


## AssignmentDate

Object representing a due date for an assignment or quiz. If the due date came from an assignment override, it will have an 'id' field.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | (Optional, missing if 'base' is present) id of the assignment override this date represents e.g. `1` |
| `base` | boolean |  | (Optional, present if 'id' is missing) whether this date represents the assignment's or quiz's default due date e.g. `True` |
| `title` | string |  | e.g. `Summer Session` |
| `due_at` | datetime |  | The due date for the assignment. Must be between the unlock date and the lock date if there are lock dates e.g. `2013-08-28T23:59:00-06:00` |
| `unlock_at` | datetime |  | The unlock date for the assignment. Must be before the due date if there is a due date. e.g. `2013-08-01T00:00:00-06:00` |
| `lock_at` | datetime |  | The lock date for the assignment. Must be after the due date if there is a due date. e.g. `2013-08-31T23:59:00-06:00` |


## TurnitinSettings

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `originality_report_visibility` | string |  | e.g. `after_grading` |
| `s_paper_check` | boolean |  | e.g. `False` |
| `internet_check` | boolean |  | e.g. `False` |
| `journal_check` | boolean |  | e.g. `False` |
| `exclude_biblio` | boolean |  | e.g. `False` |
| `exclude_quoted` | boolean |  | e.g. `False` |
| `exclude_small_matches_type` | string |  | e.g. `percent` |
| `exclude_small_matches_value` | integer |  | e.g. `50` |


## NeedsGradingCount

Used by Assignment model

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `section_id` | string |  | The section ID e.g. `123456` |
| `needs_grading_count` | integer |  | Number of submissions that need grading e.g. `5` |


## ScoreStatistic

Used by Assignment model

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `min` | integer |  | Min score e.g. `1` |
| `max` | integer |  | Max score e.g. `10` |
| `mean` | integer |  | Mean score e.g. `6` |
| `upper_q` | integer |  | Upper quartile score e.g. `10` |
| `median` | integer |  | Median score e.g. `6` |
| `lower_q` | integer |  | Lower quartile score e.g. `1` |


## Assignment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the assignment e.g. `4` |
| `name` | string |  | the name of the assignment e.g. `some assignment` |
| `description` | string |  | the assignment description, in an HTML fragment e.g. `<p>Do the following:</p>...` |
| `created_at` | datetime |  | The time at which this assignment was originally created e.g. `2012-07-01T23:59:00-06:00` |
| `updated_at` | datetime |  | The time at which this assignment was last modified in any way e.g. `2012-07-01T23:59:00-06:00` |
| `due_at` | datetime |  | the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. e.g. `2012-07-01T23:59:00-06:00` |
| `lock_at` | datetime |  | the lock date (assignment is locked after this date). returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the lock date as it applies to the user requesting information from the API. e.g. `2012-07-01T23:59:00-06:00` |
| `unlock_at` | datetime |  | the unlock date (assignment is unlocked after this date) returns null if not present NOTE: If this assignment has assignment overrides, this field will be the unlock date as it applies to the user requesting information from the API. e.g. `2012-07-01T23:59:00-06:00` |
| `has_overrides` | boolean |  | whether this assignment has overrides e.g. `True` |
| `all_dates` | array[AssignmentDate] |  | (Optional) all dates associated with the assignment, if applicable |
| `course_id` | integer |  | the ID of the course the assignment belongs to e.g. `123` |
| `html_url` | string |  | the URL to the assignment's web page e.g. `https://...` |
| `submissions_download_url` | string |  | the URL to download all submissions as a zip e.g. `https://example.com/courses/:course_id/assignments/:id/submissions?zip=1` |
| `assignment_group_id` | integer |  | the ID of the assignment's group e.g. `2` |
| `due_date_required` | boolean |  | Boolean flag indicating whether the assignment requires a due date based on the account level setting e.g. `True` |
| `allowed_extensions` | array[string] |  | Allowed file extensions, which take effect if submission_types includes 'online_upload'. e.g. `['docx', 'ppt']` |
| `max_name_length` | integer |  | An integer indicating the maximum length an assignment's name may be e.g. `15` |
| `turnitin_enabled` | boolean |  | Boolean flag indicating whether or not Turnitin has been enabled for the assignment. NOTE: This flag will not appear unless your account has the Turnitin plugin available e.g. `True` |
| `vericite_enabled` | boolean |  | Boolean flag indicating whether or not VeriCite has been enabled for the assignment. NOTE: This flag will not appear unless your account has the VeriCite plugin available e.g. `True` |
| `turnitin_settings` | TurnitinSettings |  | Settings to pass along to turnitin to control what kinds of matches should be considered. originality_report_visibility can be 'immediate', 'after_grading', 'after_due_date', or 'never' exclude_small_matches_type can be null, 'percent', 'words' exclude_small_matches_value: - if type is null, this will be null also - if type is 'percent', this will be a number between 0 and 100 representing match size to exclude as a percentage of the document size. - if type is 'words', this will be number > 0 representing how many words a match must contain for it to be considered NOTE: This flag will not appear unless your account has the Turnitin plugin available |
| `grade_group_students_individually` | boolean |  | If this is a group assignment, boolean flag indicating whether or not students will be graded individually. e.g. `False` |
| `external_tool_tag_attributes` | ExternalToolTagAttributes |  | (Optional) assignment's settings for external tools if submission_types include 'external_tool'. Only url and new_tab are included (new_tab defaults to false).  Use the 'External Tools' API if you need more information about an external tool. |
| `peer_reviews` | boolean |  | Boolean indicating if peer reviews are required for this assignment e.g. `False` |
| `automatic_peer_reviews` | boolean |  | Boolean indicating peer reviews are assigned automatically. If false, the teacher is expected to manually assign peer reviews. e.g. `False` |
| `peer_review_count` | integer |  | Integer representing the amount of reviews each user is assigned. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. e.g. `0` |
| `peer_reviews_assign_at` | datetime |  | String representing a date the reviews are due by. Must be a date that occurs after the default due date. If blank, or date is not after the assignment's due date, the assignment's due date will be used. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. e.g. `2012-07-01T23:59:00-06:00` |
| `intra_group_peer_reviews` | boolean |  | Boolean representing whether or not members from within the same group on a group assignment can be assigned to peer review their own group's work e.g. `false` |
| `group_category_id` | integer |  | The ID of the assignment’s group set, if this is a group assignment. For group discussions, set group_category_id on the discussion topic, not the linked assignment. e.g. `1` |
| `needs_grading_count` | integer |  | if the requesting user has grading rights, the number of submissions that need grading. e.g. `17` |
| `needs_grading_count_by_section` | array[NeedsGradingCount] |  | if the requesting user has grading rights and the 'needs_grading_count_by_section' flag is specified, the number of submissions that need grading split out by section. NOTE: This key is NOT present unless you pass the 'needs_grading_count_by_section' argument as true.  ANOTHER NOTE: it's possible to be enrolled in multiple sections, and if a student is setup that way they will show an assignment that needs grading in multiple sections (effectively the count will be duplicated between sections) e.g. `[{'section_id': '123456', 'needs_grading_count': 5}, {'section_id': '654321', 'needs_grading_count': 0}]` |
| `position` | integer |  | the sorting order of the assignment in the group e.g. `1` |
| `post_to_sis` | boolean |  | (optional, present if Sync Grades to SIS feature is enabled) e.g. `True` |
| `integration_id` | string |  | (optional, Third Party unique identifier for Assignment) e.g. `12341234` |
| `integration_data` | object |  | (optional, Third Party integration data for assignment) e.g. `{'5678': '0954'}` |
| `points_possible` | number |  | the maximum points possible for the assignment e.g. `12.0` |
| `submission_types` | array[string] |  | the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation' e.g. `['online_text_entry']` |
| `has_submitted_submissions` | boolean |  | If true, the assignment has been submitted to by at least one student e.g. `True` |
| `grading_type` | string |  | The type of grading the assignment receives; one of 'pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points' e.g. `points` |
| `grading_standard_id` | integer |  | The id of the grading standard being applied to this assignment. Valid if grading_type is 'letter_grade' or 'gpa_scale'. |
| `published` | boolean |  | Whether the assignment is published e.g. `True` |
| `unpublishable` | boolean |  | Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the assignment. e.g. `False` |
| `only_visible_to_overrides` | boolean |  | Whether the assignment is only visible to overrides. e.g. `False` |
| `locked_for_user` | boolean |  | Whether or not this is locked for the user. e.g. `False` |
| `lock_info` | LockInfo |  | (Optional) Information for the user about the lock. Present when locked_for_user is true. |
| `lock_explanation` | string |  | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. e.g. `This assignment is locked until September 1 at 12:00am` |
| `quiz_id` | integer |  | (Optional) id of the associated quiz (applies only when submission_types is ['online_quiz']) e.g. `620` |
| `anonymous_submissions` | boolean |  | (Optional) whether anonymous submissions are accepted (applies only to quiz assignments) e.g. `False` |
| `discussion_topic` | DiscussionTopic |  | (Optional) the DiscussionTopic associated with the assignment, if applicable |
| `freeze_on_copy` | boolean |  | (Optional) Boolean indicating if assignment will be frozen when it is copied. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. e.g. `False` |
| `frozen` | boolean |  | (Optional) Boolean indicating if assignment is frozen for the calling user. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. e.g. `False` |
| `frozen_attributes` | array[string] |  | (Optional) Array of frozen attributes for the assignment. Only account administrators currently have permission to change an attribute in this list. Will be empty if no attributes are frozen for this assignment. Possible frozen attributes are: title, description, lock_at, points_possible, grading_type, submission_types, assignment_group_id, allowed_extensions, group_category_id, notify_of_update, peer_reviews NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. e.g. `['title']` |
| `submission` | Submission |  | (Optional) If 'submission' is included in the 'include' parameter, includes a Submission object that represents the current user's (user who is requesting information from the api) current submission for the assignment. See the Submissions API for an example response. If the user does not have a submission, this key will be absent. |
| `use_rubric_for_grading` | boolean |  | (Optional) If true, the rubric is directly tied to grading the assignment. Otherwise, it is only advisory. Included if there is an associated rubric. e.g. `True` |
| `rubric_settings` | object |  | (Optional) An object describing the basic attributes of the rubric, including the point total. Included if there is an associated rubric. e.g. `{'points_possible': '12'}` |
| `rubric` | array[RubricCriteria] |  | (Optional) A list of scoring criteria and ratings for each rubric criterion. Included if there is an associated rubric. |
| `assignment_visibility` | array[integer] |  | (Optional) If 'assignment_visibility' is included in the 'include' parameter, includes an array of student IDs who can see this assignment. e.g. `[137, 381, 572]` |
| `overrides` | array[AssignmentOverride] |  | (Optional) If 'overrides' is included in the 'include' parameter, includes an array of assignment override objects. |
| `omit_from_final_grade` | boolean |  | (Optional) If true, the assignment will be omitted from the student's final grade e.g. `True` |
| `hide_in_gradebook` | boolean |  | (Optional) If true, the assignment will not be shown in any gradebooks e.g. `True` |
| `moderated_grading` | boolean |  | Boolean indicating if the assignment is moderated. e.g. `True` |
| `grader_count` | integer |  | The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors. e.g. `3` |
| `final_grader_id` | integer |  | The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments. e.g. `3` |
| `grader_comments_visible_to_graders` | boolean |  | Boolean indicating if provisional graders' comments are visible to other provisional graders. Only relevant for moderated assignments. e.g. `True` |
| `graders_anonymous_to_graders` | boolean |  | Boolean indicating if provisional graders' identities are hidden from other provisional graders. Only relevant for moderated assignments with grader_comments_visible_to_graders set to true. e.g. `True` |
| `grader_names_visible_to_final_grader` | boolean |  | Boolean indicating if provisional grader identities are visible to the final grader. Only relevant for moderated assignments. e.g. `True` |
| `anonymous_grading` | boolean |  | Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities. e.g. `True` |
| `allowed_attempts` | integer |  | The number of submission attempts a student can make for this assignment. -1 is considered unlimited. e.g. `2` |
| `post_manually` | boolean |  | Whether the assignment has manual posting enabled. Only relevant for courses using New Gradebook. e.g. `True` |
| `score_statistics` | ScoreStatistic |  | (Optional) If 'score_statistics' and 'submission' are included in the 'include' parameter and statistics are available, includes the min, max, and mode for this assignment |
| `can_submit` | boolean |  | (Optional) If retrieving a single assignment and 'can_submit' is included in the 'include' parameter, flags whether user has the right to submit the assignment (i.e. checks enrollment dates, submission types, locked status, attempts remaining, etc...). Including 'can submit' automatically includes 'submission' in the include parameter. Not available when observed_users are included. e.g. `True` |
| `ab_guid` | array[string] |  | (Optional) The academic benchmark(s) associated with the assignment or the assignment's rubric. Only included if 'ab_guid' is included in the 'include' parameter. e.g. `['ABCD', 'EFGH']` |
| `annotatable_attachment_id` | integer |  | The id of the attachment to be annotated by students. Relevant only if submission_types includes 'student_annotation'. |
| `anonymize_students` | boolean |  | (Optional) Boolean indicating whether student names are anonymized e.g. `False` |
| `require_lockdown_browser` | boolean |  | (Optional) Boolean indicating whether the Respondus LockDown Browser® is required for this assignment. e.g. `False` |
| `important_dates` | boolean |  | (Optional) Boolean indicating whether this assignment has important dates. e.g. `False` |
| `muted` | boolean |  | (Optional, Deprecated) Boolean indicating whether notifications are muted for this assignment. e.g. `False` |
| `anonymous_peer_reviews` | boolean |  | Boolean indicating whether peer reviews are anonymous. e.g. `False` |
| `anonymous_instructor_annotations` | boolean |  | Boolean indicating whether instructor anotations are anonymous. e.g. `False` |
| `graded_submissions_exist` | boolean |  | Boolean indicating whether this assignment has graded submissions. e.g. `False` |
| `is_quiz_assignment` | boolean |  | Boolean indicating whether this is a quiz lti assignment. e.g. `False` |
| `in_closed_grading_period` | boolean |  | Boolean indicating whether this assignment is in a closed grading period. e.g. `False` |
| `can_duplicate` | boolean |  | Boolean indicating whether this assignment can be duplicated. e.g. `False` |
| `original_course_id` | integer |  | If this assignment is a duplicate, it is the original assignment's course_id e.g. `4` |
| `original_assignment_id` | integer |  | If this assignment is a duplicate, it is the original assignment's id e.g. `4` |
| `original_lti_resource_link_id` | integer |  | If this assignment is a duplicate, it is the original assignment's lti_resource_link_id e.g. `4` |
| `original_assignment_name` | string |  | If this assignment is a duplicate, it is the original assignment's name e.g. `some assignment` |
| `original_quiz_id` | integer |  | If this assignment is a duplicate, it is the original assignment's quiz_id e.g. `4` |
| `workflow_state` | string |  | String indicating what state this assignment is in. e.g. `unpublished` |


## BasicUser

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | The user's ID e.g. `123456` |
| `name` | string |  | The user's name e.g. `Dankey Kang` |


## AssignmentOverride

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the assignment override e.g. `4` |
| `assignment_id` | integer |  | the ID of the assignment the override applies to (present if the override applies to an assignment) e.g. `123` |
| `quiz_id` | integer |  | the ID of the quiz the override applies to (present if the override applies to a quiz) e.g. `123` |
| `context_module_id` | integer |  | the ID of the module the override applies to (present if the override applies to a module) e.g. `123` |
| `discussion_topic_id` | integer |  | the ID of the discussion the override applies to (present if the override applies to an ungraded discussion) e.g. `123` |
| `wiki_page_id` | integer |  | the ID of the page the override applies to (present if the override applies to a page) e.g. `123` |
| `attachment_id` | integer |  | the ID of the file the override applies to (present if the override applies to a file) e.g. `123` |
| `student_ids` | array[integer] |  | the IDs of the override's target students (present if the override targets an ad-hoc set of students) e.g. `[1, 2, 3]` |
| `group_id` | integer |  | the ID of the override's target group (present if the override targets a group and the assignment is a group assignment) e.g. `2` |
| `course_section_id` | integer |  | the ID of the overrides's target section (present if the override targets a section) e.g. `1` |
| `title` | string |  | the title of the override e.g. `an assignment override` |
| `due_at` | datetime |  | the overridden due at (present if due_at is overridden) e.g. `2012-07-01T23:59:00-06:00` |
| `all_day` | boolean |  | the overridden all day flag (present if due_at is overridden) e.g. `True` |
| `all_day_date` | datetime |  | the overridden all day date (present if due_at is overridden) e.g. `2012-07-01` |
| `unlock_at` | datetime |  | the overridden unlock at (present if unlock_at is overridden) e.g. `2012-07-01T23:59:00-06:00` |
| `lock_at` | datetime |  | the overridden lock at, if any (present if lock_at is overridden) e.g. `2012-07-01T23:59:00-06:00` |
