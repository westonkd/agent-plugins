# CommMessages

> Canvas LMS REST API — `/comm_messages` resource. Base path `/api`.

## GET /v1/comm_messages

**List of CommMessages for a user**  —  `list_of_commmessages_for_user`

Retrieve a paginated list of messages sent to a user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | query | yes | The user id for whom you want to retrieve CommMessages |
| `start_time` | DateTime | query |  | The beginning of the time range you want to retrieve message from. Up to a year prior to the current date is available. |
| `end_time` | DateTime | query |  | The end of the time range you want to retrieve messages for. Up to a year prior to the current date is available. |

**Returns:** `array[CommMessage]`


---

# Models


## CommMessage

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the CommMessage. e.g. `42` |
| `created_at` | datetime |  | The date and time this message was created e.g. `2013-03-19T21:00:00Z` |
| `sent_at` | datetime |  | The date and time this message was sent e.g. `2013-03-20T22:42:00Z` |
| `workflow_state` | string |  | The workflow state of the message. Possible values: 'created' : The message has been created, but not yet processed. 'staged' : The message is queued for sending. 'sending' : The message is being sent currently. 'sent' : The message has been successfully sent. 'bounced' : An error occurred during the sending of the message.'dashboard' : The message has been sent to the dashboard. 'closed' :  The message has been sent and closed, typically for dashboard messages or messages sent to deleted users. 'cancelled' : The message was cancelled before it could be sent. e.g. `sent` |
| `from` | string |  | The address that was put in the 'from' field of the message e.g. `notifications@example.com` |
| `from_name` | string |  | The display name for the from address e.g. `Instructure Canvas` |
| `to` | string |  | The address the message was sent to: e.g. `someone@example.com` |
| `reply_to` | string |  | The reply_to header of the message e.g. `notifications+specialdata@example.com` |
| `subject` | string |  | The message subject e.g. `example subject line` |
| `body` | string |  | The plain text body of the message e.g. `This is the body of the message` |
| `html_body` | string |  | The HTML body of the message. e.g. `<html><body>This is the body of the message</body></html>` |
