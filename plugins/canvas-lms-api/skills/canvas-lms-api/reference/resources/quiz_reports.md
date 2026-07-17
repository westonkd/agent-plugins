# Quiz Reports

> Canvas LMS REST API — `/quiz_reports` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/reports

**Retrieve all quiz reports**  —  `retrieve_all_quiz_reports`

Returns a list of all available reports.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `includes_all_versions` | boolean | query |  | Whether to retrieve reports that consider all the submissions or only the most recent. Defaults to false, ignored for item_analysis reports. |

**Returns:** `array[QuizReport]`

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/reports

**Create a quiz report**  —  `create_quiz_report`

Create and return a new report for this quiz. If a previously
generated report matches the arguments and is still current (i.e.
there have been no new submissions), it will be returned.

*Responses*

* <code>400 Bad Request</code> if the specified report type is invalid
* <code>409 Conflict</code> if a quiz report of the specified type is already being
  generated

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `quiz_report[report_type]` | string | form | yes | The type of report to be generated. Allowed: `student_analysis`, `item_analysis` |
| `quiz_report[includes_all_versions]` | boolean | form |  | Whether the report should consider all submissions or only the most recent. Defaults to false, ignored for item_analysis. |
| `include` | String[] | form |  | Whether the output should include documents for the file and/or progress objects associated with this report. (Note: JSON-API only) Allowed: `file`, `progress` |

**Returns:** `QuizReport`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}

**Get a quiz report**  —  `get_quiz_report`

Returns the data for a single quiz report.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | String[] | query |  | Whether the output should include documents for the file and/or progress objects associated with this report. (Note: JSON-API only) Allowed: `file`, `progress` |

**Returns:** `QuizReport`

## DELETE /v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}

**Abort the generation of a report, or remove a previously generated one**  —  `abort_generation_of_report_or_remove_previously_generated_one`

This API allows you to cancel a previous request you issued for a report to
be generated. Or in the case of an already generated report, you'd like to
remove it, perhaps to generate it another time with an updated version that
provides new features.

You must check the report's generation status before attempting to use this
interface. See the "workflow_state" property of the QuizReport's Progress
object for more information. Only when the progress reports itself in a
"queued" state can the generation be aborted.

*Responses*

- <code>204 No Content</code> if your request was accepted
- <code>422 Unprocessable Entity</code> if the report is not being generated
  or can not be aborted at this stage

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## QuizReport

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the quiz report e.g. `5` |
| `quiz_id` | integer |  | the ID of the quiz e.g. `4` |
| `report_type` | string |  | which type of report this is possible values: 'student_analysis', 'item_analysis' e.g. `student_analysis` |
| `readable_type` | string |  | a human-readable (and localized) version of the report_type e.g. `Student Analysis` |
| `includes_all_versions` | boolean |  | boolean indicating whether the report represents all submissions or only the most recent ones for each student e.g. `True` |
| `anonymous` | boolean |  | boolean indicating whether the report is for an anonymous survey. if true, no student names will be included in the csv e.g. `False` |
| `generatable` | boolean |  | boolean indicating whether the report can be generated, which is true unless the quiz is a survey one e.g. `True` |
| `created_at` | datetime |  | when the report was created e.g. `2013-05-01T12:34:56-07:00` |
| `updated_at` | datetime |  | when the report was last updated e.g. `2013-05-01T12:34:56-07:00` |
| `url` | string |  | the API endpoint for this report e.g. `http://canvas.example.com/api/v1/courses/1/quizzes/1/reports/1` |
| `file` | File |  | if the report has finished generating, a File object that represents it. refer to the Files API for more information about the format |
| `progress_url` | string |  | if the report has not yet finished generating, a URL where information about its progress can be retrieved. refer to the Progress API for more information (Note: not available in JSON-API format) |
| `progress` | Progress |  | if the report is being generated, a Progress object that represents the operation. Refer to the Progress API for more information about the format. (Note: available only in JSON-API format) |
