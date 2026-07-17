---
name: canvas-lms-api
description: >-
  Subject-matter expert on the Canvas LMS REST API. Use when working with
  Canvas LMS API endpoints, request/response parameters, object models,
  authentication (OAuth2 / access tokens), pagination, SIS imports & CSV
  formats, LTI / LTI Advantage tools, Live Events & Caliper, or Canvas RBAC
  role permissions. Covers all 142 API resource groups (~1,078 endpoints),
  their models, and the conceptual guides. Trigger on questions about how to
  call a Canvas endpoint, what parameters/fields it takes or returns, how to
  authenticate or paginate, or which permission an action requires.
---

# Canvas LMS REST API — SME

Authoritative reference for the Canvas LMS REST API: **142 resource groups,
~1,078 endpoints, 274 object models**, plus narrative guides (auth, pagination,
uploads, SIS, LTI, Live Events) and the full RBAC permission catalog.

The corpus is large, so it is **not** loaded up front. This file is the map:
use the routing steps below to open only the one or two narrow files a task
needs. Everything under `reference/` is generated from the official Canvas
Swagger docs (see *Regenerating* at the bottom).

## When to use
- Constructing or debugging a call to a Canvas endpoint (path, method, params).
- Looking up what fields a request accepts or a response returns (object models).
- Auth (OAuth2 / access tokens / JWT), pagination, rate limiting, SIS IDs.
- SIS bulk import CSV formats; LTI / LTI Advantage tool config & launches.
- Live Events / Caliper event payloads.
- Which Canvas role **permission** gates an action.

## How to navigate this skill (progressive disclosure)

1. **Find the endpoint.** Grep the endpoint index for a keyword — it holds one
   line per endpoint (method, path, summary, nickname):
   ```
   grep -i "enroll a user" reference/endpoints-index.md
   ```
   Each `### Resource — resources/<slug>.md` header tells you which detail file
   to open next.

2. **Open the resource detail.** `reference/resources/<slug>.md` has every
   endpoint for that resource with full parameter tables (type, in, required,
   allowed values, description), return type, and the resource's object
   **Models**. Read only the file you need — e.g. `reference/resources/courses.md`.

3. **Read a concept guide** for anything that isn't a single endpoint — auth,
   pagination, file uploads, SIS CSV, LTI, Live Events. See
   `reference/guides/README.md` for the indexed list, then open the one guide.

4. **Look up a permission.** Grep the consolidated RBAC file:
   ```
   grep -i "manage_grades" reference/permissions.md
   ```

5. **Browse by area.** `reference/catalog.md` lists all 142 resources with
   endpoint/model counts. The **Resource map** below groups them by domain.

Don't dump whole files into context speculatively — grep first, then open the
single matching file.

## API essentials

- **Base URL:** `https://<canvas-host>/api/v1/` (a few newer endpoints use
  `/api/lti/...` or unversioned paths — the resource files show the exact path).
- **Auth:** Bearer token — `Authorization: Bearer <token>`. Tokens come from
  manual access tokens or OAuth2. Post-2015 keys expire in 1h → use refresh
  tokens. Deep dive: `reference/guides/oauth.md`, `oauth_endpoints.md`,
  `jwt_access_tokens.md`; manage tokens via the `access_tokens` resource.
- **Pagination:** list endpoints default to 10/page; set `?per_page=`. **Follow
  the `Link` header** (`rel="next"`), treat URLs as opaque. Full rules:
  `reference/guides/pagination.md`.
- **Rate limiting:** Canvas throttles per-token; a `403 Forbidden` with
  `X-Rate-Limit-Remaining: 0` means throttled — back off. See
  `reference/guides/throttling.md`.
- **Object IDs & SIS IDs:** reference objects by Canvas ID, or by SIS ID with a
  prefix, e.g. `sis_login_id:`, `sis_user_id:`, `sis_course_id:`
  (`courses/sis_course_id:ABC123`). See `reference/guides/object_ids.md`.
- **Array params:** repeated/bracketed, e.g. `include[]=enrollments&include[]=locked`.
  Parameter tables list allowed `include[]` / `state[]` values per endpoint.
- **Nested params:** form bodies are namespaced, e.g. `course[name]`,
  `assignment[points_possible]` (the parameter tables show these literal names).
- **GraphQL:** Canvas also exposes a GraphQL endpoint — `reference/guides/graphql.md`.

## Resource map (142 resources → `reference/resources/<slug>.md`)

**Courses, Sections & Terms** — `courses`, `sections`, `enrollment_terms`,
`course_pace`, `blackout_dates`, `favorites`, `tabs`, `learning_object_dates`

**Enrollments & People** — `enrollments`, `users`, `user_observees`,
`temporary_enrollment_pairings`, `logins`

**Accounts & Institution Admin** — `accounts`, `accounts_(lti)`, `admins`,
`roles`, `account_calendars`, `account_notifications`, `brand_configs`,
`shared_brand_configs`, `content_security_policy_settings`, `feature_flags`

**Authentication, Tokens & Security** — `access_tokens`, `inst_access_tokens`,
`jw_ts`, `api_token_scopes`, `public_jwk`, `security`, `authentication_providers`,
`authentications_log`, `developer_keys`, `developer_key_account_bindings`

**Assignments** — `assignments`, `assignment_groups`, `assignment_extensions`,
`peer_reviews`

**Quizzes (Classic)** — `quizzes`, `quiz_questions`, `quiz_question_groups`,
`quiz_reports`, `quiz_statistics`, `quiz_submissions`, `quiz_submission_questions`,
`quiz_submission_events`, `quiz_submission_files`, `quiz_submission_user_list`,
`quiz_extensions`, `course_quiz_extensions`, `quiz_assignment_overrides`,
`quiz_ip_filters`, `assessment_question_banks`

**Grades & Gradebook** — `submissions`, `submission_comments`, `gradebook_history`,
`grade_change_log`, `grading_periods`, `grading_period_sets`, `grading_standards`,
`custom_gradebook_columns`, `late_policy`, `moderated_grading`, `what_if_grades`

**Outcomes & Rubrics** — `outcomes`, `outcome_groups`, `outcome_results`,
`outcome_imports`, `rubrics`, `proficiency_ratings`, `live_assessments`

**Course Content** — `modules`, `pages`, `files`, `discussion_topics`,
`announcements`, `announcement_external_feeds`, `discovery_pages`, `media_objects`,
`collaborations`, `conferences`, `block_editor_template`, `content_shares`

**Migration, Blueprint & Export** — `content_migrations`, `content_exports`,
`e_pub_exports`, `blueprint_courses`, `progress`

**Calendar, Communication & Planner** — `calendar_events`, `appointment_groups`,
`planner`, `conversations`, `comm_messages`, `communication_channels`,
`notification_preferences`, `bookmarks`

**Groups** — `groups`, `group_categories`, `microsoft_sync___groups`

**LTI & External Tools** — `external_tools`, `lti_registrations`, `lti_deployments`,
`lti_context_controls`, `lti_resource_links`, `lti_launch_definitions`,
`lti_dynamic_registrations`, `lti_advantage_feature_flags`, `lti_2_authorization`,
`tool_configuration_api`, `asset_processor`, `names_and_role`, `line_items`,
`score`, `result`, `notice_handlers`

**Plagiarism & Originality** — `plagiarism_detection_platform_assignments`,
`plagiarism_detection_platform_users`, `plagiarism_detection_submissions`,
`webhooks_subscriptions_for_plagiarism_platform`, `originality_reports`

**SIS & Data Integration** — `sis_imports`, `sis_import_errors`, `sis_integration`,
`data_services`, `services`

**Reports, Logs & Accessibility** — `account_reports`, `course_reports`,
`course_audit_log`, `history`, `error_reports`, `accessibility_course_scans`,
`accessibility_course_statistics`

**Polls** — `polls`, `poll_sessions`, `poll_choices`, `poll_submissions`

**AI & Assist** — `ai_conversations`, `ai_experiences`, `study_assist`,
`canvas_career_experiences`

**Portfolios & Search** — `e_portfolios`, `search`, `smart_search`

> Note on grading/LTI overlap: `line_items`, `score`, and `result` are the LTI
> Advantage **Assignment & Grade Services (AGS)** endpoints, grouped here under
> LTI; `names_and_role` is LTI **NRPS**. Use them for tool-driven grade passback.

## Concept guides

Full list with summaries: `reference/guides/README.md`. Frequently needed:
- **Core:** `pagination`, `object_ids`, `throttling`, `masquerading`,
  `endpoint_attributes`, `graphql`, `overview`
- **Auth:** `oauth`, `oauth_endpoints`, `jwt_access_tokens`
- **Files & content:** `file_uploads` (the 3-step upload flow), `content_item`
  (Deep Linking), `document_processor`
- **SIS & bulk import:** `sis_csv`, `provisioning`, `outcomes_csv`,
  `group_category_csv`, `differentiation_tags_csv`
- **LTI & tools:** `tools_intro`, `tools_xml`, `tools_variable_substitutions`,
  `lti_launch_overview`, `lti_dev_key_config`, `placements_overview`,
  `plagiarism_platform`, `pns`, `registration`
- **Live Events & Caliper:** ~36 `data_service_*` guides — event definitions and
  JSON payload examples (e.g. `data_service_canvas_assignment`,
  `data_service_caliper_basic`).

## Permissions (RBAC)

`reference/permissions.md` consolidates every account/course role permission —
what it enables and its dependencies — keyed by the `manage_*` / `view_*` names
used by the **Roles API** (`reference/resources/roles.md`). It opens with an
overview of which permissions are account-level vs course-level. Grep by key,
e.g. `grep -i "manage_course_content" reference/permissions.md`.

## Regenerating the reference

`reference/` is committed so the skill is self-contained when installed. To
rebuild it from the raw Canvas Swagger docs (the gitignored `doc/api/` source
dump), run from the plugin root (`plugins/canvas-lms-api/`):

```
python3 scripts/build_reference.py
```

The build is deterministic and idempotent (stdlib only) and writes to
`skills/canvas-lms-api/reference/`. Re-run it when the `doc/api/` snapshot is
refreshed from a newer Canvas version.
