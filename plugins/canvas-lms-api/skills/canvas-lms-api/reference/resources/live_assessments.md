# LiveAssessments

> Canvas LMS REST API — `/live_assessments` resource. Base path `/api`.

## POST /v1/courses/{course_id}/live_assessments/{assessment_id}/results

**Create live assessment results**  —  `create_live_assessment_results`

Creates live assessment results and adds them to a live assessment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assessment_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/live_assessments/{assessment_id}/results

**List live assessment results**  —  `list_live_assessment_results`

Returns a paginated list of live assessment results

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assessment_id` | string | path | yes | ID |
| `user_id` | integer (int64) | query |  | If set, restrict results to those for this user |

**Returns:** `void`

## POST /v1/courses/{course_id}/live_assessments

**Create or find a live assessment**  —  `create_or_find_live_assessment`

Creates or finds an existing live assessment with the given key and aligns it with
the linked outcome

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/live_assessments

**List live assessments**  —  `list_live_assessments`

Returns a paginated list of live assessments.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## Result

A pass/fail results for a student

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | A unique identifier for this result e.g. `42` |
| `passed` | boolean |  | Whether the user passed or not e.g. `True` |
| `assessed_at` | datetime |  | When this result was recorded e.g. `2014-05-13T00:01:57-06:00` |
| `links` | ResultLinks |  | Unique identifiers of objects associated with this result e.g. `{'user': '42', 'assessor': '23', 'assessment': '5'}` |


## ResultLinks

Unique identifiers of objects associated with a result

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `user` | string |  | A unique identifier for the user to whom this result applies e.g. `42` |
| `assessor` | string |  | A unique identifier for the user who created this result e.g. `23` |
| `assessment` | string |  | A unique identifier for the assessment that this result is for e.g. `5` |


## Assessment

A simple assessment that collects pass/fail results for a student

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | A unique identifier for this live assessment e.g. `42` |
| `key` | string |  | A client specified unique identifier for the assessment e.g. `2014-05-27,outcome_52` |
| `title` | string |  | A human readable title for the assessment e.g. `May 27th Reading Assessment` |
