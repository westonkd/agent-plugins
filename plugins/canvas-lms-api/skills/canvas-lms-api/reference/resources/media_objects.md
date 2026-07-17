# Media Objects

> Canvas LMS REST API — `/media_objects` resource. Base path `/api`.

## GET /v1/media_objects/{media_object_id}/media_tracks

**List media tracks for a Media Object or Attachment**  —  `list_media_tracks_for_media_object_or_attachment_media_objects`

List the media tracks associated with a media object or attachment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `media_object_id` | string | path | yes | ID |
| `include` | array[string] | query |  | By default, index returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content Allowed: `content`, `webvtt_content`, `updated_at`, `created_at` |

**Returns:** `array[MediaTrack]`

## GET /v1/media_attachments/{attachment_id}/media_tracks

**List media tracks for a Media Object or Attachment**  —  `list_media_tracks_for_media_object_or_attachment_media_attachments`

List the media tracks associated with a media object or attachment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `attachment_id` | string | path | yes | ID |
| `include` | array[string] | query |  | By default, index returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content Allowed: `content`, `webvtt_content`, `updated_at`, `created_at` |

**Returns:** `array[MediaTrack]`

## PUT /v1/media_objects/{media_object_id}/media_tracks

**Update Media Tracks**  —  `update_media_tracks_media_objects`

Replace the media tracks associated with a media object or attachment with
the array of tracks provided in the body.
Update will
delete any existing tracks not listed,
leave untouched any tracks with no content field,
and update or create tracks with a content field.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `media_object_id` | string | path | yes | ID |
| `include` | array[string] | form |  | By default, an update returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content Allowed: `content`, `webvtt_content`, `updated_at`, `created_at` |

**Returns:** `array[MediaTrack]`

## PUT /v1/media_attachments/{attachment_id}/media_tracks

**Update Media Tracks**  —  `update_media_tracks_media_attachments`

Replace the media tracks associated with a media object or attachment with
the array of tracks provided in the body.
Update will
delete any existing tracks not listed,
leave untouched any tracks with no content field,
and update or create tracks with a content field.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `attachment_id` | string | path | yes | ID |
| `include` | array[string] | form |  | By default, an update returns id, locale, kind, media_object_id, and user_id for each of the result MediaTracks. Use include[] to add additional fields. For example include[]=content Allowed: `content`, `webvtt_content`, `updated_at`, `created_at` |

**Returns:** `array[MediaTrack]`

## GET /v1/media_objects

**List Media Objects**  —  `list_media_objects_media_objects`

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `sort` | string | query |  | Field to sort on. Default is "title"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. Allowed: `title`, `created_at` |
| `order` | string | query |  | Sort direction. Default is "asc" Allowed: `asc`, `desc` |
| `exclude` | array[string] | query |  | Array of data to exclude. By excluding "sources" and "tracks", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks Allowed: `sources`, `tracks` |

**Returns:** `array[MediaObject]`

## GET /v1/courses/{course_id}/media_objects

**List Media Objects**  —  `list_media_objects_courses_media_objects`

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `sort` | string | query |  | Field to sort on. Default is "title"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. Allowed: `title`, `created_at` |
| `order` | string | query |  | Sort direction. Default is "asc" Allowed: `asc`, `desc` |
| `exclude` | array[string] | query |  | Array of data to exclude. By excluding "sources" and "tracks", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks Allowed: `sources`, `tracks` |

**Returns:** `array[MediaObject]`

## GET /v1/groups/{group_id}/media_objects

**List Media Objects**  —  `list_media_objects_groups_media_objects`

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `sort` | string | query |  | Field to sort on. Default is "title"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. Allowed: `title`, `created_at` |
| `order` | string | query |  | Sort direction. Default is "asc" Allowed: `asc`, `desc` |
| `exclude` | array[string] | query |  | Array of data to exclude. By excluding "sources" and "tracks", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks Allowed: `sources`, `tracks` |

**Returns:** `array[MediaObject]`

## GET /v1/media_attachments

**List Media Objects**  —  `list_media_objects_media_attachments`

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `sort` | string | query |  | Field to sort on. Default is "title"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. Allowed: `title`, `created_at` |
| `order` | string | query |  | Sort direction. Default is "asc" Allowed: `asc`, `desc` |
| `exclude` | array[string] | query |  | Array of data to exclude. By excluding "sources" and "tracks", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks Allowed: `sources`, `tracks` |

**Returns:** `array[MediaObject]`

## GET /v1/courses/{course_id}/media_attachments

**List Media Objects**  —  `list_media_objects_courses_media_attachments`

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `sort` | string | query |  | Field to sort on. Default is "title"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. Allowed: `title`, `created_at` |
| `order` | string | query |  | Sort direction. Default is "asc" Allowed: `asc`, `desc` |
| `exclude` | array[string] | query |  | Array of data to exclude. By excluding "sources" and "tracks", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks Allowed: `sources`, `tracks` |

**Returns:** `array[MediaObject]`

## GET /v1/groups/{group_id}/media_attachments

**List Media Objects**  —  `list_media_objects_groups_media_attachments`

Returns media objects created by the user making the request. When
using the second version, returns media objects associated with
the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `sort` | string | query |  | Field to sort on. Default is "title"  title:: sorts on user_entered_title if available, title if not.  created_at:: sorts on the object's creation time. Allowed: `title`, `created_at` |
| `order` | string | query |  | Sort direction. Default is "asc" Allowed: `asc`, `desc` |
| `exclude` | array[string] | query |  | Array of data to exclude. By excluding "sources" and "tracks", the api will not need to query kaltura, which greatly speeds up its response.  sources:: Do not query kaltura for media_sources tracks:: Do not query kaltura for media_tracks Allowed: `sources`, `tracks` |

**Returns:** `array[MediaObject]`

## PUT /v1/media_objects/{media_object_id}

**Update Media Object**  —  `update_media_object_media_objects`

Updates the title of a media object.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `media_object_id` | string | path | yes | ID |
| `user_entered_title` | string | form |  | The new title. |
| `viewer_restrictions` | Hash | form |  | A JSON object describing viewer access restrictions for this media. - show_rolling_transcript [Optional, Boolean]: Whether to show the rolling transcripts of the media during playback, or not. |

**Returns:** `void`

## PUT /v1/media_attachments/{attachment_id}

**Update Media Object**  —  `update_media_object_media_attachments`

Updates the title of a media object.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `attachment_id` | string | path | yes | ID |
| `user_entered_title` | string | form |  | The new title. |
| `viewer_restrictions` | Hash | form |  | A JSON object describing viewer access restrictions for this media. - show_rolling_transcript [Optional, Boolean]: Whether to show the rolling transcripts of the media during playback, or not. |

**Returns:** `void`


---

# Models


## MediaTrack

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  |  |
| `user_id` | integer (int64) |  |  |
| `media_object_id` | integer (int64) |  |  |
| `kind` | string |  |  |
| `locale` | string |  |  |
| `content` | string |  |  |
| `created_at` | string |  |  |
| `updated_at` | string |  |  |
| `webvtt_content` | string |  |  |


## MediaObject

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `can_add_captions` | boolean |  |  |
| `user_entered_title` | string |  |  |
| `title` | string |  |  |
| `media_id` | string |  |  |
| `media_type` | string |  |  |
| `media_tracks` | string |  |  |
| `media_sources` | string |  |  |
