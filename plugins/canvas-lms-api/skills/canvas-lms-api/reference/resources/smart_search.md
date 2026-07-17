# Smart Search

> Canvas LMS REST API — `/smart_search` resource. Base path `/api`.

## GET /v1/courses/{course_id}/smartsearch

**Search course content**  —  `search_course_content`

Find course content using a meaning-based search

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `q` | string | query | yes | The search query |
| `filter` | array[string] | query |  | Types of objects to search. By default, all supported types are searched. Supported types include +pages+, +assignments+, +announcements+, and +discussion_topics+. |
| `include` | array[string] | query |  | Optional information to include with each search result: modules:: An array of module objects that the search result belongs to. status:: The published status for all results and the due_date for all assignments. Allowed: `status`, `modules` |

**Returns:** `array[SearchResult]`


---

# Models


## SearchResult

Reference to an object that matches a smart search

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `content_id` | integer (int64) |  | The ID of the matching object. e.g. `2` |
| `content_type` | string |  | The type of the matching object. e.g. `WikiPage` |
| `title` | string |  | The title of the matching object. e.g. `Nicolaus Copernicus` |
| `body` | string |  | The body of the matching object. e.g. `Nicolaus Copernicus was a Renaissance-era mathematician and astronomer who...` |
| `html_url` | string |  | The Canvas URL of the matching object. e.g. `https://canvas.example.com/courses/123/pages/nicolaus-copernicus` |
| `distance` | number |  | The distance between the search query and the result. Smaller numbers indicate closer matches. e.g. `0.212` |
