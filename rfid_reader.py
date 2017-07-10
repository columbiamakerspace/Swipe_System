import re
import pynput
import threading


class RfidReader(object):
    """Capture keyboard input from the RFID scanner"""
    _rfid = []

    def __init__(self,
                 rfid_regex=r'^[0-9A-z]+\n[0-9A-z]{10}$',
                 allowed_chars_regex=r'[0-9A-z\n]'):
        self.rfid_regex = rfid_regex
        self.allowed_chars_regex = allowed_chars_regex
        self.t = threading.Thread(
            target=self._pynput_listener, name="_pynput_listener")
        self.t.start()

    def _pynput_listener(self):
        with pynput.keyboard.Listener(on_press=self._on_press) as l:
            l.join()

    def _on_press(self, key):
        k = None
        if isinstance(key, pynput.keyboard.KeyCode) \
                and re.match('^%s$' % self.allowed_chars_regex, key.char):
            k = key.char
        elif key == pynput.keyboard.Key.enter:
            k = '\n'
        if k is not None:
            self._rfid.append(k)

    def get(self):
        rv = ''.join(self._rfid)
        if re.match(self.rfid_regex, rv):
            self._rfid = []
            return rv
        return ''

if __name__ == '__main__':
    # for testing...
    k = RfidReader()
    while True:
        import time
        time.sleep(.1)
        z = k.get()
        if z:
            print('rfid <%s>' % z)
