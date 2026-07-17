# Submission Comments

> Canvas LMS REST API — `/submission_comments` resource. Base path `/api`.

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id}

**Edit a submission comment**  —  `edit_submission_comment`

Edit the given submission comment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `comment` | string | form |  | If this argument is present, edit the text of a comment. |

**Returns:** `SubmissionComment`

## DELETE /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id}

**Delete a submission comment**  —  `delete_submission_comment`

Delete the given submission comment.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `SubmissionComment`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files

**Upload a file**  —  `upload_file`

Upload a file to attach to a submission comment

See the {file:file.file_uploads.html File Upload Documentation} for details on the file upload workflow.

The final step of the file upload workflow will return the attachment data,
including the new file id. The caller can then PUT the file_id to the
submission API to attach it to a comment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |

**Returns:** `void`
