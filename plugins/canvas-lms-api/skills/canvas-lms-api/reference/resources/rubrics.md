# Rubrics

> Canvas LMS REST API — `/rubrics` resource. Base path `/api`.

## POST /v1/courses/{course_id}/rubrics

**Create a single rubric**  —  `create_single_rubric`

Returns the rubric with the given id.

Unfortunately this endpoint does not return a standard Rubric object,
instead it returns a hash that looks like
  { 'rubric': Rubric, 'rubric_association': RubricAssociation }

This may eventually be deprecated in favor of a more standardized return
value, but that is not currently planned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | integer (int64) | form |  | The id of the rubric |
| `rubric_association_id` | integer (int64) | form |  | The id of the rubric association object (not the course/assignment itself, but the join table record id). It can be used in place of +rubric_association[association_id]+ and +rubric_association[association_type]+ if desired. |
| `rubric[title]` | string | form |  | The title of the rubric |
| `rubric[free_form_criterion_comments]` | boolean | form |  | Whether or not you can write custom comments in the ratings field for a rubric |
| `rubric_association[association_id]` | integer (int64) | form |  | The id of the object with which this rubric is associated |
| `rubric_association[association_type]` | string | form |  | The type of object this rubric is associated with Allowed: `Assignment`, `Course`, `Account` |
| `rubric_association[use_for_grading]` | boolean | form |  | Whether or not the associated rubric is used for grade calculation |
| `rubric_association[hide_score_total]` | boolean | form |  | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. |
| `rubric_association[purpose]` | string | form |  | Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context |
| `rubric[criteria]` | Hash | form |  | An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects |

**Returns:** `void`

## PUT /v1/courses/{course_id}/rubrics/{id}

**Update a single rubric**  —  `update_single_rubric`

Returns the rubric with the given id.

Unfortunately this endpoint does not return a standard Rubric object,
instead it returns a hash that looks like
  { 'rubric': Rubric, 'rubric_association': RubricAssociation }

This may eventually be deprecated in favor of a more standardized return
value, but that is not currently planned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | integer (int64) | path | yes | The id of the rubric |
| `rubric_association_id` | integer (int64) | form |  | The id of the rubric association object (not the course/assignment itself, but the join table record id). It can be used in place of +rubric_association[association_id]+ and +rubric_association[association_type]+ if desired. |
| `rubric[title]` | string | form |  | The title of the rubric |
| `rubric[free_form_criterion_comments]` | boolean | form |  | Whether or not you can write custom comments in the ratings field for a rubric |
| `rubric[skip_updating_points_possible]` | boolean | form |  | Whether or not to update the points possible |
| `rubric_association[association_id]` | integer (int64) | form |  | The id of the object with which this rubric is associated |
| `rubric_association[association_type]` | string | form |  | The type of object this rubric is associated with Allowed: `Assignment`, `Course`, `Account` |
| `rubric_association[use_for_grading]` | boolean | form |  | Whether or not the associated rubric is used for grade calculation |
| `rubric_association[hide_score_total]` | boolean | form |  | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. |
| `rubric_association[purpose]` | string | form |  | Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context Allowed: `grading`, `bookmark` |
| `rubric[criteria]` | Hash | form |  | An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/rubrics/{id}

**Delete a single**  —  `delete_single`

Deletes a Rubric and removes all RubricAssociations.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Rubric`

## GET /v1/accounts/{account_id}/rubrics

**List rubrics**  —  `list_rubrics_accounts`

Returns the paginated list of active rubrics for the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/rubrics

**List rubrics**  —  `list_rubrics_courses`

Returns the paginated list of active rubrics for the current context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/accounts/{account_id}/rubrics/{id}

**Get a single rubric**  —  `get_single_rubric_accounts`

Returns the rubric with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Related records to include in the response. Allowed: `assessments`, `graded_assessments`, `peer_assessments`, `associations`, `assignment_associations`, `course_associations`, `account_associations` |
| `style` | string | query |  | Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted. Allowed: `full`, `comments_only` |

**Returns:** `Rubric`

## GET /v1/courses/{course_id}/rubrics/{id}

**Get a single rubric**  —  `get_single_rubric_courses`

Returns the rubric with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Related records to include in the response. Allowed: `assessments`, `graded_assessments`, `peer_assessments`, `associations`, `assignment_associations`, `course_associations`, `account_associations` |
| `style` | string | query |  | Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted. Allowed: `full`, `comments_only` |

**Returns:** `Rubric`

## GET /v1/courses/{course_id}/rubrics/{id}/used_locations

**Get the courses and assignments for a rubric**  —  `get_courses_and_assignments_for_rubric_courses`

Returns the courses and assignments where a rubric is being used

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `UsedLocations`

## GET /v1/accounts/{account_id}/rubrics/{id}/used_locations

**Get the courses and assignments for a rubric**  —  `get_courses_and_assignments_for_rubric_accounts`

Returns the courses and assignments where a rubric is being used

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `UsedLocations`

## POST /v1/courses/{course_id}/rubrics/upload

**Creates a rubric using a CSV file**  —  `creates_rubric_using_csv_file_courses`

Returns the rubric import object that was created

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `RubricImport`

## POST /v1/accounts/{account_id}/rubrics/upload

**Creates a rubric using a CSV file**  —  `creates_rubric_using_csv_file_accounts`

Returns the rubric import object that was created

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `RubricImport`

## GET /v1/rubrics/upload_template

**Templated file for importing a rubric**  —  `templated_file_for_importing_rubric`

Returns a CSV template file that can be used to import rubrics into Canvas.

**Returns:** `a CSV file in the format that can be imported`

## GET /v1/courses/{course_id}/rubrics/upload/{id}

**Get the status of a rubric import**  —  `get_status_of_rubric_import_courses`

Can return the latest rubric import for an account or course, or a specific import by id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `RubricImport`

## GET /v1/accounts/{account_id}/rubrics/upload/{id}

**Get the status of a rubric import**  —  `get_status_of_rubric_import_accounts`

Can return the latest rubric import for an account or course, or a specific import by id

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `RubricImport`

## POST /v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments

**Create a single rubric assessment**  —  `create_single_rubric_assessment`

Returns the rubric assessment with the given id.
The returned object also provides the information of
  :ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | integer (int64) | path | yes | The id of the course |
| `rubric_association_id` | integer (int64) | path | yes | The id of the object with which this rubric assessment is associated |
| `provisional` | string | form |  | (optional) Indicates whether this assessment is provisional, defaults to false. |
| `final` | string | form |  | (optional) Indicates a provisional grade will be marked as final. It only takes effect if the provisional param is passed as true. Defaults to false. |
| `graded_anonymously` | boolean | form |  | (optional) Defaults to false |
| `rubric_assessment` | Hash | form |  | A Hash of data to complement the rubric assessment: The user id that refers to the person being assessed   rubric_assessment[user_id] Assessment type. There are only three valid types:  'grading', 'peer_review', or 'provisional_grade'   rubric_assessment[assessment_type] The points awarded for this row.   rubric_assessment[criterion_id][points] Comments to add for this row.   rubric_assessment[criterion_id][comments] For each criterion_id, change the id by the criterion number, ex: criterion_123 If the criterion_id is not specified it defaults to false, and nothing is updated. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id}

**Update a single rubric assessment**  —  `update_single_rubric_assessment`

Returns the rubric assessment with the given id.
The returned object also provides the information of
  :ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | integer (int64) | path | yes | The id of the rubric assessment |
| `course_id` | integer (int64) | path | yes | The id of the course |
| `rubric_association_id` | integer (int64) | path | yes | The id of the object with which this rubric assessment is associated |
| `provisional` | string | form |  | (optional) Indicates whether this assessment is provisional, defaults to false. |
| `final` | string | form |  | (optional) Indicates a provisional grade will be marked as final. It only takes effect if the provisional param is passed as true. Defaults to false. |
| `graded_anonymously` | boolean | form |  | (optional) Defaults to false |
| `rubric_assessment` | Hash | form |  | A Hash of data to complement the rubric assessment: The user id that refers to the person being assessed   rubric_assessment[user_id] Assessment type. There are only three valid types:  'grading', 'peer_review', or 'provisional_grade'   rubric_assessment[assessment_type] The points awarded for this row.   rubric_assessment[criterion_id][points] Comments to add for this row.   rubric_assessment[criterion_id][comments] For each criterion_id, change the id by the criterion number, ex: criterion_123 If the criterion_id is not specified it defaults to false, and nothing is updated. |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id}

**Delete a single rubric assessment**  —  `delete_single_rubric_assessment`

Deletes a rubric assessment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `rubric_association_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `RubricAssessment`

## POST /v1/courses/{course_id}/rubric_associations

**Create a RubricAssociation**  —  `create_rubricassociation`

Returns the rubric with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `rubric_association[rubric_id]` | integer (int64) | form |  | The id of the Rubric |
| `rubric_association[association_id]` | integer (int64) | form |  | The id of the object with which this rubric is associated |
| `rubric_association[association_type]` | string | form |  | The type of object this rubric is associated with Allowed: `Assignment`, `Course`, `Account` |
| `rubric_association[title]` | string | form |  | The name of the object this rubric is associated with |
| `rubric_association[use_for_grading]` | boolean | form |  | Whether or not the associated rubric is used for grade calculation |
| `rubric_association[hide_score_total]` | boolean | form |  | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. |
| `rubric_association[purpose]` | string | form |  | Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context Allowed: `grading`, `bookmark` |
| `rubric_association[bookmarked]` | boolean | form |  | Whether or not the associated rubric appears in its context |

**Returns:** `RubricAssociation`

## PUT /v1/courses/{course_id}/rubric_associations/{id}

**Update a RubricAssociation**  —  `update_rubricassociation`

Returns the rubric with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | integer (int64) | path | yes | The id of the RubricAssociation to update |
| `rubric_association[rubric_id]` | integer (int64) | form |  | The id of the Rubric |
| `rubric_association[association_id]` | integer (int64) | form |  | The id of the object with which this rubric is associated |
| `rubric_association[association_type]` | string | form |  | The type of object this rubric is associated with Allowed: `Assignment`, `Course`, `Account` |
| `rubric_association[title]` | string | form |  | The name of the object this rubric is associated with |
| `rubric_association[use_for_grading]` | boolean | form |  | Whether or not the associated rubric is used for grade calculation |
| `rubric_association[hide_score_total]` | boolean | form |  | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. |
| `rubric_association[purpose]` | string | form |  | Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context Allowed: `grading`, `bookmark` |
| `rubric_association[bookmarked]` | boolean | form |  | Whether or not the associated rubric appears in its context |

**Returns:** `RubricAssociation`

## DELETE /v1/courses/{course_id}/rubric_associations/{id}

**Delete a RubricAssociation**  —  `delete_rubricassociation`

Delete the RubricAssociation with the given ID

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `RubricAssociation`


---

# Models


## Rubric

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the rubric e.g. `1` |
| `title` | string |  | title of the rubric e.g. `some title` |
| `context_id` | integer |  | the context owning the rubric e.g. `1` |
| `context_type` | string |  | e.g. `Course` |
| `points_possible` | integer |  | e.g. `10.0` |
| `reusable` | boolean |  | e.g. `false` |
| `read_only` | boolean |  | e.g. `true` |
| `free_form_criterion_comments` | boolean |  | whether or not free-form comments are used e.g. `true` |
| `hide_score_total` | boolean |  | e.g. `true` |
| `data` | array[RubricCriterion] |  | An array with all of this Rubric's grading Criteria |
| `assessments` | array[RubricAssessment] |  | If an assessment type is included in the 'include' parameter, includes an array of rubric assessment objects for a given rubric, based on the assessment type requested. If the user does not request an assessment type this key will be absent. |
| `associations` | array[RubricAssociation] |  | If an association type is included in the 'include' parameter, includes an array of rubric association objects for a given rubric, based on the association type requested. If the user does not request an association type this key will be absent. |


## RubricCriterion

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | the ID of the criterion e.g. `_10` |
| `description` | string |  |  |
| `long_description` | string |  |  |
| `points` | integer |  | e.g. `5` |
| `criterion_use_range` | boolean |  | e.g. `false` |
| `ratings` | array[RubricRating] |  | the possible ratings for this Criterion |


## RubricRating

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | e.g. `name_2` |
| `criterion_id` | string |  | e.g. `_10` |
| `description` | string |  |  |
| `long_description` | string |  |  |
| `points` | integer |  | e.g. `5` |


## RubricAssessment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the rubric e.g. `1` |
| `rubric_id` | integer |  | the rubric the assessment belongs to e.g. `1` |
| `rubric_association_id` | integer |  | e.g. `2` |
| `score` | integer |  | e.g. `5.0` |
| `artifact_type` | string |  | the object of the assessment e.g. `Submission` |
| `artifact_id` | integer |  | the id of the object of the assessment e.g. `3` |
| `artifact_attempt` | integer |  | the current number of attempts made on the object of the assessment e.g. `2` |
| `assessment_type` | string |  | the type of assessment. values will be either 'grading', 'peer_review', or 'provisional_grade' e.g. `grading` |
| `assessor_id` | integer |  | user id of the person who made the assessment e.g. `6` |
| `data` | array[object] |  | (Optional) If 'full' is included in the 'style' parameter, returned assessments will have their full details contained in their data hash. If the user does not request a style, this key will be absent. |
| `comments` | array[string] |  | (Optional) If 'comments_only' is included in the 'style' parameter, returned assessments will include only the comments portion of their data hash. If the user does not request a style, this key will be absent. |


## RubricAssociation

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the association e.g. `1` |
| `rubric_id` | integer |  | the ID of the rubric e.g. `1` |
| `association_id` | integer |  | the ID of the object this association links to e.g. `1` |
| `association_type` | string |  | the type of object this association links to e.g. `Course` |
| `use_for_grading` | boolean |  | Whether or not the associated rubric is used for grade calculation e.g. `true` |
| `summary_data` | string |  |  |
| `purpose` | string |  | Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context. Values will be grading or bookmark. e.g. `grading` |
| `hide_score_total` | boolean |  | Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. e.g. `true` |
| `hide_points` | boolean |  | e.g. `true` |
| `hide_outcome_results` | boolean |  | e.g. `true` |
