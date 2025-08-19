import os
import shutil
import subprocess
from .constants import (
    BASE_CWD,
    ERROR_EXIST_CODE,
    PYTHON_EXECUTABLE,
    REQUIREMENTS_FILE_NAME,
    REQUIREMENTS_FILE_PATH,
    VENV_DIR,
    VENV_NAME,
)
from .logger import logger  # type: ignore


class Config:
    def CreateVirtualEnvironment(self, force: bool = False) -> None:
        if os.path.exists(VENV_DIR) and not force:
            logger.info(f"Virtual environment already exists.")
            return

        if not force:
            logger.info(f"Virtual environment does not exist. Creating...")
        else:
            logger.info(f"Recreate virtual environment...")
            shutil.rmtree(VENV_DIR)

        try:
            subprocess.run(
                ["python", "-m", "venv", VENV_NAME],
                check=True,
                cwd=BASE_CWD,
            )

        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to create virtual environment: {e}")
            exit(ERROR_EXIST_CODE)

        self.InstallDependencies()

    def _UpgradePip(self) -> None:
        logger.debug("Upgrading pip...")
        try:
            subprocess.run(
                [
                    PYTHON_EXECUTABLE,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    "pip",
                ],
                check=True,
                cwd=BASE_CWD,
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to upgrade pip: {e}")
            exit(ERROR_EXIST_CODE)

    def InstallDependencies(self) -> None:
        if not os.path.exists(REQUIREMENTS_FILE_PATH):
            logger.error(f'File "{REQUIREMENTS_FILE_NAME}" not found.')
            exit(ERROR_EXIST_CODE)

        self._UpgradePip()

        logger.info(f'Installing dependencies from "{REQUIREMENTS_FILE_NAME}"...')
        try:
            subprocess.run(
                [
                    PYTHON_EXECUTABLE,
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    REQUIREMENTS_FILE_PATH,
                ],
                check=True,
                cwd=BASE_CWD,
            )
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to install dependencies: {e}")
            exit(ERROR_EXIST_CODE)
