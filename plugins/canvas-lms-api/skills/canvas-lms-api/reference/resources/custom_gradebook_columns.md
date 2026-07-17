# Custom Gradebook Columns

> Canvas LMS REST API — `/custom_gradebook_columns` resource. Base path `/api`.

## GET /v1/courses/{course_id}/custom_gradebook_columns

**List custom gradebook columns**  —  `list_custom_gradebook_columns`

A paginated list of all custom gradebook columns for a course

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `include_hidden` | boolean | query |  | Include hidden parameters (defaults to false) |

**Returns:** `array[CustomColumn]`

## POST /v1/courses/{course_id}/custom_gradebook_columns

**Create a custom gradebook column**  —  `create_custom_gradebook_column`

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `column[title]` | string | form | yes | no description |
| `column[position]` | integer (int64) | form |  | The position of the column relative to other custom columns |
| `column[hidden]` | boolean | form |  | Hidden columns are not displayed in the gradebook |
| `column[teacher_notes]` | boolean | form |  | Set this if the column is created by a teacher.  The gradebook only supports one teacher_notes column. |
| `column[read_only]` | boolean | form |  | Set this to prevent the column from being editable in the gradebook ui |

**Returns:** `CustomColumn`

## PUT /v1/courses/{course_id}/custom_gradebook_columns/{id}

**Update a custom gradebook column**  —  `update_custom_gradebook_column`

Accepts the same parameters as custom gradebook column creation

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `CustomColumn`

## DELETE /v1/courses/{course_id}/custom_gradebook_columns/{id}

**Delete a custom gradebook column**  —  `delete_custom_gradebook_column`

Permanently deletes a custom column and its associated data

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `CustomColumn`

## POST /v1/courses/{course_id}/custom_gradebook_columns/reorder

**Reorder custom columns**  —  `reorder_custom_columns`

Puts the given columns in the specified order

<b>200 OK</b> is returned if successful

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `order` | array[integer] | form | yes | no description |

**Returns:** `void`

## GET /v1/courses/{course_id}/custom_gradebook_columns/{id}/data

**List entries for a column**  —  `list_entries_for_column`

This does not list entries for students without associated data.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `include_hidden` | boolean | query |  | If true, hidden columns will be included in the result. If false or absent, only visible columns will be returned. |

**Returns:** `array[ColumnDatum]`

## PUT /v1/courses/{course_id}/custom_gradebook_columns/{id}/data/{user_id}

**Update column data**  —  `update_column_data`

Set the content of a custom column

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |
| `user_id` | string | path | yes | ID |
| `column_data[content]` | string | form | yes | Column content.  Setting this to blank will delete the datum object. |

**Returns:** `ColumnDatum`

## PUT /v1/courses/{course_id}/custom_gradebook_column_data

**Bulk update column data**  —  `bulk_update_column_data`

Set the content of custom columns

{
  "column_data": [
    {
      "column_id": example_column_id,
      "user_id": example_student_id,
      "content": example_content
      },
      {
      "column_id": example_column_id,
      "user_id": example_student_id,
      "content: example_content
    }
  ]
}

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `column_data` | array[Array] | form | yes | Column content. Setting this to an empty string will delete the data object. |

**Returns:** `Progress`


---

# Models


## CustomColumn

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The ID of the custom gradebook column e.g. `2` |
| `teacher_notes` | boolean |  | When true, this column's visibility will be toggled in the Gradebook when a user selects to show or hide notes e.g. `False` |
| `title` | string |  | header text e.g. `Stuff` |
| `position` | integer |  | column order e.g. `1` |
| `hidden` | boolean |  | won't be displayed if hidden is true e.g. `False` |
| `read_only` | boolean |  | won't be editable in the gradebook UI e.g. `True` |


## ColumnDatum

ColumnDatum objects contain the entry for a column for each user.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `content` | string |  | e.g. `Nut allergy` |
| `user_id` | integer |  | e.g. `2` |
