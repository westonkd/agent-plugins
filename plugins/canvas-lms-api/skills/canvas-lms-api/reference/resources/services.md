# Services

> Canvas LMS REST API — `/services` resource. Base path `/api`.

## GET /v1/services/kaltura

**Get Kaltura config**  —  `get_kaltura_config`

Return the config information for the Kaltura plugin in json format.

**Returns:** `void`

## POST /v1/services/kaltura_session

**Start Kaltura session**  —  `start_kaltura_session`

Start a new Kaltura session, so that new media can be recorded and uploaded
to this Canvas instance's Kaltura instance.

**Returns:** `void`
