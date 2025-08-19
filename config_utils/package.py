import os
import subprocess

from .logger import logger
from .constants import (
    BASE_CWD,
    ERROR_EXIST_CODE,
    PYTHON_EXECUTABLE,
    REQUIREMENTS_FILE_NAME,
    REQUIREMENTS_FILE_PATH,
)


class Package:
    def Install(self, packageName: str) -> None:
        if not os.path.exists(PYTHON_EXECUTABLE):
            logger.error(f"Python executable not found: {PYTHON_EXECUTABLE}")
            exit(ERROR_EXIST_CODE)

        try:
            subprocess.run(
                [
                    PYTHON_EXECUTABLE,
                    "-m",
                    "pip",
                    "install",
                    packageName,
                ],
                check=True,
                cwd=BASE_CWD,
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install package {packageName}: {e}")
            exit(ERROR_EXIST_CODE)

        self._UpdateRequirements()

    def _UpdateRequirements(self) -> None:
        logger.info(f'Updating "{REQUIREMENTS_FILE_NAME}"...')
        try:
            subprocess.run(
                [
                    PYTHON_EXECUTABLE,
                    "-m",
                    "pip",
                    "freeze",
                    ">",
                    REQUIREMENTS_FILE_PATH,
                ],
                check=True,
                shell=True,
                cwd=BASE_CWD,
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to update requirements file: {e}")
            exit(ERROR_EXIST_CODE)

    def Uninstall(self, packageName: str) -> None:
        if not os.path.exists(PYTHON_EXECUTABLE):
            logger.error(f"Python executable not found: {PYTHON_EXECUTABLE}")
            exit(ERROR_EXIST_CODE)

        try:
            subprocess.run(
                [
                    PYTHON_EXECUTABLE,
                    "-m",
                    "pip",
                    "uninstall",
                    "-y",
                    packageName,
                ],
                check=True,
                cwd=BASE_CWD,
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to uninstall package {packageName}: {e}")
            exit(ERROR_EXIST_CODE)

        self._UpdateRequirements()
