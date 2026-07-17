# PollChoices

> Canvas LMS REST API — `/poll_choices` resource. Base path `/api`.

## GET /v1/polls/{poll_id}/poll_choices

**List poll choices in a poll**  —  `list_poll_choices_in_poll`

Returns the paginated list of PollChoices in this poll.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/polls/{poll_id}/poll_choices/{id}

**Get a single poll choice**  —  `get_single_poll_choice`

Returns the poll choice with the given id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/polls/{poll_id}/poll_choices

**Create a single poll choice**  —  `create_single_poll_choice`

Create a new poll choice for this poll

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `poll_choices[text]` | array[string] | form | yes | The descriptive text of the poll choice. |
| `poll_choices[is_correct]` | array[boolean] | form |  | Whether this poll choice is considered correct or not. Defaults to false. |
| `poll_choices[position]` | array[integer] | form |  | The order this poll choice should be returned in the context it's sibling poll choices. |

**Returns:** `void`

## PUT /v1/polls/{poll_id}/poll_choices/{id}

**Update a single poll choice**  —  `update_single_poll_choice`

Update an existing poll choice for this poll

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `poll_choices[text]` | array[string] | form | yes | The descriptive text of the poll choice. |
| `poll_choices[is_correct]` | array[boolean] | form |  | Whether this poll choice is considered correct or not.  Defaults to false. |
| `poll_choices[position]` | array[integer] | form |  | The order this poll choice should be returned in the context it's sibling poll choices. |

**Returns:** `void`

## DELETE /v1/polls/{poll_id}/poll_choices/{id}

**Delete a poll choice**  —  `delete_poll_choice`

<b>204 No Content</b> response code is returned if the deletion was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `poll_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## PollChoice

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer | yes | The unique identifier for the poll choice. e.g. `1023` |
| `poll_id` | integer | yes | The id of the poll this poll choice belongs to. e.g. `1779` |
| `is_correct` | boolean |  | Specifies whether or not this poll choice is a 'correct' choice. e.g. `true` |
| `text` | string | yes | The text of the poll choice. e.g. `Choice A` |
| `position` | integer |  | The order of the poll choice in relation to it's sibling poll choices. e.g. `1` |
