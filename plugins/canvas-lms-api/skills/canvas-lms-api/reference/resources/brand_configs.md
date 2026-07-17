# Brand Configs

> Canvas LMS REST API — `/brand_configs` resource. Base path `/api`.

## GET /v1/brand_variables

**Get the brand config variables that should be used for this domain**  —  `get_brand_config_variables_that_should_be_used_for_this_domain`

Will redirect to a static json file that has all of the brand
variables used by this account. Even though this is a redirect,
do not store the redirected url since if the account makes any changes
it will redirect to a new url. Needs no authentication.

**Returns:** `void`

## GET /v1/accounts/{account_id}/brand_variables

**Get the brand config variables for a sub-account or course**  —  `get_brand_config_variables_for_sub_account_or_course_accounts`

Will redirect to a static json file that has all of the brand
variables used by the provided context. Even though this is a redirect,
do not store the redirected url since if the sub-account makes any changes
it will redirect to a new url.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/brand_variables

**Get the brand config variables for a sub-account or course**  —  `get_brand_config_variables_for_sub_account_or_course_courses`

Will redirect to a static json file that has all of the brand
variables used by the provided context. Even though this is a redirect,
do not store the redirected url since if the sub-account makes any changes
it will redirect to a new url.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`
