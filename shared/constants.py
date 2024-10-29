import os


class Constants:
    DYNAMO_DB_TABLE = os.environ.get("DYNAMO_DB_TABLE")
    DYNAMO_DB_TABLE_LOGS = os.environ.get("DYNAMO_DB_TABLE_LOGS", "logs")
    ENVIRONMENT_SAM = os.environ.get("ENVIRONMENT_SAM", "local-sam")
    AWS_REGION = os.environ.get("AWS_REGION")
    ENDPOINT_URL_DYNAMO = os.environ.get("ENDPOINT_URL_DYNAMO", "http://")
    ENV_AWS_ACCESS_KEY = os.environ.get("ENV_AWS_ACCESS_KEY", "FAKE_ACCESS_KEY")
    ENV_AWS_SECRET_KEY = os.environ.get("ENV_AWS_SECRET_KEY", "FAKE_SECRET")


constants = Constants()
