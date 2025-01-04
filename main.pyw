import sys
from window import Window  # Importer la fonction d'interface graphique
from dl2sm import FileWatcher  # Importer la classe du watcher
from PyQt6.QtWidgets import QApplication

# Démarrer l'interface graphique
app = QApplication(sys.argv)
window = Window()
window.show()

watcher_thread = FileWatcher("C:/Program Files (x86)/Steam/userdata/207084760/534380/remote/out/save")
watcher_thread.message_signal.connect(window.display_message)
watcher_thread.start()

sys.exit(app.exec())