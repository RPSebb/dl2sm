import os
import shutil
from datetime import datetime
from PyQt6.QtCore import QThread, pyqtSignal, QTimer

class FileWatcher(QThread):

    message_signal = pyqtSignal(str)

    def __init__(self, directory_to_watch):
        super().__init__()
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.directory_to_watch = directory_to_watch
        self.files_state = {}

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_changes)
        QTimer.singleShot(0, self.check_changes)
        self.timer.start(30000)

    def copy_and_rename(self, src, dst, name):
        filename = os.path.basename(src)
        shutil.copy2(src, dst)
        shutil.move(f"{dst}/{filename}", f"{dst}/{name}")
        res = name.split('_', 3)
        date = f"{res[0][:2]}/{res[0][2:4]}/{res[0][4:]}"
        time = f"{res[1][:2]}:{res[1][2:4]}"
        self.message_signal.emit(f"{date} {time} {res[3]} has been saved.")

    def get_file_state(self):
        state = {}
        for filename in os.listdir(self.directory_to_watch):
            file_path = os.path.join(self.directory_to_watch, filename)
            if os.path.isfile(file_path) and filename.endswith(".sav"):
                state[filename] = os.path.getmtime(file_path)
        return state

    def check_changes(self):
        current_state = self.get_file_state()
        for filename, last_modified in current_state.items():
            src = os.path.join(self.directory_to_watch, filename)
            dst = os.path.join(self.current_dir, os.path.splitext(filename)[0])
            date = datetime.fromtimestamp(last_modified).strftime("%d%m%Y_%H%M%S")

            if filename not in self.files_state:
                if not os.path.exists(dst):
                    os.makedirs(dst)
                    self.message_signal.emit(f"create folder {dst}")
                self.message_signal.emit(f"watching {filename}")
                self.copy_and_rename(src, dst, f"{date}_{filename}")
            elif self.files_state[filename] != last_modified:
                self.copy_and_rename(src, dst, f"{date}_{filename}")
   
        self.files_state = current_state

    def run(self):
        self.exec()