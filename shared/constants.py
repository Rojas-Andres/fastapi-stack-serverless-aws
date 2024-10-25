import os


class Constants:
    DYNAMO_TABLA_NAME = os.environ.get("DYNAMO_DB_TABLE_NAME")
    ENVIRONMENT = os.environ.get("ENVIRONMENT")


constants = Constants()
