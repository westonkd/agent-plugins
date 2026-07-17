# Submissions

> Canvas LMS REST API — `/submissions` resource. Base path `/api`.

## POST /v1/courses/{course_id}/assignments/{assignment_id}/submissions

**Submit an assignment**  —  `submit_assignment_courses`

Make a submission for an assignment. You must be actively enrolled as a student in
the course/section to do this. Concluded and pending enrollments are not permitted.

All online turn-in submission types are supported in this API. However,
there are a few things that are not yet supported:

* Files can be submitted based on a file ID of a user or group file or through the {api:SubmissionsApiController#create_file file upload API}. However, there is no API yet for listing the user and group files.
* Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
* Integration with Google Docs is not yet supported.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `comment[text_comment]` | string | form |  | Include a textual comment with the submission. |
| `submission[group_comment]` | boolean | form |  | Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. |
| `submission[submission_type]` | string | form | yes | The type of submission being made. The assignment submission_types must include this submission type as an allowed option, or the submission will be rejected with a 400 error.  The submission_type given determines which of the following parameters is used. For instance, to submit a URL, +submission[submission_type]+ must be set to "online_url", otherwise the +submission[url]+ parameter will be ignored.  "basic_lti_launch" requires the assignment submission_type "online" or "external_tool" Allowed: `online_text_entry`, `online_url`, `online_upload`, `media_recording`, `basic_lti_launch`, `student_annotation` |
| `submission[body]` | string | form |  | Submit the assignment as an HTML document snippet. Note this HTML snippet will be sanitized using the same ruleset as a submission made from the Canvas web UI. The sanitized HTML will be returned in the response as the submission body. Requires a submission_type of "online_text_entry". |
| `submission[url]` | string | form |  | Submit the assignment as a URL. The URL scheme must be "http" or "https", no "ftp" or other URL schemes are allowed. If no scheme is given (e.g. "www.example.com") then "http" will be assumed. Requires a submission_type of "online_url" or "basic_lti_launch". |
| `submission[file_ids]` | array[integer] | form |  | Submit the assignment as a set of one or more previously uploaded files residing in the submitting user's files section (or the group's files section, for group assignments).  To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.  Requires a submission_type of "online_upload". |
| `submission[media_comment_id]` | string | form |  | The media comment id to submit. Media comment ids can be submitted via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.  Requires a submission_type of "media_recording". |
| `submission[media_comment_type]` | string | form |  | The type of media comment being submitted. Allowed: `audio`, `video` |
| `submission[user_id]` | integer (int64) | form |  | Submit on behalf of the given user. Requires grading permission. |
| `submission[annotatable_attachment_id]` | integer (int64) | form |  | The Attachment ID of the document being annotated. This should match the annotatable_attachment_id on the assignment.  Requires a submission_type of "student_annotation". |
| `submission[submitted_at]` | DateTime | form |  | Choose the time the submission is listed as submitted at.  Requires grading permission. |

**Returns:** `void`

## POST /v1/sections/{section_id}/assignments/{assignment_id}/submissions

**Submit an assignment**  —  `submit_assignment_sections`

Make a submission for an assignment. You must be actively enrolled as a student in
the course/section to do this. Concluded and pending enrollments are not permitted.

All online turn-in submission types are supported in this API. However,
there are a few things that are not yet supported:

* Files can be submitted based on a file ID of a user or group file or through the {api:SubmissionsApiController#create_file file upload API}. However, there is no API yet for listing the user and group files.
* Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
* Integration with Google Docs is not yet supported.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `comment[text_comment]` | string | form |  | Include a textual comment with the submission. |
| `submission[group_comment]` | boolean | form |  | Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. |
| `submission[submission_type]` | string | form | yes | The type of submission being made. The assignment submission_types must include this submission type as an allowed option, or the submission will be rejected with a 400 error.  The submission_type given determines which of the following parameters is used. For instance, to submit a URL, +submission[submission_type]+ must be set to "online_url", otherwise the +submission[url]+ parameter will be ignored.  "basic_lti_launch" requires the assignment submission_type "online" or "external_tool" Allowed: `online_text_entry`, `online_url`, `online_upload`, `media_recording`, `basic_lti_launch`, `student_annotation` |
| `submission[body]` | string | form |  | Submit the assignment as an HTML document snippet. Note this HTML snippet will be sanitized using the same ruleset as a submission made from the Canvas web UI. The sanitized HTML will be returned in the response as the submission body. Requires a submission_type of "online_text_entry". |
| `submission[url]` | string | form |  | Submit the assignment as a URL. The URL scheme must be "http" or "https", no "ftp" or other URL schemes are allowed. If no scheme is given (e.g. "www.example.com") then "http" will be assumed. Requires a submission_type of "online_url" or "basic_lti_launch". |
| `submission[file_ids]` | array[integer] | form |  | Submit the assignment as a set of one or more previously uploaded files residing in the submitting user's files section (or the group's files section, for group assignments).  To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.  Requires a submission_type of "online_upload". |
| `submission[media_comment_id]` | string | form |  | The media comment id to submit. Media comment ids can be submitted via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use.  Requires a submission_type of "media_recording". |
| `submission[media_comment_type]` | string | form |  | The type of media comment being submitted. Allowed: `audio`, `video` |
| `submission[user_id]` | integer (int64) | form |  | Submit on behalf of the given user. Requires grading permission. |
| `submission[annotatable_attachment_id]` | integer (int64) | form |  | The Attachment ID of the document being annotated. This should match the annotatable_attachment_id on the assignment.  Requires a submission_type of "student_annotation". |
| `submission[submitted_at]` | DateTime | form |  | Choose the time the submission is listed as submitted at.  Requires grading permission. |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/submissions

**List assignment submissions**  —  `list_assignment_submissions_courses`

A paginated list of all existing submissions for an assignment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group.  "group" will add group_id and group_name. Allowed: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `assignment`, `visibility`, `course`, `user`, `group`, `read_status`, `student_entered_score` |
| `grouped` | boolean | query |  | If this argument is true, the response will be grouped by student groups. |

**Returns:** `array[Submission]`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/submissions

**List assignment submissions**  —  `list_assignment_submissions_sections`

A paginated list of all existing submissions for an assignment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group.  "group" will add group_id and group_name. Allowed: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `assignment`, `visibility`, `course`, `user`, `group`, `read_status`, `student_entered_score` |
| `grouped` | boolean | query |  | If this argument is true, the response will be grouped by student groups. |

**Returns:** `array[Submission]`

## GET /v1/courses/{course_id}/students/submissions

**List submissions for multiple assignments**  —  `list_submissions_for_multiple_assignments_courses`

A paginated list of all existing submissions for a given set of students and assignments.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `student_ids` | array[string] | query |  | List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id "all" will return submissions for all students in the course/section as appropriate. |
| `assignment_ids` | array[string] | query |  | List of assignments to return submissions for. If none are given, submissions for all assignments are returned. |
| `grouped` | boolean | query |  | If this argument is present, the response will be grouped by student, rather than a flat array of submissions. |
| `post_to_sis` | boolean | query |  | If this argument is set to true, the response will only include submissions for assignments that have the post_to_sis flag set to true and user enrollments that were added through sis. |
| `submitted_since` | DateTime | query |  | If this argument is set, the response will only include submissions that were submitted after the specified date_time. This will exclude submissions that do not have a submitted_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `graded_since` | DateTime | query |  | If this argument is set, the response will only include submissions that were graded after the specified date_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `grading_period_id` | integer (int64) | query |  | The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account) |
| `workflow_state` | string | query |  | The current status of the submission Allowed: `submitted`, `unsubmitted`, `graded`, `pending_review` |
| `enrollment_state` | string | query |  | The current state of the enrollments. If omitted will include all enrollments that are not deleted. Allowed: `active`, `concluded` |
| `state_based_on_date` | boolean | query |  | If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow_state for the enrollments. The argument is ignored unless enrollment_state argument is also passed. |
| `order` | string | query |  | The order submissions will be returned in.  Defaults to "id".  Doesn't affect results for "grouped" mode. Allowed: `id`, `graded_at` |
| `order_direction` | string | query |  | Determines whether ordered results are returned in ascending or descending order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode. Allowed: `ascending`, `descending` |
| `include` | array[string] | query |  | Associations to include with the group. `total_scores` requires the `grouped` argument. Allowed: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `assignment`, `total_scores`, `visibility`, `course`, `user`, `sub_assignment_submissions`, `peer_review_submissions`, `student_entered_score` |

**Returns:** `void`

## GET /v1/sections/{section_id}/students/submissions

**List submissions for multiple assignments**  —  `list_submissions_for_multiple_assignments_sections`

A paginated list of all existing submissions for a given set of students and assignments.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `student_ids` | array[string] | query |  | List of student ids to return submissions for. If this argument is omitted, return submissions for the calling user. Students may only list their own submissions. Observers may only list those of associated students. The special id "all" will return submissions for all students in the course/section as appropriate. |
| `assignment_ids` | array[string] | query |  | List of assignments to return submissions for. If none are given, submissions for all assignments are returned. |
| `grouped` | boolean | query |  | If this argument is present, the response will be grouped by student, rather than a flat array of submissions. |
| `post_to_sis` | boolean | query |  | If this argument is set to true, the response will only include submissions for assignments that have the post_to_sis flag set to true and user enrollments that were added through sis. |
| `submitted_since` | DateTime | query |  | If this argument is set, the response will only include submissions that were submitted after the specified date_time. This will exclude submissions that do not have a submitted_at which will exclude unsubmitted submissions. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `graded_since` | DateTime | query |  | If this argument is set, the response will only include submissions that were graded after the specified date_time. This will exclude submissions that have not been graded. The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ. |
| `grading_period_id` | integer (int64) | query |  | The id of the grading period in which submissions are being requested (Requires grading periods to exist on the account) |
| `workflow_state` | string | query |  | The current status of the submission Allowed: `submitted`, `unsubmitted`, `graded`, `pending_review` |
| `enrollment_state` | string | query |  | The current state of the enrollments. If omitted will include all enrollments that are not deleted. Allowed: `active`, `concluded` |
| `state_based_on_date` | boolean | query |  | If omitted it is set to true. When set to false it will ignore the effective state of the student enrollments and use the workflow_state for the enrollments. The argument is ignored unless enrollment_state argument is also passed. |
| `order` | string | query |  | The order submissions will be returned in.  Defaults to "id".  Doesn't affect results for "grouped" mode. Allowed: `id`, `graded_at` |
| `order_direction` | string | query |  | Determines whether ordered results are returned in ascending or descending order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode. Allowed: `ascending`, `descending` |
| `include` | array[string] | query |  | Associations to include with the group. `total_scores` requires the `grouped` argument. Allowed: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `assignment`, `total_scores`, `visibility`, `course`, `user`, `sub_assignment_submissions`, `peer_review_submissions`, `student_entered_score` |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}

**Get a single submission**  —  `get_single_submission_courses`

Get a single submission, based on user id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group. Allowed: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `full_rubric_assessment`, `visibility`, `course`, `user`, `read_status`, `student_entered_score` |

**Returns:** `void`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}

**Get a single submission**  —  `get_single_submission_sections`

Get a single submission, based on user id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group. Allowed: `submission_history`, `submission_comments`, `submission_html_comments`, `rubric_assessment`, `full_rubric_assessment`, `visibility`, `course`, `user`, `read_status`, `student_entered_score` |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id}

**Get a single submission by anonymous id**  —  `get_single_submission_by_anonymous_id_courses`

Get a single submission, based on the submission's anonymous id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `anonymous_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group. Allowed: `submission_history`, `submission_comments`, `rubric_assessment`, `full_rubric_assessment`, `visibility`, `course`, `user`, `read_status` |

**Returns:** `void`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id}

**Get a single submission by anonymous id**  —  `get_single_submission_by_anonymous_id_sections`

Get a single submission, based on the submission's anonymous id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `anonymous_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the group. Allowed: `submission_history`, `submission_comments`, `rubric_assessment`, `full_rubric_assessment`, `visibility`, `course`, `user`, `read_status` |

**Returns:** `void`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files

**Upload a file**  —  `upload_file_courses`

Upload a file to a submission.

This API endpoint is the first step in uploading a file to a submission as a student.
See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data,
including the new file id. The caller can then POST to submit the
+online_upload+ assignment with these file ids.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files

**Upload a file**  —  `upload_file_sections`

Upload a file to a submission.

This API endpoint is the first step in uploading a file to a submission as a student.
See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data,
including the new file id. The caller can then POST to submit the
+online_upload+ assignment with these file ids.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}

**Grade or comment on a submission**  —  `grade_or_comment_on_submission_courses`

Comment on and/or update the grading for a student's assignment submission.
If any submission or rubric_assessment arguments are provided, the user
must have permission to manage grades in the appropriate context (course or
section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `comment[text_comment]` | string | form |  | Add a textual comment to the submission. |
| `comment[attempt]` | integer (int64) | form |  | The attempt number (starts at 1) to associate the comment with. |
| `comment[group_comment]` | boolean | form |  | Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. |
| `comment[media_comment_id]` | string | form |  | Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use. |
| `comment[media_comment_type]` | string | form |  | The type of media comment being added. Allowed: `audio`, `video` |
| `comment[file_ids]` | array[integer] | form |  | Attach files to this comment that were previously uploaded using the Submission Comment API's files action |
| `include` | array[string] | form |  | Associations to include with the submission. "submission_comments" is always included by default. - "submission_comments": Comments on the submission (always included) - "visibility": Whether the assignment is visible to the owner of the submission - "sub_assignment_submissions": Sub-assignment submissions for discussion checkpoints - "peer_review_submissions": Peer review submission data when peer review allocation and grading is enabled - "provisional_grades": Provisional grades (only available for moderated assignments) - "group": Group information (id and name) for group assignments Allowed: `submission_comments`, `visibility`, `sub_assignment_submissions`, `peer_review_submissions`, `provisional_grades`, `group` |
| `prefer_points_over_scheme` | boolean | form |  | Treat posted_grade as points if the value matches a grading scheme value |
| `submission[posted_grade]` | string | form |  | Assign a score to the submission, updating both the "score" and "grade" fields on the submission record. This parameter can be passed in a few different formats:  points:: A floating point or integral value, such as "13.5". The grade   will be interpreted directly as the score of the assignment.   Values above assignment.points_possible are allowed, for awarding   extra credit. percentage:: A floating point value appended with a percent sign, such as    "40%". The grade will be interpreted as a percentage score on the    assignment, where 100% == assignment.points_possible. Values above 100%    are allowed, for awarding extra credit. letter grade:: A letter grade, following the assignment's defined letter    grading scheme. For example, "A-". The resulting score will be the high    end of the defined range for the letter grade. For instance, if "B" is    defined as 86% to 84%, a letter grade of "B" will be worth 86%. The    letter grade will be rejected if the assignment does not have a defined    letter grading scheme. For more fine-grained control of scores, pass in    points or percentage rather than the letter grade. "pass/complete/fail/incomplete":: A string value of "pass" or "complete"    will give a score of 100%. "fail" or "incomplete" will give a score of    0.  Note that assignments with grading_type of "pass_fail" can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the "points" or "percentage" format is sent, the grade will only be accepted if the grade equals one of those two values. |
| `submission[excuse]` | boolean | form |  | Sets the "excused" status of an assignment. |
| `submission[late_policy_status]` | string | form |  | Sets the late policy status to either "late", "missing", "extended", "none", or null.   NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on |
| `submission[sticker]` | string | form |  | Sets the sticker for the submission. Allowed: `apple`, `basketball`, `bell`, `book`, `bookbag`, `briefcase`, `bus`, `calendar`, `chem`, `design`, `pencil`, `beaker`, `paintbrush`, `computer`, `column`, `pen`, `tablet`, `telescope`, `calculator`, `paperclip`, `composite_notebook`, `scissors`, `ruler`, `clock`, `globe`, `grad`, `gym`, `mail`, `microscope`, `mouse`, `music`, `notebook`, `page`, `panda1`, `panda2`, `panda3`, `panda4`, `panda5`, `panda6`, `panda7`, `panda8`, `panda9`, `presentation`, `science`, `science2`, `star`, `tag`, `tape`, `target`, `trophy` |
| `submission[seconds_late_override]` | integer (int64) | form |  | Sets the seconds late if late policy status is "late" |
| `submission[peer_review]` | boolean | form |  | When true, updates the peer review sub assignment submission instead of the parent assignment submission. The parent assignment must have peer reviews enabled, the peer_review_allocation_and_grading feature flag must be enabled for the course, and the assignment must have an associated peer review sub assignment. If any of these conditions are not met, the API will return a 422 error. |
| `rubric_assessment` | RubricAssessment | form |  | Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:  The points awarded for this row.   rubric_assessment[criterion_id][points]  The rating id for the row.   rubric_assessment[criterion_id][rating_id]  Comments to add for this row.   rubric_assessment[criterion_id][comments]  For example, if the assignment rubric is (in JSON format):   !!!javascript   [     {       'id': 'crit1',       'points': 10,       'description': 'Criterion 1',       'ratings':       [         { 'id': 'rat1', 'description': 'Good', 'points': 10 },         { 'id': 'rat2', 'description': 'Poor', 'points': 3 }       ]     },     {       'id': 'crit2',       'points': 5,       'description': 'Criterion 2',       'ratings':       [         { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },         { 'id': 'rat2', 'description': 'Complete', 'points': 5 },         { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }       ]     }   ]  Then a possible set of values for rubric_assessment would be:     rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done. |

**Returns:** `void`

## PUT /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}

**Grade or comment on a submission**  —  `grade_or_comment_on_submission_sections`

Comment on and/or update the grading for a student's assignment submission.
If any submission or rubric_assessment arguments are provided, the user
must have permission to manage grades in the appropriate context (course or
section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `comment[text_comment]` | string | form |  | Add a textual comment to the submission. |
| `comment[attempt]` | integer (int64) | form |  | The attempt number (starts at 1) to associate the comment with. |
| `comment[group_comment]` | boolean | form |  | Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. |
| `comment[media_comment_id]` | string | form |  | Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use. |
| `comment[media_comment_type]` | string | form |  | The type of media comment being added. Allowed: `audio`, `video` |
| `comment[file_ids]` | array[integer] | form |  | Attach files to this comment that were previously uploaded using the Submission Comment API's files action |
| `include` | array[string] | form |  | Associations to include with the submission. "submission_comments" is always included by default. - "submission_comments": Comments on the submission (always included) - "visibility": Whether the assignment is visible to the owner of the submission - "sub_assignment_submissions": Sub-assignment submissions for discussion checkpoints - "peer_review_submissions": Peer review submission data when peer review allocation and grading is enabled - "provisional_grades": Provisional grades (only available for moderated assignments) - "group": Group information (id and name) for group assignments Allowed: `submission_comments`, `visibility`, `sub_assignment_submissions`, `peer_review_submissions`, `provisional_grades`, `group` |
| `prefer_points_over_scheme` | boolean | form |  | Treat posted_grade as points if the value matches a grading scheme value |
| `submission[posted_grade]` | string | form |  | Assign a score to the submission, updating both the "score" and "grade" fields on the submission record. This parameter can be passed in a few different formats:  points:: A floating point or integral value, such as "13.5". The grade   will be interpreted directly as the score of the assignment.   Values above assignment.points_possible are allowed, for awarding   extra credit. percentage:: A floating point value appended with a percent sign, such as    "40%". The grade will be interpreted as a percentage score on the    assignment, where 100% == assignment.points_possible. Values above 100%    are allowed, for awarding extra credit. letter grade:: A letter grade, following the assignment's defined letter    grading scheme. For example, "A-". The resulting score will be the high    end of the defined range for the letter grade. For instance, if "B" is    defined as 86% to 84%, a letter grade of "B" will be worth 86%. The    letter grade will be rejected if the assignment does not have a defined    letter grading scheme. For more fine-grained control of scores, pass in    points or percentage rather than the letter grade. "pass/complete/fail/incomplete":: A string value of "pass" or "complete"    will give a score of 100%. "fail" or "incomplete" will give a score of    0.  Note that assignments with grading_type of "pass_fail" can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the "points" or "percentage" format is sent, the grade will only be accepted if the grade equals one of those two values. |
| `submission[excuse]` | boolean | form |  | Sets the "excused" status of an assignment. |
| `submission[late_policy_status]` | string | form |  | Sets the late policy status to either "late", "missing", "extended", "none", or null.   NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on |
| `submission[sticker]` | string | form |  | Sets the sticker for the submission. Allowed: `apple`, `basketball`, `bell`, `book`, `bookbag`, `briefcase`, `bus`, `calendar`, `chem`, `design`, `pencil`, `beaker`, `paintbrush`, `computer`, `column`, `pen`, `tablet`, `telescope`, `calculator`, `paperclip`, `composite_notebook`, `scissors`, `ruler`, `clock`, `globe`, `grad`, `gym`, `mail`, `microscope`, `mouse`, `music`, `notebook`, `page`, `panda1`, `panda2`, `panda3`, `panda4`, `panda5`, `panda6`, `panda7`, `panda8`, `panda9`, `presentation`, `science`, `science2`, `star`, `tag`, `tape`, `target`, `trophy` |
| `submission[seconds_late_override]` | integer (int64) | form |  | Sets the seconds late if late policy status is "late" |
| `submission[peer_review]` | boolean | form |  | When true, updates the peer review sub assignment submission instead of the parent assignment submission. The parent assignment must have peer reviews enabled, the peer_review_allocation_and_grading feature flag must be enabled for the course, and the assignment must have an associated peer review sub assignment. If any of these conditions are not met, the API will return a 422 error. |
| `rubric_assessment` | RubricAssessment | form |  | Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:  The points awarded for this row.   rubric_assessment[criterion_id][points]  The rating id for the row.   rubric_assessment[criterion_id][rating_id]  Comments to add for this row.   rubric_assessment[criterion_id][comments]  For example, if the assignment rubric is (in JSON format):   !!!javascript   [     {       'id': 'crit1',       'points': 10,       'description': 'Criterion 1',       'ratings':       [         { 'id': 'rat1', 'description': 'Good', 'points': 10 },         { 'id': 'rat2', 'description': 'Poor', 'points': 3 }       ]     },     {       'id': 'crit2',       'points': 5,       'description': 'Criterion 2',       'ratings':       [         { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },         { 'id': 'rat2', 'description': 'Complete', 'points': 5 },         { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }       ]     }   ]  Then a possible set of values for rubric_assessment would be:     rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id}

**Grade or comment on a submission by anonymous id**  —  `grade_or_comment_on_submission_by_anonymous_id_courses`

Comment on and/or update the grading for a student's assignment submission,
fetching the submission by anonymous id (instead of user id). If any
submission or rubric_assessment arguments are provided, the user must
have permission to manage grades in the appropriate context (course or
section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `anonymous_id` | string | path | yes | ID |
| `comment[text_comment]` | string | form |  | Add a textual comment to the submission. |
| `comment[group_comment]` | boolean | form |  | Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. |
| `comment[media_comment_id]` | string | form |  | Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use. |
| `comment[media_comment_type]` | string | form |  | The type of media comment being added. Allowed: `audio`, `video` |
| `comment[file_ids]` | array[integer] | form |  | Attach files to this comment that were previously uploaded using the Submission Comment API's files action |
| `include` | array[string] | form |  | Associations to include with the submission. "submission_comments" is always included by default. - "submission_comments": Comments on the submission (always included) - "visibility": Whether the assignment is visible to the owner of the submission - "sub_assignment_submissions": Sub-assignment submissions for discussion checkpoints - "peer_review_submissions": Peer review submission data when peer review allocation and grading is enabled - "provisional_grades": Provisional grades (only available for moderated assignments) - "group": Group information (id and name) for group assignments Allowed: `submission_comments`, `visibility`, `sub_assignment_submissions`, `peer_review_submissions`, `provisional_grades`, `group` |
| `submission[posted_grade]` | string | form |  | Assign a score to the submission, updating both the "score" and "grade" fields on the submission record. This parameter can be passed in a few different formats:  points:: A floating point or integral value, such as "13.5". The grade   will be interpreted directly as the score of the assignment.   Values above assignment.points_possible are allowed, for awarding   extra credit. percentage:: A floating point value appended with a percent sign, such as    "40%". The grade will be interpreted as a percentage score on the    assignment, where 100% == assignment.points_possible. Values above 100%    are allowed, for awarding extra credit. letter grade:: A letter grade, following the assignment's defined letter    grading scheme. For example, "A-". The resulting score will be the high    end of the defined range for the letter grade. For instance, if "B" is    defined as 86% to 84%, a letter grade of "B" will be worth 86%. The    letter grade will be rejected if the assignment does not have a defined    letter grading scheme. For more fine-grained control of scores, pass in    points or percentage rather than the letter grade. "pass/complete/fail/incomplete":: A string value of "pass" or "complete"    will give a score of 100%. "fail" or "incomplete" will give a score of    0.  Note that assignments with grading_type of "pass_fail" can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the "points" or "percentage" format is sent, the grade will only be accepted if the grade equals one of those two values. |
| `submission[excuse]` | boolean | form |  | Sets the "excused" status of an assignment. |
| `submission[late_policy_status]` | string | form |  | Sets the late policy status to either "late", "missing", "extended", "none", or null.   NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on |
| `submission[seconds_late_override]` | integer (int64) | form |  | Sets the seconds late if late policy status is "late" |
| `rubric_assessment` | RubricAssessment | form |  | Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:  The points awarded for this row.   rubric_assessment[criterion_id][points]  The rating id for the row.   rubric_assessment[criterion_id][rating_id]  Comments to add for this row.   rubric_assessment[criterion_id][comments]  For example, if the assignment rubric is (in JSON format):   !!!javascript   [     {       'id': 'crit1',       'points': 10,       'description': 'Criterion 1',       'ratings':       [         { 'id': 'rat1', 'description': 'Good', 'points': 10 },         { 'id': 'rat2', 'description': 'Poor', 'points': 3 }       ]     },     {       'id': 'crit2',       'points': 5,       'description': 'Criterion 2',       'ratings':       [         { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },         { 'id': 'rat2', 'description': 'Complete', 'points': 5 },         { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }       ]     }   ]  Then a possible set of values for rubric_assessment would be:     rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done. |

**Returns:** `void`

## PUT /v1/sections/{section_id}/assignments/{assignment_id}/anonymous_submissions/{anonymous_id}

**Grade or comment on a submission by anonymous id**  —  `grade_or_comment_on_submission_by_anonymous_id_sections`

Comment on and/or update the grading for a student's assignment submission,
fetching the submission by anonymous id (instead of user id). If any
submission or rubric_assessment arguments are provided, the user must
have permission to manage grades in the appropriate context (course or
section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `anonymous_id` | string | path | yes | ID |
| `comment[text_comment]` | string | form |  | Add a textual comment to the submission. |
| `comment[group_comment]` | boolean | form |  | Whether or not this comment should be sent to the entire group (defaults to false). Ignored if this is not a group assignment or if no text_comment is provided. |
| `comment[media_comment_id]` | string | form |  | Add an audio/video comment to the submission. Media comments can be added via this API, however, note that there is not yet an API to generate or list existing media comments, so this functionality is currently of limited use. |
| `comment[media_comment_type]` | string | form |  | The type of media comment being added. Allowed: `audio`, `video` |
| `comment[file_ids]` | array[integer] | form |  | Attach files to this comment that were previously uploaded using the Submission Comment API's files action |
| `include` | array[string] | form |  | Associations to include with the submission. "submission_comments" is always included by default. - "submission_comments": Comments on the submission (always included) - "visibility": Whether the assignment is visible to the owner of the submission - "sub_assignment_submissions": Sub-assignment submissions for discussion checkpoints - "peer_review_submissions": Peer review submission data when peer review allocation and grading is enabled - "provisional_grades": Provisional grades (only available for moderated assignments) - "group": Group information (id and name) for group assignments Allowed: `submission_comments`, `visibility`, `sub_assignment_submissions`, `peer_review_submissions`, `provisional_grades`, `group` |
| `submission[posted_grade]` | string | form |  | Assign a score to the submission, updating both the "score" and "grade" fields on the submission record. This parameter can be passed in a few different formats:  points:: A floating point or integral value, such as "13.5". The grade   will be interpreted directly as the score of the assignment.   Values above assignment.points_possible are allowed, for awarding   extra credit. percentage:: A floating point value appended with a percent sign, such as    "40%". The grade will be interpreted as a percentage score on the    assignment, where 100% == assignment.points_possible. Values above 100%    are allowed, for awarding extra credit. letter grade:: A letter grade, following the assignment's defined letter    grading scheme. For example, "A-". The resulting score will be the high    end of the defined range for the letter grade. For instance, if "B" is    defined as 86% to 84%, a letter grade of "B" will be worth 86%. The    letter grade will be rejected if the assignment does not have a defined    letter grading scheme. For more fine-grained control of scores, pass in    points or percentage rather than the letter grade. "pass/complete/fail/incomplete":: A string value of "pass" or "complete"    will give a score of 100%. "fail" or "incomplete" will give a score of    0.  Note that assignments with grading_type of "pass_fail" can only be assigned a score of 0 or assignment.points_possible, nothing inbetween. If a posted_grade in the "points" or "percentage" format is sent, the grade will only be accepted if the grade equals one of those two values. |
| `submission[excuse]` | boolean | form |  | Sets the "excused" status of an assignment. |
| `submission[late_policy_status]` | string | form |  | Sets the late policy status to either "late", "missing", "extended", "none", or null.   NB: "extended" values can only be set in the UI when the "UI features for 'extended' Submissions" Account Feature is on |
| `submission[seconds_late_override]` | integer (int64) | form |  | Sets the seconds late if late policy status is "late" |
| `rubric_assessment` | RubricAssessment | form |  | Assign a rubric assessment to this assignment submission. The sub-parameters here depend on the rubric for the assignment. The general format is, for each row in the rubric:  The points awarded for this row.   rubric_assessment[criterion_id][points]  The rating id for the row.   rubric_assessment[criterion_id][rating_id]  Comments to add for this row.   rubric_assessment[criterion_id][comments]  For example, if the assignment rubric is (in JSON format):   !!!javascript   [     {       'id': 'crit1',       'points': 10,       'description': 'Criterion 1',       'ratings':       [         { 'id': 'rat1', 'description': 'Good', 'points': 10 },         { 'id': 'rat2', 'description': 'Poor', 'points': 3 }       ]     },     {       'id': 'crit2',       'points': 5,       'description': 'Criterion 2',       'ratings':       [         { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },         { 'id': 'rat2', 'description': 'Complete', 'points': 5 },         { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }       ]     }   ]  Then a possible set of values for rubric_assessment would be:     rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done. |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students

**List gradeable students**  —  `list_gradeable_students`

A paginated list of gradeable students for the assignment. The caller must have permission to view grades.

If anonymous grading is enabled for the current assignment and the allow_new_anonymous_id parameter is passed,
the returned data will not include any values identifying the student, but will instead include an
assignment-specific anonymous ID for each student.

Section-limited instructors will only see students in their own sections.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `sort` | string | query |  | Sort results by this field. Allowed: `name` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |

**Returns:** `array[UserDisplay if anonymous grading is not enabled for the assignment or if the allow_new_anonymous_id parameter is not true]`

## GET /v1/courses/{course_id}/assignments/gradeable_students

**List multiple assignments gradeable students**  —  `list_multiple_assignments_gradeable_students`

A paginated list of students eligible to submit a list of assignments. The caller must have
permission to view grades for the requested course.

Section-limited instructors will only see students in their own sections.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_ids` | array[string] | query |  | Assignments being requested |

**Returns:** `void`

## POST /v1/courses/{course_id}/submissions/update_grades

**Grade or comment on multiple submissions**  —  `grade_or_comment_on_multiple_submissions_courses_submissions`

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `grade_data[<student_id>][posted_grade]` | string | form |  | See documentation for the posted_grade argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][excuse]` | boolean | form |  | See documentation for the excuse argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][rubric_assessment]` | RubricAssessment | form |  | See documentation for the rubric_assessment argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][text_comment]` | string | form |  | no description |
| `grade_data[<student_id>][group_comment]` | boolean | form |  | no description |
| `grade_data[<student_id>][media_comment_id]` | string | form |  | no description |
| `grade_data[<student_id>][media_comment_type]` | string | form |  | no description Allowed: `audio`, `video` |
| `grade_data[<student_id>][file_ids]` | array[integer] | form |  | See documentation for the comment[] arguments in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<assignment_id>][<student_id>]` | integer (int64) | form |  | Specifies which assignment to grade.  This argument is not necessary when using the assignment-specific endpoints. |

**Returns:** `Progress`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades

**Grade or comment on multiple submissions**  —  `grade_or_comment_on_multiple_submissions_courses_assignments`

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `grade_data[<student_id>][posted_grade]` | string | form |  | See documentation for the posted_grade argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][excuse]` | boolean | form |  | See documentation for the excuse argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][rubric_assessment]` | RubricAssessment | form |  | See documentation for the rubric_assessment argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][text_comment]` | string | form |  | no description |
| `grade_data[<student_id>][group_comment]` | boolean | form |  | no description |
| `grade_data[<student_id>][media_comment_id]` | string | form |  | no description |
| `grade_data[<student_id>][media_comment_type]` | string | form |  | no description Allowed: `audio`, `video` |
| `grade_data[<student_id>][file_ids]` | array[integer] | form |  | See documentation for the comment[] arguments in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<assignment_id>][<student_id>]` | integer (int64) | form |  | Specifies which assignment to grade.  This argument is not necessary when using the assignment-specific endpoints. |

**Returns:** `Progress`

## POST /v1/sections/{section_id}/submissions/update_grades

**Grade or comment on multiple submissions**  —  `grade_or_comment_on_multiple_submissions_sections_submissions`

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `grade_data[<student_id>][posted_grade]` | string | form |  | See documentation for the posted_grade argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][excuse]` | boolean | form |  | See documentation for the excuse argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][rubric_assessment]` | RubricAssessment | form |  | See documentation for the rubric_assessment argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][text_comment]` | string | form |  | no description |
| `grade_data[<student_id>][group_comment]` | boolean | form |  | no description |
| `grade_data[<student_id>][media_comment_id]` | string | form |  | no description |
| `grade_data[<student_id>][media_comment_type]` | string | form |  | no description Allowed: `audio`, `video` |
| `grade_data[<student_id>][file_ids]` | array[integer] | form |  | See documentation for the comment[] arguments in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<assignment_id>][<student_id>]` | integer (int64) | form |  | Specifies which assignment to grade.  This argument is not necessary when using the assignment-specific endpoints. |

**Returns:** `Progress`

## POST /v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades

**Grade or comment on multiple submissions**  —  `grade_or_comment_on_multiple_submissions_sections_assignments`

Update the grading and comments on multiple student's assignment
submissions in an asynchronous job.

The user must have permission to manage grades in the appropriate context
(course or section).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `grade_data[<student_id>][posted_grade]` | string | form |  | See documentation for the posted_grade argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][excuse]` | boolean | form |  | See documentation for the excuse argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][rubric_assessment]` | RubricAssessment | form |  | See documentation for the rubric_assessment argument in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<student_id>][text_comment]` | string | form |  | no description |
| `grade_data[<student_id>][group_comment]` | boolean | form |  | no description |
| `grade_data[<student_id>][media_comment_id]` | string | form |  | no description |
| `grade_data[<student_id>][media_comment_type]` | string | form |  | no description Allowed: `audio`, `video` |
| `grade_data[<student_id>][file_ids]` | array[integer] | form |  | See documentation for the comment[] arguments in the {api:SubmissionsApiController#update Submissions Update} documentation |
| `grade_data[<assignment_id>][<student_id>]` | integer (int64) | form |  | Specifies which assignment to grade.  This argument is not necessary when using the assignment-specific endpoints. |

**Returns:** `Progress`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read

**Mark submission as read**  —  `mark_submission_as_read_courses`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read

**Mark submission as read**  —  `mark_submission_as_read_sections`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read

**Mark submission as unread**  —  `mark_submission_as_unread_courses`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read

**Mark submission as unread**  —  `mark_submission_as_unread_sections`

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/submissions/bulk_mark_read

**Mark bulk submissions as read**  —  `mark_bulk_submissions_as_read_courses`

Accepts a string array of submission ids. Loops through and marks each submission as read

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `submissionIds` | array[string] | form |  | no description |

**Returns:** `void`

## PUT /v1/sections/{section_id}/submissions/bulk_mark_read

**Mark bulk submissions as read**  —  `mark_bulk_submissions_as_read_sections`

Accepts a string array of submission ids. Loops through and marks each submission as read

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `submissionIds` | array[string] | form |  | no description |

**Returns:** `void`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read/{item}

**Mark submission item as read**  —  `mark_submission_item_as_read_courses`

No request fields are necessary.

A submission item can be "grade", "comment" or "rubric"

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `item` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read/{item}

**Mark submission item as read**  —  `mark_submission_item_as_read_sections`

No request fields are necessary.

A submission item can be "grade", "comment" or "rubric"

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `item` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/submissions/{user_id}/clear_unread

**Clear unread status for all submissions.**  —  `clear_unread_status_for_all_submissions_courses`

Site-admin-only endpoint.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/sections/{section_id}/submissions/{user_id}/clear_unread

**Clear unread status for all submissions.**  —  `clear_unread_status_for_all_submissions_sections`

Site-admin-only endpoint.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read

**Get rubric assessments read state**  —  `get_rubric_assessments_read_state_courses_rubric_comments`

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read

**Get rubric assessments read state**  —  `get_rubric_assessments_read_state_courses_rubric_assessments`

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read

**Get rubric assessments read state**  —  `get_rubric_assessments_read_state_sections_rubric_comments`

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read

**Get rubric assessments read state**  —  `get_rubric_assessments_read_state_sections_rubric_assessments`

Return whether new rubric comments/grading made on a submission have been seen by the student being assessed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read

**Mark rubric assessments as read**  —  `mark_rubric_assessments_as_read_courses_rubric_comments`

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read

**Mark rubric assessments as read**  —  `mark_rubric_assessments_as_read_courses_rubric_assessments`

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_comments/read

**Mark rubric assessments as read**  —  `mark_rubric_assessments_as_read_sections_rubric_comments`

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/rubric_assessments/read

**Mark rubric assessments as read**  —  `mark_rubric_assessments_as_read_sections_rubric_assessments`

Indicate that rubric comments/grading made on a submission have been read by the student being assessed.
Only the student who owns the submission can use this endpoint.

NOTE: Rubric assessments will be marked as read automatically when they are viewed in Canvas web.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read

**Get document annotations read state**  —  `get_document_annotations_read_state_courses`

Return whether annotations made on a submitted document have been read by the student

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read

**Get document annotations read state**  —  `get_document_annotations_read_state_sections`

Return whether annotations made on a submitted document have been read by the student

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read

**Mark document annotations as read**  —  `mark_document_annotations_as_read_courses`

Indicate that annotations made on a submitted document have been read by the student.
Only the student who owns the submission can use this endpoint.

NOTE: Document annotations will be marked as read automatically when they are viewed in Canvas web.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/document_annotations/read

**Mark document annotations as read**  —  `mark_document_annotations_as_read_sections`

Indicate that annotations made on a submitted document have been read by the student.
Only the student who owns the submission can use this endpoint.

NOTE: Document annotations will be marked as read automatically when they are viewed in Canvas web.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/submission_summary

**Submission Summary**  —  `submission_summary_courses`

Returns the number of submissions for the given assignment based on gradeable students
that fall into three categories: graded, ungraded, not submitted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `grouped` | boolean | query |  | If this argument is true, the response will take into account student groups. |
| `include_deactivated` | boolean | query |  | If this argument is true, the response will include deactivated students in the summary (defaults to false). |

**Returns:** `void`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/submission_summary

**Submission Summary**  —  `submission_summary_sections`

Returns the number of submissions for the given assignment based on gradeable students
that fall into three categories: graded, ungraded, not submitted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `grouped` | boolean | query |  | If this argument is true, the response will take into account student groups. |
| `include_deactivated` | boolean | query |  | If this argument is true, the response will include deactivated students in the summary (defaults to false). |

**Returns:** `void`


---

# Models


## MediaComment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `content-type` | string |  | e.g. `audio/mp4` |
| `display_name` | string |  | e.g. `something` |
| `media_id` | string |  | e.g. `3232` |
| `media_type` | string |  | e.g. `audio` |
| `url` | string |  | e.g. `http://example.com/media_url` |


## SubmissionComment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | e.g. `37` |
| `author_id` | integer |  | e.g. `134` |
| `author_name` | string |  | e.g. `Toph Beifong` |
| `author` | string |  | Abbreviated user object UserDisplay (see users API). e.g. `{}` |
| `comment` | string |  | e.g. `Well here's the thing...` |
| `created_at` | datetime |  | e.g. `2012-01-01T01:00:00Z` |
| `edited_at` | datetime |  | e.g. `2012-01-02T01:00:00Z` |
| `media_comment` | MediaComment |  |  |


## Submission

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `assignment_id` | integer |  | The submission's assignment id e.g. `23` |
| `assignment` | Assignment |  | The submission's assignment (see the assignments API) (optional) |
| `course` | Course |  | The submission's course (see the course API) (optional) |
| `attempt` | integer |  | This is the submission attempt number. e.g. `1` |
| `body` | string |  | The content of the submission, if it was submitted directly in a text field. e.g. `There are three factors too...` |
| `grade` | string |  | The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example). e.g. `A-` |
| `grade_matches_current_submission` | boolean |  | A boolean flag which is false if the student has re-submitted since the submission was last graded. e.g. `True` |
| `html_url` | string |  | URL to the submission. This will require the user to log in. e.g. `http://example.com/courses/255/assignments/543/submissions/134` |
| `preview_url` | string |  | URL to the submission preview. This will require the user to log in. e.g. `http://example.com/courses/255/assignments/543/submissions/134?preview=1` |
| `score` | number |  | The raw score e.g. `13.5` |
| `submission_comments` | array[SubmissionComment] |  | Associated comments for a submission (optional) |
| `submission_type` | string |  | The types of submission ex: ('online_text_entry'\|'online_url'\|'online_upload'\|'online_quiz'\|'media_recording'\|'student_annotation') e.g. `online_text_entry` |
| `submitted_at` | datetime |  | The timestamp when the assignment was submitted e.g. `2012-01-01T01:00:00Z` |
| `url` | string |  | The URL of the submission (for 'online_url' submissions). |
| `user_id` | integer |  | The id of the user who created the submission e.g. `134` |
| `grader_id` | integer |  | The id of the user who graded the submission. This will be null for submissions that haven't been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz autograder and autograding LTI tools).  Specifically autograded quizzes set grader_id to the negative of the quiz id.  Submissions autograded by LTI tools set grader_id to the negative of the tool id. e.g. `86` |
| `graded_at` | datetime |  | e.g. `2012-01-02T03:05:34Z` |
| `user` | User |  | The submissions user (see user API) (optional) |
| `late` | boolean |  | Whether the submission was made after the applicable due date e.g. `False` |
| `assignment_visible` | boolean |  | Whether the assignment is visible to the user who submitted the assignment. Submissions where `assignment_visible` is false no longer count towards the student's grade and the assignment can no longer be accessed by the student. `assignment_visible` becomes false for submissions that do not have a grade and whose assignment is no longer assigned to the student's section. e.g. `True` |
| `excused` | boolean |  | Whether the assignment is excused.  Excused assignments have no impact on a user's grade. e.g. `True` |
| `missing` | boolean |  | Whether the assignment is missing. e.g. `True` |
| `late_policy_status` | string |  | The status of the submission in relation to the late policy. Can be late, missing, extended, none, or null. e.g. `missing` |
| `points_deducted` | number |  | The amount of points automatically deducted from the score by the missing/late policy for a late or missing assignment. e.g. `12.3` |
| `seconds_late` | number |  | The amount of time, in seconds, that an submission is late by. e.g. `300` |
| `workflow_state` | string |  | The current state of the submission e.g. `submitted` |
| `extra_attempts` | number |  | Extra submission attempts allowed for the given user and assignment. e.g. `10` |
| `anonymous_id` | string |  | A unique short ID identifying this submission without reference to the owning user. Only included if the caller has administrator access for the current account. e.g. `acJ4Q` |
| `posted_at` | datetime |  | The date this submission was posted to the student, or nil if it has not been posted. e.g. `2020-01-02T11:10:30Z` |
| `read_status` | string |  | The read status of this submission for the given user (optional). Including read_status will mark submission(s) as read. e.g. `read` |
| `redo_request` | boolean |  | This indicates whether the submission has been reassigned by the instructor. e.g. `true` |
