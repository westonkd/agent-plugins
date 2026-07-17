# Quiz Statistics

> Canvas LMS REST API — `/quiz_statistics` resource. Base path `/api`.

## GET /v1/courses/{course_id}/quizzes/{quiz_id}/statistics

**Fetching the latest quiz statistics**  —  `fetching_latest_quiz_statistics`

This endpoint provides statistics for all quiz versions, or for a specific
quiz version, in which case the output is guaranteed to represent the
_latest_ and most current version of the quiz.

<b>200 OK</b> response code is returned if the request was successful.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `course_id` | string | path | yes | ID |
| `quiz_id` | string | path | yes | ID |
| `all_versions` | boolean | query |  | Whether the statistics report should include all submissions attempts. |

**Returns:** `void`


---

# Models


## QuizStatistics

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) | yes | The ID of the quiz statistics report. e.g. `1` |
| `quiz_id` | integer (int64) | yes | The ID of the Quiz the statistics report is for.  NOTE: AVAILABLE ONLY IN NON-JSON-API REQUESTS. e.g. `2` |
| `multiple_attempts_exist` | boolean |  | Whether there are any students that have made mutliple submissions for this quiz. e.g. `True` |
| `includes_all_versions` | boolean |  | In the presence of multiple attempts, this field describes whether the statistics describe all the submission attempts and not only the latest ones. e.g. `True` |
| `generated_at` | datetime |  | The time at which the statistics were generated, which is usually after the occurrence of a quiz event, like a student submitting it. e.g. `2013-01-23T23:59:00-07:00` |
| `url` | string |  | The API HTTP/HTTPS URL to this quiz statistics. e.g. `http://canvas.example.edu/api/v1/courses/1/quizzes/2/statistics` |
| `html_url` | string |  | The HTTP/HTTPS URL to the page where the statistics can be seen visually. e.g. `http://canvas.example.edu/courses/1/quizzes/2/statistics` |
| `question_statistics` | QuizStatisticsQuestionStatistics |  | Question-specific statistics for each question and its answers. |
| `submission_statistics` | QuizStatisticsSubmissionStatistics |  | Question-specific statistics for each question and its answers. |
| `links` | QuizStatisticsLinks |  | JSON-API construct that contains links to media related to this quiz statistics object.  NOTE: AVAILABLE ONLY IN JSON-API REQUESTS. |


## QuizStatisticsLinks

Links to media related to QuizStatistics.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `quiz` | string |  | HTTP/HTTPS API URL to the quiz this statistics describe. e.g. `http://canvas.example.edu/api/v1/courses/1/quizzes/2` |


## QuizStatisticsQuestionStatistics

Statistics for submissions made to a specific quiz question.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `responses` | integer (int64) |  | Number of students who have provided an answer to this question. Blank or empty responses are not counted. e.g. `3` |
| `answers` | QuizStatisticsAnswerStatistics |  | Statistics related to each individual pre-defined answer. |


## QuizStatisticsAnswerStatistics

Statistics for a specific pre-defined answer in a Multiple-Choice or True/False quiz question.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer (int64) |  | ID of the answer. e.g. `3866` |
| `text` | string |  | The text attached to the answer. e.g. `Blue.` |
| `weight` | integer (int64) |  | An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should 100 e.g. `100` |
| `responses` | integer (int64) |  | Number of students who have chosen this answer. e.g. `2` |


## QuizStatisticsAnswerPointBiserial

A point-biserial construct for a single pre-defined answer in a Multiple-Choice or True/False question.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `answer_id` | integer (int64) |  | ID of the answer the point biserial is for. e.g. `3866` |
| `point_biserial` | number |  | The point biserial value for this answer. Value ranges between -1 and 1. e.g. `-0.802955068546966` |
| `correct` | boolean |  | Convenience attribute that denotes whether this is the correct answer as opposed to being a distractor. This is mutually exclusive with the `distractor` value e.g. `True` |
| `distractor` | boolean |  | Convenience attribute that denotes whether this is a distractor answer and not the correct one. This is mutually exclusive with the `correct` value e.g. `False` |


## QuizStatisticsSubmissionStatistics

Generic statistics for all submissions for a quiz.

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `unique_count` | integer (int64) |  | The number of students who have taken the quiz. e.g. `3` |
| `score_average` | number |  | The mean of the student submission scores. e.g. `4.33333333333333` |
| `score_high` | number |  | The highest submission score. e.g. `6` |
| `score_low` | number |  | The lowest submission score. e.g. `3` |
| `score_stdev` | number |  | Standard deviation of the submission scores. e.g. `1.24721912892465` |
| `scores` | object |  | A percentile distribution of the student scores, each key is the percentile (ranges between 0 and 100%) while the value is the number of students who received that score. e.g. `{'50': 1, '34': 5, '100': 1}` |
| `correct_count_average` | number |  | The mean of the number of questions answered correctly by each student. e.g. `3.66666666666667` |
| `incorrect_count_average` | number |  | The mean of the number of questions answered incorrectly by each student. e.g. `5` |
| `duration_average` | number |  | The average time spent by students while taking the quiz. e.g. `42.333333333` |
