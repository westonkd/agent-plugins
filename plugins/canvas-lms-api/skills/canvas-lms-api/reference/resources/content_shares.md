# Content Shares

> Canvas LMS REST API — `/content_shares` resource. Base path `/api`.

## POST /v1/users/{user_id}/content_shares

**Create a content share**  —  `create_content_share`

Share content directly between two or more users

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `receiver_ids` | Array | form | yes | IDs of users to share the content with. |
| `content_type` | string | form | yes | Type of content you are sharing. Allowed: `assignment`, `discussion_topic`, `page`, `quiz`, `module`, `module_item` |
| `content_id` | integer (int64) | form | yes | The id of the content that you are sharing |

**Returns:** `ContentShare`

## GET /v1/users/{user_id}/content_shares/sent

**List content shares**  —  `list_content_shares_sent`

Return a paginated list of content shares a user has sent or received. Use +self+ as the user_id
to retrieve your own content shares. Only linked observers and administrators may view other users'
content shares.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[ContentShare]`

## GET /v1/users/{user_id}/content_shares/received

**List content shares**  —  `list_content_shares_received`

Return a paginated list of content shares a user has sent or received. Use +self+ as the user_id
to retrieve your own content shares. Only linked observers and administrators may view other users'
content shares.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[ContentShare]`

## GET /v1/users/{user_id}/content_shares/unread_count

**Get unread shares count**  —  `get_unread_shares_count`

Return the number of content shares a user has received that have not yet been read. Use +self+ as the user_id
to retrieve your own content shares. Only linked observers and administrators may view other users'
content shares.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `{ "unread_count": "integer" }`

## GET /v1/users/{user_id}/content_shares/{id}

**Get content share**  —  `get_content_share`

Return information about a single content share. You may use +self+ as the user_id to retrieve your own content share.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `ContentShare`

## DELETE /v1/users/{user_id}/content_shares/{id}

**Remove content share**  —  `remove_content_share`

Remove a content share from your list. Use +self+ as the user_id. Note that this endpoint does not delete other users'
copies of the content share.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/users/{user_id}/content_shares/{id}/add_users

**Add users to content share**  —  `add_users_to_content_share`

Send a previously created content share to additional users

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `receiver_ids` | Array | form |  | IDs of users to share the content with. |

**Returns:** `ContentShare`

## PUT /v1/users/{user_id}/content_shares/{id}

**Update a content share**  —  `update_content_share`

Mark a content share read or unread

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `read_state` | string | form |  | Read state for the content share Allowed: `read`, `unread` |

**Returns:** `ContentShare`


---

# Models


## ContentShare

Content shared between users

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The id of the content share for the current user e.g. `1` |
| `name` | string |  | The name of the shared content e.g. `War of 1812 homework` |
| `content_type` | string |  | The type of content that was shared. Can be assignment, discussion_topic, page, quiz, module, or module_item. e.g. `assignment` |
| `created_at` | datetime |  | The datetime the content was shared with this user. e.g. `2017-05-09T10:12:00Z` |
| `updated_at` | datetime |  | The datetime the content was updated. e.g. `2017-05-09T10:12:00Z` |
| `user_id` | integer |  | The id of the user who sent or received the content share. e.g. `1578941` |
| `sender` | object |  | The user who shared the content. This field is provided only to receivers; it is not populated in the sender's list of sent content shares. e.g. `{'id': 1, 'display_name': 'Matilda Vargas', 'avatar_image_url': 'http://localhost:3000/image_url', 'html_url': 'http://localhost:3000/users/1'}` |
| `receivers` | array[object] |  | An Array of users the content is shared with.  This field is provided only to senders; an empty array will be returned for the receiving users. e.g. `[{'id': 1, 'display_name': 'Jon Snow', 'avatar_image_url': 'http://localhost:3000/image_url2', 'html_url': 'http://localhost:3000/users/2'}]` |
| `source_course` | object |  | The course the content was originally shared from. e.g. `{'id': 787, 'name': 'History 105'}` |
| `read_state` | string |  | Whether the recipient has viewed the content share. e.g. `read` |
| `content_export` | ContentExport |  | The content export record associated with this content share e.g. `{'id': 42}` |
