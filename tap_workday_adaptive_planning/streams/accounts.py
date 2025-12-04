from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Accounts(FullTableStream):
    tap_stream_id = "accounts"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "accounts"
    path = "/v40/exportAccounts"

