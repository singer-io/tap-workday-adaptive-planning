from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class UserPermissionSets(FullTableStream):
    tap_stream_id = "user_permission_sets"
    key_properties = ["userGuid"]
    replication_method = "FULL_TABLE"
    data_key = "users"
    path = "/v1/users/permissionSets"

