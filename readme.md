

## NoSQL Workbech
    - Este servicio lo instale para tener una interfaz grafica de como se veria mi tabla de dynamo local
    https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html

## Correr proyecto local

- Instalar sam cli
    - https://docs.aws.amazon.com/es_es/serverless-application-model/latest/developerguide/install-sam-cli.html

- Comandos a correr Makefile creacion de dynamo y tablas local
    - make up
    - Crear entorno virtual
        - virtualenv venv
    - Activar entorno virtual
        - source ./venv/bin/activate
    - Instalar librerias en ese entorno
        - pip install -r local.txt
    - make create-tables-dynamo

- Correr proyecto con sam
    - make sam-build
    - make sam-local

## Consideraciones

- El .env es el que toma las variables de entorno en para python como tal (el cual se encuentra aca shared/constants.py ) y en parameters.json son parametros de los template de cloudformation

## Deploy local


- list profiles local
    - cat ~/.aws/credentials

  The first time it is deployed it should be run with **sam deploy --guided --profile MY_PROFILE**
  ```bash
  $ sam build --use-container && sam deploy --config-env develop|staging|production && rm -rf .aws-sam
  $ sam deploy --profile YOUR_PROFILE --config-env develop


# Deploy

sam deploy --guided --profile pheno
sam build --use-container
sam deploy --profile pheno --config-env develop

## Evidencias stack desplegado

- Aws Images deploy
    - Api gateway rest deploy evidence 
        - ![](images/aws_images/deploy_images/api_gateway_rest_deploy.png)
    - Dynamo table deploy evidence 
        - ![](images/aws_images/deploy_images/dynamo_table_deploy.png)
    - Cloudformation deploy evidence 
        - ![](images/aws_images/deploy_images/cloudformation_deploy.png)
    - Lambdas deploy evidence 
        - ![](images/aws_images/deploy_images/lambdas_deploy.png)
    - Layer deploy evidence 
        - ![](images/aws_images/deploy_images/layer_deploy.png)

- Test Api gateway y lambdas
    - Create company
        - ![](images/aws_images/test_api_gateway/create_company.png)
    - Create User
        - ![](images/aws_images/test_api_gateway/test_create_user.png)
    - Login User
        - ![](images/aws_images/test_api_gateway/login_user_data.png)
    - Create company
        - ![](images/aws_images/test_api_gateway/create_company.png)

- Table data dynamo records
    - Table data
        - ![](images/aws_images/test_api_gateway/table_data.png)

## Local

- local sam
    - ![](images/local/loca_sam.png)

- local docker compose
    - ![](images/local/local_docker_compose_dynamo.png)

- Tables dynamo local UI
    - ![](images/local/tables_dynamo_ui_local.png)