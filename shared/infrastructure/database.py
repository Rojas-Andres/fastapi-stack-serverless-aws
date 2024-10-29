import boto3

from shared.constants import constants


def get_dynamodb_table(table_name: str):
    if "local" in constants.ENVIRONMENT_SAM:
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="us-west-2",
            endpoint_url=constants.ENDPOINT_URL_DYNAMO,
        )
    else:
        dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
    return dynamodb.Table(table_name)


table = get_dynamodb_table(constants.DYNAMO_DB_TABLE)
table_logs = get_dynamodb_table(constants.DYNAMO_DB_TABLE_LOGS)
