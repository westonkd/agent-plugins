# Tabs

> Canvas LMS REST API — `/tabs` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/tabs

**List available tabs for a course or group**  —  `list_available_tabs_for_course_or_group_accounts`

Returns a paginated list of navigation tabs available in the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "course_subject_tabs": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. Allowed: `course_subject_tabs` |

**Returns:** `void`

## GET /v1/courses/{course_id}/tabs

**List available tabs for a course or group**  —  `list_available_tabs_for_course_or_group_courses`

Returns a paginated list of navigation tabs available in the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "course_subject_tabs": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. Allowed: `course_subject_tabs` |

**Returns:** `void`

## GET /v1/groups/{group_id}/tabs

**List available tabs for a course or group**  —  `list_available_tabs_for_course_or_group_groups`

Returns a paginated list of navigation tabs available in the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "course_subject_tabs": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. Allowed: `course_subject_tabs` |

**Returns:** `void`

## GET /v1/users/{user_id}/tabs

**List available tabs for a course or group**  —  `list_available_tabs_for_course_or_group_users`

Returns a paginated list of navigation tabs available in the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "course_subject_tabs": Optional flag to return the tabs associated with a canvas_for_elementary subject course's   home page instead of the typical sidebar navigation. Only takes effect if this request is for a course context   in a canvas_for_elementary-enabled account or sub-account. Allowed: `course_subject_tabs` |

**Returns:** `void`

## PUT /v1/courses/{course_id}/tabs/{tab_id}

**Update a tab for a course**  —  `update_tab_for_course`

Home and Settings tabs are not manageable, and can't be hidden or moved

Returns a tab object

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `tab_id` | string | path | yes | ID |
| `position` | integer (int64) | form |  | The new position of the tab, 1-based |
| `hidden` | boolean | form |  | no description |

**Returns:** `Tab`


---

# Models


## Tab

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `html_url` | string |  | e.g. `/courses/1/external_tools/4` |
| `id` | string |  | e.g. `context_external_tool_4` |
| `label` | string |  | e.g. `WordPress` |
| `type` | string |  | e.g. `external` |
| `hidden` | boolean |  | only included if true e.g. `True` |
| `visibility` | string |  | possible values are: public, members, admins, and none e.g. `public` |
| `position` | integer |  | 1 based e.g. `2` |
