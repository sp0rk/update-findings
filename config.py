import yaml

def read_config():
	with open('config.yml', mode='r') as config_file:
		return yaml.safe_load(config_file)