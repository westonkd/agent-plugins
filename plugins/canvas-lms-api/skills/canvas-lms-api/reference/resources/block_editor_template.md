# BlockEditorTemplate

> Canvas LMS REST API — `/block_editor_template` resource. Base path `/api`.

## GET /v1/courses/{course_id}/block_editor_templates

**List block templates**  —  `list_block_templates`

A list of the block templates available to the current user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `sort` | string | query |  | Sort results by this field. Allowed: `name`, `created_at`, `updated_at` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |
| `drafts` | boolean | query |  | If true, include draft templates. If false or omitted only published templates will be returned. |
| `type` | array[string] | query |  | What type of templates should be returned. Allowed: `page`, `section`, `block` |
| `include` | array[string] | query |  | no description Allowed: `node_tree`, `thumbnail` |

**Returns:** `array[BlockEditorTemplate]`


---

# Models


## BlockEditorTemplate

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the page e.g. `1` |
| `name` | string |  | name of the template e.g. `Navigation Bar` |
| `description` | string |  | description of the template e.g. `A bar of links to other content` |
| `created_at` | datetime |  | the creation date for the template e.g. `2012-08-06T16:46:33-06:00` |
| `updated_at` | datetime |  | the date the template was last updated e.g. `2012-08-08T14:25:20-06:00` |
| `node_tree` | string |  | The JSON data that is the template |
| `editor_version` | string |  | The version of the editor that created the template e.g. `1.0` |
| `template_type` | string |  | The type of template. One of 'block', 'section', or 'page' e.g. `page` |
| `workflow_state` | string |  | String indicating what state this assignment is in. e.g. `unpublished` |
