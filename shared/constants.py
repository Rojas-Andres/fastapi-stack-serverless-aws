import os


class Constants:
    DYNAMO_DB_TABLE = os.environ.get("DYNAMO_DB_TABLE")
    ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")


constants = Constants()
