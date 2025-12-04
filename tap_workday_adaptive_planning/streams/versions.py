from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Versions(FullTableStream):
    tap_stream_id = "versions"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "versions"
    path = "/v40/exportVersions"

