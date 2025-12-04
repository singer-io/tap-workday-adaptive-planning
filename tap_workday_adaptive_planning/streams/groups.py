from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Groups(FullTableStream):
    tap_stream_id = "groups"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "groups"
    path = "/v40/exportGroups"

