from tap_workday_adaptive_planning.streams.abstracts import IncrementalStream

class ExchangeRateTypes(IncrementalStream):
    tap_stream_id = "exchange_rate_types"
    key_properties = [""]
    replication_method = "INCREMENTAL"
    data_key = ""
    path = "/v1/exchangeRateTypes"

