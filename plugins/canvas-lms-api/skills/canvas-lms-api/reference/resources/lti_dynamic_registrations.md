# LTI Dynamic Registrations

> Canvas LMS REST API — `/lti_dynamic_registrations` resource. Base path `/api`.

## GET /lti/registrations/{registration_id}

**Get Dynamic Registration Configuration**  —  `get_dynamic_registration_configuration`

Retrieves the LTI Dynamic Registration configuration for a given registration.
This endpoint provides the complete registration configuration including client details,
scopes, redirect URIs, and LTI tool configuration. Authentication is required via
developer key access token with appropriate LTI registration scopes.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `registration_id` | integer (int64) | path | yes | The ID of the LTI IMS Registration to retrieve configuration for |

**Returns:** `{Object} LTI Dynamic Registration configuration containing: - client_id: The global developer key ID as a string - application_type: Always "web" for LTI registrations - grant_types: Array of supported OAuth2 grant types - initiate_login_uri: URL for LTI login initiation - redirect_uris: Array of allowed redirect URIs after authentication - response_types: Array of supported OAuth2 response types (always "id_token") - client_name: Display name of the LTI tool - jwks_uri: URL to the tool's JSON Web Key Set - logo_uri: URL to the tool's logo/icon - token_endpoint_auth_method: Authentication method (always "private_key_jwt") - scope: Space-separated string of OAuth2 scopes including LTI scopes and "openid" - LTI tool configuration object with placements and Canvas-specific extensions - registration_client_uri: URL to view/manage the registration in Canvas - deployment_id: The deployment ID for the root account deployment (if exists)`

## POST /lti/registrations

**Create a Dynamic Registration**  —  `create_dynamic_registration`

The final step of the Dynamic Registration process.
Refer to the Registration guide linked at the top of this page for usage of this endpoint.
Requires special Dynamic Registration token and is not for out-of-band use.

**Returns:** `void`
