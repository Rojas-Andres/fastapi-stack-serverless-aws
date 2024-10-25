import json
import sys


def generate_params(json_file):
    with open(json_file, "r") as f:
        params = json.load(f)

    param_overrides = " ".join([f"{key}={value}" for key, value in params.items()])
    return param_overrides


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python generate_params.py <archivo.json>")
        sys.exit(1)

    json_file = sys.argv[1]
    param_overrides = generate_params(json_file)
    print(param_overrides)
