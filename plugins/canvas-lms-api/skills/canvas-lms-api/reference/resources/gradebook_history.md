# Gradebook History

> Canvas LMS REST API — `/gradebook_history` resource. Base path `/api`.

## GET /v1/courses/{course_id}/gradebook_history/days

**Days in gradebook history for this course**  —  `days_in_gradebook_history_for_this_course`

Returns a map of dates to grader/assignment groups

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the contextual course for this API call |

**Returns:** `array[Day]`

## GET /v1/courses/{course_id}/gradebook_history/{date}

**Details for a given date in gradebook history for this course**  —  `details_for_given_date_in_gradebook_history_for_this_course`

Returns the graders who worked on this day, along with the assignments they worked on.
More details can be obtained by selecting a grader and assignment and calling the
'submissions' api endpoint for a given date.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the contextual course for this API call |
| `date` | string | path | yes | The date for which you would like to see detailed information |

**Returns:** `array[Grader]`

## GET /v1/courses/{course_id}/gradebook_history/{date}/graders/{grader_id}/assignments/{assignment_id}/submissions

**Lists submissions**  —  `lists_submissions`

Gives a nested list of submission versions

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the contextual course for this API call |
| `date` | string | path | yes | The date for which you would like to see submissions |
| `grader_id` | integer (int64) | path | yes | The ID of the grader for which you want to see submissions |
| `assignment_id` | integer (int64) | path | yes | The ID of the assignment for which you want to see submissions |

**Returns:** `array[SubmissionHistory]`

## GET /v1/courses/{course_id}/gradebook_history/feed

**List uncollated submission versions**  —  `list_uncollated_submission_versions`

Gives a paginated, uncollated list of submission versions for all matching
submissions in the context. This SubmissionVersion objects will not include
the +new_grade+ or +previous_grade+ keys, only the +grade+; same for
+graded_at+ and +grader+.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the contextual course for this API call |
| `assignment_id` | integer (int64) | query |  | The ID of the assignment for which you want to see submissions. If absent, versions of submissions from any assignment in the course are included. |
| `user_id` | integer (int64) | query |  | The ID of the user for which you want to see submissions. If absent, versions of submissions from any user in the course are included. |
| `ascending` | boolean | query |  | Returns submission versions in ascending date order (oldest first). If absent, returns submission versions in descending date order (newest first). |

**Returns:** `array[SubmissionVersion]`


---

# Models


## Grader

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the user_id of the user who graded the contained submissions e.g. `27` |
| `name` | string |  | the name of the user who graded the contained submissions e.g. `Some User` |
| `assignments` | array[integer] |  | the assignment groups for all submissions in this response that were graded by this user.  The details are not nested inside here, but the fact that an assignment is present here means that the grader did grade submissions for this assignment on the contextual date. You can use the id of a grader and of an assignment to make another API call to find all submissions for a grader/assignment combination on a given date. e.g. `[1, 2, 3]` |


## Day

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `date` | datetime |  | the date represented by this entry e.g. `1986-08-09` |
| `graders` | integer |  | an array of the graders who were responsible for the submissions in this response. the submissions are grouped according to the person who graded them and the assignment they were submitted for. e.g. `[]` |


## SubmissionVersion

A SubmissionVersion object contains all the fields that a Submission object does, plus additional fields prefixed with current_* new_* and previous_* described below.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `assignment_id` | integer |  | the id of the assignment this submissions is for e.g. `22604` |
| `assignment_name` | string |  | the name of the assignment this submission is for e.g. `some assignment` |
| `body` | string |  | the body text of the submission e.g. `text from the submission` |
| `current_grade` | string |  | the most up to date grade for the current version of this submission e.g. `100` |
| `current_graded_at` | datetime |  | the latest time stamp for the grading of this submission e.g. `2013-01-31T18:16:31Z` |
| `current_grader` | string |  | the name of the most recent grader for this submission e.g. `Grader Name` |
| `grade_matches_current_submission` | boolean |  | boolean indicating whether the grade is equal to the current submission grade e.g. `True` |
| `graded_at` | datetime |  | time stamp for the grading of this version of the submission e.g. `2013-01-31T18:16:31Z` |
| `grader` | string |  | the name of the user who graded this version of the submission e.g. `Grader Name` |
| `grader_id` | integer |  | the user id of the user who graded this version of the submission e.g. `67379` |
| `id` | integer |  | the id of the submission of which this is a version e.g. `11607` |
| `new_grade` | string |  | the updated grade provided in this version of the submission e.g. `100` |
| `new_graded_at` | datetime |  | the timestamp for the grading of this version of the submission (alias for graded_at) e.g. `2013-01-31T18:16:31Z` |
| `new_grader` | string |  | alias for 'grader' e.g. `Grader Name` |
| `previous_grade` | string |  | the grade for the submission version immediately preceding this one e.g. `90` |
| `previous_graded_at` | datetime |  | the timestamp for the grading of the submission version immediately preceding this one e.g. `2013-01-29T12:12:12Z` |
| `previous_grader` | string |  | the name of the grader who graded the version of this submission immediately preceding this one e.g. `Graded on submission` |
| `score` | integer |  | the score for this version of the submission e.g. `100` |
| `user_name` | string |  | the name of the student who created this submission e.g. `student@example.com` |
| `submission_type` | string |  | the type of submission e.g. `online` |
| `url` | string |  | the url of the submission, if there is one |
| `user_id` | integer |  | the user ID of the student who created this submission e.g. `67376` |
| `workflow_state` | string |  | the state of the submission at this version e.g. `unsubmitted` |


## SubmissionHistory

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `submission_id` | integer |  | the id of the submission e.g. `4` |
| `versions` | array[SubmissionVersion] |  | an array of all the versions of this submission |
