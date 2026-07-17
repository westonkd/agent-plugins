# Plagiarism Detection Submissions

> Canvas LMS REST API — `/plagiarism_detection_submissions` resource. Base path `/api`.

## GET /lti/assignments/{assignment_id}/submissions/{submission_id}

**Get a single submission**  —  `get_single_submission`

Get a single submission, based on submission id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |

**Returns:** `void`

## GET /lti/assignments/{assignment_id}/submissions/{submission_id}/history

**Get the history of a single submission**  —  `get_history_of_single_submission`

Get a list of all attempts made for a submission, based on submission id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## Submission

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `lti_course_id` | string |  | e.g. `66157096483e6b3a50bfedc6bac902c0b20a8241` |
| `course_id` | integer |  | e.g. `10000000000060` |
| `assignment_id` | integer |  | The submission's assignment id e.g. `23` |
| `attempt` | integer |  | This is the submission attempt number. e.g. `1` |
| `body` | string |  | The content of the submission, if it was submitted directly in a text field. e.g. `There are three factors too...` |
| `submission_type` | string |  | The types of submission ex: ('online_text_entry'\|'online_url'\|'online_upload'\|'media_recording'\|'student_annotation') e.g. `online_text_entry` |
| `submitted_at` | datetime |  | The timestamp when the assignment was submitted e.g. `2012-01-01T01:00:00Z` |
| `url` | string |  | The URL of the submission (for 'online_url' submissions). |
| `user_id` | integer |  | The id of the user who created the submission e.g. `134` |
| `eula_agreement_timestamp` | string |  | UTC timestamp showing when the user agreed to the EULA (if given by the tool provider) e.g. `1508250487578` |
| `workflow_state` | string |  | The current state of the submission e.g. `submitted` |
| `attachments` | File |  | Files that are attached to the submission |


## File

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `size` | integer |  | e.g. `4` |
| `content-type` | string |  | e.g. `text/plain` |
| `url` | string |  | e.g. `http://www.example.com/files/569/download?download_frd=1` |
| `id` | integer |  | e.g. `569` |
| `display_name` | string |  | e.g. `file.txt` |
| `created_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
| `updated_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
