import datetime


def datetime_diff(datetime_a: datetime, datetime_b: datetime, into: int = 1) -> int:
    """Difference between two datetime objects.

    :param datetime_a: datetime object to compare to b
    :param datetime_b: datetime object to compare to a
    :param into: difference by minutes(default = 1), seconds(default = 2), hours(default =3)

    :return: int
    """
    if datetime_a > datetime_b:
        return int(abs((datetime_a - datetime_b).total_seconds() / 60 * into))
    else:
        return int(abs((datetime_a - datetime_b).total_seconds() / 60 * into))
