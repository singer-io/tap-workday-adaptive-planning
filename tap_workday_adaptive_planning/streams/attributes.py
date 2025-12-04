from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Attributes(FullTableStream):
    tap_stream_id = "attributes"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "attributes"
    path = "/v40/exportAttributes"

