# This is a simple python based health check utility that I will be building the program around
import platform
import socket
import psutil
import getpass
from datetime import datetime

print("=== PC HEALTH REPORT ===")

print("Computer Name:", socket.gethostname())
print("User:", getpass.getuser())
print("OS:", platform.system(), platform.release())

print("IP Address:", socket.gethostbyname(socket.gethostname()))

print("CPU Usage:", psutil.cpu_percent(interval=1), "%")

ram = psutil.virtual_memory()
print("RAM Usage:", ram.percent, "%")

disk = psutil.disk_usage('/')
print("Free Disk Space:", round(disk.free / (1024**3), 2), "GB")

print("Report Time:", datetime.now())
