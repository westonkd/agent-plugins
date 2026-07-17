# Logins

> Canvas LMS REST API — `/logins` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/logins

**List user logins**  —  `list_user_logins_accounts`

Given a user ID, return a paginated list of that user's logins for the given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/users/{user_id}/logins

**List user logins**  —  `list_user_logins_users`

Given a user ID, return a paginated list of that user's logins for the given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/users/reset_password

**Kickoff password recovery flow**  —  `kickoff_password_recovery_flow`

Given a user email, generate a nonce and email it to the user

**Returns:** `void`

## POST /v1/accounts/{account_id}/logins

**Create a user login**  —  `create_user_login`

Create a new login for an existing user in the given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `user[id]` | string | form | yes | The ID of the user to create the login for. |
| `login[unique_id]` | string | form | yes | The unique ID for the new login. |
| `login[password]` | string | form |  | The new login's password. |
| `login[sis_user_id]` | string | form |  | SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. |
| `login[integration_id]` | string | form |  | Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. The Integration ID is a secondary identifier useful for more complex SIS integrations. |
| `login[authentication_provider_id]` | string | form |  | The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider). |
| `login[declared_user_type]` | string | form |  | The declared intention of the user type. This can be set, but does not change any Canvas functionality with respect to their access. A user can still be a teacher, admin, student, etc. in any particular context without regard to this setting. This can be used for administrative purposes for integrations to be able to more easily identify why the user was created. Valid values are:   * administrative   * observer   * staff   * student   * student_other   * teacher |
| `user[existing_user_id]` | string | form |  | A Canvas User ID to identify a user in a trusted account (alternative to `id`, `existing_sis_user_id`, or `existing_integration_id`). This parameter is not available in OSS Canvas. |
| `user[existing_integration_id]` | string | form |  | An Integration ID to identify a user in a trusted account (alternative to `id`, `existing_user_id`, or `existing_sis_user_id`). This parameter is not available in OSS Canvas. |
| `user[existing_sis_user_id]` | string | form |  | An SIS User ID to identify a user in a trusted account (alternative to `id`, `existing_integration_id`, or `existing_user_id`). This parameter is not available in OSS Canvas. |
| `user[trusted_account]` | string | form |  | The domain of the account to search for the user. This field is required when identifying a user in a trusted account. This parameter is not available in OSS Canvas. |

**Returns:** `void`

## PUT /v1/accounts/{account_id}/logins/{id}

**Edit a user login**  —  `edit_user_login`

Update an existing login for a user in the given account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `login[unique_id]` | string | form |  | The new unique ID for the login. |
| `login[password]` | string | form |  | The new password for the login. Admins can only set a password for another user if the "Password setting by admins" account setting is enabled. |
| `login[old_password]` | string | form |  | The prior password for the login. Required if the caller is changing their own password. |
| `login[sis_user_id]` | string | form |  | SIS ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. |
| `login[integration_id]` | string | form |  | Integration ID for the login. To set this parameter, the caller must be able to manage SIS permissions on the account. The Integration ID is a secondary identifier useful for more complex SIS integrations. |
| `login[authentication_provider_id]` | string | form |  | The authentication provider this login is associated with. Logins associated with a specific provider can only be used with that provider. Legacy providers (LDAP, CAS, SAML) will search for logins associated with them, or unassociated logins. New providers will only search for logins explicitly associated with them. This can be the integer ID of the provider, or the type of the provider (in which case, it will find the first matching provider). To unassociate from a known provider, specify null or an empty string. |
| `login[workflow_state]` | string | form |  | Used to suspend or re-activate a login. Allowed: `active`, `suspended` |
| `login[declared_user_type]` | string | form |  | The declared intention of the user type. This can be set, but does not change any Canvas functionality with respect to their access. A user can still be a teacher, admin, student, etc. in any particular context without regard to this setting. This can be used for administrative purposes for integrations to be able to more easily identify why the user was created. Valid values are:   * administrative   * observer   * staff   * student   * student_other   * teacher |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `void`

## DELETE /v1/users/{user_id}/logins/{id}

**Delete a user login**  —  `delete_user_login`

Delete an existing login.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`
