from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class TaskRunDetails(FullTableStream):
    tap_stream_id = "task_run_details"
    key_properties = "id"
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "/v1/{taskId}/runs/{taskRunId}"

