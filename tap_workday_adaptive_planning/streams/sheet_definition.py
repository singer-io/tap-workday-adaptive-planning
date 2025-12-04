from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class SheetDefinition(FullTableStream):
    tap_stream_id = "sheet_definition"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "modeled-sheet"
    path = "/v40/exportSheetDefinition"

