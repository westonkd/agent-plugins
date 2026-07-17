# AI Experiences

> Canvas LMS REST API — `/ai_experiences` resource. Base path `/api`.

## GET /v1/courses/{course_id}/ai_experiences

**List AI experiences**  —  `list_ai_experiences`

Retrieve the paginated list of AI experiences for a course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `workflow_state` | string | query |  | Only return experiences with the specified workflow state. Allowed values: published, unpublished, deleted |

**Returns:** `array[AiExperience]`

## GET /v1/courses/{course_id}/ai_experiences/{id}

**Show an AI experience**  —  `show_ai_experience`

Retrieve an AI experience by ID

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AiExperience`

## GET /v1/courses/{course_id}/ai_experiences/new

**Show new AI experience form**  —  `show_new_ai_experience_form`

Display the form for creating a new AI experience

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/ai_experiences/{id}/edit

**Show edit AI experience form**  —  `show_edit_ai_experience_form`

Display the form for editing an existing AI experience

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/ai_experiences

**Create an AI experience**  —  `create_ai_experience`

Create a new AI experience for the specified course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `title` | string | form | yes | The title of the AI experience. |
| `description` | string | form |  | The description of the AI experience. |
| `facts` | string | form |  | The AI facts for the experience. |
| `learning_objective` | string | form | yes | The learning objectives for this experience. |
| `pedagogical_guidance` | string | form | yes | The pedagogical guidance for the experience. |
| `workflow_state` | string | form |  | The initial state of the experience. Defaults to 'unpublished'. Allowed values: published, unpublished |

**Returns:** `AiExperience`

## PUT /v1/courses/{course_id}/ai_experiences/{id}

**Update an AI experience**  —  `update_ai_experience`

Update an existing AI experience

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `title` | string | form |  | The title of the AI experience. |
| `description` | string | form |  | The description of the AI experience. |
| `facts` | string | form |  | The AI facts for the experience. |
| `learning_objective` | string | form | yes | The learning objectives for this experience. |
| `pedagogical_guidance` | string | form | yes | The pedagogical guidance for the experience. |
| `workflow_state` | string | form |  | The state of the experience. Allowed values: published, unpublished |

**Returns:** `AiExperience`

## DELETE /v1/courses/{course_id}/ai_experiences/{id}

**Delete an AI experience**  —  `delete_ai_experience`

Delete an AI experience (soft delete - marks as deleted)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AiExperience`

## GET /v1/courses/{course_id}/ai_experiences/{id}/ai_conversations

**List student AI conversations**  —  `list_student_ai_conversations`

Retrieve the latest AI conversation for each student in the course for this AI experience.
Only available to teachers and course managers.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array[AiConversation]`

## GET /v1/courses/{course_id}/ai_experiences/{id}/ai_conversations/{conversation_id}

**Show student AI conversation**  —  `show_student_ai_conversation`

Retrieve a specific student's AI conversation with full message history.
Only available to teachers and course managers.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `conversation_id` | string | path | yes | ID |

**Returns:** `AiConversation`


---

# Models


## AiExperience

An AI Experience for interactive learning

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the AI experience e.g. `234` |
| `title` | string |  | The title for the AI experience e.g. `Customer Service Simulation` |
| `description` | string |  | The description of the AI experience e.g. `Practice customer service skills in a simulated environment` |
| `facts` | string |  | The AI facts for the experience (optional) e.g. `You are a customer service representative...` |
| `learning_objective` | string |  | The learning objectives for this experience e.g. `Students will practice active listening and problem-solving` |
| `pedagogical_guidance` | string |  | The pedagogical guidance for the experience e.g. `A customer is calling about a billing issue` |
| `workflow_state` | string |  | The current published state of the AI experience e.g. `published` |
| `course_id` | integer |  | The course this experience belongs to e.g. `1578941` |
