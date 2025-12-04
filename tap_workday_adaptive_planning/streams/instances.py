from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Instances(FullTableStream):
    tap_stream_id = "instances"
    key_properties = ["code"]
    replication_method = "FULL_TABLE"
    data_key = "instances"
    path = "/v40/exportInstances"

