# Pages

> Canvas LMS REST API — `/pages` resource. Base path `/api`.

## GET /v1/courses/{course_id}/front_page

**Show front page**  —  `show_front_page_courses`

Retrieve the content of the front page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `Page`

## GET /v1/groups/{group_id}/front_page

**Show front page**  —  `show_front_page_groups`

Retrieve the content of the front page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `Page`

## POST /v1/courses/{course_id}/pages/{url_or_id}/duplicate

**Duplicate page**  —  `duplicate_page`

Duplicate a wiki page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |

**Returns:** `Page`

## PUT /v1/courses/{course_id}/front_page

**Update/create front page**  —  `update_create_front_page_courses`

Update the title or contents of the front page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `wiki_page[title]` | string | form |  | The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result. |
| `wiki_page[body]` | string | form |  | The content for the new page. |
| `wiki_page[editing_roles]` | string | form |  | Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).  "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user. Allowed: `teachers`, `students`, `members`, `public` |
| `wiki_page[notify_of_update]` | boolean | form |  | Whether participants should be notified when this page changes. |
| `wiki_page[published]` | boolean | form |  | Whether the page is published (true) or draft state (false). |

**Returns:** `Page`

## PUT /v1/groups/{group_id}/front_page

**Update/create front page**  —  `update_create_front_page_groups`

Update the title or contents of the front page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `wiki_page[title]` | string | form |  | The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result. |
| `wiki_page[body]` | string | form |  | The content for the new page. |
| `wiki_page[editing_roles]` | string | form |  | Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).  "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user. Allowed: `teachers`, `students`, `members`, `public` |
| `wiki_page[notify_of_update]` | boolean | form |  | Whether participants should be notified when this page changes. |
| `wiki_page[published]` | boolean | form |  | Whether the page is published (true) or draft state (false). |

**Returns:** `Page`

## GET /v1/courses/{course_id}/pages

**List pages**  —  `list_pages_courses`

A paginated list of the wiki pages associated with a course or group

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `sort` | string | query |  | Sort results by this field. Allowed: `title`, `created_at`, `updated_at` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |
| `search_term` | string | query |  | The partial title of the pages to match and return. |
| `published` | boolean | query |  | If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status. |
| `include` | array[string] | query |  | - "body": Optionally include the page body with each Page. If this is a block_editor page, returns the block_editor_attributes. Allowed: `body` |

**Returns:** `array[Page]`

## GET /v1/groups/{group_id}/pages

**List pages**  —  `list_pages_groups`

A paginated list of the wiki pages associated with a course or group

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `sort` | string | query |  | Sort results by this field. Allowed: `title`, `created_at`, `updated_at` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |
| `search_term` | string | query |  | The partial title of the pages to match and return. |
| `published` | boolean | query |  | If true, include only published paqes. If false, exclude published pages. If not present, do not filter on published status. |
| `include` | array[string] | query |  | - "body": Optionally include the page body with each Page. If this is a block_editor page, returns the block_editor_attributes. Allowed: `body` |

**Returns:** `array[Page]`

## POST /v1/courses/{course_id}/pages

**Create page**  —  `create_page_courses`

Create a new wiki page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `wiki_page[title]` | string | form | yes | The title for the new page. |
| `wiki_page[body]` | string | form |  | The content for the new page. |
| `wiki_page[editing_roles]` | string | form |  | Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).  "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user. Allowed: `teachers`, `students`, `members`, `public` |
| `wiki_page[notify_of_update]` | boolean | form |  | Whether participants should be notified when this page changes. |
| `wiki_page[published]` | boolean | form |  | Whether the page is published (true) or draft state (false). |
| `wiki_page[front_page]` | boolean | form |  | Set an unhidden page as the front page (if true) |
| `wiki_page[publish_at]` | DateTime | form |  | Schedule a future date/time to publish the page. This will have no effect unless the "Scheduled Page Publication" feature is enabled in the account. If a future date is supplied, the page will be unpublished and +wiki_page[published]+ will be ignored. |

**Returns:** `Page`

## POST /v1/groups/{group_id}/pages

**Create page**  —  `create_page_groups`

Create a new wiki page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `wiki_page[title]` | string | form | yes | The title for the new page. |
| `wiki_page[body]` | string | form |  | The content for the new page. |
| `wiki_page[editing_roles]` | string | form |  | Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).  "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user. Allowed: `teachers`, `students`, `members`, `public` |
| `wiki_page[notify_of_update]` | boolean | form |  | Whether participants should be notified when this page changes. |
| `wiki_page[published]` | boolean | form |  | Whether the page is published (true) or draft state (false). |
| `wiki_page[front_page]` | boolean | form |  | Set an unhidden page as the front page (if true) |
| `wiki_page[publish_at]` | DateTime | form |  | Schedule a future date/time to publish the page. This will have no effect unless the "Scheduled Page Publication" feature is enabled in the account. If a future date is supplied, the page will be unpublished and +wiki_page[published]+ will be ignored. |

**Returns:** `Page`

## GET /v1/courses/{course_id}/pages/{url_or_id}

**Show page**  —  `show_page_courses`

Retrieve the content of a wiki page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |

**Returns:** `Page`

## GET /v1/groups/{group_id}/pages/{url_or_id}

**Show page**  —  `show_page_groups`

Retrieve the content of a wiki page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |

**Returns:** `Page`

## PUT /v1/courses/{course_id}/pages/{url_or_id}

**Update/create page**  —  `update_create_page_courses`

Update the title or contents of a wiki page

NOTE: You cannot specify the ID when creating a page. If you pass a numeric value
as the page identifier and that does not represent a page ID that already
exists, it will be interpreted as a URL.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `wiki_page[title]` | string | form |  | The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result. |
| `wiki_page[body]` | string | form |  | The content for the new page. |
| `wiki_page[editing_roles]` | string | form |  | Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).  "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user. Allowed: `teachers`, `students`, `members`, `public` |
| `wiki_page[notify_of_update]` | boolean | form |  | Whether participants should be notified when this page changes. |
| `wiki_page[published]` | boolean | form |  | Whether the page is published (true) or draft state (false). |
| `wiki_page[publish_at]` | DateTime | form |  | Schedule a future date/time to publish the page. This will have no effect unless the "Scheduled Page Publication" feature is enabled in the account. If a future date is set and the page is already published, it will be unpublished. |
| `wiki_page[front_page]` | boolean | form |  | Set an unhidden page as the front page (if true) |

**Returns:** `Page`

## PUT /v1/groups/{group_id}/pages/{url_or_id}

**Update/create page**  —  `update_create_page_groups`

Update the title or contents of a wiki page

NOTE: You cannot specify the ID when creating a page. If you pass a numeric value
as the page identifier and that does not represent a page ID that already
exists, it will be interpreted as a URL.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `wiki_page[title]` | string | form |  | The title for the new page. NOTE: changing a page's title will change its url. The updated url will be returned in the result. |
| `wiki_page[body]` | string | form |  | The content for the new page. |
| `wiki_page[editing_roles]` | string | form |  | Which user roles are allowed to edit this page. Any combination of these roles is allowed (separated by commas).  "teachers":: Allows editing by teachers in the course. "students":: Allows editing by students in the course. "members":: For group wikis, allows editing by members of the group. "public":: Allows editing by any user. Allowed: `teachers`, `students`, `members`, `public` |
| `wiki_page[notify_of_update]` | boolean | form |  | Whether participants should be notified when this page changes. |
| `wiki_page[published]` | boolean | form |  | Whether the page is published (true) or draft state (false). |
| `wiki_page[publish_at]` | DateTime | form |  | Schedule a future date/time to publish the page. This will have no effect unless the "Scheduled Page Publication" feature is enabled in the account. If a future date is set and the page is already published, it will be unpublished. |
| `wiki_page[front_page]` | boolean | form |  | Set an unhidden page as the front page (if true) |

**Returns:** `Page`

## DELETE /v1/courses/{course_id}/pages/{url_or_id}

**Delete page**  —  `delete_page_courses`

Delete a wiki page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |

**Returns:** `Page`

## DELETE /v1/groups/{group_id}/pages/{url_or_id}

**Delete page**  —  `delete_page_groups`

Delete a wiki page

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |

**Returns:** `Page`

## GET /v1/courses/{course_id}/pages/{url_or_id}/revisions

**List revisions**  —  `list_revisions_courses`

A paginated list of the revisions of a page. Callers must have update rights on the page in order to see page history.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |

**Returns:** `array[PageRevision]`

## GET /v1/groups/{group_id}/pages/{url_or_id}/revisions

**List revisions**  —  `list_revisions_groups`

A paginated list of the revisions of a page. Callers must have update rights on the page in order to see page history.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |

**Returns:** `array[PageRevision]`

## GET /v1/courses/{course_id}/pages/{url_or_id}/revisions/latest

**Show revision**  —  `show_revision_courses_latest`

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `summary` | boolean | query |  | If set, exclude page content from results |

**Returns:** `PageRevision`

## GET /v1/groups/{group_id}/pages/{url_or_id}/revisions/latest

**Show revision**  —  `show_revision_groups_latest`

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `summary` | boolean | query |  | If set, exclude page content from results |

**Returns:** `PageRevision`

## GET /v1/courses/{course_id}/pages/{url_or_id}/revisions/{revision_id}

**Show revision**  —  `show_revision_courses_revision_id`

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `revision_id` | string | path | yes | ID |
| `summary` | boolean | query |  | If set, exclude page content from results |

**Returns:** `PageRevision`

## GET /v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id}

**Show revision**  —  `show_revision_groups_revision_id`

Retrieve the metadata and optionally content of a revision of the page.
Note that retrieving historic versions of pages requires edit rights.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `revision_id` | string | path | yes | ID |
| `summary` | boolean | query |  | If set, exclude page content from results |

**Returns:** `PageRevision`

## POST /v1/courses/{course_id}/pages/{url_or_id}/revisions/{revision_id}

**Revert to revision**  —  `revert_to_revision_courses`

Revert a page to a prior revision.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `revision_id` | integer (int64) | path | yes | The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions) |

**Returns:** `PageRevision`

## POST /v1/groups/{group_id}/pages/{url_or_id}/revisions/{revision_id}

**Revert to revision**  —  `revert_to_revision_groups`

Revert a page to a prior revision.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `revision_id` | integer (int64) | path | yes | The revision to revert to (use the {api:WikiPagesApiController#revisions List Revisions API} to see available revisions) |

**Returns:** `PageRevision`


---

# Models


## Page

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `page_id` | integer |  | the ID of the page e.g. `1` |
| `url` | string |  | the unique locator for the page e.g. `my-page-title` |
| `title` | string |  | the title of the page e.g. `My Page Title` |
| `created_at` | datetime |  | the creation date for the page e.g. `2012-08-06T16:46:33-06:00` |
| `updated_at` | datetime |  | the date the page was last updated e.g. `2012-08-08T14:25:20-06:00` |
| `hide_from_students` | boolean |  | (DEPRECATED) whether this page is hidden from students (note: this is always reflected as the inverse of the published value) e.g. `False` |
| `editing_roles` | string |  | roles allowed to edit the page; comma-separated list comprising a combination of 'teachers', 'students', 'members', and/or 'public' if not supplied, course defaults are used e.g. `teachers,students` |
| `last_edited_by` | User |  | the User who last edited the page (this may not be present if the page was imported from another system) |
| `body` | string |  | the page content, in HTML (present when requesting a single page; optionally included when listing pages) e.g. `<p>Page Content</p>` |
| `published` | boolean |  | whether the page is published (true) or draft state (false). e.g. `True` |
| `publish_at` | datetime |  | scheduled publication date for this page e.g. `2022-09-01T00:00:00` |
| `front_page` | boolean |  | whether this page is the front page for the wiki e.g. `False` |
| `locked_for_user` | boolean |  | Whether or not this is locked for the user. e.g. `False` |
| `lock_info` | LockInfo |  | (Optional) Information for the user about the lock. Present when locked_for_user is true. |
| `lock_explanation` | string |  | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. e.g. `This page is locked until September 1 at 12:00am` |
| `editor` | string |  | The editor used to create and edit this page. May be one of 'rce' or 'block_editor'. e.g. `rce` |
| `block_editor_attributes` | object |  | The block editor attributes for this page. (optionally included, and only if this is a block editor created page) e.g. `{'id': 278, 'version': '0.2', 'blocks': '{...block json here...}'}` |


## PageRevision

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `revision_id` | integer |  | an identifier for this revision of the page e.g. `7` |
| `updated_at` | datetime |  | the time when this revision was saved e.g. `2012-08-07T11:23:58-06:00` |
| `latest` | boolean |  | whether this is the latest revision or not e.g. `True` |
| `edited_by` | User |  | the User who saved this revision, if applicable (this may not be present if the page was imported from another system) |
| `url` | string |  | the following fields are not included in the index action and may be omitted from the show action via summary=1 the historic url of the page e.g. `old-page-title` |
| `title` | string |  | the historic page title e.g. `Old Page Title` |
| `body` | string |  | the historic page contents e.g. `<p>Old Page Content</p>` |
