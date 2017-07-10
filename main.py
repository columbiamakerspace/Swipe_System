#!/usr/bin/env python


from redis_connection import RedisConnection
from rfid_reader import RfidReader
from display_manager import DisplayManager

SETTINGS = {
    'user_privileges': {
        '3d_printer': False,
        'laser_cutter': False,
        'mill': False,
        'vinyl_cutter': False,
        'soldering_iron': False,
        'drill_press': False,
        'sewing_machine': False,
        'oscilloscope': False,
        'user': False,
        'superuser': False,
        'banned': False},
    'rfid_regex': r'^[0-9A-z]+\n[0-9A-z]{10}$'
}

rfid_reader = RfidReader(SETTINGS['rfid_regex'])
db = RedisConnection(
    uid_regex=SETTINGS['rfid_regex'],
    user_privileges=SETTINGS['user_privileges'],
)
display = DisplayManager(db=db, user_privileges=SETTINGS['user_privileges'])

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
        display.update_ui(rfid)
    display.window.after(100, process_rfid)

#  if condition: #  sync_with_db
#  if other_condition:
    #  perform_operation
display.window.after(100, process_rfid)
display.window.mainloop()
# TODO: exit properly
