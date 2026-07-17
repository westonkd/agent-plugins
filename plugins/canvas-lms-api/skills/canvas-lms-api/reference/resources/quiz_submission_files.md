# Quiz Submission Files

> Canvas LMS REST API — `/quiz_submission_files` resource. Base path `/api`.

## POST /v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files

**Upload a file**  —  `upload_file`

Associate a new quiz submission file

This API endpoint is the first step in uploading a quiz submission file.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow as these parameters are interpreted as per the
documentation there.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `name` | string | form |  | The name of the quiz submission file |
| `on_duplicate` | string | form |  | How to handle duplicate names |

**Returns:** `void`
