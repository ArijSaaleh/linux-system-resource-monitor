import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class SystemMonitorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("System Resource Monitor")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.disk_label = QLabel("Disk Usage: -")
        layout.addWidget(self.disk_label)

        self.network_label = QLabel("Network Usage: -")
        layout.addWidget(self.network_label)

        self.cpu_label = QLabel("CPU Usage: -")
        layout.addWidget(self.cpu_label)

        self.memory_label = QLabel("Memory Usage: -")
        layout.addWidget(self.memory_label)

        self.update_usage()
        self.update_disk_usage()
        self.update_network_usage()

    def update_usage(self):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        self.cpu_label.setText(f"CPU Usage: {cpu_usage:.2f}%")
        self.memory_label.setText(f"Memory Usage: {memory_usage:.2f}%")
        self.timer = self.startTimer(1000)

    def update_disk_usage(self):
        partitions = psutil.disk_partitions()
        disk_text = "Disk Usage:\n"
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_text += f"{partition.device}: {usage.percent:.2f}% used\n"
        self.disk_label.setText(disk_text)

    def update_network_usage(self):
        network = psutil.net_io_counters()
        network_text = f"Network Usage:\nUpload: {network.bytes_sent} bytes\nDownload: {network.bytes_recv} bytes"
        self.network_label.setText(network_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor_app = SystemMonitorApp()
    monitor_app.show()
    sys.exit(app.exec_())
