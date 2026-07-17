# LTI ContextControls

> Canvas LMS REST API — `/lti_context_controls` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls

**List All Context Controls**  —  `list_all_context_controls`

List all LTI ContextControls for the given LTI Registration.
These controls are partitioned by LTI Deployment, and have added
calculated fields for display in the Canvas UI.

This endpoint is used to populate the Availability page for an LTI Registration
and may not be useful for general API Usage. For listing all ContextControls
for a given Deployment, see the LTI Deployments - List Controls for Deployment endpoint.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |

**Returns:** `array[Lti::Deployment]`

## GET /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id}

**Show LTI Context Control**  —  `show_lti_context_control`

Display details of the specified LTI ContextControl for the specified LTI registration in this context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::ContextControl`

## POST /v1/accounts/{current_account_id}/lti_registrations/{registration_id}/controls

**Create LTI Context Control**  —  `create_lti_context_control`

Create a new LTI ContextControl for the specified LTI registration in this context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `current_account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `account_id` | integer (int64) | form |  | The Canvas ID of the Account that owns this. One of account_id or course_id must be present. Can also be a string. |
| `course_id` | integer (int64) | form |  | The Canvas ID of the Course that owns this. One of account_id or course_id must be present. Can also be a string. |
| `deployment_id` | integer (int64) | form |  | The Canvas ID of the ContextExternalTool that owns this, representing an LTI deployment. If absent, this ContextControl will be associated with the Deployment of this Registration at the Root Account level. If that is not present, this request will fail. |
| `available` | boolean | form |  | The state of this tool in this context. `true` shows the tool in this context and all contexts below it. `false` disables the tool for this context and all contexts below it. Defaults to true. |
| `comment` | string | form |  | A comment to add the to the change-log entry explaining why the changes were made. |

**Returns:** `Lti::ContextControl`

## POST /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/bulk

**Bulk Create LTI Context Controls**  —  `bulk_create_lti_context_controls`

Create up to 100 new LTI ContextControls for the specified LTI registration in this context.
Control parameters are sent as a JSON array of objects, each with the same parameters as the Create LTI Context Control endpoint.
Note that if a control already exists for the specified context and deployment, it will be updated instead of created.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `registration_id` | string | path | yes | ID |
| `comment` | string | form |  | A comment to add the to the change-log entry explaining why the changes were made. |
| `account_id` | array[integer] | path | yes | The Canvas ID of the Account that owns this. One of account_id or course_id must be present. Can also be a string. |
| `course_id` | array[integer] | form |  | The Canvas ID of the Course that owns this. One of account_id or course_id must be present. Can also be a string. |
| `deployment_id` | array[integer] | form |  | The Canvas ID of the ContextExternalTool that owns this, representing an LTI deployment. If absent, this ContextControl will be associated with the Deployment of this Registration at the Root Account level. If that is not present, this request will fail. |
| `available` | array[boolean] | form |  | The state of this tool in this context. `true` shows the tool in this context and all contexts below it. `false` disables the tool for this context and all contexts below it. Defaults to true. |

**Returns:** `Lti::ContextControl`

## PUT /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id}

**Modify a Context Control**  —  `modify_context_control`

Changes the availability of a context control. This endpoint can only be used
to change the availability of a context control; no other attributes about the
control (such as which course or account it belongs to) can be changed here.
To change those values, the control should be deleted and a new one created
instead.

Returns the context control with its new availability value applied.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `available` | boolean | form | yes | the new value for this control's availability |
| `comment` | string | form |  | A comment to add the to the change-log entry explaining why the changes were made. |

**Returns:** `Lti::ContextControl`

## DELETE /v1/accounts/{account_id}/lti_registrations/{registration_id}/controls/{id}

**Delete a Context Control**  —  `delete_context_control`

Deletes a context control. Returns the control that is now deleted.

Note: Deleting the "primary" control for a deployment (the control associated with the context
where the deployment is installed) is not allowed and will return an error. This prevents
situations where a deployment cannot be managed from the Apps page.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `registration_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Lti::ContextControl`


---

# Models


## Lti::ContextControl

Represent availability of an LTI registration in a specific context

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the Canvas ID of the Lti::ContextControl object e.g. `2` |
| `course_id` | integer |  | the Canvas ID of the Course that owns this. one of this or account_id will always be present e.g. `2` |
| `account_id` | integer |  | the Canvas ID of the Account that owns this. one of this or course_id will always be present e.g. `2` |
| `deployment_id` | integer |  | the Canvas ID of the ContextExternalTool that owns this, representing an LTI deployment e.g. `2` |
| `available` | boolean |  | The state of this tool in this context. `true` means the tool is available in this context and in all contexts below it. e.g. `True` |
| `path` | string |  | A representation of the account hierarchy for the context that owns this object. Used for checking availability during LTI operations. e.g. `a1.a2.c3.` |
| `display_path` | array[string] |  | For UI display. Names of the accounts in the context's hierarchy. Excludes the root, and the current account if context is an account. e.g. `['Sub Account', 'Other Account']` |
| `context_name` | string |  | For UI display. The name of the context this object is associated with e.g. `My Course` |
| `depth` | integer |  | For UI display. The depth of ContextControls for this particular deployment account chain, which can be different from the number of accounts in the chain. e.g. `2` |
| `course_count` | integer |  | For UI display. The number of courses in this account and all nested subaccounts. 0 when context is a Course. e.g. `402` |
| `child_control_count` | integer |  | For UI display. The number of controls for accounts below this one, including all nested subaccounts. 0 when context is a Course. e.g. `42` |
| `subaccount_count` | integer |  | For UI display. The number of subaccounts for this account. Includes all nested subaccounts. 0 when context is a Course. e.g. `42` |
| `workflow_state` | string |  | The state of the object e.g. `active` Allowed: `active`, `deleted` |
| `created_at` | string |  | Timestamp of the object's creation e.g. `2024-01-01T00:00:00Z` |
| `updated_at` | string |  | Timestamp of the object's last update e.g. `2024-01-01T00:00:00Z` |
| `created_by` | User |  | The user that created this object. Not always present. e.g. `{'type': 'User'}` |
| `updated_by` | User |  | The user that last updated this object. Not always present. e.g. `{'type': 'User'}` |
