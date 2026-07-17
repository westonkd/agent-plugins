# Discussion Topics

> Canvas LMS REST API — `/discussion_topics` resource. Base path `/api`.

## GET /v1/courses/{course_id}/discussion_topics

**List discussion topics**  —  `list_discussion_topics_courses`

Returns the paginated list of discussion topics for this course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include` | array[string] | query |  | If "all_dates" is passed, all dates associated with graded discussions' assignments will be included. if "sections" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If "sections_user_count" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If "overrides" is passed, the overrides for the assignment will be included Allowed: `all_dates`, `sections`, `sections_user_count`, `overrides` |
| `order_by` | string | query |  | Determines the order of the discussion topic list. Defaults to "position". Allowed: `position`, `recent_activity`, `title` |
| `scope` | string | query |  | Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string. Allowed: `locked`, `unlocked`, `pinned`, `unpinned` |
| `only_announcements` | boolean | query |  | Return announcements instead of discussion topics. Defaults to false |
| `filter_by` | string | query |  | The state of the discussion topic to return. Currently only supports unread state. Allowed: `all`, `unread` |
| `search_term` | string | query |  | The partial title of the discussion topics to match and return. |
| `exclude_context_module_locked_topics` | boolean | query |  | For students, exclude topics that are locked by module progression. Defaults to false. |

**Returns:** `array[DiscussionTopic]`

## GET /v1/groups/{group_id}/discussion_topics

**List discussion topics**  —  `list_discussion_topics_groups`

Returns the paginated list of discussion topics for this course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `include` | array[string] | query |  | If "all_dates" is passed, all dates associated with graded discussions' assignments will be included. if "sections" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If "sections_user_count" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If "overrides" is passed, the overrides for the assignment will be included Allowed: `all_dates`, `sections`, `sections_user_count`, `overrides` |
| `order_by` | string | query |  | Determines the order of the discussion topic list. Defaults to "position". Allowed: `position`, `recent_activity`, `title` |
| `scope` | string | query |  | Only return discussion topics in the given state(s). Defaults to including all topics. Filtering is done after pagination, so pages may be smaller than requested if topics are filtered. Can pass multiple states as comma separated string. Allowed: `locked`, `unlocked`, `pinned`, `unpinned` |
| `only_announcements` | boolean | query |  | Return announcements instead of discussion topics. Defaults to false |
| `filter_by` | string | query |  | The state of the discussion topic to return. Currently only supports unread state. Allowed: `all`, `unread` |
| `search_term` | string | query |  | The partial title of the discussion topics to match and return. |
| `exclude_context_module_locked_topics` | boolean | query |  | For students, exclude topics that are locked by module progression. Defaults to false. |

**Returns:** `array[DiscussionTopic]`

## POST /v1/courses/{course_id}/discussion_topics

**Create a new discussion topic**  —  `create_new_discussion_topic_courses`

Create an new discussion topic for the course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `title` | string | form |  | no description |
| `message` | string | form |  | no description |
| `discussion_type` | string | form |  | The type of discussion. Defaults to side_comment or not_threaded if not value is given. Accepted values are 'side_comment', 'not_threaded' for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions. Allowed: `side_comment`, `threaded`, `not_threaded` |
| `published` | boolean | form |  | Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics. |
| `delayed_post_at` | DateTime | form |  | If a timestamp is given, the topic will not be published until that time. |
| `allow_rating` | boolean | form |  | Whether or not users can rate entries in this topic. |
| `lock_at` | DateTime | form |  | If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked. |
| `podcast_enabled` | boolean | form |  | If true, the topic will have an associated podcast feed. |
| `podcast_has_student_posts` | boolean | form |  | If true, the podcast will include posts from students as well. Implies podcast_enabled. |
| `require_initial_post` | boolean | form |  | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. |
| `assignment` | Assignment | form |  | To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it's taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object |
| `is_announcement` | boolean | form |  | If true, this topic is an announcement. It will appear in the announcement's section rather than the discussions section. This requires announcment-posting permissions. |
| `pinned` | boolean | form |  | If true, this topic will be listed in the "Pinned Discussion" section |
| `position_after` | string | form |  | By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed. |
| `group_category_id` | integer (int64) | form |  | If present, the topic will become a group discussion assigned to the group. |
| `only_graders_can_rate` | boolean | form |  | If true, only graders will be allowed to rate entries. |
| `sort_order` | string | form |  | Default sort order of the discussion. Accepted values are "asc", "desc". Allowed: `asc`, `desc` |
| `sort_order_locked` | boolean | form |  | If true, users cannot choose their prefered sort order |
| `expanded` | boolean | form |  | If true, thread will be expanded by default |
| `expanded_locked` | boolean | form |  | If true, users cannot choose their prefered thread expansion setting |
| `sort_by_rating` | boolean | form |  | (DEPRECATED) If true, entries will be sorted by rating. |
| `attachment` | File | form |  | A multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |
| `specific_sections` | string | form |  | A comma-separated list of sections ids to which the discussion topic should be made specific to.  If it is not desired to make the discussion topic specific to sections, then this parameter may be omitted or set to "all".  Can only be present only on announcements and only those that are for a course (as opposed to a group). |
| `lock_comment` | boolean | form |  | If is_announcement and lock_comment are true, ‘Allow Participants to Comment’ setting is disabled. |

**Returns:** `void`

## POST /v1/groups/{group_id}/discussion_topics

**Create a new discussion topic**  —  `create_new_discussion_topic_groups`

Create an new discussion topic for the course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `title` | string | form |  | no description |
| `message` | string | form |  | no description |
| `discussion_type` | string | form |  | The type of discussion. Defaults to side_comment or not_threaded if not value is given. Accepted values are 'side_comment', 'not_threaded' for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions. Allowed: `side_comment`, `threaded`, `not_threaded` |
| `published` | boolean | form |  | Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics. |
| `delayed_post_at` | DateTime | form |  | If a timestamp is given, the topic will not be published until that time. |
| `allow_rating` | boolean | form |  | Whether or not users can rate entries in this topic. |
| `lock_at` | DateTime | form |  | If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked. |
| `podcast_enabled` | boolean | form |  | If true, the topic will have an associated podcast feed. |
| `podcast_has_student_posts` | boolean | form |  | If true, the podcast will include posts from students as well. Implies podcast_enabled. |
| `require_initial_post` | boolean | form |  | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. |
| `assignment` | Assignment | form |  | To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it's taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object |
| `is_announcement` | boolean | form |  | If true, this topic is an announcement. It will appear in the announcement's section rather than the discussions section. This requires announcment-posting permissions. |
| `pinned` | boolean | form |  | If true, this topic will be listed in the "Pinned Discussion" section |
| `position_after` | string | form |  | By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed. |
| `group_category_id` | integer (int64) | form |  | If present, the topic will become a group discussion assigned to the group. |
| `only_graders_can_rate` | boolean | form |  | If true, only graders will be allowed to rate entries. |
| `sort_order` | string | form |  | Default sort order of the discussion. Accepted values are "asc", "desc". Allowed: `asc`, `desc` |
| `sort_order_locked` | boolean | form |  | If true, users cannot choose their prefered sort order |
| `expanded` | boolean | form |  | If true, thread will be expanded by default |
| `expanded_locked` | boolean | form |  | If true, users cannot choose their prefered thread expansion setting |
| `sort_by_rating` | boolean | form |  | (DEPRECATED) If true, entries will be sorted by rating. |
| `attachment` | File | form |  | A multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |
| `specific_sections` | string | form |  | A comma-separated list of sections ids to which the discussion topic should be made specific to.  If it is not desired to make the discussion topic specific to sections, then this parameter may be omitted or set to "all".  Can only be present only on announcements and only those that are for a course (as opposed to a group). |
| `lock_comment` | boolean | form |  | If is_announcement and lock_comment are true, ‘Allow Participants to Comment’ setting is disabled. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{topic_id}

**Update a topic**  —  `update_topic_courses`

Update an existing discussion topic for the course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `title` | string | form |  | no description |
| `message` | string | form |  | no description |
| `discussion_type` | string | form |  | The type of discussion. Defaults to side_comment or not_threaded if not value is given. Accepted values are 'side_comment', 'not_threaded' for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions. Allowed: `side_comment`, `threaded`, `not_threaded` |
| `published` | boolean | form |  | Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics. |
| `delayed_post_at` | DateTime | form |  | If a timestamp is given, the topic will not be published until that time. |
| `lock_at` | DateTime | form |  | If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked. |
| `podcast_enabled` | boolean | form |  | If true, the topic will have an associated podcast feed. |
| `podcast_has_student_posts` | boolean | form |  | If true, the podcast will include posts from students as well. Implies podcast_enabled. |
| `require_initial_post` | boolean | form |  | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. |
| `assignment` | Assignment | form |  | To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it's taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object |
| `is_announcement` | boolean | form |  | If true, this topic is an announcement. It will appear in the announcement's section rather than the discussions section. This requires announcment-posting permissions. |
| `pinned` | boolean | form |  | If true, this topic will be listed in the "Pinned Discussion" section |
| `position_after` | string | form |  | By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed. |
| `group_category_id` | integer (int64) | form |  | If present, the topic will become a group discussion assigned to the group. |
| `allow_rating` | boolean | form |  | If true, users will be allowed to rate entries. |
| `only_graders_can_rate` | boolean | form |  | If true, only graders will be allowed to rate entries. |
| `sort_order` | string | form |  | Default sort order of the discussion. Accepted values are "asc", "desc". Allowed: `asc`, `desc` |
| `sort_order_locked` | boolean | form |  | If true, users cannot choose their prefered sort order |
| `expanded` | boolean | form |  | If true, thread will be expanded by default |
| `expanded_locked` | boolean | form |  | If true, users cannot choose their prefered thread expansion setting |
| `sort_by_rating` | boolean | form |  | (DEPRECATED) If true, entries will be sorted by rating. |
| `specific_sections` | string | form |  | A comma-separated list of sections ids to which the discussion topic should be made specific too.  If it is not desired to make the discussion topic specific to sections, then this parameter may be omitted or set to "all".  Can only be present only on announcements and only those that are for a course (as opposed to a group). |
| `lock_comment` | boolean | form |  | If is_announcement and lock_comment are true, ‘Allow Participants to Comment’ setting is disabled. |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/{topic_id}

**Update a topic**  —  `update_topic_groups`

Update an existing discussion topic for the course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `title` | string | form |  | no description |
| `message` | string | form |  | no description |
| `discussion_type` | string | form |  | The type of discussion. Defaults to side_comment or not_threaded if not value is given. Accepted values are 'side_comment', 'not_threaded' for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions. Allowed: `side_comment`, `threaded`, `not_threaded` |
| `published` | boolean | form |  | Whether this topic is published (true) or draft state (false). Only teachers and TAs have the ability to create draft state topics. |
| `delayed_post_at` | DateTime | form |  | If a timestamp is given, the topic will not be published until that time. |
| `lock_at` | DateTime | form |  | If a timestamp is given, the topic will be scheduled to lock at the provided timestamp. If the timestamp is in the past, the topic will be locked. |
| `podcast_enabled` | boolean | form |  | If true, the topic will have an associated podcast feed. |
| `podcast_has_student_posts` | boolean | form |  | If true, the podcast will include posts from students as well. Implies podcast_enabled. |
| `require_initial_post` | boolean | form |  | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. |
| `assignment` | Assignment | form |  | To create an assignment discussion, pass the assignment parameters as a sub-object. See the {api:AssignmentsApiController#create Create an Assignment API} for the available parameters. The name parameter will be ignored, as it's taken from the discussion title. If you want to make a discussion that was an assignment NOT an assignment, pass set_assignment = false as part of the assignment object |
| `is_announcement` | boolean | form |  | If true, this topic is an announcement. It will appear in the announcement's section rather than the discussions section. This requires announcment-posting permissions. |
| `pinned` | boolean | form |  | If true, this topic will be listed in the "Pinned Discussion" section |
| `position_after` | string | form |  | By default, discussions are sorted chronologically by creation date, you can pass the id of another topic to have this one show up after the other when they are listed. |
| `group_category_id` | integer (int64) | form |  | If present, the topic will become a group discussion assigned to the group. |
| `allow_rating` | boolean | form |  | If true, users will be allowed to rate entries. |
| `only_graders_can_rate` | boolean | form |  | If true, only graders will be allowed to rate entries. |
| `sort_order` | string | form |  | Default sort order of the discussion. Accepted values are "asc", "desc". Allowed: `asc`, `desc` |
| `sort_order_locked` | boolean | form |  | If true, users cannot choose their prefered sort order |
| `expanded` | boolean | form |  | If true, thread will be expanded by default |
| `expanded_locked` | boolean | form |  | If true, users cannot choose their prefered thread expansion setting |
| `sort_by_rating` | boolean | form |  | (DEPRECATED) If true, entries will be sorted by rating. |
| `specific_sections` | string | form |  | A comma-separated list of sections ids to which the discussion topic should be made specific too.  If it is not desired to make the discussion topic specific to sections, then this parameter may be omitted or set to "all".  Can only be present only on announcements and only those that are for a course (as opposed to a group). |
| `lock_comment` | boolean | form |  | If is_announcement and lock_comment are true, ‘Allow Participants to Comment’ setting is disabled. |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/discussion_topics/{topic_id}

**Delete a topic**  —  `delete_topic_courses`

Deletes the discussion topic. This will also delete the assignment, if it's
an assignment discussion.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/discussion_topics/{topic_id}

**Delete a topic**  —  `delete_topic_groups`

Deletes the discussion topic. This will also delete the assignment, if it's
an assignment discussion.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/discussion_topics/reorder

**Reorder pinned topics**  —  `reorder_pinned_topics_courses`

Puts the pinned discussion topics in the specified order.
All pinned topics should be included.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `order` | array[integer] | form | yes | The ids of the pinned discussion topics in the desired order. (For example, "order=104,102,103".) |

**Returns:** `void`

## POST /v1/groups/{group_id}/discussion_topics/reorder

**Reorder pinned topics**  —  `reorder_pinned_topics_groups`

Puts the pinned discussion topics in the specified order.
All pinned topics should be included.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `order` | array[integer] | form | yes | The ids of the pinned discussion topics in the desired order. (For example, "order=104,102,103".) |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}

**Update an entry**  —  `update_entry_courses`

Update an existing discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `message` | string | form |  | The updated body of the entry. |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id}

**Update an entry**  —  `update_entry_groups`

Update an existing discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the edit is not allowed, a 401 will be returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `message` | string | form |  | The updated body of the entry. |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}

**Delete an entry**  —  `delete_entry_courses`

Delete a discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.

The discussion will be marked deleted, and the user_id and message will be cleared out.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{id}

**Delete an entry**  —  `delete_entry_groups`

Delete a discussion entry.

The entry must have been created by the current user, or the current user
must have admin rights to the discussion. If the delete is not allowed, a 401 will be returned.

The discussion will be marked deleted, and the user_id and message will be cleared out.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/discussion_topics/{topic_id}

**Get a single topic**  —  `get_single_topic_courses`

Returns data on an individual discussion topic. See the List action for the response formatting.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `include` | array[string] | query |  | If "all_dates" is passed, all dates associated with graded discussions' assignments will be included. if "sections" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If "sections_user_count" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If "overrides" is passed, the overrides for the assignment will be included Allowed: `all_dates`, `sections`, `sections_user_count`, `overrides` |

**Returns:** `void`

## GET /v1/groups/{group_id}/discussion_topics/{topic_id}

**Get a single topic**  —  `get_single_topic_groups`

Returns data on an individual discussion topic. See the List action for the response formatting.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `include` | array[string] | query |  | If "all_dates" is passed, all dates associated with graded discussions' assignments will be included. if "sections" is passed, includes the course sections that are associated with the topic, if the topic is specific to certain sections of the course. If "sections_user_count" is passed, then:   (a) If sections were asked for *and* the topic is specific to certain       course sections, includes the number of users in each       section. (as part of the section json asked for above)   (b) Else, includes at the root level the total number of users in the       topic's context (group or course) that the topic applies to. If "overrides" is passed, the overrides for the assignment will be included Allowed: `all_dates`, `sections`, `sections_user_count`, `overrides` |

**Returns:** `void`

## GET /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries

**Find Last Summary**  —  `find_last_summary_courses`

Returns:
(1) last userInput (what current user had keyed in to produce the last discussion summary),
(2) last discussion summary generated by the current user for current discussion topic, based on userInput,
(3) and some usage information.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries

**Find Last Summary**  —  `find_last_summary_groups`

Returns:
(1) last userInput (what current user had keyed in to produce the last discussion summary),
(2) last discussion summary generated by the current user for current discussion topic, based on userInput,
(3) and some usage information.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries

**Find or Create Summary**  —  `find_or_create_summary_courses`

Generates a summary for a discussion topic. Returns the summary text and usage information.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `userInput` | string | form |  | Areas or topics for the summary to focus on. |

**Returns:** `void`

## POST /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries

**Find or Create Summary**  —  `find_or_create_summary_groups`

Generates a summary for a discussion topic. Returns the summary text and usage information.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `userInput` | string | form |  | Areas or topics for the summary to focus on. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries/disable

**Disable summary**  —  `disable_summary_courses`

Deprecated, to remove after VICE-5047 gets merged
Disables the summary for a discussion topic.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries/disable

**Disable summary**  —  `disable_summary_groups`

Deprecated, to remove after VICE-5047 gets merged
Disables the summary for a discussion topic.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/discussion_topics/{topic_id}/summaries/{summary_id}/feedback

**Summary Feedback**  —  `summary_feedback_courses`

Persists feedback on a discussion topic summary.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `summary_id` | string | path | yes | ID |
| `_action` | string | form |  | Required The action to take on the summary. Possible values are: - "seen": Marks the summary as seen. This action saves the feedback if it's not already persisted. - "like": Marks the summary as liked. - "dislike": Marks the summary as disliked. - "add_comment": Adds a written comment to a disliked summary. Requires the "comment" parameter. - "reset_like": Resets the like status of the summary. - "regenerate": Regenerates the summary feedback. - "disable_summary": Disables the summary feedback. Any other value will result in an error response. |
| `comment` | string | form |  | Optional A written explanation for the dislike. Only used with the "add_comment" action. Maximum 1024 characters. |

**Returns:** `void`

## POST /v1/groups/{group_id}/discussion_topics/{topic_id}/summaries/{summary_id}/feedback

**Summary Feedback**  —  `summary_feedback_groups`

Persists feedback on a discussion topic summary.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `summary_id` | string | path | yes | ID |
| `_action` | string | form |  | Required The action to take on the summary. Possible values are: - "seen": Marks the summary as seen. This action saves the feedback if it's not already persisted. - "like": Marks the summary as liked. - "dislike": Marks the summary as disliked. - "add_comment": Adds a written comment to a disliked summary. Requires the "comment" parameter. - "reset_like": Resets the like status of the summary. - "regenerate": Regenerates the summary feedback. - "disable_summary": Disables the summary feedback. Any other value will result in an error response. |
| `comment` | string | form |  | Optional A written explanation for the dislike. Only used with the "add_comment" action. Maximum 1024 characters. |

**Returns:** `void`

## GET /v1/courses/{course_id}/discussion_topics/{topic_id}/view

**Get the full topic**  —  `get_full_topic_courses`

Return a cached structure of the discussion topic, containing all entries,
their authors, and their message bodies.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

In some rare situations, this cached structure may not be available yet. In
that case, the server will respond with a 503 error, and the caller should
try again soon.

The response is an object containing the following keys:
* "participants": A list of summary information on users who have posted to
  the discussion. Each value is an object containing their id, display_name,
  and avatar_url.
* "unread_entries": A list of entry ids that are unread by the current
  user. this implies that any entry not in this list is read.
* "entry_ratings": A map of entry ids to ratings by the current user. Entries
  not in this list have no rating. Only populated if rating is enabled.
* "forced_entries": A list of entry ids that have forced_read_state set to
  true. This flag is meant to indicate the entry's read_state has been
  manually set to 'unread' by the user, so the entry should not be
  automatically marked as read.
* "view": A threaded view of all the entries in the discussion, containing
  the id, user_id, and message.
* "new_entries": Because this view is eventually consistent, it's possible
  that newly created or updated entries won't yet be reflected in the view.
  If the application wants to also get a flat list of all entries not yet
  reflected in the view, pass include_new_entries=1 to the request and this
  array of entries will be returned. These entries are returned in a flat
  array, in ascending created_at order.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/groups/{group_id}/discussion_topics/{topic_id}/view

**Get the full topic**  —  `get_full_topic_groups`

Return a cached structure of the discussion topic, containing all entries,
their authors, and their message bodies.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

In some rare situations, this cached structure may not be available yet. In
that case, the server will respond with a 503 error, and the caller should
try again soon.

The response is an object containing the following keys:
* "participants": A list of summary information on users who have posted to
  the discussion. Each value is an object containing their id, display_name,
  and avatar_url.
* "unread_entries": A list of entry ids that are unread by the current
  user. this implies that any entry not in this list is read.
* "entry_ratings": A map of entry ids to ratings by the current user. Entries
  not in this list have no rating. Only populated if rating is enabled.
* "forced_entries": A list of entry ids that have forced_read_state set to
  true. This flag is meant to indicate the entry's read_state has been
  manually set to 'unread' by the user, so the entry should not be
  automatically marked as read.
* "view": A threaded view of all the entries in the discussion, containing
  the id, user_id, and message.
* "new_entries": Because this view is eventually consistent, it's possible
  that newly created or updated entries won't yet be reflected in the view.
  If the application wants to also get a flat list of all entries not yet
  reflected in the view, pass include_new_entries=1 to the request and this
  array of entries will be returned. These entries are returned in a flat
  array, in ascending created_at order.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/discussion_topics/{topic_id}/entries

**Post an entry**  —  `post_entry_courses`

Create a new entry in a discussion topic. Returns a json representation of
the created entry (see documentation for 'entries' method) on success.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `message` | string | form |  | The body of the entry. |
| `attachment` | string | form |  | a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |

**Returns:** `void`

## POST /v1/groups/{group_id}/discussion_topics/{topic_id}/entries

**Post an entry**  —  `post_entry_groups`

Create a new entry in a discussion topic. Returns a json representation of
the created entry (see documentation for 'entries' method) on success.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `message` | string | form |  | The body of the entry. |
| `attachment` | string | form |  | a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |

**Returns:** `void`

## POST /v1/courses/{course_id}/discussion_topics/{topic_id}/duplicate

**Duplicate discussion topic**  —  `duplicate_discussion_topic_courses`

Duplicate a discussion topic according to context (Course/Group)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `DiscussionTopic`

## POST /v1/groups/{group_id}/discussion_topics/{topic_id}/duplicate

**Duplicate discussion topic**  —  `duplicate_discussion_topic_groups`

Duplicate a discussion topic according to context (Course/Group)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `DiscussionTopic`

## GET /v1/courses/{course_id}/discussion_topics/{topic_id}/entries

**List topic entries**  —  `list_topic_entries_courses`

Retrieve the (paginated) top-level entries in a discussion topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Will include the 10 most recent replies, if any, for each entry returned.

If the topic is a root topic with children corresponding to groups of a
group assignment, entries from those subtopics for which the user belongs
to the corresponding group will be returned.

Ordering of returned entries is newest-first by posting timestamp (reply
activity is ignored).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/groups/{group_id}/discussion_topics/{topic_id}/entries

**List topic entries**  —  `list_topic_entries_groups`

Retrieve the (paginated) top-level entries in a discussion topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Will include the 10 most recent replies, if any, for each entry returned.

If the topic is a root topic with children corresponding to groups of a
group assignment, entries from those subtopics for which the user belongs
to the corresponding group will be returned.

Ordering of returned entries is newest-first by posting timestamp (reply
activity is ignored).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies

**Post a reply**  —  `post_reply_courses`

Add a reply to an entry in a discussion topic. Returns a json
representation of the created reply (see documentation for 'replies'
method) on success.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `message` | string | form |  | The body of the entry. |
| `attachment` | string | form |  | a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |

**Returns:** `void`

## POST /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies

**Post a reply**  —  `post_reply_groups`

Add a reply to an entry in a discussion topic. Returns a json
representation of the created reply (see documentation for 'replies'
method) on success.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `message` | string | form |  | The body of the entry. |
| `attachment` | string | form |  | a multipart/form-data form-field-style attachment. Attachments larger than 1 kilobyte are subject to quota restrictions. |

**Returns:** `void`

## GET /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies

**List entry replies**  —  `list_entry_replies_courses`

Retrieve the (paginated) replies to a top-level entry in a discussion
topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Ordering of returned entries is newest-first by creation timestamp.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies

**List entry replies**  —  `list_entry_replies_groups`

Retrieve the (paginated) replies to a top-level entry in a discussion
topic.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

Ordering of returned entries is newest-first by creation timestamp.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/discussion_topics/{topic_id}/entry_list

**List entries**  —  `list_entries_courses`

Retrieve a paginated list of discussion entries, given a list of ids.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `ids` | array[string] | query |  | A list of entry ids to retrieve. Entries will be returned in id order, smallest id first. |

**Returns:** `void`

## GET /v1/groups/{group_id}/discussion_topics/{topic_id}/entry_list

**List entries**  —  `list_entries_groups`

Retrieve a paginated list of discussion entries, given a list of ids.

May require (depending on the topic) that the user has posted in the topic.
If it is required, and the user has not posted, will respond with a 403
Forbidden status and the body 'require_initial_post'.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `ids` | array[string] | query |  | A list of entry ids to retrieve. Entries will be returned in id order, smallest id first. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{topic_id}/read

**Mark topic as read**  —  `mark_topic_as_read_courses`

Mark the initial text of the discussion topic as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/{topic_id}/read

**Mark topic as read**  —  `mark_topic_as_read_groups`

Mark the initial text of the discussion topic as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/read_all

**Mark all topic as read**  —  `mark_all_topic_as_read_courses`

Mark the initial text of all the discussion topics as read in  the context.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/read_all

**Mark all topic as read**  —  `mark_all_topic_as_read_groups`

Mark the initial text of all the discussion topics as read in  the context.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/discussion_topics/{topic_id}/read

**Mark topic as unread**  —  `mark_topic_as_unread_courses`

Mark the initial text of the discussion topic as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/discussion_topics/{topic_id}/read

**Mark topic as unread**  —  `mark_topic_as_unread_groups`

Mark the initial text of the discussion topic as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{topic_id}/read_all

**Mark all entries as read**  —  `mark_all_entries_as_read_courses`

Mark the discussion topic and all its entries as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `forced_read_state` | boolean | form |  | A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/{topic_id}/read_all

**Mark all entries as read**  —  `mark_all_entries_as_read_groups`

Mark the discussion topic and all its entries as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `forced_read_state` | boolean | form |  | A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/discussion_topics/{topic_id}/read_all

**Mark all entries as unread**  —  `mark_all_entries_as_unread_courses`

Mark the discussion topic and all its entries as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `forced_read_state` | boolean | query |  | A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/discussion_topics/{topic_id}/read_all

**Mark all entries as unread**  —  `mark_all_entries_as_unread_groups`

Mark the discussion topic and all its entries as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `forced_read_state` | boolean | query |  | A boolean value to set all of the entries' forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read

**Mark entry as read**  —  `mark_entry_as_read_courses`

Mark a discussion entry as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `forced_read_state` | boolean | form |  | A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read

**Mark entry as read**  —  `mark_entry_as_read_groups`

Mark a discussion entry as read.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `forced_read_state` | boolean | form |  | A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read

**Mark entry as unread**  —  `mark_entry_as_unread_courses`

Mark a discussion entry as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `forced_read_state` | boolean | query |  | A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/read

**Mark entry as unread**  —  `mark_entry_as_unread_groups`

Mark a discussion entry as unread.

No request fields are necessary.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `forced_read_state` | boolean | query |  | A boolean value to set the entry's forced_read_state. No change is made if this argument is not specified. |

**Returns:** `void`

## POST /v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating

**Rate entry**  —  `rate_entry_courses`

Rate a discussion entry.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `rating` | integer (int64) | form |  | A rating to set on this entry. Only 0 and 1 are accepted. |

**Returns:** `void`

## POST /v1/groups/{group_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating

**Rate entry**  —  `rate_entry_groups`

Rate a discussion entry.

On success, the response will be 204 No Content with an empty body.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |
| `entry_id` | string | path | yes | ID |
| `rating` | integer (int64) | form |  | A rating to set on this entry. Only 0 and 1 are accepted. |

**Returns:** `void`

## PUT /v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed

**Subscribe to a topic**  —  `subscribe_to_topic_courses`

Subscribe to a topic to receive notifications about new entries

On success, the response will be 204 No Content with an empty body

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed

**Subscribe to a topic**  —  `subscribe_to_topic_groups`

Subscribe to a topic to receive notifications about new entries

On success, the response will be 204 No Content with an empty body

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed

**Unsubscribe from a topic**  —  `unsubscribe_from_topic_courses`

Unsubscribe from a topic to stop receiving notifications about new entries

On success, the response will be 204 No Content with an empty body

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/discussion_topics/{topic_id}/subscribed

**Unsubscribe from a topic**  —  `unsubscribe_from_topic_groups`

Unsubscribe from a topic to stop receiving notifications about new entries

On success, the response will be 204 No Content with an empty body

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `topic_id` | string | path | yes | ID |

**Returns:** `void`


---

# Models


## FileAttachment

A file attachment

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `content-type` | string |  | e.g. `unknown/unknown` |
| `url` | string |  | e.g. `http://www.example.com/courses/1/files/1/download` |
| `filename` | string |  | e.g. `content.txt` |
| `display_name` | string |  | e.g. `content.txt` |


## DiscussionTopic

A discussion topic

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of this topic. e.g. `1` |
| `title` | string |  | The topic title. e.g. `Topic 1` |
| `message` | string |  | The HTML content of the message body. e.g. `<p>content here</p>` |
| `html_url` | string |  | The URL to the discussion topic in canvas. e.g. `https://<canvas>/courses/1/discussion_topics/2` |
| `posted_at` | datetime |  | The datetime the topic was posted. If it is null it hasn't been posted yet. (see delayed_post_at) e.g. `2037-07-21T13:29:31Z` |
| `last_reply_at` | datetime |  | The datetime for when the last reply was in the topic. e.g. `2037-07-28T19:38:31Z` |
| `require_initial_post` | boolean |  | If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. e.g. `False` |
| `user_can_see_posts` | boolean |  | Whether or not posts in this topic are visible to the user. e.g. `True` |
| `discussion_subentry_count` | integer |  | The count of entries in the topic. e.g. `0` |
| `read_state` | string |  | The read_state of the topic for the current user, 'read' or 'unread'. e.g. `read` |
| `unread_count` | integer |  | The count of unread entries of this topic for the current user. e.g. `0` |
| `subscribed` | boolean |  | Whether or not the current user is subscribed to this topic. e.g. `True` |
| `subscription_hold` | string |  | (Optional) Why the user cannot subscribe to this topic. Only one reason will be returned even if multiple apply. Can be one of: 'initial_post_required': The user must post a reply first; 'not_in_group_set': The user is not in the group set for this graded group discussion; 'not_in_group': The user is not in this topic's group; 'topic_is_announcement': This topic is an announcement e.g. `not_in_group_set` |
| `assignment_id` | integer |  | The unique identifier of the assignment if the topic is for grading, otherwise null. |
| `delayed_post_at` | datetime |  | The datetime to publish the topic (if not right away). |
| `published` | boolean |  | Whether this discussion topic is published (true) or draft state (false) e.g. `True` |
| `lock_at` | datetime |  | The datetime to lock the topic (if ever). |
| `locked` | boolean |  | Whether or not the discussion is 'closed for comments'. e.g. `False` |
| `pinned` | boolean |  | Whether or not the discussion has been 'pinned' by an instructor e.g. `False` |
| `locked_for_user` | boolean |  | Whether or not this is locked for the user. e.g. `True` |
| `lock_info` | LockInfo |  | (Optional) Information for the user about the lock. Present when locked_for_user is true. |
| `lock_explanation` | string |  | (Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. e.g. `This discussion is locked until September 1 at 12:00am` |
| `user_name` | string |  | The username of the topic creator. e.g. `User Name` |
| `topic_children` | array[integer] |  | DEPRECATED An array of topic_ids for the group discussions the user is a part of. e.g. `[5, 7, 10]` |
| `group_topic_children` | array[object] |  | An array of group discussions the user is a part of. Fields include: id, group_id e.g. `[{'id': 5, 'group_id': 1}, {'id': 7, 'group_id': 5}, {'id': 10, 'group_id': 4}]` |
| `root_topic_id` | integer |  | If the topic is for grading and a group assignment this will point to the original topic in the course. |
| `podcast_url` | string |  | If the topic is a podcast topic this is the feed url for the current user. e.g. `/feeds/topics/1/enrollment_1XAcepje4u228rt4mi7Z1oFbRpn3RAkTzuXIGOPe.rss` |
| `discussion_type` | string |  | The type of discussion. Values are 'side_comment' or 'not_threaded', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions. e.g. `side_comment` |
| `group_category_id` | integer |  | The unique identifier of the group category if the topic is a group discussion, otherwise null. |
| `attachments` | array[FileAttachment] |  | Array of file attachments. |
| `permissions` | object |  | The current user's permissions on this topic. e.g. `{'attach': True}` |
| `allow_rating` | boolean |  | Whether or not users can rate entries in this topic. e.g. `True` |
| `only_graders_can_rate` | boolean |  | Whether or not grade permissions are required to rate entries. e.g. `True` |
| `sort_by_rating` | boolean |  | DEPRECATED, Whether or not entries should be sorted by rating. e.g. `True` |
| `sort_order` | string |  | How entries should be sorted by default. e.g. `asc` |
| `sort_order_locked` | boolean |  | Can users decide their preferred sort order. e.g. `True` |
| `expand` | boolean |  | Threaded replies should be expanded by default. e.g. `True` |
| `expand_locked` | boolean |  | Can users decide their preferred thread expand setting. e.g. `True` |
