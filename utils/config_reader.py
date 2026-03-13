import yaml

def get_config():
    with open("config/config.yaml") as file:
        return yaml.safe_load(file)