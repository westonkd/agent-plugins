# Learning Object Dates

> Canvas LMS REST API — `/learning_object_dates` resource. Base path `/api`.

## GET /v1/courses/{course_id}/modules/{context_module_id}/date_details

**Get a learning object's date information**  —  `get_learning_object_s_date_information_modules`

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `context_module_id` | string | path | yes | ID |
| `include` | array[Array] | query |  | Array of strings indicating what additional data to include in the response. Valid values: - "peer_review": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - "child_peer_review_override_dates": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. |
| `exclude` | array[Array] | query |  | Array of strings indicating what data to exclude from the response. Valid values: - "peer_review_overrides": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - "child_override_due_dates": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. |

**Returns:** `LearningObjectDates`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/date_details

**Get a learning object's date information**  —  `get_learning_object_s_date_information_assignments`

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `include` | array[Array] | query |  | Array of strings indicating what additional data to include in the response. Valid values: - "peer_review": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - "child_peer_review_override_dates": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. |
| `exclude` | array[Array] | query |  | Array of strings indicating what data to exclude from the response. Valid values: - "peer_review_overrides": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - "child_override_due_dates": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. |

**Returns:** `LearningObjectDates`

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/date_details

**Get a learning object's date information**  —  `get_learning_object_s_date_information_quizzes`

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `include` | array[Array] | query |  | Array of strings indicating what additional data to include in the response. Valid values: - "peer_review": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - "child_peer_review_override_dates": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. |
| `exclude` | array[Array] | query |  | Array of strings indicating what data to exclude from the response. Valid values: - "peer_review_overrides": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - "child_override_due_dates": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. |

**Returns:** `LearningObjectDates`

## GET /v1/courses/{course_id}/discussion_topics/{discussion_topic_id}/date_details

**Get a learning object's date information**  —  `get_learning_object_s_date_information_discussion_topics`

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `discussion_topic_id` | string | path | yes | ID |
| `include` | array[Array] | query |  | Array of strings indicating what additional data to include in the response. Valid values: - "peer_review": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - "child_peer_review_override_dates": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. |
| `exclude` | array[Array] | query |  | Array of strings indicating what data to exclude from the response. Valid values: - "peer_review_overrides": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - "child_override_due_dates": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. |

**Returns:** `LearningObjectDates`

## GET /v1/courses/{course_id}/pages/{url_or_id}/date_details

**Get a learning object's date information**  —  `get_learning_object_s_date_information_pages`

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `include` | array[Array] | query |  | Array of strings indicating what additional data to include in the response. Valid values: - "peer_review": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - "child_peer_review_override_dates": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. |
| `exclude` | array[Array] | query |  | Array of strings indicating what data to exclude from the response. Valid values: - "peer_review_overrides": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - "child_override_due_dates": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. |

**Returns:** `LearningObjectDates`

## GET /v1/courses/{course_id}/files/{attachment_id}/date_details

**Get a learning object's date information**  —  `get_learning_object_s_date_information_files`

Get a learning object's date-related information, including due date, availability dates,
override status, and a paginated list of all assignment overrides for the item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `attachment_id` | string | path | yes | ID |
| `include` | array[Array] | query |  | Array of strings indicating what additional data to include in the response. Valid values: - "peer_review": includes peer review sub assignment information and overrides in the response.   If a peer review sub assignment exists, it is returned regardless of the Peer Review   Allocation and Grading feature state. If no peer review sub assignment exists,   the feature must be enabled to receive a null value; otherwise the key is omitted. - "child_peer_review_override_dates": each assignment override will include a peer_review_dates   field containing the matched peer review override data (id, due_at, unlock_at, lock_at)   for that override. The field will be present as null if no matching peer review override exists. |
| `exclude` | array[Array] | query |  | Array of strings indicating what data to exclude from the response. Valid values: - "peer_review_overrides": when include[]=peer_review is also specified, the   peer_review_sub_assignment object will not include the overrides array, reducing the   response payload size. This is useful when using include[]=child_peer_review_override_dates   since the peer review override data is already embedded in the parent assignment overrides. - "child_override_due_dates": prevents the sub_assignment_due_dates field from being included   in assignment override responses, even when discussion checkpoints are enabled. This reduces   response payload size when checkpoint due date information is not needed. |

**Returns:** `LearningObjectDates`

## PUT /v1/courses/{course_id}/assignments/{assignment_id}/date_details

**Update a learning object's date information**  —  `update_learning_object_s_date_information_assignments`

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `due_at` | DateTime | form |  | The learning object's due date. Not applicable for ungraded discussions, pages, and files. |
| `unlock_at` | DateTime | form |  | The learning object's unlock date. Must be before the due date if there is one. |
| `lock_at` | DateTime | form |  | The learning object's lock date. Must be after the due date if there is one. |
| `only_visible_to_overrides` | boolean | form |  | Whether the learning object is only assigned to students who are targeted by an override. |
| `assignment_overrides` | array[Array] | form |  | List of overrides to apply to the learning object. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the object's overrides. Keys for each override object can include: 'id', 'title', 'due_at', 'unlock_at', 'lock_at', 'student_ids', and 'course_section_id', 'course_id', 'noop_id', and 'unassign_item'. |
| `peer_review` | Hash | form |  | Optional peer review configuration for assignments with peer reviews enabled. Requires the peer_review_allocation_and_grading feature flag. Keys can include: 'due_at', 'unlock_at', 'lock_at', 'peer_review_overrides' |
| `peer_review[due_at]` | DateTime | form |  | The peer review due date |
| `peer_review[unlock_at]` | DateTime | form |  | The peer review unlock date (when peer reviews become available) |
| `peer_review[lock_at]` | DateTime | form |  | The peer review lock date (when peer reviews are no longer available) |
| `peer_review[peer_review_overrides]` | array[Array] | form |  | List of peer review overrides. Each override can include: 'id', 'due_at', 'unlock_at', 'lock_at', 'student_ids', 'course_section_id', 'course_id', 'group_id', 'unassign_item' |

**Returns:** `void`

## PUT /v1/courses/{course_id}/quizzes/{quiz_id}/date_details

**Update a learning object's date information**  —  `update_learning_object_s_date_information_quizzes`

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `due_at` | DateTime | form |  | The learning object's due date. Not applicable for ungraded discussions, pages, and files. |
| `unlock_at` | DateTime | form |  | The learning object's unlock date. Must be before the due date if there is one. |
| `lock_at` | DateTime | form |  | The learning object's lock date. Must be after the due date if there is one. |
| `only_visible_to_overrides` | boolean | form |  | Whether the learning object is only assigned to students who are targeted by an override. |
| `assignment_overrides` | array[Array] | form |  | List of overrides to apply to the learning object. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the object's overrides. Keys for each override object can include: 'id', 'title', 'due_at', 'unlock_at', 'lock_at', 'student_ids', and 'course_section_id', 'course_id', 'noop_id', and 'unassign_item'. |
| `peer_review` | Hash | form |  | Optional peer review configuration for assignments with peer reviews enabled. Requires the peer_review_allocation_and_grading feature flag. Keys can include: 'due_at', 'unlock_at', 'lock_at', 'peer_review_overrides' |
| `peer_review[due_at]` | DateTime | form |  | The peer review due date |
| `peer_review[unlock_at]` | DateTime | form |  | The peer review unlock date (when peer reviews become available) |
| `peer_review[lock_at]` | DateTime | form |  | The peer review lock date (when peer reviews are no longer available) |
| `peer_review[peer_review_overrides]` | array[Array] | form |  | List of peer review overrides. Each override can include: 'id', 'due_at', 'unlock_at', 'lock_at', 'student_ids', 'course_section_id', 'course_id', 'group_id', 'unassign_item' |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{discussion_topic_id}/date_details

**Update a learning object's date information**  —  `update_learning_object_s_date_information_discussion_topics`

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `discussion_topic_id` | string | path | yes | ID |
| `due_at` | DateTime | form |  | The learning object's due date. Not applicable for ungraded discussions, pages, and files. |
| `unlock_at` | DateTime | form |  | The learning object's unlock date. Must be before the due date if there is one. |
| `lock_at` | DateTime | form |  | The learning object's lock date. Must be after the due date if there is one. |
| `only_visible_to_overrides` | boolean | form |  | Whether the learning object is only assigned to students who are targeted by an override. |
| `assignment_overrides` | array[Array] | form |  | List of overrides to apply to the learning object. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the object's overrides. Keys for each override object can include: 'id', 'title', 'due_at', 'unlock_at', 'lock_at', 'student_ids', and 'course_section_id', 'course_id', 'noop_id', and 'unassign_item'. |
| `peer_review` | Hash | form |  | Optional peer review configuration for assignments with peer reviews enabled. Requires the peer_review_allocation_and_grading feature flag. Keys can include: 'due_at', 'unlock_at', 'lock_at', 'peer_review_overrides' |
| `peer_review[due_at]` | DateTime | form |  | The peer review due date |
| `peer_review[unlock_at]` | DateTime | form |  | The peer review unlock date (when peer reviews become available) |
| `peer_review[lock_at]` | DateTime | form |  | The peer review lock date (when peer reviews are no longer available) |
| `peer_review[peer_review_overrides]` | array[Array] | form |  | List of peer review overrides. Each override can include: 'id', 'due_at', 'unlock_at', 'lock_at', 'student_ids', 'course_section_id', 'course_id', 'group_id', 'unassign_item' |

**Returns:** `void`

## PUT /v1/courses/{course_id}/pages/{url_or_id}/date_details

**Update a learning object's date information**  —  `update_learning_object_s_date_information_pages`

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `url_or_id` | string | path | yes | ID |
| `due_at` | DateTime | form |  | The learning object's due date. Not applicable for ungraded discussions, pages, and files. |
| `unlock_at` | DateTime | form |  | The learning object's unlock date. Must be before the due date if there is one. |
| `lock_at` | DateTime | form |  | The learning object's lock date. Must be after the due date if there is one. |
| `only_visible_to_overrides` | boolean | form |  | Whether the learning object is only assigned to students who are targeted by an override. |
| `assignment_overrides` | array[Array] | form |  | List of overrides to apply to the learning object. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the object's overrides. Keys for each override object can include: 'id', 'title', 'due_at', 'unlock_at', 'lock_at', 'student_ids', and 'course_section_id', 'course_id', 'noop_id', and 'unassign_item'. |
| `peer_review` | Hash | form |  | Optional peer review configuration for assignments with peer reviews enabled. Requires the peer_review_allocation_and_grading feature flag. Keys can include: 'due_at', 'unlock_at', 'lock_at', 'peer_review_overrides' |
| `peer_review[due_at]` | DateTime | form |  | The peer review due date |
| `peer_review[unlock_at]` | DateTime | form |  | The peer review unlock date (when peer reviews become available) |
| `peer_review[lock_at]` | DateTime | form |  | The peer review lock date (when peer reviews are no longer available) |
| `peer_review[peer_review_overrides]` | array[Array] | form |  | List of peer review overrides. Each override can include: 'id', 'due_at', 'unlock_at', 'lock_at', 'student_ids', 'course_section_id', 'course_id', 'group_id', 'unassign_item' |

**Returns:** `void`

## PUT /v1/courses/{course_id}/files/{attachment_id}/date_details

**Update a learning object's date information**  —  `update_learning_object_s_date_information_files`

Updates date-related information for learning objects, including due date, availability dates,
override status, and assignment overrides.

Returns 204 No Content response code if successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `attachment_id` | string | path | yes | ID |
| `due_at` | DateTime | form |  | The learning object's due date. Not applicable for ungraded discussions, pages, and files. |
| `unlock_at` | DateTime | form |  | The learning object's unlock date. Must be before the due date if there is one. |
| `lock_at` | DateTime | form |  | The learning object's lock date. Must be after the due date if there is one. |
| `only_visible_to_overrides` | boolean | form |  | Whether the learning object is only assigned to students who are targeted by an override. |
| `assignment_overrides` | array[Array] | form |  | List of overrides to apply to the learning object. Overrides that already exist should include an ID and will be updated if needed. New overrides will be created for overrides in the list without an ID. Overrides not included in the list will be deleted. Providing an empty list will delete all of the object's overrides. Keys for each override object can include: 'id', 'title', 'due_at', 'unlock_at', 'lock_at', 'student_ids', and 'course_section_id', 'course_id', 'noop_id', and 'unassign_item'. |
| `peer_review` | Hash | form |  | Optional peer review configuration for assignments with peer reviews enabled. Requires the peer_review_allocation_and_grading feature flag. Keys can include: 'due_at', 'unlock_at', 'lock_at', 'peer_review_overrides' |
| `peer_review[due_at]` | DateTime | form |  | The peer review due date |
| `peer_review[unlock_at]` | DateTime | form |  | The peer review unlock date (when peer reviews become available) |
| `peer_review[lock_at]` | DateTime | form |  | The peer review lock date (when peer reviews are no longer available) |
| `peer_review[peer_review_overrides]` | array[Array] | form |  | List of peer review overrides. Each override can include: 'id', 'due_at', 'unlock_at', 'lock_at', 'student_ids', 'course_section_id', 'course_id', 'group_id', 'unassign_item' |

**Returns:** `void`


---

# Models


## LearningObjectDates

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the learning object (not present for checkpoints) e.g. `4` |
| `due_at` | datetime |  | the due date for the learning object. returns null if not present or applicable. never applicable for ungraded discussions, pages, and files e.g. `2012-07-01T23:59:00-06:00` |
| `lock_at` | datetime |  | the lock date (learning object is locked after this date). returns null if not present e.g. `2012-07-01T23:59:00-06:00` |
| `reply_to_topic_due_at` | datetime |  | the reply_to_topic sub_assignment due_date. returns null if not present e.g. `2012-07-01T23:59:00-06:00` |
| `required_replies_due_at` | datetime |  | the reply_to_entry sub_assignment due_date. returns null if not present e.g. `2012-07-01T23:59:00-06:00` |
| `unlock_at` | datetime |  | the unlock date (learning object is unlocked after this date). returns null if not present e.g. `2012-07-01T23:59:00-06:00` |
| `only_visible_to_overrides` | boolean |  | whether the learning object is only visible to overrides e.g. `False` |
| `graded` | boolean |  | whether the learning object is graded (and thus has a due date) e.g. `True` |
| `blueprint_date_locks` | array[string] |  | [exclusive to blueprint child content only] list of lock types e.g. `['due_dates', 'availability_dates']` |
| `visible_to_everyone` | boolean |  | whether the learning object is visible to everyone e.g. `True` |
| `overrides` | array[AssignmentOverride] |  | paginated list of AssignmentOverride objects |
| `checkpoints` | array[LearningObjectDates] |  | list of Checkpoint objects, only present if a learning object has subAssignments |
| `tag` | string |  | the tag identifying the type of checkpoint (only present for checkpoints) e.g. `reply_to_topic` |
| `peer_review_sub_assignment` | object |  | peer review sub assignment details. If a peer review sub assignment exists, it is returned regardless of the Peer Review Allocation and Grading feature state. If no peer review sub assignment exists, the feature must be enabled to receive a null value; otherwise the key is omitted. |
