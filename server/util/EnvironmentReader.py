import os

from dotenv import load_dotenv


class EnvironmentReader:

    @staticmethod
    def get(variableName: str, castTo: type = None):
        load_dotenv()
        var = os.getenv(variableName)
        if castTo:
            var = castTo(var)
        return var
