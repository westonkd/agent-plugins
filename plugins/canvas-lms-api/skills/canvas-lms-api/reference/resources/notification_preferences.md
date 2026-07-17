# Notification Preferences

> Canvas LMS REST API — `/notification_preferences` resource. Base path `/api`.

## GET /v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences

**List preferences**  —  `list_preferences_communication_channel_id`

Fetch all preferences for the given communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `communication_channel_id` | string | path | yes | ID |

**Returns:** `array[NotificationPreference]`

## GET /v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences

**List preferences**  —  `list_preferences_type`

Fetch all preferences for the given communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `type` | string | path | yes | ID |
| `address` | string | path | yes | ID |

**Returns:** `array[NotificationPreference]`

## GET /v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories

**List of preference categories**  —  `list_of_preference_categories`

Fetch all notification preference categories for the given communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `communication_channel_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences/{notification}

**Get a preference**  —  `get_preference_communication_channel_id`

Fetch the preference for the given notification for the given communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `communication_channel_id` | string | path | yes | ID |
| `notification` | string | path | yes | ID |

**Returns:** `NotificationPreference`

## GET /v1/users/{user_id}/communication_channels/{type}/{address}/notification_preferences/{notification}

**Get a preference**  —  `get_preference_type`

Fetch the preference for the given notification for the given communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `type` | string | path | yes | ID |
| `address` | string | path | yes | ID |
| `notification` | string | path | yes | ID |

**Returns:** `NotificationPreference`

## PUT /v1/users/self/communication_channels/{communication_channel_id}/notification_preferences/{notification}

**Update a preference**  —  `update_preference_communication_channel_id`

Change the preference for a single notification for a single communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `communication_channel_id` | string | path | yes | ID |
| `notification` | string | path | yes | ID |
| `notification_preferences[frequency]` | string | form | yes | The desired frequency for this notification |

**Returns:** `void`

## PUT /v1/users/self/communication_channels/{type}/{address}/notification_preferences/{notification}

**Update a preference**  —  `update_preference_type`

Change the preference for a single notification for a single communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `type` | string | path | yes | ID |
| `address` | string | path | yes | ID |
| `notification` | string | path | yes | ID |
| `notification_preferences[frequency]` | string | form | yes | The desired frequency for this notification |

**Returns:** `void`

## PUT /v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category}

**Update preferences by category**  —  `update_preferences_by_category`

Change the preferences for multiple notifications based on the category for a single communication channel

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `communication_channel_id` | string | path | yes | ID |
| `category` | string | path | yes | The name of the category. Must be parameterized (e.g. The category "Course Content" should be "course_content") |
| `notification_preferences[frequency]` | string | form | yes | The desired frequency for each notification in the category |

**Returns:** `void`

## PUT /v1/users/self/communication_channels/{communication_channel_id}/notification_preferences

**Update multiple preferences**  —  `update_multiple_preferences_communication_channel_id`

Change the preferences for multiple notifications for a single communication channel at once

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `communication_channel_id` | string | path | yes | ID |
| `notification_preferences[<X>][frequency]` | string | form | yes | The desired frequency for <X> notification |

**Returns:** `void`

## PUT /v1/users/self/communication_channels/{type}/{address}/notification_preferences

**Update multiple preferences**  —  `update_multiple_preferences_type`

Change the preferences for multiple notifications for a single communication channel at once

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `type` | string | path | yes | ID |
| `address` | string | path | yes | ID |
| `notification_preferences[<X>][frequency]` | string | form | yes | The desired frequency for <X> notification |

**Returns:** `void`


---

# Models


## NotificationPreference

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `href` | string |  | e.g. `https://canvas.instructure.com/users/1/communication_channels/email/student@example.edu/notification_preferences/new_announcement` |
| `notification` | string |  | The notification this preference belongs to e.g. `new_announcement` |
| `category` | string |  | The category of that notification e.g. `announcement` |
| `frequency` | string |  | How often to send notifications to this communication channel for the given notification. Possible values are 'immediately', 'daily', 'weekly', and 'never' e.g. `daily` |
