from datetime import datetime

import click


def print_output(input_date: datetime, sma: float):
    """Write output to file.

    note -- in huge files, if this rstrip turn out to be an issue
    it is possible make same changes before call.
    """

    stripped_sma = str(sma).rstrip('0').rstrip('.')
    return click.echo({"date": str(input_date), "average_delivery_time": eval(stripped_sma)})

