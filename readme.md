

## NoSQL Workbech
    - Este servicio lo instale para tener una interfaz grafica de como se veria mi tabla de dynamo local
    https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html

## Correr proyecto local

- Instalar sam cli
    - https://docs.aws.amazon.com/es_es/serverless-application-model/latest/developerguide/install-sam-cli.html

- Comandos a correr Makefile creacion de dynamo y tablas local
    - make up
    - make create-tables-dynamo

- Correr proyecto con sam
    - make sam-build
    - make sam-local
