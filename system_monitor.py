import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

def update_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    #{memory_usage:.2f}%")

def update_network_usage():
    network = psutil.net_io_counters()
    network_text = f"Network Usage:\nUpload: {network.bytes_sent} bytes\nDownload: {network.bytes_recv} bytes"
    network_label.setText(network_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor_app = SystemMonitorApp()
    monitor_app.show()
    sys.exit(app.exec_())
