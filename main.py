#!/usr/bin/env python

# -----------------------------------------------------------
# GUI tool for keeping track of users & the tools they are
# trained on in Columbia's student run Makerspace
# Written for the 2017 Columbia Makerspace swipe system
# - Yonah Elorza 2017, with database assistance from Max Alto
#
#
# Dependencies:
#   * swig 3.0.12
#       ** PCRE
# -----------------------------------------------------------

import manage
from rfid_reader import RfidReader
import display_manager

rfid_reader = RfidReader()

while True:

    # Pulling current swiped user data
    rfid = rfid_reader.get()

    display_manager.update_ui(rfid)
    #  if condition:
        #  sync_with_db
    #  if other_condition:
        #  perform_operation
