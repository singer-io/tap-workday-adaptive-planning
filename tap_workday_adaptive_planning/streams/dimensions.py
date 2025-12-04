from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Dimensions(FullTableStream):
    tap_stream_id = "dimensions"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "dimensions"
    path = "/v40/exportDimensions"

