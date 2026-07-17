# Data Services

> Canvas LMS REST API — `/data_services` resource. Base path `/api`.

## POST /lti/accounts/{account_id}/data_services

**Create a Data Services Event Subscription**  —  `create_data_services_event_subscription`

Creates a Data Service Event subscription for the specified event type and
context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `subscription[ContextId]` | string | form | yes | The id of the context for the subscription. |
| `subscription[ContextType]` | string | form | yes | The type of context for the subscription. Must be 'assignment', 'account', or 'course'. |
| `subscription[EventTypes]` | Array | form | yes | Array of strings representing the event types for the subscription. |
| `subscription[Format]` | string | form | yes | Format to deliver the live events. Must be 'live-event' or 'caliper'. |
| `subscription[TransportMetadata]` | Object | form | yes | An object with a single key: 'Url'. Example: { "Url": "sqs.example" } |
| `subscription[TransportType]` | string | form | yes | Must be either 'sqs' or 'https'. |
| `subscription[OwnerId]` | string | form |  | The globalId of the user making the subscription. If not present, will default to the tool id. The user will be validated to exist on account and have the data_services permission, otherwise will throw a 422 error. |

**Returns:** `DataServiceSubscription`

## PUT /lti/accounts/{account_id}/data_services/{id}

**Update a Data Services Event Subscription**  —  `update_data_services_event_subscription`

Updates a Data Service Event subscription for the specified event type and
context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `subscription[ContextId]` | string | form |  | The id of the context for the subscription. |
| `subscription[ContextType]` | string | form |  | The type of context for the subscription. Must be 'assignment', 'account', or 'course'. |
| `subscription[EventTypes]` | Array | form |  | Array of strings representing the event types for the subscription. |
| `subscription[Format]` | string | form |  | Format to deliver the live events. Must be 'live-event' or 'caliper'. |
| `subscription[TransportMetadata]` | Object | form |  | An object with a single key: 'Url'. Example: { "Url": "sqs.example" } |
| `subscription[TransportType]` | string | form |  | Must be either 'sqs' or 'https'. |
| `subscription[State]` | string | form |  | Must be either 'Active' or 'Deleted" |
| `subscription[UpdatedBy]` | string | form |  | The globalId of the user updating the subscription. If not present, will default to the tool id. The user will be validated to exist on account and have the data_services permission, otherwise will throw a 422 error. |

**Returns:** `DataServiceSubscription`

## GET /lti/accounts/{account_id}/data_services/{id}

**Show a Data Services Event Subscription**  —  `show_data_services_event_subscription`

Show existing Data Services Event Subscription

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `DataServiceSubscription`

## GET /lti/accounts/{account_id}/data_services

**List all Data Services Event Subscriptions**  —  `list_all_data_services_event_subscriptions`

This endpoint returns a paginated list with a default limit of 100 items per result set.
You can retrieve the next result set by setting a 'StartKey' header in your next request
with the value of the 'EndKey' header in the response.

Note that this will return all active subscription and the last 90 days of deleted subscriptions.
It does not include subscriptions with an owner type of 'external_tool' or 'internal_service'.

Example use of a 'StartKey' header object:
  { "Id":"71d6dfba-0547-477d-b41d-db8cb528c6d1","OwnerId":"domain.instructure.com" }

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `DataServiceSubscription`

## DELETE /lti/accounts/{account_id}/data_services/{id}

**Destroy a Data Services Event Subscription**  —  `destroy_data_services_event_subscription`

Destroy existing Data Services Event Subscription

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `DataServiceSubscription`


---

# Models


## DataServiceSubscription

A subscription to a data service live event.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `ContextId` | string |  | The id of the context for the subscription. e.g. `8ADadf-asdfas-asdfas-asdfaew` |
| `ContextType` | string |  | The type of context for the subscription. Must be 'assignment', or 'root_account' e.g. `root_account` |
| `EventTypes` | array[string] |  | Array of strings representing the event types for the subscription. e.g. `['asset_accessed']` |
| `Format` | string |  | Format to deliver the live events. Must be 'live-event' or 'caliper'. e.g. `caliper` |
| `TransportMetadata` | string |  | An object with a single key: 'Url'. e.g. `{ 	"Url":"sqs.example"}` |
| `TransportType` | string |  | The type of transport for the event. Must be either 'sqs' or 'https'. e.g. `sqs` |
