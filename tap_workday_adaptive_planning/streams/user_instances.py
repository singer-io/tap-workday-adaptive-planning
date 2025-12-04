from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class UserInstances(FullTableStream):
    tap_stream_id = "user_instances"
    key_properties = ["userGuid"]
    replication_method = "FULL_TABLE"
    data_key = "users"
    path = "/v1/users/instances"

