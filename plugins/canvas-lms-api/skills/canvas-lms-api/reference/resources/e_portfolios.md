# ePortfolios

> Canvas LMS REST API — `/e_portfolios` resource. Base path `/api`.

## GET /v1/users/{user_id}/eportfolios

**Get all ePortfolios for a User**  —  `get_all_eportfolios_for_user`

Get a list of all ePortfolios for the specified user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | deleted:: Include deleted ePortfolios. Only available to admins who can moderate_user_content. Allowed: `deleted` |

**Returns:** `array[ePortfolio]`

## GET /v1/eportfolios/{id}

**Get an ePortfolio**  —  `get_eportfolio`

Get details for a single ePortfolio.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `ePortfolio`

## DELETE /v1/eportfolios/{id}

**Delete an ePortfolio**  —  `delete_eportfolio`

Mark an ePortfolio as deleted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `ePortfolio`

## GET /v1/eportfolios/{eportfolio_id}/pages

**Get ePortfolio Pages**  —  `get_eportfolio_pages`

Get details for the pages of an ePortfolio

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `eportfolio_id` | string | path | yes | ID |

**Returns:** `array[ePortfolioPage]`

## PUT /v1/eportfolios/{eportfolio_id}/moderate

**Moderate an ePortfolio**  —  `moderate_eportfolio`

Update the spam_status of an eportfolio. Only available to admins who can
moderate_user_content.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `eportfolio_id` | string | path | yes | ID |
| `spam_status` | string | form |  | The spam status for the ePortfolio Allowed: `marked_as_spam`, `marked_as_safe` |

**Returns:** `ePortfolio`

## PUT /v1/users/{user_id}/eportfolios

**Moderate all ePortfolios for a User**  —  `moderate_all_eportfolios_for_user`

Update the spam_status for all active eportfolios of a user. Only available to
admins who can moderate_user_content.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `spam_status` | string | form |  | The spam status for all the ePortfolios Allowed: `marked_as_spam`, `marked_as_safe` |

**Returns:** `void`

## PUT /v1/eportfolios/{eportfolio_id}/restore

**Restore a deleted ePortfolio**  —  `restore_deleted_eportfolio`

Restore an ePortfolio back to active that was previously deleted. Only
available to admins who can moderate_user_content.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `eportfolio_id` | string | path | yes | ID |

**Returns:** `ePortfolio`


---

# Models


## ePortfolio

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The database ID of the ePortfolio e.g. `1` |
| `user_id` | integer |  | The user ID to which the ePortfolio belongs e.g. `1` |
| `name` | string |  | The name of the ePortfolio e.g. `My Academic Journey` |
| `public` | boolean |  | Whether or not the ePortfolio is visible without authentication e.g. `True` |
| `created_at` | datetime |  | The creation timestamp for the ePortfolio e.g. `2021-09-20T18:59:37Z` |
| `updated_at` | datetime |  | The timestamp of the last time any of the ePortfolio attributes changed e.g. `2021-09-20T18:59:37Z` |
| `workflow_state` | string |  | The state of the ePortfolio. Either 'active' or 'deleted' e.g. `active` |
| `deleted_at` | datetime |  | The timestamp when the ePortfolio was deleted, or else null e.g. `2021-09-20T18:59:37Z` |
| `spam_status` | string |  | A flag indicating whether the ePortfolio has been       flagged or moderated as spam. One of 'flagged_as_possible_spam',       'marked_as_safe', 'marked_as_spam', or null |


## ePortfolioPage

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The database ID of the ePortfolio e.g. `1` |
| `eportfolio_id` | integer |  | The ePortfolio ID to which the entry belongs e.g. `1` |
| `position` | integer |  | The positional order of the entry in the list e.g. `1` |
| `name` | string |  | The name of the ePortfolio e.g. `My Academic Journey` |
| `content` | string |  | The user entered content of the entry e.g. `A long time ago...` |
| `created_at` | datetime |  | The creation timestamp for the ePortfolio e.g. `2021-09-20T18:59:37Z` |
| `updated_at` | datetime |  | The timestamp of the last time any of the ePortfolio attributes changed e.g. `2021-09-20T18:59:37Z` |
