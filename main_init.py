import sys

from pretty_handy_init.cli_app.cli_app import CliApp

if __name__ == '__main__':
    command_line_app = CliApp(cli_args=sys.argv[1:])
    command_line_app()
