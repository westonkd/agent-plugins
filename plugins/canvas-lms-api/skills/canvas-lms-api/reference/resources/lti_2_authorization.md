# LTI 2 Authorization

> Canvas LMS REST API — `/lti_2_authorization` resource. Base path `/api`.

## POST /lti/courses/{course_id}/authorize

**authorize**  —  `authorize_courses`

Returns an access token that can be used to access other LTI services

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `grant_type` | string | form | yes | When using registration provided credentials it should contain the exact value of: "urn:ietf:params:oauth:grant-type:jwt-bearer" once a tool proxy is created When using developer credentials it should have the value of: "authorization_code" and pass the optional argument `code` defined below |
| `code` | string | form |  | Only used in conjunction with a grant type of "authorization_code".  Should contain the "reg_key" from the registration message |
| `assertion` | AuthorizationJWT | form | yes | The AuthorizationJWT here should be the JWT in a string format |

**Returns:** `array[AccessToken]`

## POST /lti/accounts/{account_id}/authorize

**authorize**  —  `authorize_accounts`

Returns an access token that can be used to access other LTI services

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `grant_type` | string | form | yes | When using registration provided credentials it should contain the exact value of: "urn:ietf:params:oauth:grant-type:jwt-bearer" once a tool proxy is created When using developer credentials it should have the value of: "authorization_code" and pass the optional argument `code` defined below |
| `code` | string | form |  | Only used in conjunction with a grant type of "authorization_code".  Should contain the "reg_key" from the registration message |
| `assertion` | AuthorizationJWT | form | yes | The AuthorizationJWT here should be the JWT in a string format |

**Returns:** `array[AccessToken]`


---

# Models


## AuthorizationJWT

This is a JWT (https://tools.ietf.org/html/rfc7519), we highly recommend using a library to create these tokens. The token should be signed with the shared secret found in the Tool Proxy, which must be using the 'splitSecret' capability. If a tool proxy has not yet been created in Canvas a developer key may be used to sign the token. In this case the ‘sub’ claim of the token should be the developer key ID.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `sub` | string |  | The Tool Proxy Guid OR Developer key ID. A developer key ID should only be used if a tool proxy has not been created in Canvas. In this case the token should be signed with the developer key rather than the tool proxy shared secret. e.g. `81c4fc5f-4931-4199-ae3b-2077de8f9325` |
| `aud` | string |  | The LTI 2 token authorization endpoint, can be found in the Tool Consumer Profile e.g. `https://example.com/api/lti/authorize` |
| `exp` | integer |  | When this token expires, should be no more than 1 minute in the future e.g. `1484685900` |
| `iat` | integer |  | The time this token was created e.g. `1484685847` |
| `jti` | string |  | A unique ID for this token. Should be a UUID e.g. `146dd925-f9ad-4703-a99e-3872000f2534` |
