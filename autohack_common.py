# autohack common variales/functions
import sys

# list of networks to hack
networks = []

# sleep timers for the threads between updates
display_sleep = 1
discovery_sleep = 120
autohack_sleep = 10

# ----- helper functions ----- #

# cleanup function, run before exiting
def cleanup(signal = 0, frame = None):
  log('Autohack Died, Exiting Cleanly')
  sys.exit(0)

def log(message):
  print message
