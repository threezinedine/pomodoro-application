import subprocess

from .constants import (
    APP_DIR,
    ERROR_EXIST_CODE,
    MAIN_SCRIPT,
    MAIN_SCRIPT_NAME,
    PYTHON_EXECUTABLE,
)
from .logger import logger


class App:
    def Run(self) -> None:
        logger.info(f'Running application in "{MAIN_SCRIPT_NAME}"...')
        try:
            subprocess.run(
                [
                    PYTHON_EXECUTABLE,
                    MAIN_SCRIPT,
                ],
                cwd=APP_DIR,
                check=True,
                shell=True,
            )
        except Exception as e:
            logger.error(f"Error occurred while running application: {e}")
            exit(ERROR_EXIST_CODE)
