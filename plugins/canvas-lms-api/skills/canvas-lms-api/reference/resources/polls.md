# Polls

> Canvas LMS REST API — `/polls` resource. Base path `/api`.

## GET /v1/polls

**List polls**  —  `list_polls`

Returns the paginated list of polls for the current user.

**Returns:** `void`

## GET /v1/polls/{id}

**Get a single poll**  —  `get_single_poll`

Returns the poll with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/polls

**Create a single poll**  —  `create_single_poll`

Create a new poll for the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `polls[question]` | array[string] | form | yes | The title of the poll. |
| `polls[description]` | array[string] | form |  | A brief description or instructions for the poll. |

**Returns:** `void`

## PUT /v1/polls/{id}

**Update a single poll**  —  `update_single_poll`

Update an existing poll belonging to the current user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `polls[question]` | array[string] | form | yes | The title of the poll. |
| `polls[description]` | array[string] | form |  | A brief description or instructions for the poll. |

**Returns:** `void`

## DELETE /v1/polls/{id}

**Delete a poll**  —  `delete_poll`

<b>204 No Content</b> response code is returned if the deletion was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## Poll

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer | yes | The unique identifier for the poll. e.g. `1023` |
| `question` | string | yes | The question/title of the poll. e.g. `What do you consider most important to your learning in this course?` |
| `description` | string |  | A short description of the poll. e.g. `This poll is to determine what priorities the students in the course have.` |
| `created_at` | string (date-time) |  | The time at which the poll was created. e.g. `2014-01-07T15:16:18Z` |
| `user_id` | integer |  | The unique identifier for the user that created the poll. e.g. `105` |
| `total_results` | object |  | An aggregate of the results of all associated poll sessions, with the poll choice id as the key, and the aggregated submission count as the value. e.g. `{'543': 20, '544': 5, '545': 17}` |
