# Authentication Providers

> Canvas LMS REST API — `/authentication_providers` resource. Base path `/api`.

## GET /v1/accounts/{account_id}/authentication_providers

**List authentication providers**  —  `list_authentication_providers`

Returns a paginated list of authentication providers

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `array[AuthenticationProvider]`

## GET /v1/accounts/{account_id}/authentication_providers/{id}

**Get authentication provider**  —  `get_authentication_provider`

Get the specified authentication provider

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AuthenticationProvider`

## POST /v1/accounts/{account_id}/authentication_providers

**Add authentication provider**  —  `add_authentication_provider`

Add external authentication provider(s) for the account.
Services may be Apple, CAS, Facebook, GitHub, Google, LDAP, LinkedIn,
Microsoft, OpenID Connect, or SAML.

Each authentication provider is specified as a set of parameters as
described below. A provider specification must include an 'auth_type'
parameter with a value of 'apple', 'canvas', 'cas', 'clever', 'facebook',
'github', 'google', 'ldap', 'linkedin', 'microsoft', 'openid_connect',
or 'saml'. The other recognized parameters depend on this
auth_type; unrecognized parameters are discarded. Provider specifications
not specifying a valid auth_type are ignored.

You can set the 'position' for any provider. The config in the 1st position
is considered the default. You can set 'jit_provisioning' for any provider
besides Canvas. You can set 'mfa_required' for any provider.

For Apple, the additional recognized parameters are:

- client_id [Required]

  The developer’s client identifier, as provided by WWDR. Not available if
  configured globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'sub' (the default), or 'email'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'firstName', 'lastName', and 'sub'.

For Canvas, the additional recognized parameter is:

- self_registration

  'all', 'none', or 'observer' - who is allowed to register as a new user

For CAS, the additional recognized parameters are:

- auth_base

  The CAS server's URL.

- log_in_url [Optional]

  An alternate SSO URL for logging into CAS. You probably should not set
  this.

For Clever, the additional recognized parameters are:

- client_id [Required]

  The Clever application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The Clever application's Client Secret. Not available if configured
  globally for Canvas.

- district_id [Optional]

  A district's Clever ID. Leave this blank to let Clever handle the details
  with its District Picker. This is required for Clever Instant Login to
  work in a multi-tenant environment.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), 'sis_id', 'email', 'student_number', or
  'teacher_number'. Note that some fields may not be populated for
  all users at Clever.

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'id',
  'sis_id', 'email', 'student_number', and 'teacher_number'.

For Facebook, the additional recognized parameters are:

- app_id [Required]

  The Facebook App ID. Not available if configured globally for Canvas.

- app_secret [Required]

  The Facebook App Secret. Not available if configured globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), or 'email'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'first_name', 'id', 'last_name', 'locale', and 'name'.

For GitHub, the additional recognized parameters are:

- domain [Optional]

  The domain of a GitHub Enterprise installation. I.e.
  github.mycompany.com. If not set, it will default to the public
  github.com.

- client_id [Required]

  The GitHub application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The GitHub application's Client Secret. Not available if configured
  globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), or 'login'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'id', 'login', and 'name'.

For Google, the additional recognized parameters are:

- client_id [Required]

  The Google application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The Google application's Client Secret. Not available if configured
  globally for Canvas.

- hosted_domain [Optional]

  A Google Apps domain to restrict logins to. See
  https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'sub' (the default), or 'email'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'family_name', 'given_name', 'locale', 'name', and 'sub'.

For LDAP, the additional recognized parameters are:

- auth_host

  The LDAP server's URL.

- auth_port [Optional, Integer]

  The LDAP server's TCP port. (default: 389)

- auth_over_tls [Optional]

  Whether to use TLS. Can be 'simple_tls', or 'start_tls'. For backwards
  compatibility, booleans are also accepted, with true meaning simple_tls.
  If not provided, it will default to start_tls.

- auth_base [Optional]

  A default treebase parameter for searches performed against the LDAP
  server.

- auth_filter

  LDAP search filter. Use !{{login}} as a placeholder for the username
  supplied by the user. For example: "(sAMAccountName=!{{login}})".

- identifier_format [Optional]

  The LDAP attribute to use to look up the Canvas login. Omit to use
  the username supplied by the user.

- auth_username

  Username

- auth_password

  Password

For LinkedIn, the additional recognized parameters are:

- client_id [Required]

  The LinkedIn application's Client ID. Not available if configured globally
  for Canvas.

- client_secret [Required]

  The LinkedIn application's Client Secret. Not available if configured
  globally for Canvas.

- login_attribute [Optional]

  The attribute to use to look up the user's login in Canvas. Either
  'id' (the default), or 'emailAddress'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'emailAddress',
  'firstName', 'id', 'formattedName', and 'lastName'.

For Microsoft, the additional recognized parameters are:

- application_id [Required]

  The application's ID.

- application_secret [Required]

  The application's Client Secret (Password)

- tenant [Optional]

  See https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-protocols/
  Valid values are 'common', 'organizations', 'consumers', or an Azure Active Directory Tenant
  (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to 'common'

- login_attribute [Optional]

  See https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-tokens/#idtokens
  Valid values are 'sub', 'email', 'oid', or 'preferred_username'. Note
  that email may not always be populated in the user's profile at
  Microsoft. Oid will not be populated for personal Microsoft accounts.
  Defaults to 'sub'

- federated_attributes [Optional]

  See FederatedAttributesConfig. Valid provider attributes are 'email',
  'name', 'preferred_username', 'oid', and 'sub'.

For OpenID Connect, the additional recognized parameters are:

- client_id [Required]

  The application's Client ID.

- client_secret [Required]

  The application's Client Secret.

- authorize_url [Required]

  The URL for getting starting the OAuth 2.0 web flow

- token_url [Required]

  The URL for exchanging the OAuth 2.0 authorization code for an Access
  Token and ID Token

- scope [Optional]

  Space separated additional scopes to request for the token. Note that
  you need not specify the 'openid' scope, or any scopes that can be
  automatically inferred by the rules defined at
  http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims

- end_session_endpoint [Optional]

  URL to send the end user to after logging out of Canvas. See
  https://openid.net/specs/openid-connect-session-1_0.html#RPLogout

- userinfo_endpoint [Optional]

  URL to request additional claims from. If the initial ID Token received
  from the provider cannot be used to satisfy the login_attribute and
  all federated_attributes, this endpoint will be queried for additional
  information.

- login_attribute [Optional]

  The attribute of the ID Token to look up the user's login in Canvas.
  Defaults to 'sub'.

- federated_attributes [Optional]

  See FederatedAttributesConfig. Any value is allowed for the provider
  attribute names, but standard claims are listed at
  http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims

For SAML, the additional recognized parameters are:

- metadata [Optional]

  An XML document to parse as SAML metadata, and automatically populate idp_entity_id,
  log_in_url, log_out_url, certificate_fingerprint, and identifier_format

- metadata_uri [Optional]

  A URI to download the SAML metadata from, and automatically populate idp_entity_id,
  log_in_url, log_out_url, certificate_fingerprint, and identifier_format. This URI
  will also be saved, and the metadata periodically refreshed, automatically. If
  the metadata contains multiple entities, also supply idp_entity_id to distinguish
  which one you want (otherwise the only entity in the metadata will be inferred).
  If you provide the URI 'urn:mace:incommon' or 'http://ukfederation.org.uk',
  the InCommon or UK Access Management Federation metadata aggregate, respectively,
  will be used instead, and additional validation checks will happen (including
  validating that the metadata has been properly signed with the
  appropriate key).

- idp_entity_id

  The SAML IdP's entity ID

- log_in_url

  The SAML service's SSO target URL

- log_out_url [Optional]

  The SAML service's SLO target URL

- certificate_fingerprint

  The SAML service's certificate fingerprint.

- identifier_format

  The SAML service's identifier format. Must be one of:

  - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
  - urn:oasis:names:tc:SAML:2.0:nameid-format:entity
  - urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos
  - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
  - urn:oasis:names:tc:SAML:2.0:nameid-format:transient
  - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
  - urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName
  - urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName

- requested_authn_context [Optional]

  The SAML AuthnContext

- sig_alg [Optional]

  If set, +AuthnRequest+, +LogoutRequest+, and +LogoutResponse+ messages
  are signed with the corresponding algorithm. Supported algorithms are:

  - {http://www.w3.org/2000/09/xmldsig#rsa-sha1}
  - {http://www.w3.org/2001/04/xmldsig-more#rsa-sha256}

  RSA-SHA1 and RSA-SHA256 are acceptable aliases.

- federated_attributes [Optional]

  See FederatedAttributesConfig. Any value is allowed for the provider attribute names.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `AuthenticationProvider`

## PUT /v1/accounts/{account_id}/authentication_providers/{id}

**Update authentication provider**  —  `update_authentication_provider`

Update an authentication provider using the same options as the
{api:AuthenticationProvidersController#create Add authentication provider} endpoint.
You cannot update an existing provider to a new authentication type.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AuthenticationProvider`

## DELETE /v1/accounts/{account_id}/authentication_providers/{id}

**Delete authentication provider**  —  `delete_authentication_provider`

Delete the config

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `void`

## PUT /v1/accounts/{account_id}/authentication_providers/{id}/restore

**Restore a deleted authentication provider**  —  `restore_deleted_authentication_provider`

Restore an authentication provider back to active that was previously deleted. Only
available to admins who can manage_account_settings for given root account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `AuthenticationProvider`

## GET /v1/accounts/{account_id}/sso_settings

**Show account auth settings**  —  `show_account_auth_settings`

The way to get the current state of each account level setting
that's relevant to Single Sign On configuration

You can list the current state of each setting with "update_sso_settings"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `SSOSettings`

## PUT /v1/accounts/{account_id}/sso_settings

**Update account auth settings**  —  `update_account_auth_settings`

For various cases of mixed SSO configurations, you may need to set some
configuration at the account level to handle the particulars of your
setup.

This endpoint accepts a PUT request to set several possible account
settings. All setting are optional on each request, any that are not
provided at all are simply retained as is.  Any that provide the key but
a null-ish value (blank string, null, undefined) will be UN-set.

You can list the current state of each setting with "show_sso_settings"

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |

**Returns:** `SSOSettings`


---

# Models


## AuthenticationProvider

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `identifier_format` | string |  | Valid for SAML providers. e.g. `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` |
| `auth_type` | string |  | Valid for all providers. e.g. `saml` |
| `id` | integer |  | Valid for all providers. e.g. `1649` |
| `log_out_url` | string |  | Valid for SAML providers. e.g. `http://example.com/saml1/slo` |
| `log_in_url` | string |  | Valid for SAML and CAS providers. e.g. `http://example.com/saml1/sli` |
| `certificate_fingerprint` | string |  | Valid for SAML providers. e.g. `111222` |
| `requested_authn_context` | string |  | Valid for SAML providers. |
| `auth_host` | string |  | Valid for LDAP providers. e.g. `127.0.0.1` |
| `auth_filter` | string |  | Valid for LDAP providers. e.g. `filter1` |
| `auth_over_tls` | integer |  | Valid for LDAP providers. |
| `auth_base` | string |  | Valid for LDAP and CAS providers. |
| `auth_username` | string |  | Valid for LDAP providers. e.g. `username1` |
| `auth_port` | integer |  | Valid for LDAP providers. |
| `position` | integer |  | Valid for all providers. e.g. `1` |
| `idp_entity_id` | string |  | Valid for SAML providers. e.g. `http://example.com/saml1` |
| `login_attribute` | string |  | Valid for SAML providers. e.g. `nameid` |
| `sig_alg` | string |  | Valid for SAML providers. e.g. `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256` |
| `jit_provisioning` | boolean |  | Just In Time provisioning. Valid for all providers except Canvas (which has the similar in concept self_registration setting). |
| `federated_attributes` | FederatedAttributesConfig |  |  |
| `mfa_required` | boolean |  | If multi-factor authentication is required when logging in with this authentication provider. The account must not have MFA disabled. |


## SSOSettings

Settings that are applicable across an account's authentication configuration, even if there are multiple individual providers

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `login_handle_name` | string |  | The label used for unique login identifiers. e.g. `Username` |
| `change_password_url` | string |  | The url to redirect users to for password resets. Leave blank for default Canvas behavior e.g. `https://example.com/reset_password` |
| `auth_discovery_url` | string |  | If a discovery url is set, canvas will forward all users to that URL when they need to be authenticated. That page will need to then help the user figure out where they need to go to log in. If no discovery url is configured, the first configuration will be used to attempt to authenticate the user. e.g. `https://example.com/which_account` |
| `unknown_user_url` | string |  | If an unknown user url is set, Canvas will forward to that url when a service authenticates a user, but that user does not exist in Canvas. The default behavior is to present an error. e.g. `https://example.com/register_for_canvas` |
| `login_help_url` | string |  | A login help URL shown as a 'Trouble logging in?' link on the login page and in failed login messages. Falls back to the global setting if not set. e.g. `https://example.com/login-help` |


## FederatedAttributesConfig

A mapping of Canvas attribute names to attribute names that a provider may send, in order to update the value of these attributes when a user logs in. The values can be a FederatedAttributeConfig, or a raw string corresponding to the "attribute" property of a FederatedAttributeConfig. In responses, full FederatedAttributeConfig objects are returned if JIT provisioning is enabled, otherwise just the attribute names are returned.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `admin_roles` | string |  | A comma separated list of role names to grant to the user. Note that these only apply at the root account level, and not sub-accounts. If the attribute is not marked for provisioning only, the user will also be removed from any other roles they currently hold that are not still specified by the IdP. |
| `display_name` | string |  | The full display name of the user |
| `email` | string |  | The user's e-mail address |
| `given_name` | string |  | The first, or given, name of the user |
| `integration_id` | string |  | The secondary unique identifier for SIS purposes |
| `locale` | string |  | The user's preferred locale/language |
| `name` | string |  | The full name of the user |
| `sis_user_id` | string |  | The unique SIS identifier |
| `sortable_name` | string |  | The full name of the user for sorting purposes |
| `surname` | string |  | The surname, or last name, of the user |
| `timezone` | string |  | The user's preferred time zone |


## FederatedAttributeConfig

A single attribute name to be federated when a user logs in

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `attribute` | string |  | The name of the attribute as it will be sent from the authentication provider e.g. `mail` |
| `provisioning_only` | boolean |  | If the attribute should be applied only when provisioning a new user, rather than all logins e.g. `False` |
| `autoconfirm` | boolean |  | (only for email) If the email address is trusted and should be automatically confirmed e.g. `False` |
