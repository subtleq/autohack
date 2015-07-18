#!/usr/bin/python
# program to auto hack nearby networks
import threading
import signal
import curses
import time
import os

# list of networks to hack
networks = []

# sleep timers for the threads between updates
display_sleep = 1
discovery_sleep = 120
autohack_sleep = 10

# curses object, used for cleanup
stdscr = curses.initscr()

# update the command line display TODO
def display_thread():
  # put into try/except to cleanup curses without issues
  try:
    # initial setup
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
    while True:
      # update display

      # sleep until next update time
      time.sleep(display_sleep)
  except:
    cleanup()

# add information about found networks to the shared network list TODO
def update_networks(found_networks, interface):
  global networks
  return 0

# update the list of nearby networks
def discovery_thread():
  while True:
    # get the interfaces on this machine
    interfaces = [x.split(' ')[0] for x in os.popen('ifconfig -s', 'r').read().split('\n')[2:]][:-1]

    # get a list of current networks
    for interface in interfaces:
      # get a list of networks seen by the interface
      interface_networks = os.popen('iwlist ' + interface + ' scanning', 'r').read()
      # update those networks in the global state
      update_networks(interface_networks, interface)
    
    # sleep until next update time
    time.sleep(discovery_sleep)

# attempt to hack most promising network TODO
def autohack_thread():
  global networks
  while True:
    # sleep until next update time
    time.sleep(autohack_sleep)

# ----- helper functions ----- #

# cleanup function, run before exiting
def cleanup():
  curses.nocbreak()
  stdscr.keypad(0)
  curses.echo()
  sys.exit(0)

# ----- main function ----- #

# attach signal catchers to perform cleanup
signal.signal(signal.SIGINT, cleanup)

# start display thread
threading.Thread(target=display_thread)

# start network discovery thread
threading.Thread(target=discovery_thread)

# start autohack thread
threading.Thread(target=autohack_thread)

# stay alive
while True:
  sleep(1)

