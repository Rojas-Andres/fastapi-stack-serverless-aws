param_overrides=$(python local_files/generate_params.py parameters.json)

echo "Starting SAM BUILD API Gateway"
echo $param_overrides
sam build --use-container --parameter-overrides $param_overrides