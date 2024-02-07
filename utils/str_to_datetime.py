from datetime import datetime


def str_to_datetime(input_str: datetime, date_format: str = '%Y-%m-%d %H:%M:%S.%f') -> datetime:
    """Difference between two datetime objects.

        :param input_str: datetime object to compare to be incremented
        :param date_format: define datetime format

        :return: datetime
        """
    date_format = date_format
    input_datetime = datetime.strptime(input_str, date_format)
    return input_datetime
