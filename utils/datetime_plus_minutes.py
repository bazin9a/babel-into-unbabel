from datetime import datetime, timedelta


def datetime_plus_minutes(input_datetime: datetime, minutes: int) -> datetime:
    """Difference between two datetime objects.

        :param input_datetime: datetime object to compare to be incremented
        :param minutes: minutes to add

        :return: datetime
        """
    return input_datetime + timedelta(minutes=minutes)
