import os
import signal
import sys
import time
import cffi

ffi = cffi.FFI()
ffi.cdef("""
int WINAPI SetConsoleCtrlHandler(
   void*            HandlerRoutine,
   int              Add
);
""")
kernel32 = ffi.dlopen("kernel32.dll")

# Stop ignoring CTRL_C_EVENT
kernel32.SetConsoleCtrlHandler(ffi.NULL, 0)

try:
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    time.sleep(10)
except KeyboardInterrupt:
    print("ok")
    sys.exit(0)
else:
    print("FAIL")
    sys.exit(1)
