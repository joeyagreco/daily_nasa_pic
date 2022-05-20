import os

from dotenv import load_dotenv


class EnvironmentReader:

    @staticmethod
    def get(variableName: str, castTo: type = str):
        """
        Returns the environment variable.
        Casts to the given type if given (default is string).
        """
        load_dotenv()
        var = os.getenv(variableName)
        var = castTo(var)
        return var
