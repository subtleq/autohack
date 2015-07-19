# autohack hacking functions and thread
from autohack_common import *

# attempt to hack most promising network TODO
def autohack_thread():
  global networks
  while True:
    # sleep until next update time
    time.sleep(autohack_sleep)

