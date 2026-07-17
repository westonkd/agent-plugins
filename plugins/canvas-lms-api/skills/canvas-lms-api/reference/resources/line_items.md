# Line Items

> Canvas LMS REST API — `/line_items` resource. Base path `/api`.

## POST /lti/courses/{course_id}/line_items

**Create a Line Item**  —  `create_line_item`

Create a new Line Item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `scoreMaximum` | number (float) | form | yes | The maximum score for the line item. Scores created for the Line Item may exceed this value. |
| `label` | string | form | yes | The label for the Line Item. If no resourceLinkId is specified this value will also be used as the name of the placeholder assignment. |
| `resourceId` | string | form |  | A Tool Provider specified id for the Line Item. Multiple line items may share the same resourceId within a given context. |
| `tag` | string | form |  | A value used to qualify a line Item beyond its ids. Line Items may be queried by this value in the List endpoint. Multiple line items can share the same tag within a given context. |
| `resourceLinkId` | string | form |  | The resource link id the Line Item should be attached to. This value should match the LTI id of the Canvas assignment associated with the tool. |
| `startDateTime` | string | form |  | The ISO8601 date and time when the line item is made available. Corresponds to the assignment's unlock_at date. |
| `endDateTime` | string | form |  | The ISO8601 date and time when the line item stops receiving submissions. Corresponds to the assignment's due_at date. |
| `https://canvas.instructure.com/lti/submission_type` | object | form |  | (EXTENSION) - Optional block to set Assignment Submission Type when creating a new assignment is created. type - 'none' or 'external_tool':: external_tool_url - Submission URL only used when type: 'external_tool':: |

**Returns:** `LineItem`

## PUT /lti/courses/{course_id}/line_items/{id}

**Update a Line Item**  —  `update_line_item`

Update new Line Item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `scoreMaximum` | number (float) | form |  | The maximum score for the line item. Scores created for the Line Item may exceed this value. |
| `label` | string | form |  | The label for the Line Item. If no resourceLinkId is specified this value will also be used as the name of the placeholder assignment. |
| `resourceId` | string | form |  | A Tool Provider specified id for the Line Item. Multiple line items may share the same resourceId within a given context. |
| `tag` | string | form |  | A value used to qualify a line Item beyond its ids. Line Items may be queried by this value in the List endpoint. Multiple line items can share the same tag within a given context. |
| `startDateTime` | string | form |  | The ISO8601 date and time when the line item is made available. Corresponds to the assignment's unlock_at date. |
| `endDateTime` | string | form |  | The ISO8601 date and time when the line item stops receiving submissions. Corresponds to the assignment's due_at date. |

**Returns:** `LineItem`

## GET /lti/courses/{course_id}/line_items/{id}

**Show a Line Item**  —  `show_line_item`

Show existing Line Item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include.  "launch_url":: includes the launch URL for this line item using the "https\://canvas.instructure.com/lti/launch_url" extension Allowed: `launch_url` |

**Returns:** `LineItem`

## GET /lti/courses/{course_id}/line_items

**List line Items**  —  `list_line_items`

List all Line Items for a course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `tag` | string | query |  | If specified only Line Items with this tag will be included. |
| `resource_id` | string | query |  | If specified only Line Items with this resource_id will be included. |
| `resource_link_id` | string | query |  | If specified only Line Items attached to the specified resource_link_id will be included. |
| `limit` | string | query |  | May be used to limit the number of Line Items returned in a page |
| `include` | array[string] | query |  | Array of additional information to include.  "launch_url":: includes the launch URL for each line item using the "https\://canvas.instructure.com/lti/launch_url" extension Allowed: `launch_url` |

**Returns:** `LineItem`

## DELETE /lti/courses/{course_id}/line_items/{id}

**Delete a Line Item**  —  `delete_line_item`

Delete an existing Line Item

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `LineItem`


---

# Models


## LineItem

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | The fully qualified URL for showing, updating, and deleting the Line Item e.g. `http://institution.canvas.com/api/lti/courses/5/line_items/2` |
| `scoreMaximum` | number |  | The maximum score of the Line Item e.g. `50` |
| `label` | string |  | The label of the Line Item. e.g. `50` |
| `tag` | string |  | Tag used to qualify a line Item beyond its ids e.g. `50` |
| `resourceId` | string |  | A Tool Provider specified id for the Line Item. Multiple line items can share the same resourceId within a given context e.g. `50` |
| `resourceLinkId` | string |  | The resource link id the Line Item is attached to e.g. `50` |
| `https://canvas.instructure.com/lti/submission_type` | string |  | The extension that defines the submission_type of the line_item. Only returns if set through the line_item create endpoint. e.g. `{ 	"type":"external_tool", 	"external_tool_url":"https://my.launch.url", }` |
| `https://canvas.instructure.com/lti/launch_url` | string |  | The launch url of the Line Item. Only returned if `include=launch_url` query parameter is passed, and only for Show and List actions. e.g. `https://my.tool.url/launch` |
