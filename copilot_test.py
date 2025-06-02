import subprocess
import platform

def get_uptime():
    try:
        system = platform.system()
        if system == "Windows":
            result = subprocess.run(["net", "stats", "srv"], capture_output=True, text=True, check=True)
            print("System Uptime Info:\n", result.stdout)
        elif system == "Linux" or system == "Darwin":
            result = subprocess.run(["uptime"], capture_output=True, text=True, check=True)
            print("System Uptime:", result.stdout.strip())
        else:
            print("Unsupported OS:", system)
    except subprocess.CalledProcessError as e:
        print("Error getting uptime:", e)

if __name__ == "__main__":
    get_uptime()

 
