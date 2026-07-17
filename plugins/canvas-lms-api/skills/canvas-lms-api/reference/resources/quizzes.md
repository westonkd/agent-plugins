# Quizzes

> Canvas LMS REST API — `/quizzes` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes

**List quizzes in a course**  —  `list_quizzes_in_course`

Returns the paginated list of Quizzes in this course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `search_term` | string | query |  | The partial title of the quizzes to match and return. |

**Returns:** `array[Quiz]`

## GET /v1/courses/{course_id}/quizzes/{id}

**Get a single quiz**  —  `get_single_quiz`

Returns the quiz with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Quiz`

## POST /v1/courses/{course_id}/quizzes

**Create a quiz**  —  `create_quiz`

Create a new quiz for this course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz[title]` | string | form | yes | The quiz title. |
| `quiz[description]` | string | form |  | A description of the quiz. |
| `quiz[quiz_type]` | string | form |  | The type of quiz. Allowed: `practice_quiz`, `assignment`, `graded_survey`, `survey` |
| `quiz[assignment_group_id]` | integer (int64) | form |  | The assignment group id to put the assignment in. Defaults to the top assignment group in the course. Only valid if the quiz is graded, i.e. if quiz_type is "assignment" or "graded_survey". |
| `quiz[time_limit]` | integer (int64) | form |  | Time limit to take this quiz, in minutes. Set to null for no time limit. Defaults to null. |
| `quiz[shuffle_answers]` | boolean | form |  | If true, quiz answers for multiple choice questions will be randomized for each student. Defaults to false. |
| `quiz[hide_results]` | string | form |  | Dictates whether or not quiz results are hidden from students. If null, students can see their results after any attempt. If "always", students can never see their results. If "until_after_last_attempt", students can only see results after their last attempt. (Only valid if allowed_attempts > 1). Defaults to null. Allowed: `always`, `until_after_last_attempt` |
| `quiz[show_correct_answers]` | boolean | form |  | Only valid if hide_results=null If false, hides correct answers from students when quiz results are viewed. Defaults to true. |
| `quiz[show_correct_answers_last_attempt]` | boolean | form |  | Only valid if show_correct_answers=true and allowed_attempts > 1 If true, hides correct answers from students when quiz results are viewed until they submit the last attempt for the quiz. Defaults to false. |
| `quiz[show_correct_answers_at]` | DateTime | form |  | Only valid if show_correct_answers=true If set, the correct answers will be visible by students only after this date, otherwise the correct answers are visible once the student hands in their quiz submission. |
| `quiz[hide_correct_answers_at]` | DateTime | form |  | Only valid if show_correct_answers=true If set, the correct answers will stop being visible once this date has passed. Otherwise, the correct answers will be visible indefinitely. |
| `quiz[allowed_attempts]` | integer (int64) | form |  | Number of times a student is allowed to take a quiz. Set to -1 for unlimited attempts. Defaults to 1. |
| `quiz[scoring_policy]` | string | form |  | Required and only valid if allowed_attempts > 1. Scoring policy for a quiz that students can take multiple times. Defaults to "keep_highest". Allowed: `keep_highest`, `keep_latest` |
| `quiz[one_question_at_a_time]` | boolean | form |  | If true, shows quiz to student one question at a time. Defaults to false. |
| `quiz[cant_go_back]` | boolean | form |  | Only valid if one_question_at_a_time=true If true, questions are locked after answering. Defaults to false. |
| `quiz[access_code]` | string | form |  | Restricts access to the quiz with a password. For no access code restriction, set to null. Defaults to null. |
| `quiz[ip_filter]` | string | form |  | Restricts access to the quiz to computers in a specified IP range. Filters can be a comma-separated list of addresses, or an address followed by a mask  Examples:   "192.168.217.1"   "192.168.217.1/24"   "192.168.217.1/255.255.255.0"  For no IP filter restriction, set to null. Defaults to null. |
| `quiz[due_at]` | DateTime | form |  | The day/time the quiz is due. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z. |
| `quiz[lock_at]` | DateTime | form |  | The day/time the quiz is locked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z. |
| `quiz[unlock_at]` | DateTime | form |  | The day/time the quiz is unlocked for students. Accepts times in ISO 8601 format, e.g. 2011-10-21T18:48Z. |
| `quiz[published]` | boolean | form |  | Whether the quiz should have a draft state of published or unpublished. NOTE: If students have started taking the quiz, or there are any submissions for the quiz, you may not unpublish a quiz and will recieve an error. |
| `quiz[one_time_results]` | boolean | form |  | Whether students should be prevented from viewing their quiz results past the first time (right after they turn the quiz in.) Only valid if "hide_results" is not set to "always". Defaults to false. |
| `quiz[only_visible_to_overrides]` | boolean | form |  | Whether this quiz is only visible to overrides (Only useful if 'differentiated assignments' account setting is on) Defaults to false. |

**Returns:** `Quiz`

## PUT /v1/courses/{course_id}/quizzes/{id}

**Edit a quiz**  —  `edit_quiz`

Modify an existing quiz. See the documentation for quiz creation.

Additional arguments:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `quiz[notify_of_update]` | boolean | form |  | If true, notifies users that the quiz has changed. Defaults to true |

**Returns:** `Quiz`

## DELETE /v1/courses/{course_id}/quizzes/{id}

**Delete a quiz**  —  `delete_quiz`

Deletes a quiz and returns the deleted quiz object.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Quiz`

## POST /v1/courses/{course_id}/quizzes/{id}/reorder

**Reorder quiz items**  —  `reorder_quiz_items`

Change order of the quiz questions or groups within the quiz

<b>204 No Content</b> response code is returned if the reorder was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `order[id]` | array[integer] | form | yes | The associated item's unique identifier |
| `order[type]` | array[string] | form |  | The type of item is either 'question' or 'group' Allowed: `question`, `group` |

**Returns:** `void`

## POST /v1/courses/{course_id}/quizzes/{id}/validate_access_code

**Validate quiz access code**  —  `validate_quiz_access_code`

Accepts an access code and returns a boolean indicating whether that access code is correct

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `access_code` | string | form | yes | The access code being validated |

**Returns:** `boolean`


---

# Models


## Quiz

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the quiz e.g. `5` |
| `title` | string |  | the title of the quiz e.g. `Hamlet Act 3 Quiz` |
| `html_url` | string |  | the HTTP/HTTPS URL to the quiz e.g. `http://canvas.example.edu/courses/1/quizzes/2` |
| `mobile_url` | string |  | a url suitable for loading the quiz in a mobile webview.  it will persiste the headless session and, for quizzes in public courses, will force the user to login e.g. `http://canvas.example.edu/courses/1/quizzes/2?persist_healdess=1&force_user=1` |
| `preview_url` | string |  | A url that can be visited in the browser with a POST request to preview a quiz as the teacher. Only present when the user may grade e.g. `http://canvas.example.edu/courses/1/quizzes/2/take?preview=1` |
| `description` | string |  | the description of the quiz e.g. `This is a quiz on Act 3 of Hamlet` |
| `quiz_type` | string |  | type of quiz possible values: 'practice_quiz', 'assignment', 'graded_survey', 'survey' e.g. `assignment` |
| `assignment_group_id` | integer |  | the ID of the quiz's assignment group: e.g. `3` |
| `time_limit` | integer |  | quiz time limit in minutes e.g. `5` |
| `shuffle_answers` | boolean |  | shuffle answers for students? e.g. `False` |
| `hide_results` | string |  | let students see their quiz responses? possible values: null, 'always', 'until_after_last_attempt' e.g. `always` |
| `show_correct_answers` | boolean |  | show which answers were correct when results are shown? only valid if hide_results=null e.g. `True` |
| `show_correct_answers_last_attempt` | boolean |  | restrict the show_correct_answers option above to apply only to the last submitted attempt of a quiz that allows multiple attempts. only valid if show_correct_answers=true and allowed_attempts > 1 e.g. `True` |
| `show_correct_answers_at` | datetime |  | when should the correct answers be visible by students? only valid if show_correct_answers=true e.g. `2013-01-23T23:59:00-07:00` |
| `hide_correct_answers_at` | datetime |  | prevent the students from seeing correct answers after the specified date has passed. only valid if show_correct_answers=true e.g. `2013-01-23T23:59:00-07:00` |
| `one_time_results` | boolean |  | prevent the students from seeing their results more than once (right after they submit the quiz) e.g. `True` |
| `scoring_policy` | string |  | which quiz score to keep (only if allowed_attempts != 1) possible values: 'keep_highest', 'keep_latest' e.g. `keep_highest` |
| `allowed_attempts` | integer |  | how many times a student can take the quiz -1 = unlimited attempts e.g. `3` |
| `one_question_at_a_time` | boolean |  | show one question at a time? e.g. `False` |
| `question_count` | integer |  | the number of questions in the quiz e.g. `12` |
| `points_possible` | integer |  | The total point value given to the quiz e.g. `20` |
| `cant_go_back` | boolean |  | lock questions after answering? only valid if one_question_at_a_time=true e.g. `False` |
| `access_code` | string |  | access code to restrict quiz access e.g. `2beornot2be` |
| `ip_filter` | string |  | IP address or range that quiz access is limited to e.g. `123.123.123.123` |
| `due_at` | datetime |  | when the quiz is due e.g. `2013-01-23T23:59:00-07:00` |
| `lock_at` | datetime |  | when to lock the quiz |
| `unlock_at` | datetime |  | when to unlock the quiz e.g. `2013-01-21T23:59:00-07:00` |
| `published` | boolean |  | whether the quiz has a published or unpublished draft state. e.g. `True` |
| `unpublishable` | boolean |  | Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the quiz. e.g. `True` |
| `locked_for_user` | boolean |  | Whether or not this is locked for the user. e.g. `False` |
| `lock_info` | LockInfo |  | (Optional) Information for the user about the lock. Present when locked_for_user is true. |
| `lock_explanation` | string |  | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. e.g. `This quiz is locked until September 1 at 12:00am` |
| `speedgrader_url` | string |  | Link to SpeedGrader for this quiz. Will not be present if quiz is unpublished e.g. `http://canvas.instructure.com/courses/1/speed_grader?assignment_id=1` |
| `quiz_extensions_url` | string |  | Link to endpoint to send extensions for this quiz. e.g. `http://canvas.instructure.com/courses/1/quizzes/2/quiz_extensions` |
| `permissions` | QuizPermissions |  | Permissions the user has for the quiz |
| `all_dates` | array[AssignmentDate] |  | list of due dates for the quiz |
| `version_number` | integer |  | Current version number of the quiz e.g. `3` |
| `question_types` | array[string] |  | List of question types in the quiz e.g. `['multiple_choice', 'essay']` |
| `anonymous_submissions` | boolean |  | Whether survey submissions will be kept anonymous (only applicable to 'graded_survey', 'survey' quiz types) e.g. `False` |


## QuizPermissions

Permissions the user has for the quiz

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `read` | boolean |  | whether the user can view the quiz e.g. `True` |
| `submit` | boolean |  | whether the user may submit a submission for the quiz e.g. `True` |
| `create` | boolean |  | whether the user may create a new quiz e.g. `True` |
| `manage` | boolean |  | whether the user may edit, update, or delete the quiz e.g. `True` |
| `read_statistics` | boolean |  | whether the user may view quiz statistics for this quiz e.g. `True` |
| `review_grades` | boolean |  | whether the user may review grades for all quiz submissions for this quiz e.g. `True` |
| `update` | boolean |  | whether the user may update the quiz e.g. `True` |
