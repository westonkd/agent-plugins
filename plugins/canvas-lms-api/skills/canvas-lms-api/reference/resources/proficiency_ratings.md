# Proficiency Ratings

> Canvas LMS REST API — `/proficiency_ratings` resource. Base path `/api`.

## POST /v1/accounts/{account_id}/outcome_proficiency

**Create/update proficiency ratings**  —  `create_update_proficiency_ratings_accounts`

Create or update account-level proficiency ratings. These ratings will apply to all
sub-accounts, unless they have their own account-level proficiency ratings defined.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `ratings[description]` | array[string] | form |  | The description of the rating level. |
| `ratings[points]` | array[integer] | form |  | The non-negative number of points of the rating level. Points across ratings should be strictly decreasing in value. |
| `ratings[mastery]` | array[integer] | form |  | Indicates the rating level where mastery is first achieved. Only one rating in a proficiency should be marked for mastery. |
| `ratings[color]` | array[integer] | form |  | The color associated with the rating level. Should be a hex color code like '00FFFF'. |

**Returns:** `Proficiency`

## POST /v1/courses/{course_id}/outcome_proficiency

**Create/update proficiency ratings**  —  `create_update_proficiency_ratings_courses`

Create or update account-level proficiency ratings. These ratings will apply to all
sub-accounts, unless they have their own account-level proficiency ratings defined.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `ratings[description]` | array[string] | form |  | The description of the rating level. |
| `ratings[points]` | array[integer] | form |  | The non-negative number of points of the rating level. Points across ratings should be strictly decreasing in value. |
| `ratings[mastery]` | array[integer] | form |  | Indicates the rating level where mastery is first achieved. Only one rating in a proficiency should be marked for mastery. |
| `ratings[color]` | array[integer] | form |  | The color associated with the rating level. Should be a hex color code like '00FFFF'. |

**Returns:** `Proficiency`

## GET /v1/accounts/{account_id}/outcome_proficiency

**Get proficiency ratings**  —  `get_proficiency_ratings_accounts`

Get account-level proficiency ratings. If not defined for this account,
it will return proficiency ratings for the nearest super-account with ratings defined.
Will return 404 if none found.

  Examples:
    curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
        -H 'Authorization: Bearer <token>'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `Proficiency`

## GET /v1/courses/{course_id}/outcome_proficiency

**Get proficiency ratings**  —  `get_proficiency_ratings_courses`

Get account-level proficiency ratings. If not defined for this account,
it will return proficiency ratings for the nearest super-account with ratings defined.
Will return 404 if none found.

  Examples:
    curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
        -H 'Authorization: Bearer <token>'

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `Proficiency`


---

# Models


## ProficiencyRating

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `description` | string |  | The description of the rating e.g. `Exceeds Mastery` |
| `points` | number |  | A non-negative number of points for the rating e.g. `4` |
| `mastery` | boolean |  | Indicates the rating where mastery is first achieved e.g. `False` |
| `color` | string |  | The hex color code of the rating e.g. `02672D` |


## Proficiency

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `ratings` | array |  | An array of proficiency ratings. See the ProficiencyRating specification above. e.g. `[]` |
