import boto3

from shared.constants import constants


def get_dynamodb_table(table_name: str):
    if constants.ENVIRONMENT == "local":
        dynamodb = boto3.resource(
            "dynamodb", region_name="us-west-2", endpoint_url="http://localhost:8000"
        )
    else:
        dynamodb = boto3.resource("dynamodb", region_name="us-west-2")
    return dynamodb.Table(table_name)


table = get_dynamodb_table(constants.DYNAMO_TABLA_NAME)
