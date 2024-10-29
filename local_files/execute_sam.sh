param_overrides=$(python local_files/generate_params.py parameters.json)

echo "Starting SAM Local API Gateway"
echo $param_overrides
sam local start-api --parameter-overrides $param_overrides --docker-network dynamodb-local-network
