from tap_workday_adaptive_planning.streams.accounts import Accounts
from tap_workday_adaptive_planning.streams.currencies import Currencies
from tap_workday_adaptive_planning.streams.attributes import Attributes
from tap_workday_adaptive_planning.streams.calendar import Calendar
from tap_workday_adaptive_planning.streams.configurable_model_data import ConfigurableModelData
from tap_workday_adaptive_planning.streams.data import Data
from tap_workday_adaptive_planning.streams.dimension_families import DimensionFamilies
from tap_workday_adaptive_planning.streams.dimensions import Dimensions
from tap_workday_adaptive_planning.streams.dimension_mapping import DimensionMapping
from tap_workday_adaptive_planning.streams.groups import Groups
from tap_workday_adaptive_planning.streams.instances import Instances
from tap_workday_adaptive_planning.streams.levels import Levels
from tap_workday_adaptive_planning.streams.locales import Locales
from tap_workday_adaptive_planning.streams.modeled_sheet_data import ModeledSheetData
from tap_workday_adaptive_planning.streams.roles import Roles
from tap_workday_adaptive_planning.streams.permission_sets import PermissionSets
from tap_workday_adaptive_planning.streams.security_audit import SecurityAudit
from tap_workday_adaptive_planning.streams.sheet_definition import SheetDefinition
from tap_workday_adaptive_planning.streams.sheets import Sheets
from tap_workday_adaptive_planning.streams.metadata_time import MetadataTime
from tap_workday_adaptive_planning.streams.transaction_definition import TransactionDefinition
from tap_workday_adaptive_planning.streams.users import Users
from tap_workday_adaptive_planning.streams.versions import Versions
from tap_workday_adaptive_planning.streams.exchange_rate_types import ExchangeRateTypes
from tap_workday_adaptive_planning.streams.sheet_availability import SheetAvailability
from tap_workday_adaptive_planning.streams.tenant_versions import TenantVersions
from tap_workday_adaptive_planning.streams.user_instances import UserInstances
from tap_workday_adaptive_planning.streams.user_permission_sets import UserPermissionSets
from tap_workday_adaptive_planning.streams.tasks import Tasks
from tap_workday_adaptive_planning.streams.task_run_details import TaskRunDetails

STREAMS = {
    "accounts": Accounts,
    "currencies": Currencies,
    "attributes": Attributes,
    "calendar": Calendar,
    "configurable_model_data": ConfigurableModelData,
    "data": Data,
    "dimension_families": DimensionFamilies,
    "dimensions": Dimensions,
    "dimension_mapping": DimensionMapping,
    "groups": Groups,
    "instances": Instances,
    "levels": Levels,
    "locales": Locales,
    "modeled_sheet_data": ModeledSheetData,
    "roles": Roles,
    "permission_sets": PermissionSets,
    "security_audit": SecurityAudit,
    "sheet_definition": SheetDefinition,
    "sheets": Sheets,
    "metadata_time": MetadataTime,
    "transaction_definition": TransactionDefinition,
    "users": Users,
    "versions": Versions,
    "exchange_rate_types": ExchangeRateTypes,
    "sheet_availability": SheetAvailability,
    "tenant_versions": TenantVersions,
    "user_instances": UserInstances,
    "user_permission_sets": UserPermissionSets,
    "tasks": Tasks,
    "task_run_details": TaskRunDetails,
}

