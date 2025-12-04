from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Sheets(FullTableStream):
    tap_stream_id = "sheets"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "sheets"
    path = "/v40/exportSheets"

