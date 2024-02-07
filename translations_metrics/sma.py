from collections import deque
from datetime import timedelta

import click
from utils import file_snapshot
from utils.datetime_plus_minutes import datetime_plus_minutes
from utils.str_to_datetime import str_to_datetime

# TODO: refactoring repo to use the following
"""
class <SMATranslations>():
    def __init__(self):
    
class SMATranslation():
    def __init__(self):

"""


@click.command()
@click.pass_context
def sma_translations_process(ctx: click.Context) -> None:
    """Translations Simple Moving Average (TSMA).

    This metric is hardly coupled with the concept,
    of translation. We could have done a more agnostic version (SMA),
    but it could compromise the performance. And we should take advantage
    of the input file being ordered.
    To avoid inconsistencies and since input file is a stream of events,
    this method will process over a snapshot.

    This module output the result to a TXT file.
    Note for SMA calculation there are two ways tsma changes:
        1. every new event
        2. the event in process is equal to window size limit
    source: [TDD](https://notion)

    :param ctx: click context -  (dict) which includes the CLI arguments

    input_file (String) --  path to the input file set in cli
    window_size (int) --  size of the window to slide over the input file

    :return: None -- output is written to file
    """

    # TODO: create a snapshot to avoid unexpected output
    # safe_file = file_snapshot.create()

    input_size = ctx.obj['cli_shared_data'].get('input_file')
    window_size = ctx.obj['cli_shared_data'].get('window_size')
    # translations simple moving average
    click.echo(window_size)

    # deque class of Translations
    translations_durations = deque()

    # open file for reading
    with open(input_size, 'r') as file:

        # first event timestamp
        first_event = dict(eval(file.readline()))
        prev_process_timestamp = str_to_datetime(first_event["timestamp"])

        click.echo(prev_process_timestamp)
        # set next first time check
        next_time_check = prev_process_timestamp
        next_timestamp_check = datetime_plus_minutes(prev_process_timestamp, window_size)

        for event in file:
            # new event as timestamp limit for changes check
            event = dict(eval(file.readline()))
            next_timestamp = str_to_datetime(event["timestamp"])

            while prev_process_timestamp <= next_timestamp_check:
                click.echo(next_timestamp_check)
                #
                # translations_durations.append()
                # average_durations = avg(translations_durations.values())
                # len_of_durations = len(translations_durations.values())
                # translation_sma = average_durations / len_of_durations
                if prev_process_timestamp == next_timestamp_check:
                    next_timestamp_check = datetime_plus_minutes(prev_process_timestamp, window_size)
                    break

                # 1 minute step in the file
                prev_process_timestamp = datetime_plus_minutes(prev_process_timestamp, 1)

            # set previous timestamp before next iteration
            prev_process_timestamp = event["timestamp"]
            click.echo(prev_process_timestamp)

