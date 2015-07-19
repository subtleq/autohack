# network discovery functions and thread
from autohack_common import *

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

