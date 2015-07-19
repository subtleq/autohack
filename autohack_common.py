# autohack common variales/functions
import curses
import sys

# list of networks to hack
networks = []

# sleep timers for the threads between updates
display_sleep = 1
discovery_sleep = 120
autohack_sleep = 10

# curses object, used for cleanup
stdscr = curses.initscr()

# ----- helper functions ----- #

# cleanup function, run before exiting
def cleanup(signal = 0, frame = None):
  print 'Autohack Died, Exiting Cleanly'
  curses.nocbreak()
  stdscr.keypad(0)
  curses.echo()
  sys.exit(0)

