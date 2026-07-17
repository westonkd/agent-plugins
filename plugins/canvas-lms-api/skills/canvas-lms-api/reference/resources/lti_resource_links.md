# LTI Resource Links

> Canvas LMS REST API — `/lti_resource_links` resource. Base path `/api`.

## GET /v1/courses/{course_id}/lti_resource_links

**List LTI Resource Links**  —  `list_lti_resource_links`

Returns all Resource Links in the specified course. This includes links
that are associated with Assignments, Module Items, Collaborations, and
that are embedded in rich content. This endpoint is paginated, and will
return 50 links per page by default.
Links are sorted by the order in which they were created.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include_deleted` | boolean | query |  | Include deleted resource links and links associated with deleted content in response. Default is false. |
| `per_page` | integer (int64) | query |  | The number of registrations to return per page. Defaults to 50. |

**Returns:** `array[Lti::ResourceLink]`

## GET /v1/courses/{course_id}/lti_resource_links/{id}

**Show an LTI Resource Link**  —  `show_lti_resource_link`

Return details about the specified resource link. The ID can be in the standard
Canvas format ("1"), or in these special formats:

- resource_link_uuid:<uuid> - Find the resource link by its resource_link_uuid
- lookup_uuid:<uuid> - Find the resource link by its lookup_uuid

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include_deleted` | boolean | query |  | Include deleted resource links in search. Default is false. |

**Returns:** `Lti::ResourceLink`

## POST /v1/courses/{course_id}/lti_resource_links

**Create an LTI Resource Link**  —  `create_lti_resource_link`

Create a new LTI Resource Link in the specified course with the provided parameters.

<b>Caution!</b> Resource Links are usually created by the tool via LTI Deep Linking. The tool has no
knowledge of links created via this API, and may not be able to handle or launch them.

Links created using this API cannot be associated with a specific piece of Canvas content,
like an Assignment, Module Item, or Collaboration. Links created using this API are only suitable
for embedding in rich content using the `canvas_launch_url` provided in the API response.

This link will be associated with the ContextExternalTool available in this context that matches the provided url.
If a matching tool is not found, the link will not be created and this will return an error.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url` | string | form | yes | The launch URL for this resource link. |
| `title` | string | form |  | The title of the resource link. |
| `custom` | Hash | form |  | Custom parameters to be sent to the tool when launching this link. |

**Returns:** `Lti::ResourceLink`

## POST /v1/courses/{course_id}/lti_resource_links/bulk

**Bulk Create LTI Resource Links**  —  `bulk_create_lti_resource_links`

Create up to 100 new LTI Resource Links in the specified course with the provided parameters.

<b>Caution!</b> Resource Links are usually created by the tool via LTI Deep Linking. The tool has no
knowledge of links created via this API, and may not be able to handle or launch them.

Links created using this API cannot be associated with a specific piece of Canvas content,
like an Assignment, Module Item, or Collaboration. Links created using this API are only suitable
for embedding in rich content using the `canvas_launch_url` provided in the API response.

Each link will be associated with the ContextExternalTool available in this context that matches the provided url.
If a matching tool is not found, or any parameters are invalid, no links will be created and this will return an error.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `POST` | string | form |  | body [Required, Array] The POST body should be a JSON array of objects containing the parameters for each link to create. |
| `url` | array[string] | form | yes | Each object must contain a launch URL. |
| `title` | array[string] | form |  | Each object may contain a title. |
| `custom` | array[Hash] | form |  | Custom parameters to be sent to the tool when launching this link. |

**Returns:** `Lti::ResourceLink`

## PUT /v1/courses/{course_id}/lti_resource_links/{id}

**Update an LTI Resource Link**  —  `update_lti_resource_link`

Update the specified resource link with the provided parameters.

<b>Caution!</b> Changing existing links may result in launch errors.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `url` | string | form |  | The launch URL for this resource link. <b>Caution!</b> URL must match the URL or domain of the tool associated with this resource link |
| `custom` | Hash | form |  | Custom parameters to be sent to the tool when launching this link. <b>Caution!</b> Changing these from what the tool provided could result in errors if the tool doesn't see what it's expecting. |
| `include_deleted` | boolean | form |  | Update link even if it is deleted. Default is false. |
| `context_external_tool_id` | integer (int64) | form |  | The Canvas identifier for the LTI 1.3 External Tool that the LTI Resource Link was originally installed from. <b>Caution!</b> The resource link url must match the tool's domain or url. |

**Returns:** `Lti::ResourceLink`

## DELETE /v1/courses/{course_id}/lti_resource_links/{id}

**Delete an LTI Resource Link**  —  `delete_lti_resource_link`

Delete the specified resource link. The ID can be in the standard
Canvas format ("1"), or in these special formats:

- resource_link_uuid:<uuid> - Find the resource link by its resource_link_uuid
- lookup_uuid:<uuid> - Find the resource link by its lookup_uuid

Only links that are not associated with Assignments, Module Items, or Collaborations can be deleted.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::ResourceLink`


---

# Models


## Lti::ResourceLink

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The Canvas identifier for the LTI Resource Link. e.g. `1` |
| `context_id` | integer |  | The Canvas identifier for the context that the LTI Resource Link is associated with. e.g. `1` |
| `context_type` | string |  | The type of the context that the LTI Resource Link is associated with. e.g. `Course` Allowed: `Course`, `Assignment`, `Collaboration` |
| `context_external_tool_id` | integer |  | The Canvas identifier for the LTI 1.3 External Tool that the LTI Resource Link was originally installed from. Note that this tool may have been deleted or reinstalled and may not be the tool that would be launched for this url. e.g. `1` |
| `resource_type` | string |  | The type of Canvas content for the resource link. Included for convenience. e.g. `assignment` Allowed: `assignment`, `module_item`, `collaboration`, `rich_content` |
| `canvas_launch_url` | string |  | The Canvas URL that launches the LTI Resource Link. Suitable for use in Canvas rich content e.g. `https://example.instructure.com/courses/1/external_tools/retrieve?resource_link_lookup_uuid=ae43ba23-d238-49bc-ab55-ba7f79f77896` |
| `resource_link_uuid` | string |  | The LTI identifier for the LTI Resource Link, included as the resource_link_id when this link is launched e.g. `ae43ba23-d238-49bc-ab55-ba7f79f77896` |
| `lookup_uuid` | string |  | A unique identifier for the LTI Resource Link, present in the rich content representation. Remains the same across content migration. e.g. `c522554a-d4be-49ef-b163-9c87fdc6ad6f` |
| `title` | string |  | The title of the LTI Resource Link. Usually tool-provided, or matches the assignment name e.g. `Assignment 1` |
| `url` | string |  | The tool URL to which the LTI Resource Link will launch e.g. `https://example.com/lti/launch/content_item/123` |
| `lti_1_1_id` | string |  | The LTI 1.1 identifier for the LTI Resource Link, included in lti1p1 migration claim when launched. Only present if tool was migrated from 1.1 to 1.3. e.g. `6a8aaca162bfc4393804afd4cd53cd94413c48bb` |
| `created_at` | string |  | Timestamp of the resource link's creation e.g. `2024-01-01T00:00:00Z` |
| `updated_at` | string |  | Timestamp of the resource link's last update e.g. `2024-01-01T00:00:00Z` |
| `workflow_state` | string |  | The state of the resource link e.g. `active` Allowed: `active`, `deleted` |
| `associated_content_type` | string |  | Type of the associated content this resource link belongs to if present. Now only supports `ModuleItems`, later may be extend others e.g. `ModuleItem` Allowed: `ModuleItem` |
| `associated_content_id` | integer |  | The Canvas identifier of the associated content, e.g. ModuleItem related to this link. Present if associated_content_type is present e.g. `1` |
