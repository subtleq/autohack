# autohack hacking functions and thread
import time

from autohack_common import *

# attempt to hack most promising network TODO
def autohack_thread():
  log('Starting Hack Thread')
  global networks
  while True:
    # sleep until next update time
    time.sleep(autohack_sleep)

