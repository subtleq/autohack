# autohack display functions and thread
import curses
import time

from autohack_common import *

# called by curses.wrapper to prevent terminal issues
def display(stdscr):
  # main loop here
  while True:
    # update display TODO

    # sleep until next update time
    time.sleep(display_sleep)
  

# update the command line display
def display_thread():
  log('Starting Display Thread')
  curses.wrapper(display)
