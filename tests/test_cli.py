import unittest

from click.testing import CliRunner
from aws_assume_role.__main__ import main


def cli_runner(*args):
    runner = CliRunner()
    return runner.invoke(main, *args)


class TestCLI(unittest.TestCase):
    """
    Test running the CLI
    """

    def test_cli_without_args(self):
        result = cli_runner()

        assert result.exit_code == 2
        assert 'Missing option' in result.output

    def test_cli_version(self):
        result = cli_runner('-v')
        assert result.exit_code == 0
        assert 'aws-assume-role version' in result.output

        result = cli_runner('-V')
        assert result.exit_code == 0
        assert 'aws-assume-role version' in result.output

        result = cli_runner('--version')
        assert result.exit_code == 0
        assert 'aws-assume-role version' in result.output

    def test_cli_options(self):
        result = cli_runner('--role-name')
        assert result.exit_code == 2
        assert result.output == 'Error: --role-name option requires an argument\n'

        result = cli_runner('--account-id')
        assert result.exit_code == 2
        assert result.output == 'Error: --account-id option requires an argument\n'
