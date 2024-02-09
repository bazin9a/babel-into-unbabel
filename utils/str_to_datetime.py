from datetime import datetime, timedelta


def str_to_datetime(input_str: str, date_format: str = '%Y-%m-%d %H:%M:%S.%f',
                    no_seconds: bool = False) -> datetime:
    """Difference between two datetime objects.

        :param input_str: datetime object to compare to be incremented
        :param date_format: define datetime format
        :param no_seconds: remove seconds from datetime object
        :return: datetime
        """
    date_format = date_format
    input_datetime = datetime.strptime(input_str, date_format)
    if no_seconds:
        # round to nearst minute
        input_datetime += timedelta(seconds=30)
        return input_datetime.replace(second=0, microsecond=0)
    return input_datetime
