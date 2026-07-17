# Result

> Canvas LMS REST API — `/result` resource. Base path `/api`.

## GET /lti/courses/{course_id}/line_items/{line_item_id}/results

**Show a collection of Results**  —  `show_collection_of_results`

Show existing Results of a line item. Can be used to retrieve a specific student's
result by adding the user_id (defined as the lti_user_id or the Canvas user_id) as
a query parameter (i.e. user_id=1000). If user_id is included, it will return only
one Result in the collection if the result exists, otherwise it will be empty. May
also limit number of results by adding the limit query param (i.e. limit=100)

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `line_item_id` | string | path | yes | ID |

**Returns:** `Result`

## GET /lti/courses/{course_id}/line_items/{line_item_id}/results/{id}

**Show a Result**  —  `show_result`

Show existing Result of a line item.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `line_item_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `Result`


---

# Models


## Result

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | string |  | The fully qualified URL for showing the Result e.g. `http://institution.canvas.com/api/lti/courses/5/line_items/2/results/1` |
| `userId` | string |  | The lti_user_id or the Canvas user_id e.g. `50 \| 'abcasdf'` |
| `resultScore` | number |  | The score of the result as defined by Canvas, scaled to the resultMaximum e.g. `50` |
| `resultMaximum` | number |  | Maximum possible score for this result; 1 is the default value and will be assumed if not specified otherwise. Minimum value of 0 required. e.g. `50` |
| `comment` | string |  | Comment visible to the student about the result. |
| `scoreOf` | string |  | URL of the line item this belongs to e.g. `http://institution.canvas.com/api/lti/courses/5/line_items/2` |
