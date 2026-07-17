# Asset Processor

> Canvas LMS REST API — `/asset_processor` resource. Base path `/api`.

## POST /lti/asset_processors/{asset_processor_id}/reports

**Create an Asset Report**  —  `create_asset_report`

Creates a report for a given Canvas-managed asset (such as a submission
attachment).

Returns an HTTP 201 (Created) on success.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `asset_processor_id` | string | path | yes | ID |
| `assetId` | string | form |  | The UUID of the asset to which the report applies. Canvas will supply this to the tool in the the `LtiAssetProcessorSubmissionNotice`. |
| `errorCode` | string | form |  | A machine-readable code indicating the cause of the failure, for reports with a processingProgress value of `Failed`. The following standard error codes are available, but tools may use their own (in which case the tool may provide human-readable information in the `comment` field): UNSUPPORTED_ASSET_TYPE, ASSET_TOO_LARGE, ASSET_TOO_SMALL, EULA_NOT_ACCEPTED, DOWNLOAD_FAILED |
| `indicationAlt` | string | form |  | Alternate text representing the meaning of the indicationColor for screen readers or as a tooltip over the indication color. |
| `indicationColor` | string | form |  | A hex (#RRGGBB) color code the tool wishes to use indicating the outcome of an asset's report. |
| `priority` | integer (int64) | form |  | A number from 0 (meaning "good" or "success") to 5 (meaning urgent or time-critical notable features) indicating the tool's perceived priority of the report. If a priority is not known or applicable, the tool should use the value 0. |
| `processingProgress` | string | form |  | Indicates the status of the report. Should be one of the following: Processed, Processing, PendingManual, Failed, NotProcessed, NotReady. If an unrecognized value is given, the value will be stored, but will be treated by Canvas as `NotReady`. |
| `result` | string | form |  | A short string (16 characters or fewer) that briefly describes the successful result of the processing. This should be provided if processingProgress is Processed, and not provided otherwise. |
| `timestamp` | string | form |  | An ISO8601 date time value with microsecond precision. Reports with newer timestamps for the same asset and report type supersede previously submitted reports with older (or equal) timestamps. Likewise, if the timestamp provided is older than the latest timestamp for an existing report (of same asset and type), the new report will be ignored and the endpoint will return an HTTP 409 (Conflict). |
| `title` | string | form |  | A human-readable title for the report, to be displayed to the user. |
| `type` | string | form |  | An opaque value representing the type of report. |
| `visibleToOwner` | boolean | form |  | A boolean value indicates whether the indicator and report should be visible to the user who owns the asset being reported on. If no value is provided, the platform should assume a default value of false |

**Returns:** `the input arguments, as accepted and stored in the database.`

## PUT /lti/asset_processor_eulas/{context_external_tool_id}/deployment

**Update Eula Deployment Configuration**  —  `update_eula_deployment_configuration`

Provides a mechanism by which a platform can enable or disable the requirement
for users to accept a EULA within the scope of an entire deployment

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_external_tool_id` | string | path | yes | ID |
| `eulaRequired` | boolean | form |  | A boolean value representing whether or not the EULA is required for the deployment. |

**Returns:** `the input arguments as accepted and stored in the database`

## POST /lti/asset_processor_eulas/{context_external_tool_id}/user

**Create an Eula Acceptance**  —  `create_eula_acceptance`

The EULA user acceptance service provides a mechanism
by which a tool can notify a platform of whether or not a user has accepted a EULA.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_external_tool_id` | string | path | yes | ID |
| `userId` | string | form |  | The userId represents the user who has accepted or declined the EULA, `lti_id` of the Canvas User. |
| `accepted` | boolean | form |  | A boolean value representing whether or not the user has accepted the EULA |
| `timestamp` | string | form |  | The timestamp represents the time at which the user accepted or declined the EULA. This timestamp must be formatted as an ISO 8601 date time. |

**Returns:** `the input arguments as accepted and stored in the database`

## DELETE /lti/asset_processor_eulas/{context_external_tool_id}/user

**Delete Eula Acceptances for deployment**  —  `delete_eula_acceptances_for_deployment`

Remove the EULA acceptance status for all users within the current deployment.
This will allow a tool to reset the EULA acceptance status for all users,
and force them to accept the EULA again in the case that the EULA has changed.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `context_external_tool_id` | string | path | yes | ID |

**Returns:** `204 No Content`
