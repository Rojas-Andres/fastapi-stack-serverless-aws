import os


class Constants:
    DYNAMO_DB_TABLE = os.environ.get("DYNAMO_DB_TABLE")
    ENVIRONMENT_SAM = os.environ.get("ENVIRONMENT_SAM", "local-sam")
    AWS_REGION = os.environ.get("AWS_REGION")
    if ENVIRONMENT_SAM == "local-sam":
        END_POINT_URL_LOCAL = "http://dynamodb-local:8000"
    else:
        END_POINT_URL_LOCAL = "http://127.0.0.1:8000"
    ENV_AWS_ACCESS_KEY = os.environ.get("ENV_AWS_ACCESS_KEY", "FAKE_ACCESS_KEY")
    ENV_AWS_SECRET_KEY = os.environ.get("ENV_AWS_SECRET_KEY", "FAKE_SECRET")


constants = Constants()
