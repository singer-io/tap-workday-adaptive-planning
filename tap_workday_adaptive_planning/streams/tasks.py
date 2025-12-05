from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Tasks(FullTableStream):
    tap_stream_id = "tasks"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "/v1/tasks"

