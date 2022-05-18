from server.service.BotRunner import BotRunner
from server.util.CustomLogger import CustomLogger
from server.util.DateConverter import DateConverter
from server.util.EnvironmentReader import EnvironmentReader

if __name__ == "__main__":
    LOGGER = CustomLogger.getLogger()
    HOUR_TO_RUN_BOT_AT = int(EnvironmentReader.get("HOUR_TO_RUN_BOT_AT"))
    LOGGER.info("STARTING BOT...")
    LOGGER.info(f"WILL TWEET OUT DAILY AT {DateConverter.getTimeStringFromMilitaryHour(HOUR_TO_RUN_BOT_AT)}.")
    botRunner = BotRunner()
    botRunner.run(HOUR_TO_RUN_BOT_AT)
