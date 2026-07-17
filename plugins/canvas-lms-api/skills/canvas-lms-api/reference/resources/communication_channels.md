# Communication Channels

> Canvas LMS REST API — `/communication_channels` resource. Base path `/api`.

## GET /v1/users/{user_id}/communication_channels

**List user communication channels**  —  `list_user_communication_channels`

Returns a paginated list of communication channels for the specified user,
sorted by position.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[CommunicationChannel]`

## POST /v1/users/{user_id}/communication_channels

**Create a communication channel**  —  `create_communication_channel`

Creates a new communication channel for the specified user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `communication_channel[address]` | string | form | yes | An email address or SMS number. Not required for "push" type channels. |
| `communication_channel[type]` | string | form | yes | The type of communication channel.  In order to enable push notification support, the server must be properly configured (via `sns_creds` in Vault) to communicate with Amazon Simple Notification Services, and the developer key used to create the access token from this request must have an SNS ARN configured on it. Allowed: `email`, `sms`, `push` |
| `communication_channel[token]` | string | form |  | A registration id, device token, or equivalent token given to an app when registering with a push notification provider. Only valid for "push" type channels. |
| `skip_confirmation` | boolean | form |  | Only valid for site admins and account admins making requests; If true, the channel is automatically validated and no confirmation email or SMS is sent. Otherwise, the user must respond to a confirmation message to confirm the channel. |

**Returns:** `CommunicationChannel`

## DELETE /v1/users/{user_id}/communication_channels/{id}

**Delete a communication channel**  —  `delete_communication_channel_id`

Delete an existing communication channel.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `CommunicationChannel`

## DELETE /v1/users/{user_id}/communication_channels/{type}/{address}

**Delete a communication channel**  —  `delete_communication_channel_type`

Delete an existing communication channel.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `type` | string | path | yes | ID |
| `address` | string | path | yes | ID |

**Returns:** `CommunicationChannel`

## DELETE /v1/users/self/communication_channels/push

**Delete a push notification endpoint**  —  `delete_push_notification_endpoint`

**Returns:** `{success: true}`


---

# Models


## CommunicationChannel

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the communication channel. e.g. `16` |
| `address` | string |  | The address, or path, of the communication channel. e.g. `sheldon@caltech.example.com` |
| `type` | string |  | The type of communcation channel being described. Possible values are: 'email', 'push', 'sms'. This field determines the type of value seen in 'address'. e.g. `email` |
| `position` | integer |  | The position of this communication channel relative to the user's other channels when they are ordered. e.g. `1` |
| `user_id` | integer |  | The ID of the user that owns this communication channel. e.g. `1` |
| `bounce_count` | integer |  | The number of bounces the channel has experienced. This is reset if the channel sends successfully. e.g. `0` |
| `last_bounce_at` | datetime |  | The time the last bounce occurred. e.g. `2012-05-30T17:00:00Z` |
| `workflow_state` | string |  | The current state of the communication channel. Possible values are: 'unconfirmed' or 'active'. e.g. `active` |
