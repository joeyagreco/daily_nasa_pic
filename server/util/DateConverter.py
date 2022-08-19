import datetime

from server.util.CustomLogger import CustomLogger


class DateConverter:
    __LOGGER = CustomLogger.getLogger()

    @classmethod
    def getTimeStringFromMilitaryHour(cls, militaryHour: int) -> str:
        timeStr = datetime.datetime.strptime(str(militaryHour), "%H").strftime('%I:%M %p')
        # get timezone
        timezoneStr = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        return f"{timeStr} {timezoneStr}"
