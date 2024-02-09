import typing
from datetime import datetime

import click


def print_output(input_date: datetime, sma: float, output_file: typing.IO = 'output.txt') -> None:
    """Write output to file.

    note -- in huge files, if this rstrip turn out to be an issue
    it is possible make same changes before call.
    """

    stripped_sma = str(sma).rstrip('0').rstrip('.')

    try:
        with open(output_file, 'a') as file:
            file.write(f'{{"date": str({input_date}), "average_delivery_time": {eval(stripped_sma)}}}\n')
            # click.echo({"date": str(input_date), "average_delivery_time": eval(stripped_sma)})
    except IOError as e:
        click.echo(f"IO ERROR: Unable to open '{output_file}' for writing. {e}")
    return None

