import os

from .constants import BASE_CWD, ERROR_EXIST_CODE, TEMP_DIR
from .logger import logger  # type: ignore


def CreateFolderIfNotExist(
    folderName: str,
    baseFolder: str | None = None,
    pythonModule: bool = False,
) -> None:
    """
    This method is used mainly in configuration stage for creating necessary folders.

    Args:
        folderName (str): The name of the folder to create.
        baseFolder (str | None): The base folder in which to create the new folder. This
            argument is provided, the folder name will be relative to this base folder.
    """
    finalFolderPath = folderName
    if baseFolder:
        finalFolderPath = os.path.normpath(os.path.join(baseFolder, folderName))

    if not os.path.exists(finalFolderPath):
        logger.info(f'Folder "{folderName}" does not exist. Creating...')
        os.makedirs(finalFolderPath)

        if pythonModule:
            initFilePath = os.path.join(finalFolderPath, "__init__.py")
            if not os.path.exists(initFilePath):
                with open(initFilePath, "w", encoding="utf-8") as initFile:
                    initFile.write("# This file makes the folder a Python package\n")
    else:
        logger.debug(f'Folder "{folderName}" exists.')


class Folder:
    def __init__(self, folderPath: str) -> None:
        self._folderPath = folderPath

    @property
    def FolderName(self) -> str:
        return os.path.normpath(os.path.relpath(self._folderPath, BASE_CWD))

    def AllFiles(self) -> list[str]:
        if not os.path.exists(self._folderPath):
            logger.error(f'Folder "{self.FolderName}" does not exist.')
            exit(ERROR_EXIST_CODE)

        fileNames = os.listdir(self._folderPath)
        return [os.path.normpath(os.path.join(self._folderPath, f)) for f in fileNames]


class FileUtils:
    def __init__(self, filePath: str) -> None:
        self._filePath = filePath

    @property
    def IsExisted(self) -> bool:
        return os.path.exists(self._filePath)

    @property
    def RelativeFileName(self) -> str:
        return os.path.normpath(os.path.relpath(self._filePath, BASE_CWD))

    @property
    def FileName(self) -> str:
        return os.path.basename(self._filePath)

    @property
    def TempFilePath(self) -> str:
        return os.path.normpath(
            os.path.join(TEMP_DIR, f"{self.RelativeFileName}.stamp")
        )

    @property
    def IsModified(self) -> bool:
        if not self.IsExisted:
            return True

        if not os.path.exists(self.TempFilePath):
            return True

        return os.path.getmtime(self.TempFilePath) < os.path.getmtime(self._filePath)

    def Update(self) -> None:
        relativeTempFilePath = os.path.normpath(
            os.path.relpath(self.TempFilePath, BASE_CWD)
        )

        folders = os.path.split(relativeTempFilePath)[:-1]

        for folder in folders:
            try:
                os.makedirs(folder, exist_ok=True)
            except Exception as e:
                logger.error(f"Error occurred while creating folder {folder}: {e}")
                exit(ERROR_EXIST_CODE)

        with open(self.TempFilePath, "w", encoding="utf-8") as tempFile:
            tempFile.write("")
