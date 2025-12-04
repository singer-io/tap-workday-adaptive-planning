from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class MetadataTime(FullTableStream):
    tap_stream_id = "metadata_time"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "time"
    path = "/v40/exportTime"

