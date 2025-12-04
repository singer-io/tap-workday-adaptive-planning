from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Data(FullTableStream):
    tap_stream_id = "data"
    key_properties = ["account_code"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "/v40/exportData"

