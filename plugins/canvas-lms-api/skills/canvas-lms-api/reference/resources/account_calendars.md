# Account Calendars

> Canvas LMS REST API — `/account_calendars` resource. Base path `/api`.

## GET /v1/account_calendars

**List available account calendars**  —  `list_available_account_calendars`

Returns a paginated list of account calendars available to the current user.
Includes visible account calendars where the user has an account association.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `search_term` | string | query |  | When included, searches available account calendars for the term. Returns matching results. Term must be at least 2 characters. |

**Returns:** `array[{ "account_calendars": AccountCalendar, "total_results": "integer"}]`

## GET /v1/account_calendars/{account_id}

**Get a single account calendar**  —  `get_single_account_calendar`

Get details about a specific account calendar.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `AccountCalendar`

## PUT /v1/account_calendars/{account_id}

**Update a calendar**  —  `update_calendar`

Set an account calendar's visibility and auto_subscribe values. Requires the
`manage_account_calendar_visibility` permission on the account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `visible` | boolean | form |  | Allow administrators with `manage_account_calendar_events` permission to create events on this calendar, and allow users to view this calendar and its events. |
| `auto_subscribe` | boolean | form |  | When true, users will automatically see events from this account in their calendar, even if they haven't manually added that calendar. |

**Returns:** `AccountCalendar`

## PUT /v1/accounts/{account_id}/account_calendars

**Update several calendars**  —  `update_several_calendars`

Set visibility and/or auto_subscribe on many calendars simultaneously. Requires
the `manage_account_calendar_visibility` permission on the account.

Accepts a JSON array of objects containing 2-3 keys each: `id`
(the account's id, required), `visible` (a boolean indicating whether
the account calendar is visible), and `auto_subscribe` (a boolean indicating
whether users should see these events in their calendar without manually
subscribing).

Returns the count of updated accounts.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/accounts/{account_id}/account_calendars

**List all account calendars**  —  `list_all_account_calendars`

Returns a paginated list of account calendars for the provided account and
its first level of sub-accounts. Includes hidden calendars in the response.
Requires the `manage_account_calendar_visibility` permission.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `search_term` | string | query |  | When included, searches all descendent accounts of provided account for the term. Returns matching results. Term must be at least 2 characters. Can be combined with a filter value. |
| `filter` | string | query |  | When included, only returns calendars that are either visible or hidden. Can be combined with a search term. Allowed: `visible`, `hidden` |

**Returns:** `array[AccountCalendar]`

## GET /v1/accounts/{account_id}/visible_calendars_count

**Count of all visible account calendars**  —  `count_of_all_visible_account_calendars`

Returns the number of visible account calendars.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `{ "count": "integer" }`


---

# Models


## AccountCalendar

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the account associated with this calendar e.g. `204` |
| `name` | string |  | the name of the account associated with this calendar e.g. `Department of Chemistry` |
| `parent_account_id` | integer |  | the account's parent ID, or null if this is the root account e.g. `1` |
| `root_account_id` | integer |  | the ID of the root account, or null if this is the root account e.g. `1` |
| `visible` | boolean |  | whether this calendar is visible to users e.g. `True` |
| `auto_subscribe` | boolean |  | whether users see this calendar's events without needing to manually add it e.g. `False` |
| `sub_account_count` | integer |  | number of this account's direct sub-accounts e.g. `0` |
| `asset_string` | string |  | Asset string of the account e.g. `account_4` |
| `type` | string |  | Object type e.g. `account` |
| `calendar_event_url` | string |  | url to get full detailed events e.g. `/accounts/2/calendar_events/%7B%7B%20id%20%7D%7D` |
| `can_create_calendar_events` | boolean |  | whether the user can create calendar events e.g. `True` |
| `create_calendar_event_url` | string |  | API path to create events for the account e.g. `/accounts/2/calendar_events` |
| `new_calendar_event_url` | string |  | url to open the more options event editor e.g. `/accounts/6/calendar_events/new` |
