# Temporary Enrollment Pairings

> Canvas LMS REST API — `/temporary_enrollment_pairings` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/temporary_enrollment_pairings

**List temporary enrollment pairings**  —  `list_temporary_enrollment_pairings`

Returns the list of temporary enrollment pairings for a root account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[TemporaryEnrollmentPairing]`

## GET /v1/accounts/{account_id}/temporary_enrollment_pairings/{id}

**Get a single temporary enrollment pairing**  —  `get_single_temporary_enrollment_pairing`

Returns the temporary enrollment pairing with the given id.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `TemporaryEnrollmentPairing`

## GET /v1/accounts/{account_id}/temporary_enrollment_pairings/new

**New TemporaryEnrollmentPairing**  —  `new_temporaryenrollmentpairing`

Initialize an unsaved Temporary Enrollment Pairing.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `TemporaryEnrollmentPairing`

## POST /v1/accounts/{account_id}/temporary_enrollment_pairings

**Create Temporary Enrollment Pairing**  —  `create_temporary_enrollment_pairing`

Create a Temporary Enrollment Pairing.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `workflow_state` | string | form |  | The workflow state of the temporary enrollment pairing. |
| `ending_enrollment_state` | string | form |  | The ending enrollment state to be given to each associated enrollment when the enrollment period has been reached. Defaults to "deleted" if no value is given. Accepted values are "deleted", "completed", and "inactive". Allowed: `deleted`, `completed`, `inactive` |

**Returns:** `TemporaryEnrollmentPairing`

## DELETE /v1/accounts/{account_id}/temporary_enrollment_pairings/{id}

**Delete Temporary Enrollment Pairing**  —  `delete_temporary_enrollment_pairing`

Delete a temporary enrollment pairing

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `TemporaryEnrollmentPairing`


---

# Models


## TemporaryEnrollmentPairing

A pairing unique to that enrollment period given to a recipient of that temporary enrollment.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | the ID of the temporary enrollment pairing e.g. `1` |
| `workflow_state` | string |  | The current status of the temporary enrollment pairing e.g. `active` |
