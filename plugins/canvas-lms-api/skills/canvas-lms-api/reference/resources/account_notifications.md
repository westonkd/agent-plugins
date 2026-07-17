# Account Notifications

> Canvas LMS REST API — `/account_notifications` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/account_notifications

**Index of active global notification for the user**  —  `index_of_active_global_notification_for_user`

Returns a list of all global notifications in the account for the current user
Any notifications that have been closed by the user will not be returned, unless
a include_past parameter is passed in as true. Admins can request all global
notifications for the account by passing in an include_all parameter.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `include_past` | boolean | query |  | Include past and dismissed global announcements. |
| `include_all` | boolean | query |  | Include all global announcements, regardless of user's role or availability date. Only available to account admins. |
| `show_is_closed` | boolean | query |  | Include a flag for each notification indicating whether it has been read by the user. |

**Returns:** `array[AccountNotification]`

## GET /v1/accounts/{account_id}/account_notifications/{id}

**Show a global notification**  —  `show_global_notification`

Returns a global notification for the current user
A notification that has been closed by the user will not be returned

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AccountNotification`

## POST /v1/accounts/{account_id}/account_notifications

**Create a global notification**  —  `create_global_notification`

Create and return a new global notification for an account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `account_notification[subject]` | string | form | yes | The subject of the notification. |
| `account_notification[message]` | string | form | yes | The message body of the notification. |
| `account_notification[start_at]` | DateTime | form | yes | The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z |
| `account_notification[end_at]` | DateTime | form | yes | The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z |
| `account_notification[icon]` | string | form |  | The icon to display with the notification. Note: Defaults to warning. Allowed: `warning`, `information`, `question`, `error`, `calendar` |
| `account_notification_roles` | array[string] | form |  | The role(s) to send global notification to.  Note:  ommitting this field will send to everyone Example:   account_notification_roles: ["StudentEnrollment", "TeacherEnrollment"] |

**Returns:** `void`

## PUT /v1/accounts/{account_id}/account_notifications/{id}

**Update a global notification**  —  `update_global_notification`

Update global notification for an account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `account_notification[subject]` | string | form |  | The subject of the notification. |
| `account_notification[message]` | string | form |  | The message body of the notification. |
| `account_notification[start_at]` | DateTime | form |  | The start date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z |
| `account_notification[end_at]` | DateTime | form |  | The end date and time of the notification in ISO8601 format. e.g. 2014-01-01T01:00Z |
| `account_notification[icon]` | string | form |  | The icon to display with the notification. Allowed: `warning`, `information`, `question`, `error`, `calendar` |
| `account_notification_roles` | array[string] | form |  | The role(s) to send global notification to.  Note:  ommitting this field will send to everyone Example:   account_notification_roles: ["StudentEnrollment", "TeacherEnrollment"] |

**Returns:** `void`

## DELETE /v1/accounts/{account_id}/account_notifications/{id}

**Close notification for user. Destroy notification for admin**  —  `close_notification_for_user_destroy_notification_for_admin`

If the current user no longer wants to see this account notification, it can be closed with this call.
This affects the current user only.

If the current user is an admin and they pass a remove parameter with a value of "true", the account notification
will be destroyed. This affects all users.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `remove` | boolean | query |  | Destroy the account notification. |

**Returns:** `AccountNotification`


---

# Models


## AccountNotification

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `subject` | string |  | The subject of the notifications e.g. `Attention Students` |
| `message` | string |  | The message to be sent in the notification. e.g. `This is a test of the notification system.` |
| `start_at` | datetime |  | When to send out the notification. e.g. `2013-08-28T23:59:00-06:00` |
| `end_at` | datetime |  | When to expire the notification. e.g. `2013-08-29T23:59:00-06:00` |
| `icon` | string |  | The icon to display with the message.  Defaults to warning. e.g. `information` |
| `roles` | array[string] |  | (Deprecated) The roles to send the notification to.  If roles is not passed it defaults to all roles e.g. `['StudentEnrollment']` |
| `role_ids` | array[integer] |  | The roles to send the notification to.  If roles is not passed it defaults to all roles e.g. `[1]` |
| `author` | object |  | The author of the notification. Available only to admins using include_all. e.g. `{'id': 1, 'name': 'John Doe'}` |
