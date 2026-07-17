# Bookmarks

> Canvas LMS REST API — `/bookmarks` resource. Base path `/api`.

## GET /v1/users/self/bookmarks

**List bookmarks**  —  `list_bookmarks`

Returns the paginated list of bookmarks.

**Returns:** `array[Bookmark]`

## POST /v1/users/self/bookmarks

**Create bookmark**  —  `create_bookmark`

Creates a bookmark.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `name` | string | form |  | The name of the bookmark |
| `url` | string | form |  | The url of the bookmark |
| `position` | integer (int64) | form |  | The position of the bookmark. Defaults to the bottom. |
| `data` | string | form |  | The data associated with the bookmark |

**Returns:** `Bookmark`

## GET /v1/users/self/bookmarks/{id}

**Get bookmark**  —  `get_bookmark`

Returns the details for a bookmark.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `Bookmark`

## PUT /v1/users/self/bookmarks/{id}

**Update bookmark**  —  `update_bookmark`

Updates a bookmark

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `name` | string | form |  | The name of the bookmark |
| `url` | string | form |  | The url of the bookmark |
| `position` | integer (int64) | form |  | The position of the bookmark. Defaults to the bottom. |
| `data` | string | form |  | The data associated with the bookmark |

**Returns:** `Folder`

## DELETE /v1/users/self/bookmarks/{id}

**Delete bookmark**  —  `delete_bookmark`

Deletes a bookmark

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## Bookmark

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | e.g. `1` |
| `name` | string |  | e.g. `Biology 101` |
| `url` | string |  | e.g. `/courses/1` |
| `position` | integer |  | e.g. `1` |
| `data` | object |  | e.g. `{'active_tab': 1}` |
