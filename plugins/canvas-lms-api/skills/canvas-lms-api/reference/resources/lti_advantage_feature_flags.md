# LTI Advantage Feature Flags

> Canvas LMS REST API — `/lti_advantage_feature_flags` resource. Base path `/api`.

## GET /lti/courses/{course_id}/feature_flags/{feature}

**Show the specified feature flag**  —  `show_specified_feature_flag_courses`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`

## GET /lti/accounts/{account_id}/feature_flags/{feature}

**Show the specified feature flag**  —  `show_specified_feature_flag_accounts`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `feature` | string | path | yes | ID |

**Returns:** `FeatureFlag`


---

# Models


## FeatureFlag

A canvas feature flag.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `state` | string |  | The current state of the feature flag e.g. `on` |
| `name` | string |  | The name of the feature flag e.g. `New Feature` |
