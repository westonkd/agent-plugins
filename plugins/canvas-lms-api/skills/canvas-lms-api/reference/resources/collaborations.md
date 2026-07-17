# Collaborations

> Canvas LMS REST API — `/collaborations` resource. Base path `/api`.

## GET /v1/courses/{course_id}/collaborations

**List collaborations**  —  `list_collaborations_courses`

A paginated list of collaborations the current user has access to in the
context of the course provided in the url. NOTE: this only returns
ExternalToolCollaboration type collaborations.

  curl https://<canvas>/api/v1/courses/1/collaborations/

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[Collaboration]`

## GET /v1/groups/{group_id}/collaborations

**List collaborations**  —  `list_collaborations_groups`

A paginated list of collaborations the current user has access to in the
context of the course provided in the url. NOTE: this only returns
ExternalToolCollaboration type collaborations.

  curl https://<canvas>/api/v1/courses/1/collaborations/

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[Collaboration]`

## GET /v1/collaborations/{id}/members

**List members of a collaboration.**  —  `list_members_of_collaboration`

A paginated list of the collaborators of a given collaboration

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | - "collaborator_lti_id": Optional information to include with each member.   Represents an identifier to be used for the member in an LTI context. - "avatar_image_url": Optional information to include with each member.   The url for the avatar of a collaborator with type 'user'. Allowed: `collaborator_lti_id`, `avatar_image_url` |

**Returns:** `array[Collaborator]`

## GET /v1/courses/{course_id}/potential_collaborators

**List potential members**  —  `list_potential_members_courses`

A paginated list of the users who can potentially be added to a
collaboration in the given context.

For courses, this consists of all enrolled users.  For groups, it is comprised of the
group members plus the admins of the course containing the group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[User]`

## GET /v1/groups/{group_id}/potential_collaborators

**List potential members**  —  `list_potential_members_groups`

A paginated list of the users who can potentially be added to a
collaboration in the given context.

For courses, this consists of all enrolled users.  For groups, it is comprised of the
group members plus the admins of the course containing the group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[User]`


---

# Models


## Collaboration

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The unique identifier for the collaboration e.g. `43` |
| `collaboration_type` | string |  | A name for the type of collaboration e.g. `Microsoft Office` |
| `document_id` | string |  | The collaboration document identifier for the collaboration provider e.g. `oinwoenfe8w8ef_onweufe89fef` |
| `user_id` | integer |  | The canvas id of the user who created the collaboration e.g. `92` |
| `context_id` | integer |  | The canvas id of the course or group to which the collaboration belongs e.g. `77` |
| `context_type` | string |  | The canvas type of the course or group to which the collaboration belongs e.g. `Course` |
| `url` | string |  | The LTI launch url to view collaboration. |
| `created_at` | datetime |  | The timestamp when the collaboration was created e.g. `2012-06-01T00:00:00-06:00` |
| `updated_at` | datetime |  | The timestamp when the collaboration was last modified e.g. `2012-06-01T00:00:00-06:00` |
| `description` | string |  |  |
| `title` | string |  |  |
| `type` | string |  | Another representation of the collaboration type e.g. `ExternalToolCollaboration` |
| `update_url` | string |  | The LTI launch url to edit the collaboration |
| `user_name` | string |  | The name of the user who owns the collaboration e.g. `John Danger` |


## Collaborator

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer | yes | The unique user or group identifier for the collaborator. e.g. `12345` |
| `type` | string |  | The type of collaborator (e.g. 'user' or 'group'). e.g. `user` |
| `name` | string |  | The name of the collaborator. e.g. `Don Draper` |
