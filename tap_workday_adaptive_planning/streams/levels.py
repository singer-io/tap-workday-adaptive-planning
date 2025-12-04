from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Levels(FullTableStream):
    tap_stream_id = "levels"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "levels"
    path = "/v40/exportLevels"

