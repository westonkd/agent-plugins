# AI Conversations

> Canvas LMS REST API — `/ai_conversations` resource. Base path `/api`.

## GET /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}

**Show conversation**  —  `show_conversation`

Get a specific conversation by ID (for teachers viewing student conversations)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `{Object} Hash with conversation details including messages`

## GET /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations

**Get active conversation**  —  `get_active_conversation`

Get the active conversation for the current user and AI experience

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |

**Returns:** `{Object} Hash with id and messages array, or empty object if no active conversation`

## POST /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations

**Create AI conversation**  —  `create_ai_conversation`

Initialize a new conversation with the AI experience

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |

**Returns:** `{Object} Hash with conversation_id and initial messages array`

## POST /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages

**Post message to conversation**  —  `post_message_to_conversation`

Send a message to an existing conversation and get the AI response

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `message` | string | form | yes | The user's message to send to the AI |

**Returns:** `{Object} Hash with id and updated messages array`

## DELETE /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}

**Delete AI conversation**  —  `delete_ai_conversation`

Mark a conversation as completed/deleted

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `{Object} Success message`

## GET /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/evaluation

**Get conversation evaluation**  —  `get_conversation_evaluation`

Fetch evaluation data for a conversation from the llm-conversation service

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `{Object} Hash with evaluation metrics`

## POST /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages/{message_id}/feedback

**Create feedback on a conversation message**  —  `create_feedback_on_conversation_message`

Submit a like or dislike vote on an AI-generated message.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `vote` | string | form | yes | "liked" or "disliked" |
| `message_id` | string | path | yes | llm-conversation message UUID |
| `feedback_message` | string | form |  | optional text for dislike |

**Returns:** `{Object} Hash with feedback record`

## DELETE /v1/courses/{course_id}/ai_experiences/{ai_experience_id}/conversations/{id}/messages/{message_id}/feedback/{feedback_id}

**Delete feedback on a conversation message**  —  `delete_feedback_on_conversation_message`

Remove a previously submitted vote (toggling off like/dislike).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ai_experience_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `message_id` | string | path | yes | ID |
| `feedback_id` | string | path | yes | ID |

**Returns:** `{Object} Success response`
