from server.util.EnvironmentReader import EnvironmentReader


class TwitterAuth:
    API_KEY = EnvironmentReader.get("API_KEY")
    API_KEY_SECRET = EnvironmentReader.get("API_KEY_SECRET")
    BEARER_TOKEN = EnvironmentReader.get("BEARER_TOKEN")
    ACCESS_TOKEN = EnvironmentReader.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = EnvironmentReader.get("ACCESS_TOKEN_SECRET")
