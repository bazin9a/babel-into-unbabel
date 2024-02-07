import datetime


def datetime_diff(datetime_a: datetime, datetime_b: datetime, into: int = 1) -> datetime:
    """Difference between two datetime objects.

    :param datetime_a: datetime object to compare to b
    :param datetime_b: datetime object to compare to a
    :param into: difference by minutes(default = 1), seconds(default = 2), hours(default =3)

    :return: datetime
    """
    if datetime_a > datetime_b:
        return (datetime_a - datetime_b).total_seconds() / 60 * into
    else:
        return (datetime_a - datetime_b).total_seconds() / 60 * into
