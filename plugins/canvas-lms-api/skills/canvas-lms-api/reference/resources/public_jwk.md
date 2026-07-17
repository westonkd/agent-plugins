# Public JWK

> Canvas LMS REST API — `/public_jwk` resource. Base path `/api`.

## PUT /lti/developer_key/update_public_jwk

**Update Public JWK**  —  `update_public_jwk`

Rotate the public key in jwk format when using lti services

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `public_jwk` | json | form | yes | The new public jwk that will be set to the tools current public jwk. |

**Returns:** `DeveloperKey`
