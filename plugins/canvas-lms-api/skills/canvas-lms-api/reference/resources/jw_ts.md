# JWTs

> Canvas LMS REST API — `/jw_ts` resource. Base path `/api`.

## POST /v1/jwts

**Create JWT**  —  `create_jwt`

Create a unique JWT for use with other Canvas services

Generates a different JWT each time it's called. Each JWT expires
after a short window (1 hour)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `workflows` | array[string] | form |  | Adds additional data to the JWT to be used by the consuming service workflow |
| `context_type` | string | form |  | The type of the context to generate the JWT for, in case the workflow requires it. Case insensitive. Allowed: `Course`, `User`, `Account` |
| `context_id` | integer (int64) | form |  | The id of the context to generate the JWT for, in case the workflow requires it. |
| `context_uuid` | string | form |  | The uuid of the context to generate the JWT for, in case the workflow requires it. Note that context_id and context_uuid are mutually exclusive. If both are provided, an error will be returned. |
| `canvas_audience` | boolean | form |  | Defaults to true. If false, the JWT will be signed, but not encrypted, for use in downstream services. The default encrypted behaviour can be used to talk to Canvas itself. |

**Returns:** `JWT`

## POST /v1/jwts/refresh

**Refresh JWT**  —  `refresh_jwt`

Refresh a JWT for use with other canvas services

Generates a different JWT each time it's called, each one expires
after a short window (1 hour).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `jwt` | string | form | yes | An existing JWT token to be refreshed. The new token will have the same context and workflows as the existing token. |

**Returns:** `JWT`


---

# Models


## JWT

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `token` | string |  | The signed, encrypted, base64 encoded JWT e.g. `ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1qVTJSME5OSW4wLi5QbnAzS1QzLUJkZ3lQZHgtLm5JT0pOV01iZmdtQ0g3WWtybjhLeHlMbW13cl9yZExXTXF3Y0IwbXkzZDd3V1NDd0JYQkV0UTRtTVNJSVRrX0FJcG0zSU1DeThMcW5NdzA0ckdHVTkweDB3MmNJbjdHeWxOUXdveU5ZZ3UwOEN4TkZteUpCeW5FVktrdU05QlRyZXZ3Y1ZTN2hvaC1WZHRqM19PR3duRm5yUVgwSFhFVFc4R28tUGxoQVUtUnhKT0pNakx1OUxYd2NDUzZsaW9ZMno5NVU3T0hLSGNpaDBmSGVjN2FzekVJT3g4NExUeHlReGxYU3BtbFZ5LVNuYWdfbVJUeU5yNHNsMmlDWFcwSzZCNDhpWHJ1clJVVm1LUkVlVTl4ZVVJcTJPaWNpSHpfemJ0X3FrMjhkdzRyajZXRnBHSlZPNWcwTlUzVHlSWk5qdHg1S2NrTjVSQjZ1X2FzWTBScjhTY2VhNFk3Y2JFX01wcm54cFZTNDFIekVVSVRNdzVMTk1GLVpQZy52LVVDTkVJYk8zQ09EVEhPRnFXLUFR` |
