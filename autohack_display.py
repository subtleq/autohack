# autohack display functions and thread
from autohack_common import *

# update the command line display
def display_thread():
  # initialize curses, cleanup if something goes wrong
  try:
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(1)
  except:
    cleanup()

  # main loop here
  while True:
    # update display TODO

    # sleep until next update time
    time.sleep(display_sleep)

