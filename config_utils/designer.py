import os
import subprocess

from .constants import (
    APP_DIR,
    BASE_CWD,
    CONVERTED_UI_DIR,
    PYQT_TOOL_EXECUTABLE,
    PYUIC_EXECUTABLE,
    UI_DIR,
)
from .utils import CreateFolderIfNotExist, FileUtils, Folder
from .logger import logger


def OpenDesigner():
    subprocess.run([PYQT_TOOL_EXECUTABLE, "designer"])


def ConvertUIToPy(force: bool = False) -> None:
    files = Folder(UI_DIR).AllFiles()
    logger.debug(f"Found {len(files)} UI files.")

    CreateFolderIfNotExist(CONVERTED_UI_DIR, baseFolder=BASE_CWD)

    for filePath in files:
        file = FileUtils(filePath)

        if file.IsModified:
            logger.info(
                f'File "{file.RelativeFileName}" is modified. Converting to Python...'
            )

            try:
                subprocess.run(
                    [
                        PYUIC_EXECUTABLE,
                        filePath,
                        "-o",
                        os.path.normpath(
                            os.path.join(
                                CONVERTED_UI_DIR, file.FileName.replace(".ui", ".py")
                            )
                        ),
                    ],
                    check=True,
                    cwd=APP_DIR,
                    shell=True,
                )
            except Exception as e:
                logger.error(
                    f"Error occurred while converting {file.RelativeFileName}: {e}"
                )

            file.Update()
