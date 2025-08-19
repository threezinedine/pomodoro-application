import argparse


class Parser:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser(description="Pomodoro Application")

        parser.add_argument(
            "-f",
            "--force",
            action="store_true",
            help="Force recreation of the virtual environment",
        )

        subparsers = parser.add_subparsers(dest="action")

        subparsers.add_parser(
            "designer",
            help="Open the UI designer",
        )

        subparsers.add_parser(
            "convert",
            help="Convert UI files",
        )

        subparsers.add_parser(
            "config",
            help="Configure the application",
        )

        package = subparsers.add_parser(
            "package",
            help="Package the application",
        )

        package.add_argument(
            "packageAction",
            choices=["install", "uninstall"],
            help="Action to perform on the package",
        )

        package.add_argument(
            "packageName",
            help="Name of the package to install or uninstall",
        )

        subparsers.add_parser(
            "run",
            help="Run the Pomodoro timer",
        )

        self.args = parser.parse_args()
