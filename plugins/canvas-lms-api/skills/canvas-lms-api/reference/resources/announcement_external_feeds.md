# Announcement External Feeds

> Canvas LMS REST API — `/announcement_external_feeds` resource. Base path `/api`.

## GET /v1/courses/{course_id}/external_feeds

**List external feeds**  —  `list_external_feeds_courses`

Returns the paginated list of External Feeds this course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[ExternalFeed]`

## GET /v1/groups/{group_id}/external_feeds

**List external feeds**  —  `list_external_feeds_groups`

Returns the paginated list of External Feeds this course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[ExternalFeed]`

## POST /v1/courses/{course_id}/external_feeds

**Create an external feed**  —  `create_external_feed_courses`

Create a new external feed for the course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url` | string | form | yes | The url to the external rss or atom feed |
| `header_match` | boolean | form |  | If given, only feed entries that contain this string in their title will be imported |
| `verbosity` | string | form |  | Defaults to "full" Allowed: `full`, `truncate`, `link_only` |

**Returns:** `ExternalFeed`

## POST /v1/groups/{group_id}/external_feeds

**Create an external feed**  —  `create_external_feed_groups`

Create a new external feed for the course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url` | string | form | yes | The url to the external rss or atom feed |
| `header_match` | boolean | form |  | If given, only feed entries that contain this string in their title will be imported |
| `verbosity` | string | form |  | Defaults to "full" Allowed: `full`, `truncate`, `link_only` |

**Returns:** `ExternalFeed`

## DELETE /v1/courses/{course_id}/external_feeds/{external_feed_id}

**Delete an external feed**  —  `delete_external_feed_courses`

Deletes the external feed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `external_feed_id` | string | path | yes | ID |

**Returns:** `ExternalFeed`

## DELETE /v1/groups/{group_id}/external_feeds/{external_feed_id}

**Delete an external feed**  —  `delete_external_feed_groups`

Deletes the external feed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `external_feed_id` | string | path | yes | ID |

**Returns:** `ExternalFeed`


---

# Models


## ExternalFeed

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the feed e.g. `5` |
| `display_name` | string |  | The title of the feed, pulled from the feed itself. If the feed hasn't yet been pulled, a temporary name will be synthesized based on the URL e.g. `My Blog` |
| `url` | string |  | The HTTP/HTTPS URL to the feed e.g. `http://example.com/myblog.rss` |
| `header_match` | string |  | If not null, only feed entries whose title contains this string will trigger new posts in Canvas e.g. `pattern` |
| `created_at` | datetime |  | When this external feed was added to Canvas e.g. `2012-06-01T00:00:00-06:00` |
| `verbosity` | string |  | The verbosity setting determines how much of the feed's content is imported into Canvas as part of the posting. 'link_only' means that only the title and a link to the item. 'truncate' means that a summary of the first portion of the item body will be used. 'full' means that the full item body will be used. e.g. `truncate` |
