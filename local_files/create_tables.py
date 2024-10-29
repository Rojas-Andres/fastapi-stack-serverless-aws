import boto3
import time

# Configuración de DynamoDB local
dynamodb = boto3.resource("dynamodb", endpoint_url="http://localhost:8000")


def wait_for_table_creation(table_name):
    client = boto3.client("dynamodb", endpoint_url="http://localhost:8000")
    while True:
        try:
            response = client.describe_table(TableName=table_name)
            if response["Table"]["TableStatus"] == "ACTIVE":
                print(f"Tabla {table_name} está activa.")
                break
        except client.exceptions.ResourceNotFoundException:
            pass
        print(f"Esperando a que la tabla {table_name} esté disponible...")
        time.sleep(2)


def create_tables():
    """
    Crear las tablas en DynamoDB local.
    """
    print("Creando tablas en DynamoDB local...")
    try:
        print("creando tabla de AUTH")
        table_1 = dynamodb.create_table(
            TableName="DbAuthoTabledevelopment",
            KeySchema=[
                {
                    "AttributeName": "uuid",
                    "KeyType": "HASH",  # Llave primaria
                }
            ],
            AttributeDefinitions=[{"AttributeName": "uuid", "AttributeType": "S"}],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        # table_1.meta.client.get_waiter('table_exists').wait(TableName='DbAuthoTabledevelopment')
        print("Creando la tabla DbAuthoTabledevelopment...")
        wait_for_table_creation("DbAuthoTabledevelopment")
        print("Tabla DbAuthoTabledevelopment creada con éxito.")
    except Exception as e:
        print(f"Error al crear la tabla DbAuthoTabledevelopment: {e}")

    # Crear la tabla DbTable
    try:
        table_2 = dynamodb.create_table(
            TableName="DbTabledevelopment",
            KeySchema=[
                {
                    "AttributeName": "PK",
                    "KeyType": "HASH",  # Llave primaria
                },
                {
                    "AttributeName": "SK",
                    "KeyType": "RANGE",  # Llave de rango
                },
            ],
            AttributeDefinitions=[
                {"AttributeName": "PK", "AttributeType": "S"},
                {"AttributeName": "SK", "AttributeType": "S"},
            ],
            GlobalSecondaryIndexes=[
                {
                    "IndexName": "GSI1",
                    "KeySchema": [
                        {"AttributeName": "SK", "KeyType": "HASH"},
                        {"AttributeName": "PK", "KeyType": "RANGE"},
                    ],
                    "Projection": {"ProjectionType": "ALL"},
                    "ProvisionedThroughput": {
                        "ReadCapacityUnits": 5,
                        "WriteCapacityUnits": 5,
                    },
                }
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        print("Creando la tabla DbTabledevelopment...")
        table_2.meta.client.get_waiter("table_exists").wait(
            TableName="DbTabledevelopment"
        )
        print("Tabla DbTabledevelopment creada con éxito.")
    except Exception as e:
        print(f"Error al crear la tabla DbTabledevelopment: {e}")

    try:
        table_3 = dynamodb.create_table(
            TableName="DbTableLogsdevelopment",
            KeySchema=[
                {
                    "AttributeName": "api",
                    "KeyType": "HASH",  # Llave primaria
                },
                {
                    "AttributeName": "timestamp",
                    "KeyType": "RANGE",  # Llave de rango
                },
            ],
            AttributeDefinitions=[
                {"AttributeName": "api", "AttributeType": "S"},
                {"AttributeName": "timestamp", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        print("Creando la tabla DbTabledevelopment...")
        table_3.meta.client.get_waiter("table_exists").wait(
            TableName="DbTableLogsdevelopment"
        )
        print("Tabla DbTableLogsdevelopment creada con éxito.")
    except Exception as e:
        print(f"Error al crear la tabla DbTableLogsdevelopment: {e}")


if __name__ == "__main__":
    create_tables()
