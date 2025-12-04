from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class Calendar(FullTableStream):
    tap_stream_id = "calendar"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "calendars"
    path = "/v40/exportCalendar"

