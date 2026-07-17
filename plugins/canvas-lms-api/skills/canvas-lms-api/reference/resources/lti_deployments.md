# LTI Deployments

> Canvas LMS REST API — `/lti_deployments` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id}

**Show LTI Deployment**  —  `show_lti_deployment`

Display details of the specified deployment for the specified LTI registration in this context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::Deployment`

## POST /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments

**Create LTI Deployment**  —  `create_lti_deployment`

Create a new deployment for the specified LTI registration for the given context.
If no context is specified, the deployment will be created in the root account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `for_subaccount_id` | integer (int64) | form |  | (optional) If provided, the deployment will be created in the specified subaccount. |
| `for_course_id` | integer (int64) | form |  | (optional) If provided, the deployment will be created in the specified course. |
| `available` | boolean | form |  | (optional) If provided, sets the availability of the created deployment. Defaults to true. |

**Returns:** `Lti::Deployment`

## DELETE /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id}

**Delete LTI Deployment**  —  `delete_lti_deployment`

Delete the specified deployment for the specified LTI tool in this context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::Deployment`

## GET /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments

**List LTI Deployments**  —  `list_lti_deployments`

List all deployments available for the specified LTI registration.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |

**Returns:** `array[Lti::Deployment]`

## GET /v1/accounts/{account_id}/lti_registrations/{registration_id}/deployments/{id}/controls

**List LTI Context Controls**  —  `list_lti_context_controls`

List all context controls for the specified deployment. Context Controls are used to manage
LTI tool availability in contexts across Canvas.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array[Lti::ContextControl]`


---

# Models


## Lti::Deployment

A deployment of an LTI tool in Canvas

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the Canvas ID of the Lti::Deployment object e.g. `2` |
| `registration_id` | integer |  | the Canvas ID of the associated Lti::Registration object e.g. `2` |
| `deployment_id` | string |  | The Deployment ID of this deployment which is shared with launched tools e.g. `1:a2ea741a5c06bc26b36bf5a1afeba6c0faaae1ee` |
| `context_id` | integer |  | The Canvas ID of the context this deployment is associated with e.g. `2` |
| `context_type` | string |  | The type of context this deployment is associated with e.g. `Course` Allowed: `Course`, `Account` |
| `context_name` | string |  | The name of the context this deployment is associated with e.g. `My Course` |
| `workflow_state` | string |  | The workflow state of the deployment e.g. `active` Allowed: `active`, `deleted` |
| `context_controls` | array[Lti::ContextControl] |  | The context controls for this deployment. Only present in the LTI Context Controls - List All Context Controls endpoint. e.g. `[{'type': 'Lti::ContextControl'}]` |
