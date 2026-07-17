# Outcome Groups

> Canvas LMS REST API — `/outcome_groups` resource. Base path `/api`.

## GET /v1/global/root_outcome_group

**Redirect to root outcome group for context**  —  `redirect_to_root_outcome_group_for_context_global`

Convenience redirect to find the root outcome group for a particular
context. Will redirect to the appropriate outcome group's URL.

**Returns:** `void`

## GET /v1/accounts/{account_id}/root_outcome_group

**Redirect to root outcome group for context**  —  `redirect_to_root_outcome_group_for_context_accounts`

Convenience redirect to find the root outcome group for a particular
context. Will redirect to the appropriate outcome group's URL.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/root_outcome_group

**Redirect to root outcome group for context**  —  `redirect_to_root_outcome_group_for_context_courses`

Convenience redirect to find the root outcome group for a particular
context. Will redirect to the appropriate outcome group's URL.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/accounts/{account_id}/outcome_groups

**Get all outcome groups for context**  —  `get_all_outcome_groups_for_context_accounts`

Returns a list of all outcome groups in the specified context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[OutcomeGroup]`

## GET /v1/courses/{course_id}/outcome_groups

**Get all outcome groups for context**  —  `get_all_outcome_groups_for_context_courses`

Returns a list of all outcome groups in the specified context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[OutcomeGroup]`

## GET /v1/accounts/{account_id}/outcome_group_links

**Get all outcome links for context**  —  `get_all_outcome_links_for_context_accounts`

Returns a list of all outcome links in the specified context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `outcome_style` | string | query |  | The detail level of the outcomes. Defaults to "abbrev". Specify "full" for more information. |
| `outcome_group_style` | string | query |  | The detail level of the outcome groups. Defaults to "abbrev". Specify "full" for more information. |

**Returns:** `array[OutcomeLink]`

## GET /v1/courses/{course_id}/outcome_group_links

**Get all outcome links for context**  —  `get_all_outcome_links_for_context_courses`

Returns a list of all outcome links in the specified context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `outcome_style` | string | query |  | The detail level of the outcomes. Defaults to "abbrev". Specify "full" for more information. |
| `outcome_group_style` | string | query |  | The detail level of the outcome groups. Defaults to "abbrev". Specify "full" for more information. |

**Returns:** `array[OutcomeLink]`

## GET /v1/global/outcome_groups/{id}

**Show an outcome group**  —  `show_outcome_group_global`

Returns detailed information about a specific outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeGroup`

## GET /v1/accounts/{account_id}/outcome_groups/{id}

**Show an outcome group**  —  `show_outcome_group_accounts`

Returns detailed information about a specific outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeGroup`

## GET /v1/courses/{course_id}/outcome_groups/{id}

**Show an outcome group**  —  `show_outcome_group_courses`

Returns detailed information about a specific outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeGroup`

## PUT /v1/global/outcome_groups/{id}

**Update an outcome group**  —  `update_outcome_group_global`

Modify an existing outcome group. Fields not provided are left as is;
unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to
the same context as this outcome group, and must not be a descendant of
this outcome group (i.e. no cycles allowed).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `title` | string | form |  | The new outcome group title. |
| `description` | string | form |  | The new outcome group description. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `parent_outcome_group_id` | integer (int64) | form |  | The id of the new parent outcome group. |

**Returns:** `OutcomeGroup`

## PUT /v1/accounts/{account_id}/outcome_groups/{id}

**Update an outcome group**  —  `update_outcome_group_accounts`

Modify an existing outcome group. Fields not provided are left as is;
unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to
the same context as this outcome group, and must not be a descendant of
this outcome group (i.e. no cycles allowed).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `title` | string | form |  | The new outcome group title. |
| `description` | string | form |  | The new outcome group description. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `parent_outcome_group_id` | integer (int64) | form |  | The id of the new parent outcome group. |

**Returns:** `OutcomeGroup`

## PUT /v1/courses/{course_id}/outcome_groups/{id}

**Update an outcome group**  —  `update_outcome_group_courses`

Modify an existing outcome group. Fields not provided are left as is;
unrecognized fields are ignored.

When changing the parent outcome group, the new parent group must belong to
the same context as this outcome group, and must not be a descendant of
this outcome group (i.e. no cycles allowed).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `title` | string | form |  | The new outcome group title. |
| `description` | string | form |  | The new outcome group description. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `parent_outcome_group_id` | integer (int64) | form |  | The id of the new parent outcome group. |

**Returns:** `OutcomeGroup`

## DELETE /v1/global/outcome_groups/{id}

**Delete an outcome group**  —  `delete_outcome_group_global`

Deleting an outcome group deletes descendant outcome groups and outcome
links. The linked outcomes themselves are only deleted if all links to the
outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an
aligned outcome are included in this group's descendants, the group
deletion will fail.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeGroup`

## DELETE /v1/accounts/{account_id}/outcome_groups/{id}

**Delete an outcome group**  —  `delete_outcome_group_accounts`

Deleting an outcome group deletes descendant outcome groups and outcome
links. The linked outcomes themselves are only deleted if all links to the
outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an
aligned outcome are included in this group's descendants, the group
deletion will fail.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeGroup`

## DELETE /v1/courses/{course_id}/outcome_groups/{id}

**Delete an outcome group**  —  `delete_outcome_group_courses`

Deleting an outcome group deletes descendant outcome groups and outcome
links. The linked outcomes themselves are only deleted if all links to the
outcome were deleted.

Aligned outcomes cannot be deleted; as such, if all remaining links to an
aligned outcome are included in this group's descendants, the group
deletion will fail.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `OutcomeGroup`

## GET /v1/global/outcome_groups/{id}/outcomes

**List linked outcomes**  —  `list_linked_outcomes_global`

A paginated list of the immediate OutcomeLink children of the outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `outcome_style` | string | query |  | The detail level of the outcomes. Defaults to "abbrev". Specify "full" for more information. |

**Returns:** `array[OutcomeLink]`

## GET /v1/accounts/{account_id}/outcome_groups/{id}/outcomes

**List linked outcomes**  —  `list_linked_outcomes_accounts`

A paginated list of the immediate OutcomeLink children of the outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_style` | string | query |  | The detail level of the outcomes. Defaults to "abbrev". Specify "full" for more information. |

**Returns:** `array[OutcomeLink]`

## GET /v1/courses/{course_id}/outcome_groups/{id}/outcomes

**List linked outcomes**  —  `list_linked_outcomes_courses`

A paginated list of the immediate OutcomeLink children of the outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_style` | string | query |  | The detail level of the outcomes. Defaults to "abbrev". Specify "full" for more information. |

**Returns:** `array[OutcomeLink]`

## POST /v1/global/outcome_groups/{id}/outcomes

**Create/link an outcome**  —  `create_link_outcome_global`

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `outcome_id` | integer (int64) | form |  | The ID of the existing outcome to link. |
| `move_from` | integer (int64) | form |  | The ID of the old outcome group. Only used if outcome_id is present. |
| `title` | string | form |  | The title of the new outcome. Required if outcome_id is absent. |
| `display_name` | string | form |  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. |
| `description` | string | form |  | The description of the new outcome. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `mastery_points` | integer (int64) | form |  | The mastery threshold for the embedded rubric criterion. |
| `ratings[description]` | array[string] | form |  | The description of a rating level for the embedded rubric criterion. |
| `ratings[points]` | array[integer] | form |  | The points corresponding to a rating level for the embedded rubric criterion. |
| `calculation_method` | string | form |  | The new calculation method.  Defaults to "decaying_average" if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to "weighted_average" Allowed: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average` |
| `calculation_int` | integer (int64) | form |  | The new calculation int.  Only applies if the calculation_method is "weighted_average", "decaying_average" or "n_mastery". Defaults to 65 |

**Returns:** `OutcomeLink`

## PUT /v1/global/outcome_groups/{id}/outcomes/{outcome_id}

**Create/link an outcome**  —  `create_link_outcome_global_outcome_id`

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `outcome_id` | integer (int64) | path | yes | The ID of the existing outcome to link. |
| `move_from` | integer (int64) | form |  | The ID of the old outcome group. Only used if outcome_id is present. |
| `title` | string | form |  | The title of the new outcome. Required if outcome_id is absent. |
| `display_name` | string | form |  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. |
| `description` | string | form |  | The description of the new outcome. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `mastery_points` | integer (int64) | form |  | The mastery threshold for the embedded rubric criterion. |
| `ratings[description]` | array[string] | form |  | The description of a rating level for the embedded rubric criterion. |
| `ratings[points]` | array[integer] | form |  | The points corresponding to a rating level for the embedded rubric criterion. |
| `calculation_method` | string | form |  | The new calculation method.  Defaults to "decaying_average" if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to "weighted_average" Allowed: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average` |
| `calculation_int` | integer (int64) | form |  | The new calculation int.  Only applies if the calculation_method is "weighted_average", "decaying_average" or "n_mastery". Defaults to 65 |

**Returns:** `OutcomeLink`

## POST /v1/accounts/{account_id}/outcome_groups/{id}/outcomes

**Create/link an outcome**  —  `create_link_outcome_accounts`

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_id` | integer (int64) | form |  | The ID of the existing outcome to link. |
| `move_from` | integer (int64) | form |  | The ID of the old outcome group. Only used if outcome_id is present. |
| `title` | string | form |  | The title of the new outcome. Required if outcome_id is absent. |
| `display_name` | string | form |  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. |
| `description` | string | form |  | The description of the new outcome. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `mastery_points` | integer (int64) | form |  | The mastery threshold for the embedded rubric criterion. |
| `ratings[description]` | array[string] | form |  | The description of a rating level for the embedded rubric criterion. |
| `ratings[points]` | array[integer] | form |  | The points corresponding to a rating level for the embedded rubric criterion. |
| `calculation_method` | string | form |  | The new calculation method.  Defaults to "decaying_average" if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to "weighted_average" Allowed: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average` |
| `calculation_int` | integer (int64) | form |  | The new calculation int.  Only applies if the calculation_method is "weighted_average", "decaying_average" or "n_mastery". Defaults to 65 |

**Returns:** `OutcomeLink`

## PUT /v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id}

**Create/link an outcome**  —  `create_link_outcome_accounts_outcome_id`

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_id` | integer (int64) | path | yes | The ID of the existing outcome to link. |
| `move_from` | integer (int64) | form |  | The ID of the old outcome group. Only used if outcome_id is present. |
| `title` | string | form |  | The title of the new outcome. Required if outcome_id is absent. |
| `display_name` | string | form |  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. |
| `description` | string | form |  | The description of the new outcome. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `mastery_points` | integer (int64) | form |  | The mastery threshold for the embedded rubric criterion. |
| `ratings[description]` | array[string] | form |  | The description of a rating level for the embedded rubric criterion. |
| `ratings[points]` | array[integer] | form |  | The points corresponding to a rating level for the embedded rubric criterion. |
| `calculation_method` | string | form |  | The new calculation method.  Defaults to "decaying_average" if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to "weighted_average" Allowed: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average` |
| `calculation_int` | integer (int64) | form |  | The new calculation int.  Only applies if the calculation_method is "weighted_average", "decaying_average" or "n_mastery". Defaults to 65 |

**Returns:** `OutcomeLink`

## POST /v1/courses/{course_id}/outcome_groups/{id}/outcomes

**Create/link an outcome**  —  `create_link_outcome_courses`

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_id` | integer (int64) | form |  | The ID of the existing outcome to link. |
| `move_from` | integer (int64) | form |  | The ID of the old outcome group. Only used if outcome_id is present. |
| `title` | string | form |  | The title of the new outcome. Required if outcome_id is absent. |
| `display_name` | string | form |  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. |
| `description` | string | form |  | The description of the new outcome. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `mastery_points` | integer (int64) | form |  | The mastery threshold for the embedded rubric criterion. |
| `ratings[description]` | array[string] | form |  | The description of a rating level for the embedded rubric criterion. |
| `ratings[points]` | array[integer] | form |  | The points corresponding to a rating level for the embedded rubric criterion. |
| `calculation_method` | string | form |  | The new calculation method.  Defaults to "decaying_average" if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to "weighted_average" Allowed: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average` |
| `calculation_int` | integer (int64) | form |  | The new calculation int.  Only applies if the calculation_method is "weighted_average", "decaying_average" or "n_mastery". Defaults to 65 |

**Returns:** `OutcomeLink`

## PUT /v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id}

**Create/link an outcome**  —  `create_link_outcome_courses_outcome_id`

Link an outcome into the outcome group. The outcome to link can either be
specified by a PUT to the link URL for a specific outcome (the outcome_id
in the PUT URLs) or by supplying the information for a new outcome (title,
description, ratings, mastery_points) in a POST to the collection.

If linking an existing outcome, the outcome_id must identify an outcome
available to this context; i.e. an outcome owned by this group's context,
an outcome owned by an associated account, or a global outcome. With
outcome_id present, any other parameters (except move_from) are ignored.

If defining a new outcome, the outcome is created in the outcome group's
context using the provided title, description, ratings, and mastery points;
the title is required but all other fields are optional. The new outcome
is then linked into the outcome group.

If ratings are provided when creating a new outcome, an embedded rubric
criterion is included in the new outcome. This criterion's mastery_points
default to the maximum points in the highest rating if not specified in the
mastery_points parameter. Any ratings lacking a description are given a
default of "No description". Any ratings lacking a point value are given a
default of 0. If no ratings are provided, the mastery_points parameter is
ignored.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_id` | integer (int64) | path | yes | The ID of the existing outcome to link. |
| `move_from` | integer (int64) | form |  | The ID of the old outcome group. Only used if outcome_id is present. |
| `title` | string | form |  | The title of the new outcome. Required if outcome_id is absent. |
| `display_name` | string | form |  | A friendly name shown in reports for outcomes with cryptic titles, such as common core standards names. |
| `description` | string | form |  | The description of the new outcome. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard. |
| `mastery_points` | integer (int64) | form |  | The mastery threshold for the embedded rubric criterion. |
| `ratings[description]` | array[string] | form |  | The description of a rating level for the embedded rubric criterion. |
| `ratings[points]` | array[integer] | form |  | The points corresponding to a rating level for the embedded rubric criterion. |
| `calculation_method` | string | form |  | The new calculation method.  Defaults to "decaying_average" if the Outcomes New Decaying Average Calculation Method FF is ENABLED then Defaults to "weighted_average" Allowed: `weighted_average`, `decaying_average`, `n_mastery`, `latest`, `highest`, `average` |
| `calculation_int` | integer (int64) | form |  | The new calculation int.  Only applies if the calculation_method is "weighted_average", "decaying_average" or "n_mastery". Defaults to 65 |

**Returns:** `OutcomeLink`

## DELETE /v1/global/outcome_groups/{id}/outcomes/{outcome_id}

**Unlink an outcome**  —  `unlink_outcome_global`

Unlinking an outcome only deletes the outcome itself if this was the last
link to the outcome in any group in any context. Aligned outcomes cannot be
deleted; as such, if this is the last link to an aligned outcome, the
unlinking will fail.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `outcome_id` | string | path | yes | ID |

**Returns:** `OutcomeLink`

## DELETE /v1/accounts/{account_id}/outcome_groups/{id}/outcomes/{outcome_id}

**Unlink an outcome**  —  `unlink_outcome_accounts`

Unlinking an outcome only deletes the outcome itself if this was the last
link to the outcome in any group in any context. Aligned outcomes cannot be
deleted; as such, if this is the last link to an aligned outcome, the
unlinking will fail.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_id` | string | path | yes | ID |

**Returns:** `OutcomeLink`

## DELETE /v1/courses/{course_id}/outcome_groups/{id}/outcomes/{outcome_id}

**Unlink an outcome**  —  `unlink_outcome_courses`

Unlinking an outcome only deletes the outcome itself if this was the last
link to the outcome in any group in any context. Aligned outcomes cannot be
deleted; as such, if this is the last link to an aligned outcome, the
unlinking will fail.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `outcome_id` | string | path | yes | ID |

**Returns:** `OutcomeLink`

## GET /v1/global/outcome_groups/{id}/subgroups

**List subgroups**  —  `list_subgroups_global`

A paginated list of the immediate OutcomeGroup children of the outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `array[OutcomeGroup]`

## GET /v1/accounts/{account_id}/outcome_groups/{id}/subgroups

**List subgroups**  —  `list_subgroups_accounts`

A paginated list of the immediate OutcomeGroup children of the outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array[OutcomeGroup]`

## GET /v1/courses/{course_id}/outcome_groups/{id}/subgroups

**List subgroups**  —  `list_subgroups_courses`

A paginated list of the immediate OutcomeGroup children of the outcome group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `array[OutcomeGroup]`

## POST /v1/global/outcome_groups/{id}/subgroups

**Create a subgroup**  —  `create_subgroup_global`

Creates a new empty subgroup under the outcome group with the given title
and description.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `title` | string | form | yes | The title of the new outcome group. |
| `description` | string | form |  | The description of the new outcome group. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard |

**Returns:** `OutcomeGroup`

## POST /v1/accounts/{account_id}/outcome_groups/{id}/subgroups

**Create a subgroup**  —  `create_subgroup_accounts`

Creates a new empty subgroup under the outcome group with the given title
and description.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `title` | string | form | yes | The title of the new outcome group. |
| `description` | string | form |  | The description of the new outcome group. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard |

**Returns:** `OutcomeGroup`

## POST /v1/courses/{course_id}/outcome_groups/{id}/subgroups

**Create a subgroup**  —  `create_subgroup_courses`

Creates a new empty subgroup under the outcome group with the given title
and description.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `title` | string | form | yes | The title of the new outcome group. |
| `description` | string | form |  | The description of the new outcome group. |
| `vendor_guid` | string | form |  | A custom GUID for the learning standard |

**Returns:** `OutcomeGroup`

## POST /v1/global/outcome_groups/{id}/import

**Import an outcome group**  —  `import_outcome_group_global`

Creates a new subgroup of the outcome group with the same title and
description as the source group, then creates links in that new subgroup to
the same outcomes that are linked in the source group. Recurses on the
subgroups of the source group, importing them each in turn into the new
subgroup.

Allows you to copy organizational structure, but does not create copies of
the outcomes themselves, only new links.

The source group must be either global, from the same context as this
outcome group, or from an associated account. The source group cannot be
the root outcome group of its context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `source_outcome_group_id` | integer (int64) | form | yes | The ID of the source outcome group. |
| `async` | boolean | form |  | If true, perform action asynchronously.  In that case, this endpoint will return a Progress object instead of an OutcomeGroup. Use the {api:ProgressController#show progress endpoint} to query the status of the operation.  The imported outcome group id and url will be returned in the results of the Progress object as "outcome_group_id" and "outcome_group_url" |

**Returns:** `OutcomeGroup`

## POST /v1/accounts/{account_id}/outcome_groups/{id}/import

**Import an outcome group**  —  `import_outcome_group_accounts`

Creates a new subgroup of the outcome group with the same title and
description as the source group, then creates links in that new subgroup to
the same outcomes that are linked in the source group. Recurses on the
subgroups of the source group, importing them each in turn into the new
subgroup.

Allows you to copy organizational structure, but does not create copies of
the outcomes themselves, only new links.

The source group must be either global, from the same context as this
outcome group, or from an associated account. The source group cannot be
the root outcome group of its context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `source_outcome_group_id` | integer (int64) | form | yes | The ID of the source outcome group. |
| `async` | boolean | form |  | If true, perform action asynchronously.  In that case, this endpoint will return a Progress object instead of an OutcomeGroup. Use the {api:ProgressController#show progress endpoint} to query the status of the operation.  The imported outcome group id and url will be returned in the results of the Progress object as "outcome_group_id" and "outcome_group_url" |

**Returns:** `OutcomeGroup`

## POST /v1/courses/{course_id}/outcome_groups/{id}/import

**Import an outcome group**  —  `import_outcome_group_courses`

Creates a new subgroup of the outcome group with the same title and
description as the source group, then creates links in that new subgroup to
the same outcomes that are linked in the source group. Recurses on the
subgroups of the source group, importing them each in turn into the new
subgroup.

Allows you to copy organizational structure, but does not create copies of
the outcomes themselves, only new links.

The source group must be either global, from the same context as this
outcome group, or from an associated account. The source group cannot be
the root outcome group of its context.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `source_outcome_group_id` | integer (int64) | form | yes | The ID of the source outcome group. |
| `async` | boolean | form |  | If true, perform action asynchronously.  In that case, this endpoint will return a Progress object instead of an OutcomeGroup. Use the {api:ProgressController#show progress endpoint} to query the status of the operation.  The imported outcome group id and url will be returned in the results of the Progress object as "outcome_group_id" and "outcome_group_url" |

**Returns:** `OutcomeGroup`


---

# Models


## OutcomeGroup

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the outcome group e.g. `1` |
| `url` | string |  | the URL for fetching/updating the outcome group. should be treated as opaque e.g. `/api/v1/accounts/1/outcome_groups/1` |
| `parent_outcome_group` | OutcomeGroup |  | an abbreviated OutcomeGroup object representing the parent group of this outcome group, if any. omitted in the abbreviated form. |
| `context_id` | integer |  | the context owning the outcome group. may be null for global outcome groups. omitted in the abbreviated form. e.g. `1` |
| `context_type` | string |  | e.g. `Account` |
| `title` | string |  | title of the outcome group e.g. `Outcome group title` |
| `description` | string |  | description of the outcome group. omitted in the abbreviated form. e.g. `Outcome group description` |
| `vendor_guid` | string |  | A custom GUID for the learning standard. e.g. `customid9000` |
| `subgroups_url` | string |  | the URL for listing/creating subgroups under the outcome group. should be treated as opaque e.g. `/api/v1/accounts/1/outcome_groups/1/subgroups` |
| `outcomes_url` | string |  | the URL for listing/creating outcome links under the outcome group. should be treated as opaque e.g. `/api/v1/accounts/1/outcome_groups/1/outcomes` |
| `import_url` | string |  | the URL for importing another group into this outcome group. should be treated as opaque. omitted in the abbreviated form. e.g. `/api/v1/accounts/1/outcome_groups/1/import` |
| `can_edit` | boolean |  | whether the current user can update the outcome group e.g. `True` |


## OutcomeLink

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `url` | string |  | the URL for fetching/updating the outcome link. should be treated as opaque e.g. `/api/v1/accounts/1/outcome_groups/1/outcomes/1` |
| `context_id` | integer |  | the context owning the outcome link. will match the context owning the outcome group containing the outcome link; included for convenience. may be null for links in global outcome groups. e.g. `1` |
| `context_type` | string |  | e.g. `Account` |
| `outcome_group` | OutcomeGroup |  | an abbreviated OutcomeGroup object representing the group containing the outcome link. |
| `outcome` | Outcome |  | an abbreviated Outcome object representing the outcome linked into the containing outcome group. |
| `assessed` | boolean |  | whether this outcome has been used to assess a student in the context of this outcome link.  In other words, this will be set to true if the context is a course, and a student has been assessed with this outcome in that course. e.g. `True` |
| `can_unlink` | boolean |  | whether this outcome link is manageable and is not the last link to an aligned outcome |
