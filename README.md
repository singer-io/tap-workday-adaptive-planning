# tap-workday-adaptive-planning

This is a [Singer](https://singer.io) tap that produces JSON-formatted data
following the [Singer
spec](https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md).

This tap:

- Pulls raw data from the [Workday Adaptive Planning API].
- Extracts the following resources:
    - [Accounts](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xlk1623709204009.html)

    - [Currencies](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/rsm1623709205180.html)

    - [Attributes](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/qdp1623708606028.html)

    - [Calendar](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xlk1623709204009.html)

    - [ConfigurableModelData](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/pmf1623709214213.html)

    - [Data](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/mdn1623709213322.html)

    - [DimensionFamilies](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/mgx1623709216136.html)

    - [Dimensions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/fpd1623708607387.html)

    - [DimensionMapping](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/wje1623708998477.html)

    - [Groups](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/fcv1623709217119.html)

    - [Instances](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/cpq1623708996945.html)

    - [Levels](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/eaj1623708609527.html)

    - [Locales](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/wbm1623709218057.html)

    - [ModeledSheetData](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xtz1623709218885.html)

    - [Roles](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/klh1623709221023.html)

    - [PermissionSets](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/bpq1623709219931.html)

    - [SecurityAudit](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/aos1623709222711.html)

    - [SheetDefinition](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/vau1623709225945.html)

    - [Sheets](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/lwe1623709227133.html)

    - [MetadataTime](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/sjd1623709201259.html)

    - [TransactionDefinitions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/wle1623709228117.html)

    - [Users](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xkz1623709229148.html)

    - [Versions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/drf1623709230196.html)

    - [ExchangeRateTypes](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-modeling/jvh1676498737751.html)

    - [SheetAvailability](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-modeling/zxv1644595867938.html)

    - [TenantVersions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-modeling/rgs1660164357553.html)

    - [UserInstances](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-security/wqj1644596400541.html)

    - [UserPermissionSets](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-security/xga1644596183282.html)

    - [Tasks](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-tasks/tasks.html)

    - [TaskRunDetails](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-tasks/tasks.html)

- Outputs the schema for each resource
- Incrementally pulls data based on the input state


## Streams


**[accounts](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xlk1623709204009.html)**
- Data Key = accounts
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[currencies](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/rsm1623709205180.html)**
- Data Key = currencies
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[attributes](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/qdp1623708606028.html)**
- Data Key = attributes
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[calendar](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xlk1623709204009.html)**
- Data Key = calendars
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[configurable_model_data](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/pmf1623709214213.html)**
- Data Key = data
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[data](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/mdn1623709213322.html)**
- Data Key = data
- Primary keys: ['account_code']
- Replication strategy: FULL_TABLE

**[dimension_families](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/mgx1623709216136.html)**
- Data Key = families
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[dimensions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/fpd1623708607387.html)**
- Data Key = dimensions
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[dimension_mapping](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/wje1623708998477.html)**
- Data Key = dimensions
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[groups](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/fcv1623709217119.html)**
- Data Key = groups
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[instances](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/cpq1623708996945.html)**
- Data Key = instances
- Primary keys: ['code']
- Replication strategy: FULL_TABLE

**[levels](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/eaj1623708609527.html)**
- Data Key = levels
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[locales](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/wbm1623709218057.html)**
- Data Key = locales
- Primary keys: ['code']
- Replication strategy: FULL_TABLE

**[modeled_sheet_data](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xtz1623709218885.html)**
- Data Key = ConfigurableModel
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[roles](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/klh1623709221023.html)**
- Data Key = roles
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[permission_sets](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/bpq1623709219931.html)**
- Data Key = permission_sets
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[security_audit](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/aos1623709222711.html)**
- Data Key = audit
- Primary keys: ['timestamp']
- Replication strategy: FULL_TABLE

**[sheet_definition](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/vau1623709225945.html)**
- Data Key = modeled-sheet
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[sheets](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/lwe1623709227133.html)**
- Data Key = sheets
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[metadata_time](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/sjd1623709201259.html)**
- Data Key = time
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[transaction_definitions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/wle1623709228117.html)**
- Data Key = transaction
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[users](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/xkz1623709229148.html)**
- Data Key = users
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[versions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/managing-data-integration/api-documentation/metadata-and-data-create-update-and-read-methods/drf1623709230196.html)**
- Data Key = versions
- Primary keys: ['id']
- Replication strategy: FULL_TABLE

**[exchange_rate_types](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-modeling/jvh1676498737751.html)**
- Primary keys: ['']
- Replication strategy: 

**[sheet_availability](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-modeling/zxv1644595867938.html)**
- Data Key = data
- Primary keys: ['code']
- Replication strategy: FULL_TABLE

**[tenant_versions](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-modeling/rgs1660164357553.html)**
- Data Key = data
- Primary keys: ['name']
- Replication strategy: FULL_TABLE

**[user_instances](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-security/wqj1644596400541.html)**
- Data Key = users
- Primary keys: ['userGuid']
- Replication strategy: FULL_TABLE

**[user_permission_sets](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-security/xga1644596183282.html)**
- Data Key = users
- Primary keys: ['userGuid']
- Replication strategy: FULL_TABLE

**[tasks](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-tasks/tasks.html)**
- Data Key = data
- Primary keys: id
- Replication strategy: FULL_TABLE

**[task_run_details](https://doc.workday.com/adaptive-planning/en-us/workday-adaptive-planning-documentation/integration/rest-apis-json-/service-tasks/tasks.html)**
- Data Key = data
- Primary keys: id
- Replication strategy: FULL_TABLE



## Authentication

## Quick Start

1. Install

    Clone this repository, and then install using setup.py. We recommend using a virtualenv:

    ```bash
    > virtualenv -p python3 venv
    > source venv/bin/activate
    > python setup.py install
    OR
    > cd .../tap-workday-adaptive-planning
    > pip install -e .
    ```
2. Dependent libraries. The following dependent libraries were installed.
    ```bash
    > pip install singer-python
    > pip install target-stitch
    > pip install target-json

    ```
    - [singer-tools](https://github.com/singer-io/singer-tools)
    - [target-stitch](https://github.com/singer-io/target-stitch)

3. Create your tap's `config.json` file.  The tap config file for this tap should include these entries:
   - `start_date` - the default value to use if no bookmark exists for an endpoint (rfc3339 date string)
   - `user_agent` (string, optional): Process and email for API logging purposes. Example: `tap-workday-adaptive-planning <api_user_email@your_company.com>`
   - `request_timeout` (integer, `300`): Max time for which request should wait to get a response. Default request_timeout is 300 seconds.

    ```json
    {
        "start_date": "2019-01-01T00:00:00Z",
        "user_agent": "tap-workday-adaptive-planning <api_user_email@your_company.com>",
        "request_timeout": 300
    }
    ```

    Optionally, also create a `state.json` file. `currently_syncing` is an optional attribute used for identifying the last object to be synced in case the job is interrupted mid-stream. The next run would begin where the last job left off.

    ```json
    {
        "currently_syncing": "engage",
        "bookmarks": {
            "export": "2019-09-27T22:34:39.000000Z",
            "funnels": "2019-09-28T15:30:26.000000Z",
            "revenue": "2019-09-28T18:23:53Z"
        }
    }
    ```

4. Run the Tap in Discovery Mode
    This creates a catalog.json for selecting objects/fields to integrate:
    ```bash
    tap-workday-adaptive-planning --config config.json --discover > catalog.json
    ```
   See the Singer docs on discovery mode
   [here](https://github.com/singer-io/getting-started/blob/master/docs/DISCOVERY_MODE.md#discovery-mode).

5. Run the Tap in Sync Mode (with catalog) and [write out to state file](https://github.com/singer-io/getting-started/blob/master/docs/RUNNING_AND_DEVELOPING.md#running-a-singer-tap-with-a-singer-target)

    For Sync mode:
    ```bash
    > tap-workday-adaptive-planning --config tap_config.json --catalog catalog.json > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
    To load to json files to verify outputs:
    ```bash
    > tap-workday-adaptive-planning --config tap_config.json --catalog catalog.json | target-json > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```
    To pseudo-load to [Stitch Import API](https://github.com/singer-io/target-stitch) with dry run:
    ```bash
    > tap-workday-adaptive-planning --config tap_config.json --catalog catalog.json | target-stitch --config target_config.json --dry-run > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```

6. Test the Tap
    While developing the workday adaptive planning tap, the following utilities were run in accordance with Singer.io best practices:
    Pylint to improve [code quality](https://github.com/singer-io/getting-started/blob/master/docs/BEST_PRACTICES.md#code-quality):
    ```bash
    > pylint tap_workday_adaptive_planning -d missing-docstring -d logging-format-interpolation -d too-many-locals -d too-many-arguments
    ```
    Pylint test resulted in the following score:
    ```bash
    Your code has been rated at 9.67/10
    ```

    To [check the tap](https://github.com/singer-io/singer-tools#singer-check-tap) and verify working:
    ```bash
    > tap_workday_adaptive_planning --config tap_config.json --catalog catalog.json | singer-check-tap > state.json
    > tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
    ```

    #### Unit Tests

    Unit tests may be run with the following.

    ```
    python -m pytest --verbose
    ```

    Note, you may need to install test dependencies.

    ```
    pip install -e .'[dev]'
    ```
---

Copyright &copy; 2019 Stitch
