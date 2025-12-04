from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Locales(FullTableStream):
    tap_stream_id = "locales"
    key_properties = ["code"]
    replication_method = "FULL_TABLE"
    data_key = "locales"
    path = "/v40/exportLocales"

