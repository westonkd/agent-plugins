# Quiz Submission User List

> Canvas LMS REST API — `/quiz_submission_user_list` resource. Base path `/api`.

## POST /v1/courses/{course_id}/quizzes/{id}/submission_users/message

**Send a message to unsubmitted or submitted users for the quiz**  —  `send_message_to_unsubmitted_or_submitted_users_for_quiz`

{
  "body": {
    "type": "string",
    "description": "message body of the conversation to be created",
    "example": "Please take the quiz."
  },
  "recipients": {
    "type": "string",
    "description": "Who to send the message to. May be either 'submitted' or 'unsubmitted'",
    "example": "submitted"
  },
  "subject": {
    "type": "string",
    "description": "Subject of the new Conversation created",
    "example": "ATTN: Quiz 101 Students"
  }
}

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `conversations` | QuizUserConversation | form |  | - Body and recipients to send the message to. |

**Returns:** `void`


---

# Models


## QuizSubmissionUserList



## QuizSubmissionUserListMeta



## JSONAPIPagination
