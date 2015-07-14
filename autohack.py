#!/usr/bin/python
# program to auto hack nearby networks
import threading
import time

# list of networks to hack
networks = []
display_sleep = 1
discovery_sleep = 100
autohack_sleep = 10

# update the command line display TODO
def display_thread():
  while True:
    # update the display TODO
    time.sleep(display_sleep)

# update the list of nearby networks TODO  
def discovery_thread():
  while True:
    # look for nearby networks TODO
    time.sleep(discovery_sleep)

# attempt to hack most promising network TODO
def autohack_thread():
  while True:
    # hack the most promising network TODO
    time.sleep(autohack_sleep)

# main function

# start display thread
threading.Thread(target=display_thread)

# start network discovery thread
threading.Thread(target=discovery_thread)

# start autohack thread
threading.Thread(target=autohack_thread)

# stay alive
while True:
  sleep(1)
  
