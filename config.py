from os import environ, path
from dotenv import load_dotenv


basedir = path.abspath(path.dirname(__file__))
env_path = path.join(path.dirname(__file__))
load_dotenv(path.join(env_path, ".env"))

# Get the environment variables
DRIVER_PATH = environ.get('DRIVER_PATH')
