import psutil
import tkinter as tk 
from tkinter import Label

def update_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")
    memory_label.config(text=f"Memory Usage: {memory_usage:.2f}%")
    root.after(1000, update_usage)
root = tk.Tk()
root.title("System Resource Monitor")

cpu_label = Label(root, text="CPU Usage: -")
cpu_label.pack()

memory_label = Label(root, text="Memory Usage: -")
memory_label.pack()

update_usage()

root.mainloop()
