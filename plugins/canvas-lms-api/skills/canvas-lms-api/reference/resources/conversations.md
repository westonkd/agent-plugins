# Conversations

> Canvas LMS REST API — `/conversations` resource. Base path `/api`.

## GET /v1/conversations

**List conversations**  —  `list_conversations`

Returns the paginated list of conversations for the current user, most
recent ones first.

 "uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB", or "course_456".
 For users, you can use either their numeric ID or UUID prefixed with "uuid:".
 Can be an array (by setting "filter[]") or single value (by setting "filter")

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `scope` | string | query |  | When set, only return conversations of the specified type. For example, set to "unread" to return only conversations that haven't been read. The default behavior is to return all non-archived conversations (i.e. read and unread). Allowed: `unread`, `starred`, `archived`, `sent` |
| `filter` | array[string] | query |  | When set, only return conversations for the specified courses, groups or users. The id should be prefixed with its type, e.g. "user_123", |
| `filter_mode` | string | query |  | When filter[] contains multiple filters, combine them with this mode, filtering conversations that at have at least all of the contexts ("and") or at least one of the contexts ("or") Allowed: `and`, `or`, `default or` |
| `interleave_submissions` | boolean | query |  | (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored. |
| `include_all_conversation_ids` | boolean | query |  | Default is false. If true, the top-level element of the response will be an object rather than an array, and will have the keys "conversations" which will contain the paged conversation data, and "conversation_ids" which will contain the ids of all conversations under this scope/filter in the same order. |
| `include` | array[string] | query |  | "participant_avatars":: Optionally include an "avatar_url" key for each user participating in the conversation "uuid":: Optionally include an "uuid" key for each user participating in the conversation Allowed: `participant_avatars`, `uuid` |

**Returns:** `array[Conversation]`

## POST /v1/conversations

**Create a conversation**  —  `create_conversation`

Create a new conversation with one or more recipients. If there is already
an existing private conversation with the given recipients, it will be
reused.

 (either numeric IDs or UUIDs prefixed with "uuid:"),
  or course/group ids prefixed with "course_" or "group_" respectively, e.g.
  recipients[]=1&recipients[]=uuid:W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCBx&recipients[]=course_3.
  If the course/group has over 100 enrollments, 'bulk_message' and 'group_conversation' must be
  set to true.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `recipients` | array[string] | form | yes | An array of recipient ids. These may be user ids |
| `subject` | string | form |  | The subject of the conversation. This is ignored when reusing a conversation. Maximum length is 255 characters. |
| `body` | string | form | yes | The message to be sent |
| `force_new` | boolean | form |  | Forces a new message to be created, even if there is an existing private conversation. |
| `group_conversation` | boolean | form |  | Defaults to false.  When false, individual private conversations will be created with each recipient. If true, this will be a group conversation (i.e. all recipients may see all messages and replies). Must be set true if the number of recipients is over the set maximum (default is 100). |
| `attachment_ids` | array[string] | form |  | An array of attachments ids. These must be files that have been previously uploaded to the sender's "conversation attachments" folder. |
| `media_comment_id` | string | form |  | Media comment id of an audio or video file to be associated with this message. |
| `media_comment_type` | string | form |  | Type of the associated media file Allowed: `audio`, `video` |
| `mode` | string | form |  | Determines whether the messages will be created/sent synchronously or asynchronously. Defaults to sync, and this option is ignored if this is a group conversation or there is just one recipient (i.e. it must be a bulk private message). When sent async, the response will be an empty array (batch status can be queried via the {api:ConversationsController#batches batches API}) Allowed: `sync`, `async` |
| `scope` | string | form |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} Allowed: `unread`, `starred`, `archived` |
| `filter` | array[string] | form |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} |
| `filter_mode` | string | form |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} Allowed: `and`, `or`, `default or` |
| `context_code` | string | form |  | The course or group that is the context for this conversation. Same format as courses or groups in the recipients argument. |
| `include` | array[string] | form |  | "uuid":: Optionally include an "uuid" key for each user participating in the conversation Allowed: `uuid` |

**Returns:** `void`

## GET /v1/conversations/batches

**Get running batches**  —  `get_running_batches`

Returns any currently running conversation batches for the current user.
Conversation batches are created when a bulk private message is sent
asynchronously (see the mode argument to the {api:ConversationsController#create create API action}).

**Returns:** `void`

## GET /v1/conversations/{id}

**Get a single conversation**  —  `get_single_conversation`

Returns information for a single conversation for the current user. Response includes all
fields that are present in the list/index action as well as messages
and extended participant information.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `interleave_submissions` | boolean | query |  | (Obsolete) Submissions are no longer linked to conversations. This parameter is ignored. |
| `scope` | string | query |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} Allowed: `unread`, `starred`, `archived` |
| `filter` | array[string] | query |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} |
| `filter_mode` | string | query |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} Allowed: `and`, `or`, `default or` |
| `auto_mark_as_read` | boolean | query |  | Default true. If true, unread conversations will be automatically marked as read. This will default to false in a future API release, so clients should explicitly send true if that is the desired behavior. |

**Returns:** `void`

## PUT /v1/conversations/{id}

**Edit a conversation**  —  `edit_conversation`

Updates attributes for a single conversation.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `conversation[workflow_state]` | string | form |  | Change the state of this conversation Allowed: `read`, `unread`, `archived` |
| `conversation[subscribed]` | boolean | form |  | Toggle the current user's subscription to the conversation (only valid for group conversations). If unsubscribed, the user will still have access to the latest messages, but the conversation won't be automatically flagged as unread, nor will it jump to the top of the inbox. |
| `conversation[starred]` | boolean | form |  | Toggle the starred state of the current user's view of the conversation. |
| `scope` | string | form |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} Allowed: `unread`, `starred`, `archived` |
| `filter` | array[string] | form |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} |
| `filter_mode` | string | form |  | Used when generating "visible" in the API response. See the explanation under the {api:ConversationsController#index index API action} Allowed: `and`, `or`, `default or` |

**Returns:** `void`

## POST /v1/conversations/mark_all_as_read

**Mark all as read**  —  `mark_all_as_read`

Mark all conversations as read.

**Returns:** `void`

## DELETE /v1/conversations/{id}

**Delete a conversation**  —  `delete_conversation`

Delete this conversation and its messages. Note that this only deletes
this user's view of the conversation.

Response includes same fields as UPDATE action

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/conversations/{id}/add_recipients

**Add recipients**  —  `add_recipients`

Add recipients to an existing group conversation. Response is similar to
the GET/show action, except that only includes the
latest message (e.g. "joe was added to the conversation by bob")

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `recipients` | array[string] | form | yes | An array of recipient ids. These may be user ids or course/group ids prefixed with "course_" or "group_" respectively, e.g. recipients[]=1&recipients[]=2&recipients[]=course_3 |

**Returns:** `void`

## POST /v1/conversations/{id}/add_message

**Add a message**  —  `add_message`

Add a message to an existing conversation. Response is similar to the
GET/show action, except that only includes the
latest message (i.e. what we just sent)

An array of user ids. Defaults to all of the current conversation
recipients. To explicitly send a message to no other recipients,
this array should consist of the logged-in user id.

An array of message ids from this conversation to send to recipients
of the new message. Recipients who already had a copy of included
messages will not be affected.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `body` | string | form | yes | The message to be sent. |
| `attachment_ids` | array[string] | form |  | An array of attachments ids. These must be files that have been previously uploaded to the sender's "conversation attachments" folder. |
| `media_comment_id` | string | form |  | Media comment id of an audio of video file to be associated with this message. |
| `media_comment_type` | string | form |  | Type of the associated media file. Allowed: `audio`, `video` |
| `recipients` | array[string] | form |  | no description |
| `included_messages` | array[string] | form |  | no description |

**Returns:** `void`

## POST /v1/conversations/{id}/remove_messages

**Delete a message**  —  `delete_message`

Delete messages from this conversation. Note that this only affects this
user's view of the conversation. If all messages are deleted, the
conversation will be as well (equivalent to DELETE)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `remove` | array[string] | form | yes | Array of message ids to be deleted |

**Returns:** `void`

## PUT /v1/conversations

**Batch update conversations**  —  `batch_update_conversations`

Perform a change on a set of conversations. Operates asynchronously; use the {api:ProgressController#show progress endpoint}
to query the status of an operation.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `conversation_ids` | array[string] | form | yes | List of conversations to update. Limited to 500 conversations. |
| `event` | string | form | yes | The action to take on each conversation. Allowed: `mark_as_read`, `mark_as_unread`, `star`, `unstar`, `archive`, `destroy` |

**Returns:** `Progress`

## GET /v1/conversations/find_recipients

**Find recipients**  —  `find_recipients`

Deprecated, see the {api:SearchController#recipients Find recipients endpoint} in the Search API

**Returns:** `void`

## GET /v1/conversations/unread_count

**Unread count**  —  `unread_count`

Get the number of unread conversations for the current user

**Returns:** `void`


---

# Models


## Conversation

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | the unique identifier for the conversation. e.g. `2` |
| `subject` | string |  | the subject of the conversation. e.g. `2` |
| `workflow_state` | string |  | The current state of the conversation (read, unread or archived). e.g. `unread` |
| `last_message` | string |  | A <=100 character preview from the most recent message. e.g. `sure thing, here's the file` |
| `start_at` | datetime |  | the date and time at which the last message was sent. e.g. `2011-09-02T12:00:00Z` |
| `message_count` | integer |  | the number of messages in the conversation. e.g. `2` |
| `subscribed` | boolean |  | whether the current user is subscribed to the conversation. e.g. `True` |
| `private` | boolean |  | whether the conversation is private. e.g. `True` |
| `starred` | boolean |  | whether the conversation is starred. e.g. `True` |
| `properties` | array[string] |  | Additional conversation flags (last_author, attachments, media_objects). Each listed property means the flag is set to true (i.e. the current user is the most recent author, there are attachments, or there are media objects) |
| `audience` | array[integer] |  | Array of user ids who are involved in the conversation, ordered by participation level, then alphabetical. Excludes current user, unless this is a monologue. |
| `audience_contexts` | array[string] |  | Most relevant shared contexts (courses and groups) between current user and other participants. If there is only one participant, it will also include that user's enrollment(s)/ membership type(s) in each course/group. |
| `avatar_url` | string |  | URL to appropriate icon for this conversation (custom, individual or group avatar, depending on audience). e.g. `https://canvas.instructure.com/images/messages/avatar-group-50.png` |
| `participants` | array[ConversationParticipant] |  | Array of users participating in the conversation. Includes current user. |
| `visible` | boolean |  | indicates whether the conversation is visible under the current scope and filter. This attribute is always true in the index API response, and is primarily useful in create/update responses so that you can know if the record should be displayed in the UI. The default scope is assumed, unless a scope or filter is passed to the create/update API call. e.g. `True` |
| `context_name` | string |  | Name of the course or group in which the conversation is occurring. e.g. `Canvas 101` |


## ConversationParticipant

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | The user ID for the participant. e.g. `2` |
| `name` | string |  | A short name the user has selected, for use in conversations or other less formal places through the site. e.g. `Shelly` |
| `full_name` | string |  | The full name of the user. e.g. `Sheldon Cooper` |
| `avatar_url` | string |  | If requested, this field will be included and contain a url to retrieve the user's avatar. e.g. `https://canvas.instructure.com/images/messages/avatar-50.png` |
| `uuid` | string |  | The Canvas UUID for the participant. e.g. `W9GQIcdoDTqwX8mxIunDQQVL6WZTaGmpa5xovmCB` |
