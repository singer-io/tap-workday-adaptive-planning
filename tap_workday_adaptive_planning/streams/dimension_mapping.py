from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class DimensionMapping(FullTableStream):
    tap_stream_id = "dimension_mapping"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "dimensions"
    path = "/v40/exportDimensionMapping"

