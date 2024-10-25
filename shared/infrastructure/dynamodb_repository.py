from boto3.dynamodb.conditions import Key


class DynamoDBRepository:
    def __init__(self, table):
        self.table = table

    def get_item(self, pk: str, sk: str):
        response = self.table.get_item(Key={"PK": pk, "SK": sk})
        return response.get("Item")

    def put_item(self, item: dict):
        self.table.put_item(Item=item)

    def delete_item(self, pk: str, sk: str):
        self.table.delete_item(Key={"PK": pk, "SK": sk})

    def query_items(self, pk: str, sk_prefix: str):
        response = self.table.query(
            KeyConditionExpression=Key("PK").eq(pk) & Key("SK").begins_with(sk_prefix)
        )
        return response.get("Items", [])
