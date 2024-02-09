import os

import click
import pytest

from click.testing import CliRunner
from unbabel_cli.unbabel_cli import cli
from pytest import ExitCode

# TODO: this file should go under tests/unbabel_cli/cli/


def test_unbabel_cli_valid_args():
    runner = CliRunner()
    filename = 'tests/inputs/sm_input.txt'
    result = runner.invoke(cli, ['-i', filename, '-w', 10])
    assert result.exit_code == ExitCode.OK


def test_unbabel_cli_invalid_args_not_raise():
    pass


def test_unbabel_cli_logger_sma_invalid_args():
    pass


def test_unbabel_cli_check_verbose():
    pass


def test_unbabel_cli_shared_data_is_valid_set():
    pass


def test_unbabel_cli_shared_data_invalid():
    pass



# TODO: this could go inside tests/translations_metrics/sma
def test_unbabel_cli_empty_input_file():
    pass