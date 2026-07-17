# Webhooks Subscriptions for Plagiarism Platform

> Canvas LMS REST API — `/webhooks_subscriptions_for_plagiarism_platform` resource. Base path `/api`.

## POST /lti/subscriptions

**Create a Webhook Subscription**  —  `create_webhook_subscription`

Creates a webook subscription for the specified event type and
context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `subscription[ContextId]` | string | form | yes | The id of the context for the subscription. |
| `subscription[ContextType]` | string | form | yes | The type of context for the subscription. Must be 'assignment', 'account', or 'course'. |
| `subscription[EventTypes]` | Array | form | yes | Array of strings representing the event types for the subscription. |
| `subscription[Format]` | string | form | yes | Format to deliver the live events. Must be 'live-event' or 'caliper'. |
| `subscription[TransportMetadata]` | Object | form | yes | An object with a single key: 'Url'. Example: { "Url": "sqs.example" } |
| `subscription[TransportType]` | string | form | yes | Must be either 'sqs' or 'https'. |

**Returns:** `void`

## DELETE /lti/subscriptions/{id}

**Delete a Webhook Subscription**  —  `delete_webhook_subscription`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /lti/subscriptions/{id}

**Show a single Webhook Subscription**  —  `show_single_webhook_subscription`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## PUT /lti/subscriptions/{id}

**Update a Webhook Subscription**  —  `update_webhook_subscription`

This endpoint uses the same parameters as the create endpoint

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /lti/subscriptions

**List all Webhook Subscription for a tool proxy**  —  `list_all_webhook_subscription_for_tool_proxy`

This endpoint returns a paginated list with a default limit of 100 items per result set.
You can retrieve the next result set by setting a 'StartKey' header in your next request
with the value of the 'EndKey' header in the response.

Example use of a 'StartKey' header object:
  { "Id":"71d6dfba-0547-477d-b41d-db8cb528c6d1","DeveloperKey":"10000000000001" }

**Returns:** `void`
