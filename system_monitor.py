import psutil
import tkinter as tk
from tkinter import Label


def update_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")
    memory_label.config(text=f"Memory Usage: {memory_usage:.2f}%")
    root.after(1000, update_usage)


def update_disk_usage():
    partitions = psutil.disk_partitions()
    disk_text = "Disk Usage:\n"
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_text += f"{partition.device}: {usage.percent:.2f}% used\n"
    disk_label.config(text=disk_text)
    root.after(1000, update_disk_usage)


def update_network_usage():
    network = psutil.net_io_counters()
    network_text = f"Network Usage:\nUpload: {network.bytes_sent} bytes\nDownload: {network.bytes_recv} bytes"
    network_label.config(text=network_text)
    root.after(1000, update_network_usage)


root = tk.Tk()
root.title("System Resource Monitor")
disk_label = Label(root, text="Disk Usage: -")
disk_label.pack()

network_label = Label(root, text="Network Usage: -")
network_label.pack()
cpu_label = Label(root, text="CPU Usage: -")
cpu_label.pack()

memory_label = Label(root, text="Memory Usage: -")
memory_label.pack()

update_usage()
update_disk_usage()
update_network_usage()

root.mainloop()
