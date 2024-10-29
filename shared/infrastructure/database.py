import boto3

from shared.constants import constants


def get_dynamodb_table(table_name: str):
    if "local" in constants.ENVIRONMENT_SAM:
        dynamodb = boto3.resource(
            "dynamodb",
            region_name="us-west-2",
            endpoint_url=constants.END_POINT_URL_LOCAL,
        )
    else:
        dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
    return dynamodb.Table(table_name)


table = get_dynamodb_table(constants.DYNAMO_DB_TABLE)
