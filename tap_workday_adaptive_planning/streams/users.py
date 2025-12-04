from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Users(FullTableStream):
    tap_stream_id = "users"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "users"
    path = "/v40/exportUsers"

