# Discovery Pages

> Canvas LMS REST API — `/discovery_pages` resource. Base path `/api`.

## GET /v1/discovery_pages

**Get Discovery Page**  —  `get_discovery_page`

Get the discovery page configuration for the domain root account.

**Returns:** `DiscoveryPage`

## PUT /v1/discovery_pages

**Update Discovery Page**  —  `update_discovery_page`

Update or create the discovery page configuration for the domain root account.
This is a full replacement - provide the complete configuration including
primary, secondary, and active fields. Any fields omitted will be removed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `discovery_page[primary][authentication_provider_id]` | array[integer] | form | yes | The ID of an active authentication provider for this account. |
| `discovery_page[primary][label]` | array[string] | form | yes | The display label for this authentication provider button. |
| `discovery_page[primary][icon]` | array[string] | form |  | Icon key for this authentication provider button. |
| `discovery_page[secondary][authentication_provider_id]` | array[integer] | form | yes | The ID of an active authentication provider for this account. |
| `discovery_page[secondary][label]` | array[string] | form | yes | The display label for this authentication provider button. |
| `discovery_page[secondary][icon]` | array[string] | form |  | Icon key for this authentication provider button. |
| `discovery_page[active]` | boolean | form |  | Whether the discovery page is enabled. Defaults to false if not provided. |

**Returns:** `DiscoveryPage`

## POST /v1/discovery_pages/token

**Generate Discovery Page Preview Token**  —  `generate_discovery_page_preview_token`

Returns a short-lived RS256-signed JWT containing the discovery page
button link configuration, suitable for sending to the identity service
preview iframe via postMessage.

A discovery_page configuration must be provided in the request body.
Omitting it returns a 400 Bad Request.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `discovery_page[primary][authentication_provider_id]` | array[integer] | form | yes | The ID of an active authentication provider for this account. |
| `discovery_page[primary][label]` | array[string] | form |  | The display label for this authentication provider button. |
| `discovery_page[primary][icon]` | array[string] | form |  | Icon key for this authentication provider button. |
| `discovery_page[secondary][authentication_provider_id]` | array[integer] | form |  | The ID of an active authentication provider for this account. |
| `discovery_page[secondary][label]` | array[string] | form |  | The display label for this authentication provider button. |
| `discovery_page[secondary][icon]` | array[string] | form |  | Icon key for this authentication provider button. |

**Returns:** `{ "token": "eyJ..." }`


---

# Models


## DiscoveryPage

Configuration for the login discovery page

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `primary` | array[DiscoveryPageEntry] |  | Primary authentication provider buttons displayed prominently |
| `secondary` | array[DiscoveryPageEntry] |  | Secondary authentication provider buttons displayed less prominently |
| `active` | boolean |  | Whether the discovery page is enabled |


## DiscoveryPageEntry

A single authentication provider entry on the discovery page

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `authentication_provider_id` | integer |  | The ID of the authentication provider e.g. `1` |
| `label` | string |  | The display label for this provider button e.g. `Students` |
| `icon` | string |  | Icon key for this provider button e.g. `google` Allowed: `apple`, `auth0`, `classlink`, `default`, `facebook`, `github`, `google`, `linkedin`, `microsoft`, `okta`, `onelogin`, `ping` |
