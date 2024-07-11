import os


class Config:
	DEBUG = False
	TESTING = False
	SECRET_KEY = 'your_secret_key_here'  # Change this to a secure random key
	COINMARKETCAP_API_KEY = os.getenv('COINMARKETCAP_API_KEY')


class DevelopmentConfig(Config):
	DEBUG = True


class ProductionConfig(Config):
	DEBUG = False
	# Add more production-specific configurations if needed


# Set the current configuration based on the environment variable
# Default to DevelopmentConfig if FLASK_ENV is not set
config_dict = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig  # Default configuration
}


def get_config():
	flask_env = os.getenv('FLASK_ENV', 'default')
	return config_dict[flask_env]
