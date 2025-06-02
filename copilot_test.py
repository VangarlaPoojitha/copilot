import subprocess
import time

def get_uptime():
    if os.name == "posix":
        # For Linux/Unix systems
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
        uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
        print(f"System Uptime: {uptime_string}")
    elif os.name == "nt":
        # For Windows systems
        import ctypes
        import datetime
        lib = ctypes.windll.kernel32
        ticks = lib.GetTickCount64()
        uptime_seconds = int(ticks // 1000)
        uptime_string = str(datetime.timedelta(seconds=uptime_seconds))
        print(f"System Uptime: {uptime_string}")
    else:
        print("Unsupported OS")

if __name__ == "__main__":
    get_uptime()
