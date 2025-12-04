from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class TenantVersions(FullTableStream):
    tap_stream_id = "tenant_versions"
    key_properties = ["name"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "/v1/versions"

