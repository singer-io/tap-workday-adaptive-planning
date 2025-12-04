from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Currencies(FullTableStream):
    tap_stream_id = "currencies"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "currencies"
    path = "/v40/exportActiveCurrencies"

