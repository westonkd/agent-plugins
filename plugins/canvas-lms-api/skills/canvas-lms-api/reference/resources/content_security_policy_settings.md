# Content Security Policy Settings

> Canvas LMS REST API — `/content_security_policy_settings` resource. Base path `/api`.

## GET /v1/courses/{course_id}/csp_settings

**Get current settings for account or course**  —  `get_current_settings_for_account_or_course_courses`

Update multiple modules in an account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/accounts/{account_id}/csp_settings

**Get current settings for account or course**  —  `get_current_settings_for_account_or_course_accounts`

Update multiple modules in an account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/csp_settings

**Enable, disable, or clear explicit CSP setting**  —  `enable_disable_or_clear_explicit_csp_setting_courses`

Either explicitly sets CSP to be on or off for courses and sub-accounts,
or clear the explicit settings to default to those set by a parent account

Note: If "inherited" and "settings_locked" are both true for this account or course,
then the CSP setting cannot be modified.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `status` | string | form | yes | If set to "enabled" for an account, CSP will be enabled for all its courses and sub-accounts (that have not explicitly enabled or disabled it), using the allowed domains set on this account. If set to "disabled", CSP will be disabled for this account or course and for all sub-accounts that have not explicitly re-enabled it. If set to "inherited", this account or course will reset to the default state where CSP settings are inherited from the first parent account to have them explicitly set. Allowed: `enabled`, `disabled`, `inherited` |

**Returns:** `void`

## PUT /v1/accounts/{account_id}/csp_settings

**Enable, disable, or clear explicit CSP setting**  —  `enable_disable_or_clear_explicit_csp_setting_accounts`

Either explicitly sets CSP to be on or off for courses and sub-accounts,
or clear the explicit settings to default to those set by a parent account

Note: If "inherited" and "settings_locked" are both true for this account or course,
then the CSP setting cannot be modified.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `status` | string | form | yes | If set to "enabled" for an account, CSP will be enabled for all its courses and sub-accounts (that have not explicitly enabled or disabled it), using the allowed domains set on this account. If set to "disabled", CSP will be disabled for this account or course and for all sub-accounts that have not explicitly re-enabled it. If set to "inherited", this account or course will reset to the default state where CSP settings are inherited from the first parent account to have them explicitly set. Allowed: `enabled`, `disabled`, `inherited` |

**Returns:** `void`

## PUT /v1/accounts/{account_id}/csp_settings/lock

**Lock or unlock current CSP settings for sub-accounts and courses**  —  `lock_or_unlock_current_csp_settings_for_sub_accounts_and_courses`

Can only be set if CSP is explicitly enabled or disabled on this account (i.e. "inherited" is false).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `settings_locked` | boolean | form | yes | Whether sub-accounts and courses will be prevented from overriding settings inherited from this account. |

**Returns:** `void`

## POST /v1/accounts/{account_id}/csp_settings/domains

**Add an allowed domain to account**  —  `add_allowed_domain_to_account`

Adds an allowed domain for the current account. Note: this will not take effect
unless CSP is explicitly enabled on this account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `domain` | string | form | yes | no description |

**Returns:** `void`

## POST /v1/accounts/{account_id}/csp_settings/domains/batch_create

**Add multiple allowed domains to an account**  —  `add_multiple_allowed_domains_to_account`

Adds multiple allowed domains for the current account. Note: this will not take effect
unless CSP is explicitly enabled on this account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `domains` | Array | form | yes | no description |

**Returns:** `void`

## DELETE /v1/accounts/{account_id}/csp_settings/domains

**Remove a domain from account**  —  `remove_domain_from_account`

Removes an allowed domain from the current account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `domain` | string | query | yes | no description |

**Returns:** `void`
