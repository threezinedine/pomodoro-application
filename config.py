"""
This file contains all the helper functions for configuring and managing the Pomodoro Application.
"""

from config_utils.constants import CONVERTED_UI_DIR
from config_utils.parser import Parser
from config_utils.config import Config
from config_utils.app import App
from config_utils.designer import ConvertUIToPy, OpenDesigner
from config_utils.package import Package
from config_utils.utils import CreateFolderIfNotExist


def main():
    parser = Parser()

    if parser.args.action == "config":
        Config().CreateVirtualEnvironment(force=parser.args.force)
        CreateFolderIfNotExist(
            CONVERTED_UI_DIR,
            pythonModule=True,
        )
    elif parser.args.action == "convert":
        ConvertUIToPy(force=parser.args.force)
    elif parser.args.action == "designer":
        OpenDesigner()
    elif parser.args.action == "package":
        package = Package()
        if parser.args.packageAction == "install":
            package.Install(parser.args.packageName)
        elif parser.args.packageAction == "uninstall":
            package.Uninstall(parser.args.packageName)
    elif parser.args.action == "run":
        ConvertUIToPy(force=parser.args.force)
        app = App()
        app.Run()


if __name__ == "__main__":
    main()
