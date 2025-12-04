from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class ConfigurableModelData(FullTableStream):
    tap_stream_id = "configurable_model_data"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "data"
    path = "/v40/exportConfigurableModelData"

