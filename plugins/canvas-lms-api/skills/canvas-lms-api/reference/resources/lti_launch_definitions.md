# LTI Launch Definitions

> Canvas LMS REST API — `/lti_launch_definitions` resource. Base path `/api`.

## GET /v1/courses/{course_id}/lti_apps/launch_definitions

**List LTI Launch Definitions**  —  `list_lti_launch_definitions_courses`

List all tools available in this context for the given placements, in the form of Launch Definitions.
Used primarily by the Canvas frontend. API users should consider using the External Tools API instead.
This endpoint is cached for 10 minutes!

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `placements[Array]` | string | query |  | The placements to return launch definitions for. If not provided, an empty list will be returned. |
| `only_visible[Boolean]` | string | query |  | If true, only return launch definitions that are visible to the current user. Defaults to true. |
| `include_context_name[Boolean]` | string | query |  | If true, includes the deployment context name (account or course) of the tool definition in the response. This helps distinguish between tools with identical names deployed at different levels of the context hierarchy. Defaults to false. |

**Returns:** `void`

## GET /v1/accounts/{account_id}/lti_apps/launch_definitions

**List LTI Launch Definitions**  —  `list_lti_launch_definitions_accounts`

List all tools available in this context for the given placements, in the form of Launch Definitions.
Used primarily by the Canvas frontend. API users should consider using the External Tools API instead.
This endpoint is cached for 10 minutes!

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `placements[Array]` | string | query |  | The placements to return launch definitions for. If not provided, an empty list will be returned. |
| `only_visible[Boolean]` | string | query |  | If true, only return launch definitions that are visible to the current user. Defaults to true. |
| `include_context_name[Boolean]` | string | query |  | If true, includes the deployment context name (account or course) of the tool definition in the response. This helps distinguish between tools with identical names deployed at different levels of the context hierarchy. Defaults to false. |

**Returns:** `void`


---

# Models


## Lti::LaunchDefinition

A bare-bones representation of an LTI tool used by Canvas to launch the tool

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `definition_type` | string |  | The type of the launch definition. Always 'ContextExternalTool' e.g. `ContextExternalTool` |
| `definition_id` | string |  | The Canvas ID of the tool e.g. `123` |
| `name` | string |  | The display name of the tool for the given placement e.g. `My Tool` |
| `description` | string |  | The description of the tool for the given placement. e.g. `This is a tool that does things.` |
| `url` | string |  | The launch URL for the tool e.g. `https://www.example.com/launch` |
| `domain` | string |  | The domain of the tool e.g. `example.com` |
| `placements` | object |  | Placement-specific config for given placements e.g. `{'assignment_selection': {'type': 'Lti::PlacementLaunchDefinition'}}` |
| `context_name` | string |  | The name of the account or course where the tool is deployed. Only included if requested via include_context_name parameter. e.g. `My Institution` |


## Lti::PlacementLaunchDefinition

A bare-bones LTI configuration for a specific placement

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `message_type` | string |  | The LTI launch message type e.g. `LtiResourceLinkRequest` |
| `url` | string |  | The launch URL for this placement e.g. `https://www.example.com/launch?placement=assignment_selection` |
| `title` | string |  | The title of the tool for this placement e.g. `My Tool (Assignment Selection)` |
