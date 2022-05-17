import datetime

from server.util.CustomLogger import CustomLogger


class DateConverter:
    __LOGGER = CustomLogger.getLogger()

    @classmethod
    def getTimeStringFromMilitaryHour(cls, militaryHour: int) -> str:
        # get time
        timeStr = None
        if militaryHour >= 0 and militaryHour <=11:
            timeStr = f"{militaryHour}:00 AM"
        elif militaryHour == 12:
            timeStr = "12:00 PM"
        elif militaryHour >= 13 and militaryHour <=24:
            timeStr = f"{militaryHour - 12}:00 PM"
        else:
            raise ValueError("militaryHour must be 0-24")
        # get timezone
        timezoneStr = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        return f"{timeStr} {timezoneStr}"