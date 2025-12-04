from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class SecurityAudit(FullTableStream):
    tap_stream_id = "security_audit"
    key_properties = ["timestamp"]
    replication_method = "FULL_TABLE"
    data_key = "audit"
    path = "/v40/exportSecurityAudit"

