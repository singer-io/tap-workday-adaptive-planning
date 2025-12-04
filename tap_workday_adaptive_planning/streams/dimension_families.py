from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class DimensionFamilies(FullTableStream):
    tap_stream_id = "dimension_families"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "families"
    path = "/v40/exportDimensionFamilies"

