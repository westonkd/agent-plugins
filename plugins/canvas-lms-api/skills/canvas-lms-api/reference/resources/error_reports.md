# Error Reports

> Canvas LMS REST API — `/error_reports` resource. Base path `/api`.

## POST /v1/error_reports

**Create Error Report**  —  `create_error_report`

Create a new error report documenting an experienced problem

Performs the same action as when a user uses the "help -> report a problem"
dialog.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `error[subject]` | string | form | yes | The summary of the problem |
| `error[url]` | string | form |  | URL from which the report was issued |
| `error[email]` | string | form |  | Email address for the reporting user |
| `error[comments]` | string | form |  | The long version of the story from the user one what they experienced |
| `error[http_env]` | SerializedHash | form |  | A collection of metadata about the users' environment.  If not provided, canvas will collect it based on information found in the request. (Doesn't have to be HTTPENV info, could be anything JSON object that can be serialized as a hash, a mobile app might include relevant metadata for itself) |

**Returns:** `void`


---

# Models


## ErrorReport

A collection of information around a specific notification of a problem

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `subject` | string |  | The users problem summary, like an email subject line e.g. `File upload breaking` |
| `comments` | string |  | long form documentation of what was witnessed e.g. `When I went to upload a .mov file to my files page, I got an error.  Retrying didn't help, other file types seem ok` |
| `user_perceived_severity` | string |  | categorization of how bad the user thinks the problem is.  Should be one of [just_a_comment, not_urgent, workaround_possible, blocks_what_i_need_to_do, extreme_critical_emergency]. e.g. `just_a_comment` |
| `email` | string |  | the email address of the reporting user e.g. `name@example.com` |
| `url` | string |  | URL of the page on which the error was reported e.g. `https://canvas.instructure.com/courses/1` |
| `context_asset_string` | string |  | string describing the asset being interacted with at the time of error.  Formatted '[type]_[id]' e.g. `user_1` |
| `user_roles` | string |  | comma seperated list of roles the reporting user holds.  Can be one [student], or many [teacher,admin] e.g. `user,teacher,admin` |
