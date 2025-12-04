from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Roles(FullTableStream):
    tap_stream_id = "roles"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "roles"
    path = "/v40/exportRoles"

