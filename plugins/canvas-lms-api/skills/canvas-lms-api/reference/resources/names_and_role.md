# Names and Role

> Canvas LMS REST API — `/names_and_role` resource. Base path `/api`.

## GET /lti/courses/{course_id}/names_and_roles

**List Course Memberships**  —  `list_course_memberships`

Return active NamesAndRoleMemberships in the given course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `rlid` | string | query |  | If specified only NamesAndRoleMemberships with access to the LTI link references by this `rlid` will be included. Also causes the member array to be included for each returned NamesAndRoleMembership. If the `role` parameter is also present, it will be 'and-ed' together with this parameter |
| `role` | string | query |  | If specified only NamesAndRoleMemberships having this role in the given Course will be included. Value must be a fully-qualified LTI/LIS role URN. If the `rlid` parameter is also present, it will be 'and-ed' together with this parameter |
| `limit` | string | query |  | May be used to limit the number of NamesAndRoleMemberships returned in a page. Defaults to 50. |

**Returns:** `NamesAndRoleMemberships`

## GET /lti/groups/{group_id}/names_and_roles

**List Group Memberships**  —  `list_group_memberships`

Return active NamesAndRoleMemberships in the given group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| ``rlid`` | string | query |  | If specified only NamesAndRoleMemberships with access to the LTI link references by this `rlid` will be included. Also causes the member array to be included for each returned NamesAndRoleMembership. If the role parameter is also present, it will be 'and-ed' together with this parameter |
| `role` | string | query |  | If specified only NamesAndRoleMemberships having this role in the given Group will be included. Value must be a fully-qualified LTI/LIS role URN. Further, only http://purl.imsglobal.org/vocab/lis/v2/membership#Member and http://purl.imsglobal.org/vocab/lis/v2/membership#Manager are supported. If the `rlid` parameter is also present, it will be 'and-ed' together with this parameter |
| `limit` | string | query |  | May be used to limit the number of NamesAndRoleMemberships returned in a page. Defaults to 50. |

**Returns:** `NamesAndRoleMemberships`


---

# Models


## NamesAndRoleContext

An abbreviated representation of an LTI Context

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | LTI Context unique identifier e.g. `4dde05e8ca1973bcca9bffc13e1548820eee93a3` |
| `label` | string |  | LTI Context short name or code e.g. `CS-101` |
| `title` | string |  | LTI Context full name e.g. `Computer Science 101` |


## NamesAndRoleMessage

Additional attributes which would appear in the LTI launch message were this member to click the specified resource link (`rlid` query parameter)

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `https://purl.imsglobal.org/spec/lti/claim/message_type` | string |  | The type of LTI message being described. Always set to 'LtiResourceLinkRequest' e.g. `LtiResourceLinkRequest` Allowed: `LtiResourceLinkRequest` |
| `locale` | string |  | The member's preferred locale e.g. `en` |
| `https://www.instructure.com/canvas_user_id` | integer |  | The member's API ID e.g. `1` |
| `https://www.instructure.com/canvas_user_login_id` | string |  | The member's primary login username e.g. `showell@school.edu` |
| `https://purl.imsglobal.org/spec/lti/claim/custom` | object |  | Expanded LTI custom parameters that pertain to the member (as opposed to the Context) e.g. `{'message_locale': 'en', 'person_address_timezone': 'America/Denver'}` |


## NamesAndRoleMembership

A member of a LTI Context in one or more roles

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `status` | string |  | Membership state e.g. `Active` Allowed: `Active` |
| `name` | string |  | Member's full name. Only included if tool privacy level is `public` or `name_only`. e.g. `Sienna Howell` |
| `picture` | string |  | URL to the member's avatar. Only included if tool privacy level is `public`. e.g. `https://example.instructure.com/images/messages/avatar-50.png` |
| `given_name` | string |  | Member's 'first' name. Only included if tool privacy level is `public` or `name_only`. e.g. `Sienna` |
| `family_name` | string |  | Member's 'last' name. Only included if tool privacy level is `public` or `name_only`. e.g. `Howell` |
| `email` | string |  | Member's email address. Only included if tool privacy level is `public` or `email_only`. e.g. `showell@school.edu` |
| `lis_person_sourcedid` | string |  | Member's primary SIS identifier. Only included if tool privacy level is `public` or `name_only`. e.g. `1238.8763.00` |
| `user_id` | string |  | Member's unique LTI identifier. e.g. `535fa085f22b4655f48cd5a36a9215f64c062838` |
| `roles` | array[string] |  | Member's roles in the current Context, expressed as LTI/LIS URNs. e.g. `['http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor', 'http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper']` |
| `message` | array[NamesAndRoleMessage] |  | Only present when the request specifies a `rlid` query parameter. Contains additional attributes which would appear in the LTI launch message were this member to click the link referenced by the `rlid` query parameter e.g. `[{'https://purl.imsglobal.org/spec/lti/claim/message_type': 'LtiResourceLinkRequest', 'locale': 'en', 'https://www.instructure.com/canvas_user_id': 1, 'https://www.instructure.com/canvas_user_login_id': 'showell@school.edu', 'https://purl.imsglobal.org/spec/lti/claim/custom': {'message_locale': 'en', 'person_address_timezone': 'America/Denver'}}]` |


## NamesAndRoleMemberships

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | Invocation URL e.g. `https://example.instructure.com/api/lti/courses/1/names_and_roles?tlid=f91ca4d8-fa84-4a9b-b08e-47d5527416b0` |
| `context` | NamesAndRoleContext |  | The LTI Context containing the memberships e.g. `{'id': '4dde05e8ca1973bcca9bffc13e1548820eee93a3', 'label': 'CS-101', 'title': 'Computer Science 101'}` |
| `members` | array[NamesAndRoleMembership] |  | A list of NamesAndRoleMembership e.g. `[{'status': 'Active', 'name': 'Sienna Howell', 'picture': 'https://example.instructure.com/images/messages/avatar-50.png', 'given_name': 'Sienna', 'family_name': 'Howell', 'email': 'showell@school.edu', 'lis_person_sourcedid': '1238.8763.00', 'user_id': '535fa085f22b4655f48cd5a36a9215f64c062838', 'roles': ['http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor', 'http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper'], 'message': [{'https://purl.imsglobal.org/spec/lti/claim/message_type': 'LtiResourceLinkRequest', 'locale': 'en', 'https://www.instructure.com/canvas_user_id': 1, 'https://www.instructure.com/canvas_user_login_id': 'showell@school.edu', 'https://purl.imsglobal.org/spec/lti/claim/custom': {'message_locale': 'en', 'person_address_timezone': 'America/Denver'}}]}, {'status': 'Active', 'name': 'Terrence Walls', 'picture': 'https://example.instructure.com/images/messages/avatar-51.png', 'given_name': 'Terrence', 'family_name': 'Walls', 'email': 'twalls@school.edu', 'lis_person_sourcedid': '5790.3390.11', 'user_id': '86157096483e6b3a50bfedc6bac902c0b20a824f', 'roles': ['http://purl.imsglobal.org/vocab/lis/v2/membership#Learner'], 'message': [{'https://purl.imsglobal.org/spec/lti/claim/message_type': 'LtiResourceLinkRequest', 'locale': 'de', 'https://www.instructure.com/canvas_user_id': 2, 'https://www.instructure.com/canvas_user_login_id': 'twalls@school.edu', 'https://purl.imsglobal.org/spec/lti/claim/custom': {'message_locale': 'en', 'person_address_timezone': 'Europe/Berlin'}}]}]` |
