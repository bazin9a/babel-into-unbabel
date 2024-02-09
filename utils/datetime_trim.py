from datetime import datetime, timedelta
from typing import Union


def datetime_trim(input_datetime: datetime,
                  no_seconds: bool = True) -> Union[datetime, None]:
    """Difference between two datetime objects.

        :param input_datetime: datetime to trim
        :param no_seconds: remove seconds from datetime object
        :return: datetime
        """
    if no_seconds:
        new_datetime = input_datetime + timedelta(seconds=30)
        return new_datetime.replace(second=0, microsecond=0)
    return None
