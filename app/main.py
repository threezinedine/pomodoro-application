import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QApplication, QMainWindow
from uis.main_window import Ui_MainWindow
import qdarktheme  # type: ignore


class PomodoroMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # type: ignore

    def keyPressEvent(self, a0: QKeyEvent) -> None:
        if a0.key() == Qt.Key.Key_Escape:
            self.close()

        return super().keyPressEvent(a0)


def main():
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)

    app = QApplication(sys.argv)
    qdarktheme.setup_theme()

    window = PomodoroMainWindow()
    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
