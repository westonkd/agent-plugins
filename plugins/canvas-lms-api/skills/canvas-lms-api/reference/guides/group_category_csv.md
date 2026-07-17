# Group Category Import Format Documentation

Group categories can be updated in bulk by using the Group Categories Import API. Each row in a CSV file represents a user to be added to a group in the group category.

Groups that don't exist in the UI will be created. Groups that are created will only use the group_name column for creation. User columns in the file are used to identify the user to be added to the group. Users names are available in the group_category export, but not used or updated in the import process.

Standard CSV rules apply (including adherence to the CSV RFC 4180 format):

- The first row will be interpreted as a header defining the ordering of your columns. This header row is mandatory.
- Fields that contain a comma must be surrounded by double-quotes.
- Fields that contain double-quotes must also be surrounded by double-quotes, with the internal double-quotes doubled. Example: Chevy "The Man" Chase would be included in the CSV as "Chevy ""The Man"" Chase".

All text should be UTF-8 encoded.

# Group Category Data Format

## group_category.csv

| Field Name | Data Type | Required | Description |
| --- | --- | --- | --- |
| canvas_user_id | text | ✓* | The canvas id for a user, required to identify a user. |
| user_id | text | ✓* | A unique identifier used to reference users in the enrollments table. This identifier must not change for the user, and must be globally unique. In the user interface, this is called the SIS ID. |
| login_id | text | ✓* | The name that a user will use to login to Instructure. If you have an authentication service configured (like LDAP), this will be their username from the remote system. |
| group_name | text | ✓* | The name of the group. |
| canvas_group_id | text | ✓* | The canvas id for a group. |
| group_id | text | ✓* | A unique identifier used to reference groups in the group_users data. This identifier must not change for the group, and must be globally unique. This column is for identification and does not populate new groups with sis_ids |

* canvas_user_id, user_id, or login_id is required and group_name, canvas_group_id or group_id is required.

Sample:

```
canvas_user_id,user_id,login_id,group_name,canvas_group_id,group_id
92,,,Awesome Group,,
,13aa3,,,45,
,,mlemon,,,g125
```

```
canvas_user_id,user_id,login_id,group_name
92,,,Awesome Group
,13aa3,,Other Group
,,mlemon,Awesome Group
```
