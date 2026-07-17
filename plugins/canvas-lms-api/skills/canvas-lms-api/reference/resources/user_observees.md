# User Observees

> Canvas LMS REST API — `/user_observees` resource. Base path `/api`.

## GET /v1/users/{user_id}/observees

**List linked observees**  —  `list_linked_observees`

A paginated list of users that the given user is observing. This endpoint returns
users linked to the observer at the account level (such that the observer is automatically
enrolled in observees' courses); it doesn't return one-off observer enrollments from
individual courses.

*Note:* all users are allowed to list their own observees. Administrators can list
other users' observees.

The returned observees will include an attribute "observation_link_root_account_ids", a list
of ids for the root accounts the observer and observee are linked on. The observer will only be able to
observe in courses associated with these root accounts.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "avatar_url": Optionally include avatar_url. Allowed: `avatar_url` |

**Returns:** `array[User]`

## GET /v1/users/{user_id}/observers

**List linked observers**  —  `list_linked_observers`

A paginated list of observers linked to a given user.

*Note:* all users are allowed to list their own observers. Administrators can list
other users' observers.

The returned observers will include an attribute "observation_link_root_account_ids", a list
of ids for the root accounts the observer and observee are linked on. The observer will only be able to
observe in courses associated with these root accounts.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "avatar_url": Optionally include avatar_url. Allowed: `avatar_url` |

**Returns:** `array[User]`

## POST /v1/users/{user_id}/observees

**Add an observee with credentials**  —  `add_observee_with_credentials`

Register the given user to observe another user, given the observee's credentials.

*Note:* all users are allowed to add their own observees, given the observee's
credentials or access token are provided. Administrators can add observees given credentials, access token or
the {api:UserObserveesController#update observee's id}.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `observee[unique_id]` | string | form |  | The login id for the user to observe.  Required if access_token is omitted. |
| `observee[password]` | string | form |  | The password for the user to observe. Required if access_token is omitted. |
| `access_token` | string | form |  | The access token for the user to observe.  Required if <tt>observee[unique_id]</tt> or <tt>observee[password]</tt> are omitted. |
| `pairing_code` | string | form |  | A generated pairing code for the user to observe. Required if the Observer pairing code feature flag is enabled |
| `root_account_id` | integer (int64) | form |  | The ID for the root account to associate with the observation link. Defaults to the current domain account. If 'all' is specified, a link will be created for each root account associated to both the observer and observee. |

**Returns:** `User`

## GET /v1/users/{user_id}/observees/{observee_id}

**Show an observee**  —  `show_observee`

Gets information about an observed user.

*Note:* all users are allowed to view their own observees.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `observee_id` | string | path | yes | ID |

**Returns:** `User`

## GET /v1/users/{user_id}/observers/{observer_id}

**Show an observer**  —  `show_observer`

Gets information about an observer.

*Note:* all users are allowed to view their own observers.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `observer_id` | string | path | yes | ID |

**Returns:** `User`

## PUT /v1/users/{user_id}/observees/{observee_id}

**Add an observee**  —  `add_observee`

Registers a user as being observed by the given user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `observee_id` | string | path | yes | ID |
| `root_account_id` | integer (int64) | form |  | The ID for the root account to associate with the observation link. If not specified, a link will be created for each root account associated to both the observer and observee. |

**Returns:** `User`

## DELETE /v1/users/{user_id}/observees/{observee_id}

**Remove an observee**  —  `remove_observee`

Unregisters a user as being observed by the given user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `observee_id` | string | path | yes | ID |
| `root_account_id` | integer (int64) | query |  | If specified, only removes the link for the given root account |

**Returns:** `User`

## POST /v1/users/{user_id}/observer_pairing_codes

**Create observer pairing code**  —  `create_observer_pairing_code`

If the user is a student, will generate a code to be used with self registration
or observees APIs to link another user to this student.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `PairingCode`


---

# Models


## PairingCode

A code used for linking a user to a student to observe them.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `user_id` | integer (int64) |  | The ID of the user. e.g. `2` |
| `code` | string |  | The actual code to be sent to other APIs e.g. `abc123` |
| `expires_at` | string (date-time) |  | When the code expires e.g. `2012-05-30T17:45:25Z` |
| `workflow_state` | string |  | The current status of the code e.g. `active` |
