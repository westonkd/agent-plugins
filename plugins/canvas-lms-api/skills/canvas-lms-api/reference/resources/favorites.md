# Favorites

> Canvas LMS REST API — `/favorites` resource. Base path `/api`.

## GET /v1/users/self/favorites/courses

**List favorite courses**  —  `list_favorite_courses`

Retrieve the paginated list of favorite courses for the current user. If the user has not chosen
any favorites, then a selection of currently enrolled courses will be returned.

See the {api:CoursesController#index List courses API} for details on accepted include[] parameters.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `exclude_blueprint_courses` | boolean | query |  | When set, only return courses that are not configured as blueprint courses. |

**Returns:** `array[Course]`

## GET /v1/users/self/favorites/groups

**List favorite groups**  —  `list_favorite_groups`

Retrieve the paginated list of favorite groups for the current user. If the user has not chosen
any favorites, then a selection of groups that the user is a member of will be returned.

**Returns:** `array[Group]`

## POST /v1/users/self/favorites/courses/{id}

**Add course to favorites**  —  `add_course_to_favorites`

Add a course to the current user's favorites.  If the course is already
in the user's favorites, nothing happens. Canvas for Elementary subject
and homeroom courses can be added to favorites, but this has no effect in
the UI.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | The ID or SIS ID of the course to add.  The current user must be registered in the course. |

**Returns:** `Favorite`

## POST /v1/users/self/favorites/groups/{id}

**Add group to favorites**  —  `add_group_to_favorites`

Add a group to the current user's favorites.  If the group is already
in the user's favorites, nothing happens.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | The ID or SIS ID of the group to add.  The current user must be a member of the group. |

**Returns:** `Favorite`

## DELETE /v1/users/self/favorites/courses/{id}

**Remove course from favorites**  —  `remove_course_from_favorites`

Remove a course from the current user's favorites.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | the ID or SIS ID of the course to remove |

**Returns:** `Favorite`

## DELETE /v1/users/self/favorites/groups/{id}

**Remove group from favorites**  —  `remove_group_from_favorites`

Remove a group from the current user's favorites.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | the ID or SIS ID of the group to remove |

**Returns:** `Favorite`

## DELETE /v1/users/self/favorites/courses

**Reset course favorites**  —  `reset_course_favorites`

Reset the current user's course favorites to the default
automatically generated list of enrolled courses

**Returns:** `void`

## DELETE /v1/users/self/favorites/groups

**Reset group favorites**  —  `reset_group_favorites`

Reset the current user's group favorites to the default
automatically generated list of enrolled group

**Returns:** `void`


---

# Models


## Favorite

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `context_id` | integer |  | The ID of the object the Favorite refers to e.g. `1170` |
| `context_type` | string |  | The type of the object the Favorite refers to (currently, only 'Course' is supported) e.g. `Course` |
