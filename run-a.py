import sys
import subprocess

try:
    subprocess.run(
        # This works:
        "python a.py",
        # This doesn't (prints "WTFFF??"):
        #"py a.py",
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
except KeyboardInterrupt:
    print("WTFFF??")
