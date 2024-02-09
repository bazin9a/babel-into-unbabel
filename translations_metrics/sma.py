import linecache
import os
from collections import deque
from datetime import datetime
from functools import reduce

import click

from translations_metrics.const import ZERO_SMA, BASE_CASE_LIMIT, SEARCH_STEP, ONE_LINE_CASE, EMPTY_FILE
from translations_metrics.helper import print_output
from utils import file_snapshot
from utils.datetime_diff import datetime_diff
from utils.datetime_plus_minutes import datetime_plus_minutes
from utils.datetime_trim import datetime_trim
from utils.str_to_datetime import str_to_datetime

# TODO: refactoring repo to use the following
"""
-- add Collection class of SMATranslations 
    (needs more time to avoid compromise performance)
    source: 
    https://medium.com/techtofreedom/7-python-memory-optimization-tricks-to-enhance-your-codes-efficiency-5ef65bf415e7
-- add Printer for SMATranslations
-- more: 
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

    input_file = ctx.obj['cli_shared_data'].get('input_file')
    window_size = ctx.obj['cli_shared_data'].get('window_size')

    base_case = _get_base_case(input_file)

    if base_case == EMPTY_FILE:
        return

    # plus base counter
    if base_case == ONE_LINE_CASE + 1:
        event = linecache.getline(input_file, 1)
        event_dict = dict(eval(event))
        print_output(event_dict["timestamp"], event_dict["duration"])
        return

    last_event_timestamp = datetime_trim(_get_last_timestamp(input_file))

    with open(input_file, 'r') as file:

        # deque of (date, events/translations duration) tuples
        translations_durations = deque()

        # first event timestamp
        try:
            line = file.readline()
            first_event = dict(eval(line))
        except Exception:
            return
        prev_process_timestamp = datetime_trim(str_to_datetime(first_event["timestamp"]))
        print_output(prev_process_timestamp, float(ZERO_SMA))

        translations_durations.append((prev_process_timestamp, first_event["duration"]))

        timestamp_window_end = datetime_plus_minutes(prev_process_timestamp, window_size)

        search_limit = datetime_diff(prev_process_timestamp, last_event_timestamp)

        # increment the minute processed
        search_limit = search_limit + SEARCH_STEP

        for i in range(1, search_limit):
            try:
                newline = file.readline()
                event = dict(eval(newline))
            except Exception:
                return

            curr_process_timestamp = datetime_trim(str_to_datetime(event["timestamp"]))

            # range between previous and current process timestamp
            time_between_events = datetime_diff(prev_process_timestamp, curr_process_timestamp) + SEARCH_STEP

            # popleft when  diff of first date in queue and curr date > window

            for _ in range(time_between_events):
                # -- new event
                if prev_process_timestamp == curr_process_timestamp:
                    # add to durations deque
                    translations_durations.append((curr_process_timestamp, event["duration"]))

                # -- window limit
                if datetime_diff(timestamp_window_end, prev_process_timestamp) == 0:
                    translations_durations.popleft()
                    # reset next window check
                    timestamp_window_end = datetime_plus_minutes(curr_process_timestamp, window_size)

                # sma
                durations = list(map(lambda x: x[1], translations_durations))

                if durations:
                    sum_durations = reduce(lambda x, y: x + y, durations)
                    translation_sma = sum_durations / len(durations)

                # 1 minute step in the file
                prev_process_timestamp = datetime_trim(datetime_plus_minutes(prev_process_timestamp, SEARCH_STEP))

                print_output(prev_process_timestamp, translation_sma)

            # set previous timestamp before next iteration
            prev_process_timestamp = datetime_trim(str_to_datetime(event["timestamp"]), no_seconds=True)

    return None


def _get_last_timestamp(input_file: str) -> datetime:
    """Get last timestamp from file.

    :param input_file:
    :return date

    Note: the file pointer was used to jump to the end
        avoiding pass all lines.
    """
    with open(input_file, 'rb') as file:
        # read last line without loop the entire file
        file.seek(-2, os.SEEK_END)
        while file.read(1) != b'\n':
            file.seek(-2, os.SEEK_CUR)

        last_event = file.readline().decode()
        last_event_to_dict = dict(eval(last_event.strip()))

    return str_to_datetime(last_event_to_dict["timestamp"])


def _get_base_case(file_path: str) -> int:
    """Check if is base case scenarios.

    Read lines to check empty file and one line file
    :return int: line counter
    """

    with open(file_path, 'r') as file:
        count_lines = 0
        for _ in range(BASE_CASE_LIMIT):
            try:
                if bool(file.readline()):
                    count_lines += 1
                else:
                    return count_lines
            except Exception as e:
                print("test", count_lines)
                return e
    return count_lines,
