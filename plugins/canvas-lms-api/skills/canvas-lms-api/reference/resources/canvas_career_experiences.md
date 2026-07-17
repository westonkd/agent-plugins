# Canvas Career Experiences

> Canvas LMS REST API — `/canvas_career_experiences` resource. Base path `/api`.

## GET /v1/career/enabled

**Check if Canvas Career is enabled**  —  `check_if_canvas_career_is_enabled`

Returns whether the root account has Canvas Career (Horizon) enabled
in at least one subaccount.

**Returns:** `{enabled: boolean}`

## GET /v1/career/experience_summary

**Get current and available experiences**  —  `get_current_and_available_experiences`

Returns the current user's active experience and available experiences
they can switch to.

**Returns:** `ExperienceSummary`

## POST /v1/career/switch_experience

**Switch experience**  —  `switch_experience`

Switch the current user's active experience to the specified one.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `experience` | string | form | yes | The experience to switch to. Allowed: `academic`, `career` |

**Returns:** `{experience: String} The newly set experience`

## POST /v1/career/switch_role

**Switch role**  —  `switch_role`

Switch the current user's role within the current experience.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `role` | string | form | yes | The role to switch to. Allowed: `learner`, `learning_provider` |

**Returns:** `{role: String} The newly set role`


---

# Models


## ExperienceSummary

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `current_app` | string |  | The current active experience. One of: 'academic', 'career_learner', 'career_learning_provider'. e.g. `career_learner` |
| `available_apps` | array[string] |  | List of available experiences for the user. Can include: 'academic', 'career_learner', 'career_learning_provider'. e.g. `['academic', 'career_learner']` |
