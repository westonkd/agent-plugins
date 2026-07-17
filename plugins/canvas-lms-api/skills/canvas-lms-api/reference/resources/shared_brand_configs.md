# Shared Brand Configs

> Canvas LMS REST API — `/shared_brand_configs` resource. Base path `/api`.

## POST /v1/accounts/{account_id}/shared_brand_configs

**Share a BrandConfig (Theme)**  —  `share_brandconfig_theme`

Create a SharedBrandConfig, which will give the given brand_config a name
and make it available to other users of this account.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `shared_brand_config[name]` | string | form | yes | Name to share this BrandConfig (theme) as. |
| `shared_brand_config[brand_config_md5]` | string | form | yes | MD5 of brand_config to share |

**Returns:** `SharedBrandConfig`

## PUT /v1/accounts/{account_id}/shared_brand_configs/{id}

**Update a shared theme**  —  `update_shared_theme`

Update the specified shared_brand_config with a new name or to point to a new brand_config.
Uses same parameters as create.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `account_id` | string | path | yes | ID |
| `id` | string | path | yes | ID |

**Returns:** `SharedBrandConfig`

## DELETE /v1/shared_brand_configs/{id}

**Un-share a BrandConfig (Theme)**  —  `un_share_brandconfig_theme`

Delete a SharedBrandConfig, which will unshare it so you nor anyone else in
your account will see it as an option to pick from.

| Param | Type | In | Req | Description |
| --- | --- | --- | --- | --- |
| `id` | string | path | yes | ID |

**Returns:** `SharedBrandConfig`


---

# Models


## SharedBrandConfig

| Property | Type | Req | Description |
| --- | --- | --- | --- |
| `id` | integer |  | The shared_brand_config identifier. e.g. `987` |
| `account_id` | string |  | The id of the account it should be shared within. |
| `brand_config_md5` | string |  | The md5 (since BrandConfigs are identified by MD5 and not numeric id) of the BrandConfig to share. e.g. `1d31002c95842f8fe16da7dfcc0d1f39` |
| `name` | string |  | The name to share this theme as e.g. `Crimson and Gold Verson 1` |
| `created_at` | datetime |  | When this was created e.g. `2012-07-13T10:55:20-06:00` |
| `updated_at` | datetime |  | When this was last updated e.g. `2012-07-13T10:55:20-06:00` |
