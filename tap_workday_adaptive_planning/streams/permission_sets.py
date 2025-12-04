from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class PermissionSets(FullTableStream):
    tap_stream_id = "permission_sets"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "permission_sets"
    path = "/v40/exportPermissionSets"

