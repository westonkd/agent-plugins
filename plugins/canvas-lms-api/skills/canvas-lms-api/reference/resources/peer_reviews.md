# Peer Reviews

> Canvas LMS REST API — `/peer_reviews` resource. Base path `/api`.

## GET /v1/courses/{course_id}/assignments/{assignment_id}/peer_reviews

**Get all Peer Reviews**  —  `get_all_peer_reviews_courses_peer_reviews`

Get a list of all Peer Reviews for this assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the peer review. Allowed: `submission_comments`, `user` |

**Returns:** `array[PeerReview]`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/peer_reviews

**Get all Peer Reviews**  —  `get_all_peer_reviews_sections_peer_reviews`

Get a list of all Peer Reviews for this assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the peer review. Allowed: `submission_comments`, `user` |

**Returns:** `array[PeerReview]`

## GET /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews

**Get all Peer Reviews**  —  `get_all_peer_reviews_courses_submissions`

Get a list of all Peer Reviews for this assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the peer review. Allowed: `submission_comments`, `user` |

**Returns:** `array[PeerReview]`

## GET /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews

**Get all Peer Reviews**  —  `get_all_peer_reviews_sections_submissions`

Get a list of all Peer Reviews for this assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `include` | array[string] | query |  | Associations to include with the peer review. Allowed: `submission_comments`, `user` |

**Returns:** `array[PeerReview]`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews

**Create Peer Review**  —  `create_peer_review_courses`

Create a peer review for the assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `user_id` | integer (int64) | form | yes | user_id to assign as reviewer on this assignment |

**Returns:** `PeerReview`

## POST /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews

**Create Peer Review**  —  `create_peer_review_sections`

Create a peer review for the assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `user_id` | integer (int64) | form | yes | user_id to assign as reviewer on this assignment |

**Returns:** `PeerReview`

## DELETE /v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews

**Delete Peer Review**  —  `delete_peer_review_courses`

Delete a peer review for the assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `user_id` | integer (int64) | query | yes | user_id to delete as reviewer on this assignment |

**Returns:** `PeerReview`

## DELETE /v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews

**Delete Peer Review**  —  `delete_peer_review_sections`

Delete a peer review for the assignment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `section_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |
| `submission_id` | string | path | yes | ID |
| `user_id` | integer (int64) | query | yes | user_id to delete as reviewer on this assignment |

**Returns:** `PeerReview`

## POST /v1/courses/{course_id}/assignments/{assignment_id}/allocate

**Allocate Peer Review**  —  `allocate_peer_review`

Allocates a submission for the current user to peer review

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `assignment_id` | string | path | yes | ID |

**Returns:** `PeerReview`


---

# Models


## PeerReview

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `assessor_id` | integer |  | The assessors user id e.g. `23` |
| `asset_id` | integer |  | The id for the asset associated with this Peer Review e.g. `13` |
| `asset_type` | string |  | The type of the asset e.g. `Submission` |
| `id` | integer |  | The id of the Peer Review e.g. `1` |
| `user_id` | integer |  | The user id for the owner of the asset e.g. `7` |
| `workflow_state` | string |  | The state of the Peer Review, either 'assigned' or 'completed' e.g. `assigned` |
| `user` | string |  | the User object for the owner of the asset if the user include parameter is provided (see user API) (optional) e.g. `User` |
| `assessor` | string |  | The User object for the assessor if the user include parameter is provided (see user API) (optional) e.g. `User` |
| `submission_comments` | string |  | The submission comments associated with this Peer Review if the submission_comment include parameter is provided (see submissions API) (optional) e.g. `SubmissionComment` |
