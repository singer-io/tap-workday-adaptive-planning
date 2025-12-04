from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class ModeledSheetData(FullTableStream):
    tap_stream_id = "modeled_sheet_data"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "ConfigurableModel"
    path = "/v40/exportModeledSheet"

