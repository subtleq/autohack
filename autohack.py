#!/usr/bin/python
# program to auto hack nearby networks
import threading
import signal
import atexit
import time

# load all parts into here
from autohack_common import *
from autohack_discovery import *
from autohack_display import *
from autohack_hack import *

# ----- main function ----- #

# attach signal catchers to perform cleanup
signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)
atexit.register(cleanup)

# start display thread
threading.Thread(target=display_thread).start()

# start network discovery thread
threading.Thread(target=discovery_thread).start()

# start autohack thread
threading.Thread(target=autohack_thread).start()

# stay alive
while True:
  time.sleep(1)

