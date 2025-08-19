import os

BASE_CWD = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))


REQUIREMENTS_FILE_NAME = "requirements.txt"
REQUIREMENTS_FILE_PATH = os.path.normpath(
    os.path.join(
        BASE_CWD,
        REQUIREMENTS_FILE_NAME,
    )
)

TEMP_DIR = os.path.normpath(os.path.join(BASE_CWD, "temp"))

VENV_NAME = "venv"
VENV_DIR = os.path.normpath(os.path.join(BASE_CWD, VENV_NAME))

SCRIPTS_DIR: str = os.path.normpath(os.path.join(VENV_DIR, "Scripts"))
PYTHON_EXECUTABLE: str = os.path.normpath(os.path.join(SCRIPTS_DIR, "python.exe"))
PYQT_TOOL_EXECUTABLE: str = os.path.normpath(
    os.path.join(SCRIPTS_DIR, "pyqt6-tools.exe")
)
PYUIC_EXECUTABLE: str = os.path.normpath(os.path.join(SCRIPTS_DIR, "pyuic6.exe"))


APP_DIR_NAME = "app"
APP_DIR: str = os.path.normpath(os.path.join(BASE_CWD, APP_DIR_NAME))

ASSET_DIR_NAME = "assets"
ASSET_DIR: str = os.path.normpath(os.path.join(APP_DIR, ASSET_DIR_NAME))

UI_DIR_NAME = "uis"
UI_DIR: str = os.path.normpath(os.path.join(ASSET_DIR, UI_DIR_NAME))

CONVERTED_UI_DIR = os.path.normpath(os.path.join(APP_DIR, "uis"))

MAIN_SCRIPT_NAME = "main.py"
MAIN_SCRIPT: str = os.path.normpath(os.path.join(APP_DIR, MAIN_SCRIPT_NAME))


ERROR_EXIST_CODE = 1
