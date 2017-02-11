import sys
import subprocess

result = subprocess.run("python a.py",
                        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP)
print(result.returncode)
sys.exit(result.returncode)
