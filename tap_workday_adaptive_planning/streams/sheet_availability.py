from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class SheetAvailability(FullTableStream):
    tap_stream_id = "sheet_availability"
    key_properties = ["code"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "/v1/sheet/availability"

