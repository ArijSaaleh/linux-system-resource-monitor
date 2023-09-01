import psutil
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
import pyqtgraph as p
def update_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    #{memory_usage:.2f}%")

def update_network_usage():
    network = psutil.net_io_counters()
    network_text = f"Network Usage:\nUpload: {network.bytes_sent} bytes\nDownload: {network.bytes_recv} bytes"
    ##network_label.setText(network_text)

app = QApplication([])
window = loadUi("system.ui")
window.show()
app.exec_()
