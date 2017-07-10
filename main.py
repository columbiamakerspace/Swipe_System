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
from display_manager import DisplayManager

rfid_reader = RfidReader()
display = DisplayManager(
    tools=['3d_printer', 'laser_cutter', 'mill', 'vinyl_cutter',
           'soldering_iron', 'drill_press', 'sewing_machine', 'oscilloscope'],
    user_flags=['user', 'superuser', 'banned'])

dct = {
    '4808739405663507168\n2cef529fab': {
        "uni": 'ye2184',
        "first_name": 'Yonah',
        "last_name": 'Elorza',
        "user": 1,
        "drill": 1,
        "mill": 1,
        "sewing": 1,
        "printer": 1,
        "solder": 1,
        "oscope": 1,
        "vinyl": 1,
        "laser": 1,
        "super": 1,
        "banned": 0
    }
}
uni2uid = {
    'ye2184': '4808739405663507168\n2cef529fab'
}



# Pulling current swiped user data
def process_rfid():
    rfid = rfid_reader.get()
    if rfid:
        display.update_ui(rfid, dct, uni2uid)
    display.window.after(100, process_rfid)

#  if condition: #  sync_with_db
#  if other_condition:
    #  perform_operation
display.window.after(100, process_rfid)
display.window.mainloop()
# TODO: exit properly
