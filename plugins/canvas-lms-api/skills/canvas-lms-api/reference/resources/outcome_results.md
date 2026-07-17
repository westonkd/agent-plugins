# Outcome Results

> Canvas LMS REST API — `/outcome_results` resource. Base path `/api`.

## GET /v1/courses/{course_id}/outcome_results

**Get outcome results**  —  `get_outcome_results`

Gets the outcome results for users and outcomes in the specified context.

used in sLMGB

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `user_ids` | array[integer] | query |  | If specified, only the users whose ids are given will be included in the results. SIS ids can be used, prefixed by "sis_user_id:". It is an error to specify an id for a user who is not a student in the context. |
| `outcome_ids` | array[integer] | query |  | If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context. |
| `include` | array[string] | query |  | [String, "alignments"\|"outcomes"\|"outcomes.alignments"\|"outcome_groups"\|"outcome_links"\|"outcome_paths"\|"users"] Specify additional collections to be side loaded with the result. "alignments" includes only the alignments referenced by the returned results. "outcomes.alignments" includes all alignments referenced by outcomes in the context. |
| `include_hidden` | boolean | query |  | If true, results that are hidden from the learning mastery gradebook and student rollup scores will be included |

**Returns:** `void`

## POST /v1/courses/{course_id}/assign_outcome_order

**Set outcome ordering for LMGB**  —  `set_outcome_ordering_for_lmgb`

Saves the ordering of outcomes in LMGB for a user

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/outcome_rollups

**Get outcome result rollups**  —  `get_outcome_result_rollups`

Gets the outcome rollups for the users and outcomes in the specified
context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `aggregate` | string | query |  | If specified, instead of returning one rollup for each user, all the user rollups will be combined into one rollup for the course that will contain the average (or median, see below) rollup score for each outcome. Allowed: `course` |
| `aggregate_stat` | string | query |  | If aggregate rollups requested, then this value determines what statistic is used for the aggregate. Defaults to "mean" if this value is not specified. Allowed: `mean`, `median` |
| `user_ids` | array[integer] | query |  | If specified, only the users whose ids are given will be included in the results or used in an aggregate result. it is an error to specify an id for a user who is not a student in the context |
| `outcome_ids` | array[integer] | query |  | If specified, only the outcomes whose ids are given will be included in the results. it is an error to specify an id for an outcome which is not linked to the context. |
| `include` | array[string] | query |  | [String, "courses"\|"outcomes"\|"outcomes.alignments"\|"outcome_groups"\|"outcome_links"\|"outcome_paths"\|"users"] Specify additional collections to be side loaded with the result. |
| `exclude` | array[string] | query |  | Specify additional values to exclude. "missing_user_rollups" excludes rollups for users without results. "missing_outcome_results" excludes outcomes without results. Allowed: `missing_user_rollups`, `missing_outcome_results`, `` |
| `sort_by` | string | query |  | If specified, sorts outcome result rollups. "student" sorting will sort by a user's sortable name. "outcome" sorting will sort by the given outcome's rollup score. The latter requires specifying the "sort_outcome_id" parameter. By default, the sort order is ascending. Allowed: `student`, `outcome` |
| `sort_outcome_id` | integer (int64) | query |  | If outcome sorting requested, then this determines which outcome to use for rollup score sorting. |
| `sort_order` | string | query |  | If sorting requested, then this allows changing the default sort order of ascending to descending. Allowed: `asc`, `desc` |
| `add_defaults` | boolean | query |  | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the rollup. This will only take effect if the Account Level Mastery Scales FF is DISABLED |
| `contributing_scores` | boolean | query |  | **DEPRECATED**: This parameter is deprecated. Use the separate GET /api/v1/courses/:course_id/outcomes/:outcome_id/contributing_scores endpoint instead to fetch contributing scores for a specific outcome. If contributing scores are requested, then each individual outcome score will also include all graded artifacts that contributed to the outcome score |

**Returns:** `void`

## GET /v1/courses/{course_id}/outcomes/{outcome_id}/contributing_scores

**Get contributing scores**  —  `get_contributing_scores`

Gets the contributing scores for a specific outcome and set of users.
Contributing scores are the individual assignment/quiz scores that
contributed to the outcome score for each user.

Returns all alignments for the outcome in the course context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `outcome_id` | string | path | yes | ID |
| `user_ids` | array[integer] | query |  | If specified, only the users whose ids are given will be included in the results. It is an error to specify an id for a user who is not a student in the context. |
| `only_assignment_alignments` | boolean | query |  | If specified, only assignment alignments will be included in the results. |
| `show_unpublished_assignments` | boolean | query |  | If true, unpublished assignments will be included in the results. Defaults to false. |

**Returns:** `void`

## GET /v1/courses/{course_id}/outcome_mastery_distribution

**Get mastery distribution**  —  `get_mastery_distribution`

Returns the distribution of student scores across mastery levels for all outcomes.
This endpoint fetches data for ALL students (not paginated) to provide accurate
distribution statistics for charts and analytics.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `exclude` | array[string] | query |  | Optionally restrict which results are included: - "missing_user_rollups": exclude students without any scores - "missing_outcome_results": exclude outcomes without any results |
| `outcome_ids` | array[string] | query |  | Optionally restrict to specific outcome IDs |
| `student_ids` | array[string] | query |  | Optionally restrict to specific student IDs. If not provided, all students will be included. |
| `include` | array[string] | query |  | Optionally include additional data: - "alignment_distributions": include contributing score distributions for alignments |
| `only_assignment_alignments` | boolean | query |  | If true and alignment_distributions is included, only include assignment alignments. Default: false. |
| `show_unpublished_assignments` | boolean | query |  | If true, include unpublished assignments in alignment distributions. Default: false. |
| `add_defaults` | boolean | query |  | If defaults are requested, then color and mastery level defaults will be added to outcome ratings in the result. This will only take effect if the Account Level Mastery Scales FF is DISABLED |

**Returns:** `MasteryDistributionResponse`

## POST /v1/enqueue_outcome_rollup_calculation

**Enqueue a delayed Outcome Rollup Calculation Job**  —  `enqueue_delayed_outcome_rollup_calculation_job`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | form |  | The course ID for the rollup job |
| `student_uuid` | string | form |  | The student UUID for the rollup job. If provided, calculates for specific student. |

**Returns:** `RollupJob`


---

# Models


## OutcomeResult

A student's result for an outcome

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | A unique identifier for this result e.g. `42` |
| `score` | integer |  | The student's score e.g. `6` |
| `submitted_or_assessed_at` | datetime |  | The datetime the resulting OutcomeResult was submitted at, or absent that, when it was assessed. e.g. `2013-02-01T00:00:00-06:00` |
| `links` | object |  | Unique identifiers of objects associated with this result e.g. `{'user': '3', 'learning_outcome': '97', 'alignment': '53'}` |
| `percent` | number |  | score's percent of maximum points possible for outcome, scaled to reflect any custom mastery levels that differ from the learning outcome e.g. `0.65` |


## OutcomeRollupScoreLinks

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `outcome` | integer |  | The id of the related outcome e.g. `42` |


## OutcomeRollupScore

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `score` | integer |  | The rollup score for the outcome, based on the student alignment scores related to the outcome. This could be null if the student has no related scores. e.g. `3` |
| `count` | integer |  | The number of alignment scores included in this rollup. e.g. `6` |
| `links` | OutcomeRollupScoreLinks |  | e.g. `{'outcome': '42'}` |


## OutcomeRollupLinks

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `course` | integer |  | If an aggregate result was requested, the course field will be present. Otherwise, the user and section field will be present (Optional) The id of the course that this rollup applies to e.g. `42` |
| `user` | integer |  | (Optional) The id of the user that this rollup applies to e.g. `42` |
| `section` | integer |  | (Optional) The id of the section the user is in e.g. `57` |


## OutcomeRollup

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `scores` | OutcomeRollupScore |  | an array of OutcomeRollupScore objects |
| `name` | string |  | The name of the resource for this rollup. For example, the user name. e.g. `John Doe` |
| `links` | OutcomeRollupLinks |  | e.g. `{'course': 42, 'user': 42, 'section': 57}` |


## OutcomeAlignment

An asset aligned with this outcome

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | A unique identifier for this alignment e.g. `quiz_3` |
| `name` | string |  | The name of this alignment e.g. `Big mid-term test` |
| `html_url` | string |  | (Optional) A URL for details about this alignment |


## OutcomePath

The full path to an outcome

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | A unique identifier for this outcome e.g. `42` |
| `parts` | OutcomePathPart |  | an array of OutcomePathPart objects |


## OutcomePathPart

An outcome or outcome group

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `name` | string |  | The title of the outcome or outcome group e.g. `Spelling out numbers` |
