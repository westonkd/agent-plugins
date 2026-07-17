# Files

> Canvas LMS REST API — `/files` resource. Base path `/api`.

## GET /v1/courses/{course_id}/files/quota

**Get quota information**  —  `get_quota_information_courses`

Returns the total and used storage quota for the course, group, or user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/groups/{group_id}/files/quota

**Get quota information**  —  `get_quota_information_groups`

Returns the total and used storage quota for the course, group, or user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/users/{user_id}/files/quota

**Get quota information**  —  `get_quota_information_users`

Returns the total and used storage quota for the course, group, or user.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `void`

## GET /v1/courses/{course_id}/files

**List files**  —  `list_files_courses`

Returns the paginated list of files for the folder or course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `content_types` | array[string] | query |  | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `exclude_content_types` | array[string] | query |  | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `search_term` | string | query |  | The partial name of the files to match and return. |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `only` | array[Array] | query |  | Array of information to restrict to. Overrides include[]  "names":: only returns file name information |
| `sort` | string | query |  | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. Allowed: `name`, `size`, `created_at`, `updated_at`, `content_type`, `user` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |

**Returns:** `array[File]`

## GET /v1/users/{user_id}/files

**List files**  —  `list_files_users`

Returns the paginated list of files for the folder or course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `content_types` | array[string] | query |  | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `exclude_content_types` | array[string] | query |  | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `search_term` | string | query |  | The partial name of the files to match and return. |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `only` | array[Array] | query |  | Array of information to restrict to. Overrides include[]  "names":: only returns file name information |
| `sort` | string | query |  | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. Allowed: `name`, `size`, `created_at`, `updated_at`, `content_type`, `user` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |

**Returns:** `array[File]`

## GET /v1/groups/{group_id}/files

**List files**  —  `list_files_groups`

Returns the paginated list of files for the folder or course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `content_types` | array[string] | query |  | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `exclude_content_types` | array[string] | query |  | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `search_term` | string | query |  | The partial name of the files to match and return. |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `only` | array[Array] | query |  | Array of information to restrict to. Overrides include[]  "names":: only returns file name information |
| `sort` | string | query |  | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. Allowed: `name`, `size`, `created_at`, `updated_at`, `content_type`, `user` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |

**Returns:** `array[File]`

## GET /v1/folders/{id}/files

**List files**  —  `list_files_folders`

Returns the paginated list of files for the folder or course.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `content_types` | array[string] | query |  | Filter results by content-type. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `exclude_content_types` | array[string] | query |  | Exclude given content-types from your results. You can specify type/subtype pairs (e.g., 'image/jpeg'), or simply types (e.g., 'image', which will match 'image/gif', 'image/jpeg', etc.). |
| `search_term` | string | query |  | The partial name of the files to match and return. |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `only` | array[Array] | query |  | Array of information to restrict to. Overrides include[]  "names":: only returns file name information |
| `sort` | string | query |  | Sort results by this field. Defaults to 'name'. Note that `sort=user` implies `include[]=user`. Allowed: `name`, `size`, `created_at`, `updated_at`, `content_type`, `user` |
| `order` | string | query |  | The sorting order. Defaults to 'asc'. Allowed: `asc`, `desc` |

**Returns:** `array[File]`

## GET /v1/files/{id}/public_url

**Get public inline preview url**  —  `get_public_inline_preview_url`

Determine the URL that should be used for inline preview of the file.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `submission_id` | integer (int64) | query |  | The id of the submission the file is associated with.  Provide this argument to gain access to a file that has been submitted to an assignment (Canvas will verify that the file belongs to the submission and the calling user has rights to view the submission). |

**Returns:** `void`

## GET /v1/files/{id}

**Get file**  —  `get_file_files`

Returns the standard attachment json object

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `replacement_chain_context_type` | string | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The "replacement_chain_context_id" parameter must also be included. |
| `replacement_chain_context_id` | integer (int64) | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the "replacement chain." The "replacement_chain_context_type" parameter must also be included. |

**Returns:** `File`

## GET /v1/courses/{course_id}/files/{id}

**Get file**  —  `get_file_courses`

Returns the standard attachment json object

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `replacement_chain_context_type` | string | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The "replacement_chain_context_id" parameter must also be included. |
| `replacement_chain_context_id` | integer (int64) | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the "replacement chain." The "replacement_chain_context_type" parameter must also be included. |

**Returns:** `File`

## GET /v1/groups/{group_id}/files/{id}

**Get file**  —  `get_file_groups`

Returns the standard attachment json object

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `replacement_chain_context_type` | string | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The "replacement_chain_context_id" parameter must also be included. |
| `replacement_chain_context_id` | integer (int64) | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the "replacement chain." The "replacement_chain_context_type" parameter must also be included. |

**Returns:** `File`

## GET /v1/users/{user_id}/files/{id}

**Get file**  —  `get_file_users`

Returns the standard attachment json object

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include` | array[string] | query |  | Array of additional information to include.  "user":: the user who uploaded the file or last edited its content "usage_rights":: copyright and license information for the file (see UsageRights) Allowed: `user` |
| `replacement_chain_context_type` | string | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Must be set to 'course' or 'account'. The "replacement_chain_context_id" parameter must also be included. |
| `replacement_chain_context_id` | integer (int64) | query |  | When a user replaces a file during upload, Canvas keeps track of the "replacement chain."  Include this parameter if you wish Canvas to follow the replacement chain if the requested file was deleted and replaced by another.  Indicates the context ID Canvas should use when following the "replacement chain." The "replacement_chain_context_type" parameter must also be included. |

**Returns:** `File`

## GET /v1/courses/{course_id}/files/file_ref/{migration_id}

**Translate file reference**  —  `translate_file_reference`

Get information about a file from a course copy file reference

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `migration_id` | string | path | yes | ID |

**Returns:** `File`

## PUT /v1/files/{id}

**Update file**  —  `update_file`

Update some settings on the specified file

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `name` | string | form |  | The new display name of the file, with a limit of 255 characters. |
| `parent_folder_id` | string | form |  | The id of the folder to move this file into. The new folder must be in the same context as the original parent folder. If the file is in a context without folders this does not apply. |
| `on_duplicate` | string | form |  | If the file is moved to a folder containing a file with the same name, or renamed to a name matching an existing file, the API call will fail unless this parameter is supplied.  "overwrite":: Replace the existing file with the same name "rename":: Add a qualifier to make the new filename unique Allowed: `overwrite`, `rename` |
| `lock_at` | DateTime | form |  | The datetime to lock the file at |
| `unlock_at` | DateTime | form |  | The datetime to unlock the file at |
| `locked` | boolean | form |  | Flag the file as locked |
| `hidden` | boolean | form |  | Flag the file as hidden |
| `visibility_level` | string | form |  | Configure which roles can access this file |

**Returns:** `File`

## DELETE /v1/files/{id}

**Delete file**  —  `delete_file`

Remove the specified file. Unlike most other DELETE endpoints, using this
endpoint will result in comprehensive, irretrievable destruction of the file.
It should be used with the `replace` parameter set to true in cases where the
file preview also needs to be destroyed (such as to remove files that violate
privacy laws).

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `replace` | boolean | query |  | This action is irreversible. If replace is set to true the file contents will be replaced with a generic "file has been removed" file. This also destroys any previews that have been generated for the file. Must have manage files and become other users permissions |

**Returns:** `File`

## GET /v1/files/{id}/icon_metadata

**Get icon metadata**  —  `get_icon_metadata`

Returns the icon maker file attachment metadata

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/files/{id}/reset_verifier  *(deprecated)*

**Reset link verifier**  —  `reset_link_verifier`

> ⚠️ Deprecated: The UUID-based verification method for file access is being deprecated.
This endpoint will no longer be available as UUID verification for file
access is being phased out.

Resets the link verifier. Any existing links to the file using
the previous hard-coded "verifier" parameter will no longer
automatically grant access.

Must have manage files and become other users permissions

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `File`

## GET /v1/folders/{id}/folders

**List folders**  —  `list_folders`

Returns the paginated list of folders in the folder.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/courses/{course_id}/folders

**List all folders**  —  `list_all_folders_courses`

Returns the paginated list of all folders for the given context. This will
be returned as a flat list containing all subfolders as well.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/users/{user_id}/folders

**List all folders**  —  `list_all_folders_users`

Returns the paginated list of all folders for the given context. This will
be returned as a flat list containing all subfolders as well.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/groups/{group_id}/folders

**List all folders**  —  `list_all_folders_groups`

Returns the paginated list of all folders for the given context. This will
be returned as a flat list containing all subfolders as well.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/courses/{course_id}/folders/by_path/*full_path

**Resolve path**  —  `resolve_path_courses_full_path`

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/courses/{course_id}/folders/by_path

**Resolve path**  —  `resolve_path_courses`

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/users/{user_id}/folders/by_path/*full_path

**Resolve path**  —  `resolve_path_users_full_path`

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/users/{user_id}/folders/by_path

**Resolve path**  —  `resolve_path_users`

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/groups/{group_id}/folders/by_path/*full_path

**Resolve path**  —  `resolve_path_groups_full_path`

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/groups/{group_id}/folders/by_path

**Resolve path**  —  `resolve_path_groups`

Given the full path to a folder, returns a list of all Folders in the path hierarchy,
starting at the root folder, and ending at the requested folder. The given path is
relative to the context's root folder and does not include the root folder's name
(e.g., "course files"). If an empty path is given, the context's root folder alone
is returned. Otherwise, if no folder exists with the given full path, a Not Found
error is returned.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[Folder]`

## GET /v1/courses/{course_id}/folders/{id}

**Get folder**  —  `get_folder_courses`

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Folder`

## GET /v1/users/{user_id}/folders/{id}

**Get folder**  —  `get_folder_users`

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Folder`

## GET /v1/groups/{group_id}/folders/{id}

**Get folder**  —  `get_folder_groups`

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Folder`

## GET /v1/folders/{id}

**Get folder**  —  `get_folder_folders`

Returns the details for a folder

You can get the root folder from a context by using 'root' as the :id.
For example, you could get the root folder for a course like:

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `Folder`

## PUT /v1/folders/{id}

**Update folder**  —  `update_folder`

Updates a folder

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `name` | string | form |  | The new name of the folder |
| `parent_folder_id` | string | form |  | The id of the folder to move this folder into. The new folder must be in the same context as the original parent folder. |
| `lock_at` | DateTime | form |  | The datetime to lock the folder at |
| `unlock_at` | DateTime | form |  | The datetime to unlock the folder at |
| `locked` | boolean | form |  | Flag the folder as locked |
| `hidden` | boolean | form |  | Flag the folder as hidden |
| `position` | integer (int64) | form |  | Set an explicit sort position for the folder |

**Returns:** `Folder`

## POST /v1/courses/{course_id}/folders

**Create folder**  —  `create_folder_courses`

Creates a folder in the specified context

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `name` | string | form | yes | The name of the folder |
| `parent_folder_id` | string | form |  | The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used. |
| `parent_folder_path` | string | form |  | The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used. |
| `lock_at` | DateTime | form |  | The datetime to lock the folder at |
| `unlock_at` | DateTime | form |  | The datetime to unlock the folder at |
| `locked` | boolean | form |  | Flag the folder as locked |
| `hidden` | boolean | form |  | Flag the folder as hidden |
| `position` | integer (int64) | form |  | Set an explicit sort position for the folder |

**Returns:** `Folder`

## POST /v1/users/{user_id}/folders

**Create folder**  —  `create_folder_users`

Creates a folder in the specified context

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `name` | string | form | yes | The name of the folder |
| `parent_folder_id` | string | form |  | The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used. |
| `parent_folder_path` | string | form |  | The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used. |
| `lock_at` | DateTime | form |  | The datetime to lock the folder at |
| `unlock_at` | DateTime | form |  | The datetime to unlock the folder at |
| `locked` | boolean | form |  | Flag the folder as locked |
| `hidden` | boolean | form |  | Flag the folder as hidden |
| `position` | integer (int64) | form |  | Set an explicit sort position for the folder |

**Returns:** `Folder`

## POST /v1/groups/{group_id}/folders

**Create folder**  —  `create_folder_groups`

Creates a folder in the specified context

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `name` | string | form | yes | The name of the folder |
| `parent_folder_id` | string | form |  | The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used. |
| `parent_folder_path` | string | form |  | The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used. |
| `lock_at` | DateTime | form |  | The datetime to lock the folder at |
| `unlock_at` | DateTime | form |  | The datetime to unlock the folder at |
| `locked` | boolean | form |  | Flag the folder as locked |
| `hidden` | boolean | form |  | Flag the folder as hidden |
| `position` | integer (int64) | form |  | Set an explicit sort position for the folder |

**Returns:** `Folder`

## POST /v1/folders/{folder_id}/folders

**Create folder**  —  `create_folder_folders`

Creates a folder in the specified context

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `folder_id` | string | path | yes | ID |
| `name` | string | form | yes | The name of the folder |
| `parent_folder_id` | string | form |  | The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used. |
| `parent_folder_path` | string | form |  | The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used. |
| `lock_at` | DateTime | form |  | The datetime to lock the folder at |
| `unlock_at` | DateTime | form |  | The datetime to unlock the folder at |
| `locked` | boolean | form |  | Flag the folder as locked |
| `hidden` | boolean | form |  | Flag the folder as hidden |
| `position` | integer (int64) | form |  | Set an explicit sort position for the folder |

**Returns:** `Folder`

## POST /v1/accounts/{account_id}/folders

**Create folder**  —  `create_folder_accounts`

Creates a folder in the specified context

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `name` | string | form | yes | The name of the folder |
| `parent_folder_id` | string | form |  | The id of the folder to store the new folder in. An error will be returned if this does not correspond to an existing folder. If this and parent_folder_path are sent an error will be returned. If neither is given, a default folder will be used. |
| `parent_folder_path` | string | form |  | The path of the folder to store the new folder in. The path separator is the forward slash `/`, never a back slash. The parent folder will be created if it does not already exist. This parameter only applies to new folders in a context that has folders, such as a user, a course, or a group. If this and parent_folder_id are sent an error will be returned. If neither is given, a default folder will be used. |
| `lock_at` | DateTime | form |  | The datetime to lock the folder at |
| `unlock_at` | DateTime | form |  | The datetime to unlock the folder at |
| `locked` | boolean | form |  | Flag the folder as locked |
| `hidden` | boolean | form |  | Flag the folder as hidden |
| `position` | integer (int64) | form |  | Set an explicit sort position for the folder |

**Returns:** `Folder`

## DELETE /v1/folders/{id}

**Delete folder**  —  `delete_folder`

Remove the specified folder. You can only delete empty folders unless you
set the 'force' flag

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |
| `force` | boolean | query |  | Set to 'true' to allow deleting a non-empty folder |

**Returns:** `void`

## POST /v1/folders/{folder_id}/files

**Upload a file**  —  `upload_file`

Upload a file to a folder.

This API endpoint is the first step in uploading a file.
See the {file:file.file_uploads.html File Upload Documentation} for details on
the file upload workflow.

Only those with the "Manage Files" permission on a course or group can
upload files to a folder in that course or group.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `folder_id` | string | path | yes | ID |

**Returns:** `void`

## POST /v1/folders/{dest_folder_id}/copy_file

**Copy a file**  —  `copy_file`

Copy a file from elsewhere in Canvas into a folder.

Copying a file across contexts (between courses and users) is permitted,
but the source and destination must belong to the same institution.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `dest_folder_id` | string | path | yes | ID |
| `source_file_id` | string | form | yes | The id of the source file |
| `on_duplicate` | string | form |  | What to do if a file with the same name already exists at the destination. If such a file exists and this parameter is not given, the call will fail.  "overwrite":: Replace an existing file with the same name "rename":: Add a qualifier to make the new filename unique Allowed: `overwrite`, `rename` |

**Returns:** `File`

## POST /v1/folders/{dest_folder_id}/copy_folder

**Copy a folder**  —  `copy_folder`

Copy a folder (and its contents) from elsewhere in Canvas into a folder.

Copying a folder across contexts (between courses and users) is permitted,
but the source and destination must belong to the same institution.
If the source and destination folders are in the same context, the
source folder may not contain the destination folder. A folder will be
renamed at its destination if another folder with the same name already
exists.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `dest_folder_id` | string | path | yes | ID |
| `source_folder_id` | string | form | yes | The id of the source folder |

**Returns:** `Folder`

## GET /v1/courses/{course_id}/folders/media

**Get uploaded media folder for user**  —  `get_uploaded_media_folder_for_user_courses`

Returns the details for a designated upload folder that the user has rights to
upload to, and creates it if it doesn't exist.

If the current user does not have the permissions to manage files
in the course or group, the folder will belong to the current user directly.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `Folder`

## GET /v1/groups/{group_id}/folders/media

**Get uploaded media folder for user**  —  `get_uploaded_media_folder_for_user_groups`

Returns the details for a designated upload folder that the user has rights to
upload to, and creates it if it doesn't exist.

If the current user does not have the permissions to manage files
in the course or group, the folder will belong to the current user directly.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `Folder`

## PUT /v1/courses/{course_id}/usage_rights

**Set usage rights**  —  `set_usage_rights_courses`

Sets copyright and license information for one or more files

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `file_ids` | array[string] | form | yes | List of ids of files to set usage rights for. |
| `folder_ids` | array[string] | form |  | List of ids of folders to search for files to set usage rights for. Note that new files uploaded to these folders do not automatically inherit these rights. |
| `publish` | boolean | form |  | Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save). |
| `usage_rights[use_justification]` | string | form | yes | The intellectual property justification for using the files in Canvas Allowed: `own_copyright`, `used_by_permission`, `fair_use`, `public_domain`, `creative_commons` |
| `usage_rights[legal_copyright]` | string | form |  | The legal copyright line for the files |
| `usage_rights[license]` | string | form |  | The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types. |

**Returns:** `UsageRights`

## PUT /v1/groups/{group_id}/usage_rights

**Set usage rights**  —  `set_usage_rights_groups`

Sets copyright and license information for one or more files

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `file_ids` | array[string] | form | yes | List of ids of files to set usage rights for. |
| `folder_ids` | array[string] | form |  | List of ids of folders to search for files to set usage rights for. Note that new files uploaded to these folders do not automatically inherit these rights. |
| `publish` | boolean | form |  | Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save). |
| `usage_rights[use_justification]` | string | form | yes | The intellectual property justification for using the files in Canvas Allowed: `own_copyright`, `used_by_permission`, `fair_use`, `public_domain`, `creative_commons` |
| `usage_rights[legal_copyright]` | string | form |  | The legal copyright line for the files |
| `usage_rights[license]` | string | form |  | The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types. |

**Returns:** `UsageRights`

## PUT /v1/users/{user_id}/usage_rights

**Set usage rights**  —  `set_usage_rights_users`

Sets copyright and license information for one or more files

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `file_ids` | array[string] | form | yes | List of ids of files to set usage rights for. |
| `folder_ids` | array[string] | form |  | List of ids of folders to search for files to set usage rights for. Note that new files uploaded to these folders do not automatically inherit these rights. |
| `publish` | boolean | form |  | Whether the file(s) or folder(s) should be published on save, provided that usage rights have been specified (set to `true` to publish on save). |
| `usage_rights[use_justification]` | string | form | yes | The intellectual property justification for using the files in Canvas Allowed: `own_copyright`, `used_by_permission`, `fair_use`, `public_domain`, `creative_commons` |
| `usage_rights[legal_copyright]` | string | form |  | The legal copyright line for the files |
| `usage_rights[license]` | string | form |  | The license that applies to the files. See the {api:UsageRightsController#licenses List licenses endpoint} for the supported license types. |

**Returns:** `UsageRights`

## DELETE /v1/courses/{course_id}/usage_rights

**Remove usage rights**  —  `remove_usage_rights_courses`

Removes copyright and license information associated with one or more files

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `file_ids` | array[string] | query | yes | List of ids of files to remove associated usage rights from. |
| `folder_ids` | array[string] | query |  | List of ids of folders. Usage rights will be removed from all files in these folders. |

**Returns:** `void`

## DELETE /v1/groups/{group_id}/usage_rights

**Remove usage rights**  —  `remove_usage_rights_groups`

Removes copyright and license information associated with one or more files

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |
| `file_ids` | array[string] | query | yes | List of ids of files to remove associated usage rights from. |
| `folder_ids` | array[string] | query |  | List of ids of folders. Usage rights will be removed from all files in these folders. |

**Returns:** `void`

## DELETE /v1/users/{user_id}/usage_rights

**Remove usage rights**  —  `remove_usage_rights_users`

Removes copyright and license information associated with one or more files

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |
| `file_ids` | array[string] | query | yes | List of ids of files to remove associated usage rights from. |
| `folder_ids` | array[string] | query |  | List of ids of folders. Usage rights will be removed from all files in these folders. |

**Returns:** `void`

## GET /v1/courses/{course_id}/content_licenses

**List licenses**  —  `list_licenses_courses`

A paginated list of licenses that can be applied

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |

**Returns:** `array[License]`

## GET /v1/groups/{group_id}/content_licenses

**List licenses**  —  `list_licenses_groups`

A paginated list of licenses that can be applied

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `group_id` | string | path | yes | ID |

**Returns:** `array[License]`

## GET /v1/users/{user_id}/content_licenses

**List licenses**  —  `list_licenses_users`

A paginated list of licenses that can be applied

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `user_id` | string | path | yes | ID |

**Returns:** `array[License]`


---

# Models


## File

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | e.g. `569` |
| `folder_id` | integer |  | e.g. `4207` |
| `display_name` | string |  | e.g. `file.txt` |
| `filename` | string |  | e.g. `file.txt` |
| `content-type` | string |  | e.g. `text/plain` |
| `url` | string |  | e.g. `http://www.example.com/files/569/download?download_frd=1` |
| `size` | integer |  | file size in bytes e.g. `43451` |
| `created_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
| `updated_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
| `unlock_at` | datetime |  | e.g. `2012-07-07T14:58:50Z` |
| `locked` | boolean |  | e.g. `False` |
| `hidden` | boolean |  | e.g. `False` |
| `lock_at` | datetime |  | e.g. `2012-07-20T14:58:50Z` |
| `hidden_for_user` | boolean |  | e.g. `False` |
| `visibility_level` | string |  | Changes who can access the file. Valid options are 'inherit' (the default), 'course', 'institution', and 'public'. Only valid in course endpoints. e.g. `course` |
| `thumbnail_url` | string |  |  |
| `modified_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
| `mime_class` | string |  | simplified content-type mapping e.g. `html` |
| `media_entry_id` | string |  | identifier for file in third-party transcoding service e.g. `m-3z31gfpPf129dD3sSDF85SwSDFnwe` |
| `locked_for_user` | boolean |  | e.g. `False` |
| `lock_info` | LockInfo |  |  |
| `lock_explanation` | string |  | e.g. `This assignment is locked until September 1 at 12:00am` |
| `preview_url` | string |  | optional: url to the document preview. This url is specific to the user making the api call. Only included in submission endpoints. |


## Folder

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `context_type` | string |  | e.g. `Course` |
| `context_id` | integer |  | e.g. `1401` |
| `files_count` | integer |  | e.g. `0` |
| `position` | integer |  | e.g. `3` |
| `updated_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
| `folders_url` | string |  | e.g. `https://www.example.com/api/v1/folders/2937/folders` |
| `files_url` | string |  | e.g. `https://www.example.com/api/v1/folders/2937/files` |
| `full_name` | string |  | e.g. `course files/11folder` |
| `lock_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
| `id` | integer |  | e.g. `2937` |
| `folders_count` | integer |  | e.g. `0` |
| `name` | string |  | e.g. `11folder` |
| `parent_folder_id` | integer |  | e.g. `2934` |
| `created_at` | datetime |  | e.g. `2012-07-06T14:58:50Z` |
| `unlock_at` | datetime |  |  |
| `hidden` | boolean |  | e.g. `False` |
| `hidden_for_user` | boolean |  | e.g. `False` |
| `locked` | boolean |  | e.g. `True` |
| `locked_for_user` | boolean |  | e.g. `False` |
| `for_submissions` | boolean |  | If true, indicates this is a read-only folder containing files submitted to assignments e.g. `False` |


## UsageRights

Describes the copyright and license information for a File

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `legal_copyright` | string |  | Copyright line for the file e.g. `(C) 2014 Incom Corporation Ltd` |
| `use_justification` | string |  | Justification for using the file in a Canvas course. Valid values are 'own_copyright', 'public_domain', 'used_by_permission', 'fair_use', 'creative_commons' e.g. `creative_commons` |
| `license` | string |  | License identifier for the file. e.g. `cc_by_sa` |
| `license_name` | string |  | Readable license name e.g. `CC Attribution Share-Alike` |
| `message` | string |  | Explanation of the action performed e.g. `4 files updated` |
| `file_ids` | array[integer] |  | List of ids of files that were updated e.g. `[1, 2, 3]` |


## License

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | a short string identifying the license e.g. `cc_by_sa` |
| `name` | string |  | the name of the license e.g. `CC Attribution ShareAlike` |
| `url` | string |  | a link to the license text e.g. `http://creativecommons.org/licenses/by-sa/4.0` |
