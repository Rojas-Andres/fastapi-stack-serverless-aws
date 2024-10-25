param_overrides=$(python local_files/generate_params.py parameters.json)

sam local start-api --parameter-overrides $param_overrides --docker-network dynamodb-local-network
