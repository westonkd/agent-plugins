# Score

> Canvas LMS REST API — `/score` resource. Base path `/api`.

## POST /lti/courses/{course_id}/line_items/{line_item_id}/scores

**Create a Score**  —  `create_score`

Create a new Result from the score params. If this is for the first created line_item for a
resourceLinkId, or it is a line item that is not attached to a resourceLinkId, then a submission
record will be created for the associated assignment when gradingProgress is set to
FullyGraded or PendingManual.

The submission score will also be updated when a score object is sent with either of those
two values for gradingProgress. If a score object is sent with either of FullyGraded or
PendingManual as the value for gradingProgress and scoreGiven is missing, the assignment
will not be graded. This also supposes the line_item meets the condition to create a submission.

A submission comment with an unknown author will be created when the comment value is included.
This also supposes the line_item meets the condition to create a submission.

It is also possible to submit a file along with this score, which will attach the file to the
submission that is created. Files should be formatted as Content Items, with the correct syntax
below.

Returns a url pointing to the Result. If any files were submitted, also returns the Content Items
which were sent in the request, each with a url pointing to the Progress of the file upload.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `line_item_id` | string | path | yes | ID |
| `userId` | string | form | yes | The lti_user_id or the Canvas user_id. Returns a 422 if user not found in Canvas or is not a student. |
| `activityProgress` | string | form | yes | Indicate to Canvas the status of the user towards the activity's completion. Must be one of Initialized, Started, InProgress, Submitted, Completed. |
| `gradingProgress` | string | form | yes | Indicate to Canvas the status of the grading process. A value of PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded. |
| `timestamp` | string | form | yes | Date and time when the score was modified in the tool. Should use ISO8601-formatted date with subsecond precision. Returns a 400 if the timestamp is earlier than the updated_at time of the Result. |
| `scoreGiven` | number | form |  | The Current score received in the tool for this line item and user, scaled to the scoreMaximum |
| `scoreMaximum` | number | form |  | Maximum possible score for this result; it must be present if scoreGiven is present. Returns 422 if not present when scoreGiven is present. |
| `comment` | string | form |  | Comment visible to the student about this score. |
| `submission` | Object | form |  | Contains metadata about the submission attempt. Supported fields listed below. |
| `submission[submittedAt]` | string | form |  | Date and time that the submission was originally created. Should use ISO8601-formatted date with subsecond precision. If the submittedAt time has not changed from its current value, the submission attempt number will not be incremented. |
| `https://canvas.instructure.com/lti/submission` | Object | form |  | (EXTENSION) Optional submission type and data. Fields listed below. |
| `https://canvas.instructure.com/lti/submission[new_submission]` | boolean | form |  | (EXTENSION field) flag to indicate that this is a new submission. Defaults to true unless submission_type is none. |
| `https://canvas.instructure.com/lti/submission[preserve_score]` | boolean | form |  | (EXTENSION field) flag to prevent a request from clearing an existing grade for a submission. Defaults to false. |
| `https://canvas.instructure.com/lti/submission[prioritize_non_tool_grade]` | boolean | form |  | (EXTENSION field) flag to prevent a request from overwriting an existing grade for a submission. Defaults to false. |
| `https://canvas.instructure.com/lti/submission[submission_type]` | string | form |  | (EXTENSION field) permissible values are: none, basic_lti_launch, online_text_entry, external_tool, online_upload, or online_url. Defaults to external_tool. Ignored if content_items are provided. |
| `https://canvas.instructure.com/lti/submission[submission_data]` | string | form |  | (EXTENSION field) submission data (URL or body text). Only used for submission_types basic_lti_launch, online_text_entry, online_url. Ignored if content_items are provided. |
| `https://canvas.instructure.com/lti/submission[submitted_at]` | string | form |  | (EXTENSION field) Date and time that the submission was originally created. Should use ISO8601-formatted date with subsecond precision. This should match the date and time that the original submission happened in Canvas. Use of submission.submittedAt is preferred. |
| `https://canvas.instructure.com/lti/submission[content_items]` | Array | form |  | (EXTENSION field) Files that should be included with the submission. Each item should contain `type: file`, and a url pointing to the file. It can also contain a title, and an explicit MIME type if needed (otherwise, MIME type will be inferred from the title or url). If any items are present, submission_type will be online_upload. |

**Returns:** `array[resultUrl String The url to the result that was created.]`


---

# Models


## Score

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `userId` | string |  | The lti_user_id or the Canvas user_id e.g. `50 \| 'abcasdf'` |
| `scoreGiven` | number |  | The Current score received in the tool for this line item and user, scaled to the scoreMaximum e.g. `50` |
| `scoreMaximum` | number |  | Maximum possible score for this result; it must be present if scoreGiven is present. e.g. `50` |
| `comment` | string |  | Comment visible to the student about this score. |
| `timestamp` | string |  | Date and time when the score was modified in the tool. Should use subsecond precision. e.g. `2017-04-16T18:54:36.736+00:00` |
| `activityProgress` | string |  | Indicate to Canvas the status of the user towards the activity's completion. Must be one of Initialized, Started, InProgress, Submitted, Completed e.g. `Completed` |
| `gradingProgress` | string |  | Indicate to Canvas the status of the grading process. A value of PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded e.g. `FullyGraded` |
| `submission` | object |  | Contains metadata about the submission attempt, like submittedAt: Date and time that the submission was originally created - should use ISO8601-formatted date with subsecond precision. e.g. `{'submittedAt': '2017-04-14T18:54:36.736+00:00'}` |
