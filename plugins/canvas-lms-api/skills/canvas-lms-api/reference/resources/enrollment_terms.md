# Enrollment Terms

> Canvas LMS REST API — `/enrollment_terms` resource. Base path `/api`.

## POST /v1/accounts/{account_id}/terms

**Create enrollment term**  —  `create_enrollment_term`

Create a new enrollment term for the specified account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `enrollment_term[name]` | string | form |  | The name of the term. |
| `enrollment_term[start_at]` | DateTime | form |  | The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z. |
| `enrollment_term[end_at]` | DateTime | form |  | The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z. |
| `enrollment_term[sis_term_id]` | string | form |  | The unique SIS identifier for the term. |
| `enrollment_term[overrides][enrollment_type][start_at]` | DateTime | form |  | The day/time the term starts, overridden for the given enrollment type. *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment |
| `enrollment_term[overrides][enrollment_type][end_at]` | DateTime | form |  | The day/time the term ends, overridden for the given enrollment type. *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment |

**Returns:** `EnrollmentTerm`

## PUT /v1/accounts/{account_id}/terms/{id}

**Update enrollment term**  —  `update_enrollment_term`

Update an existing enrollment term for the specified account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `enrollment_term[name]` | string | form |  | The name of the term. |
| `enrollment_term[start_at]` | DateTime | form |  | The day/time the term starts. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z. |
| `enrollment_term[end_at]` | DateTime | form |  | The day/time the term ends. Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z. |
| `enrollment_term[sis_term_id]` | string | form |  | The unique SIS identifier for the term. |
| `enrollment_term[overrides][enrollment_type][start_at]` | DateTime | form |  | The day/time the term starts, overridden for the given enrollment type. *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment |
| `enrollment_term[overrides][enrollment_type][end_at]` | DateTime | form |  | The day/time the term ends, overridden for the given enrollment type. *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment |
| `override_sis_stickiness` | boolean | form |  | Default is true. If false, any fields containing “sticky” changes will not be updated. See SIS CSV Format documentation for information on which fields can have SIS stickiness |

**Returns:** `EnrollmentTerm`

## DELETE /v1/accounts/{account_id}/terms/{id}

**Delete enrollment term**  —  `delete_enrollment_term`

Delete the specified enrollment term.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `EnrollmentTerm`

## GET /v1/accounts/{account_id}/terms

**List enrollment terms**  —  `list_enrollment_terms`

An object with a paginated list of all of the terms in the account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `workflow_state` | array[string] | query |  | If set, only returns terms that are in the given state. Defaults to 'active'. Allowed: `active`, `deleted`, `all` |
| `include` | array[string] | query |  | Array of additional information to include.  "overrides":: term start/end dates overridden for different enrollment types "course_count":: the number of courses in each term Allowed: `overrides` |
| `term_name` | string | query |  | If set, only returns terms that match the given search keyword. Search keyword is matched against term name. |

**Returns:** `EnrollmentTermsList`

## GET /v1/accounts/{account_id}/terms/{id}

**Retrieve enrollment term**  —  `retrieve_enrollment_term`

Retrieves the details for an enrollment term in the account. Includes overrides by default.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `EnrollmentTerm`


---

# Models


## EnrollmentTerm

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the enrollment term. e.g. `1` |
| `sis_term_id` | string |  | The SIS id of the term. Only included if the user has permission to view SIS information. e.g. `Sp2014` |
| `sis_import_id` | integer |  | the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. e.g. `34` |
| `name` | string |  | The name of the term. e.g. `Spring 2014` |
| `start_at` | datetime |  | The datetime of the start of the term. e.g. `2014-01-06T08:00:00-05:00` |
| `end_at` | datetime |  | The datetime of the end of the term. e.g. `2014-05-16T05:00:00-04:00` |
| `workflow_state` | string |  | The state of the term. Can be 'active' or 'deleted'. e.g. `active` |
| `overrides` | object |  | Term date overrides for specific enrollment types e.g. `{'StudentEnrollment': {'start_at': '2014-01-07T08:00:00-05:00', 'end_at': '2014-05-14T05:00:00-04:0'}}` |
| `course_count` | integer |  | The number of courses in the term (available via include) e.g. `80` |


## EnrollmentTermsList

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `enrollment_terms` | array[EnrollmentTerm] |  | a paginated list of all terms in the account e.g. `[]` |
