# Feature Flags

> Canvas LMS REST API — `/feature_flags` resource. Base path `/api`.

## GET /v1/courses/{course_id}/features

**List features**  —  `list_features_courses`

A paginated list of all features that apply to a given Account, Course, or User.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `hide_inherited_enabled` | boolean | query |  | When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. |

**Returns:** `array[Feature]`

## GET /v1/accounts/{account_id}/features

**List features**  —  `list_features_accounts`

A paginated list of all features that apply to a given Account, Course, or User.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `hide_inherited_enabled` | boolean | query |  | When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. |

**Returns:** `array[Feature]`

## GET /v1/users/{user_id}/features

**List features**  —  `list_features_users`

A paginated list of all features that apply to a given Account, Course, or User.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `hide_inherited_enabled` | boolean | query |  | When true, feature flags that are enabled in a higher context and cannot be overridden will be omitted. |

**Returns:** `array[Feature]`

## GET /v1/courses/{course_id}/features/enabled

**List enabled features**  —  `list_enabled_features_courses`

A paginated list of all features that are enabled on a given Account, Course, or User.
Only the feature names are returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/accounts/{account_id}/features/enabled

**List enabled features**  —  `list_enabled_features_accounts`

A paginated list of all features that are enabled on a given Account, Course, or User.
Only the feature names are returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/users/{user_id}/features/enabled

**List enabled features**  —  `list_enabled_features_users`

A paginated list of all features that are enabled on a given Account, Course, or User.
Only the feature names are returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/features/environment

**List environment features**  —  `list_environment_features`

Return a hash of global feature options that pertain to the
Canvas user interface. This is the same information supplied to the
web interface as +ENV.FEATURES+.

**Returns:** `void`

## GET /v1/courses/{course_id}/features/flags/{feature}

**Get feature flag**  —  `get_feature_flag_courses`

Get the feature flag that applies to a given Account, Course, or User.
The flag may be defined on the object, or it may be inherited from a parent
account. You can look at the context_id and context_type of the returned object
to determine which is the case. If these fields are missing, then the object
is the global Canvas default.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`

## GET /v1/accounts/{account_id}/features/flags/{feature}

**Get feature flag**  —  `get_feature_flag_accounts`

Get the feature flag that applies to a given Account, Course, or User.
The flag may be defined on the object, or it may be inherited from a parent
account. You can look at the context_id and context_type of the returned object
to determine which is the case. If these fields are missing, then the object
is the global Canvas default.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`

## GET /v1/users/{user_id}/features/flags/{feature}

**Get feature flag**  —  `get_feature_flag_users`

Get the feature flag that applies to a given Account, Course, or User.
The flag may be defined on the object, or it may be inherited from a parent
account. You can look at the context_id and context_type of the returned object
to determine which is the case. If these fields are missing, then the object
is the global Canvas default.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`

## PUT /v1/courses/{course_id}/features/flags/{feature}

**Set feature flag**  —  `set_feature_flag_courses`

Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
a feature flag for the same feature in any state other than "allowed".

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |
| `state` | string | form |  | "off":: The feature is not available for the course, user, or account and sub-accounts. "allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in             sub-accounts and courses by setting a feature flag on the sub-account or course. "on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts. Allowed: `off`, `allowed`, `on` |

**Returns:** `FeatureFlag`

## PUT /v1/accounts/{account_id}/features/flags/{feature}

**Set feature flag**  —  `set_feature_flag_accounts`

Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
a feature flag for the same feature in any state other than "allowed".

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |
| `state` | string | form |  | "off":: The feature is not available for the course, user, or account and sub-accounts. "allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in             sub-accounts and courses by setting a feature flag on the sub-account or course. "on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts. Allowed: `off`, `allowed`, `on` |

**Returns:** `FeatureFlag`

## PUT /v1/users/{user_id}/features/flags/{feature}

**Set feature flag**  —  `set_feature_flag_users`

Set a feature flag for a given Account, Course, or User. This call will fail if a parent account sets
a feature flag for the same feature in any state other than "allowed".

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |
| `state` | string | form |  | "off":: The feature is not available for the course, user, or account and sub-accounts. "allowed":: (valid only on accounts) The feature is off in the account, but may be enabled in             sub-accounts and courses by setting a feature flag on the sub-account or course. "on":: The feature is turned on unconditionally for the user, course, or account and sub-accounts. Allowed: `off`, `allowed`, `on` |

**Returns:** `FeatureFlag`

## DELETE /v1/courses/{course_id}/features/flags/{feature}

**Remove feature flag**  —  `remove_feature_flag_courses`

Remove feature flag for a given Account, Course, or User.  (Note that the flag must
be defined on the Account, Course, or User directly.)  The object will then inherit
the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
then lower-level account flags that were masked by this one will apply again.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`

## DELETE /v1/accounts/{account_id}/features/flags/{feature}

**Remove feature flag**  —  `remove_feature_flag_accounts`

Remove feature flag for a given Account, Course, or User.  (Note that the flag must
be defined on the Account, Course, or User directly.)  The object will then inherit
the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
then lower-level account flags that were masked by this one will apply again.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`

## DELETE /v1/users/{user_id}/features/flags/{feature}

**Remove feature flag**  —  `remove_feature_flag_users`

Remove feature flag for a given Account, Course, or User.  (Note that the flag must
be defined on the Account, Course, or User directly.)  The object will then inherit
the feature flags from a higher account, if any exist.  If this flag was 'on' or 'off',
then lower-level account flags that were masked by this one will apply again.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`


---

# Models


## Feature

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `feature` | string |  | The symbolic name of the feature, used in FeatureFlags e.g. `fancy_wickets` |
| `display_name` | string |  | The user-visible name of the feature e.g. `Fancy Wickets` |
| `applies_to` | string |  | The type of object the feature applies to (RootAccount, Account, Course, or User):  * RootAccount features may only be controlled by flags on root accounts.  * Account features may be controlled by flags on accounts and their parent accounts.  * Course features may be controlled by flags on courses and their parent accounts.  * User features may be controlled by flags on users and site admin only. e.g. `Course` |
| `feature_flag` | FeatureFlag |  | The FeatureFlag that applies to the caller e.g. `{'feature': 'fancy_wickets', 'state': 'allowed'}` |
| `root_opt_in` | boolean |  | If true, a feature that is 'allowed' globally will be 'off' by default in root accounts. Otherwise, root accounts inherit the global 'allowed' setting, which allows sub-accounts and courses to turn features on with no root account action. e.g. `True` |
| `beta` | boolean |  | Whether the feature is a feature preview. If true, opting in includes ongoing updates outside the regular release schedule. e.g. `True` |
| `early_access_program` | boolean |  | Indicates the feature is part of the Early Access Program. e.g. `False` |
| `autoexpand` | boolean |  | Whether the details of the feature are autoexpanded on page load vs. the user clicking to expand. e.g. `True` |
| `release_notes_url` | string |  | A URL to the release notes describing the feature e.g. `http://canvas.example.com/release_notes#fancy_wickets` |


## FeatureFlag

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `context_type` | string |  | The type of object to which this flag applies (Account, Course, or User). (This field is not present if this FeatureFlag represents the global Canvas default) e.g. `Account` |
| `context_id` | integer |  | The id of the object to which this flag applies (This field is not present if this FeatureFlag represents the global Canvas default) e.g. `1038` |
| `feature` | string |  | The feature this flag controls e.g. `fancy_wickets` |
| `state` | string |  | The policy for the feature at this context.  can be 'off', 'allowed', 'allowed_on', or 'on'. e.g. `allowed` |
| `locked` | boolean |  | If set, this feature flag cannot be changed in the caller's context because the flag is set 'off' or 'on' in a higher context e.g. `False` |
