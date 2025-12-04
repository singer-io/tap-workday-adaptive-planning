from tap_workday_adaptive_planning.streams.abstracts import FullTableStream

class TransactionDefinition(FullTableStream):
    tap_stream_id = "transaction_definition"
    key_properties = ["id"]
    replication_method = "FULL_TABLE"
    data_key = "transaction"
    path = "/v40/exportTransactionDefinition"

