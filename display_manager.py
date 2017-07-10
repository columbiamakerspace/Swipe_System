from itertools import chain
try:
    import Tkinter as tk
except:
    import tkinter as tk
import ttk

import manage


class DisplayManager(object):
    def notebook(self):
        '''
        Create the tabs on the UI page.  Each tab is called a "frame".
        '''
        nb = ttk.Notebook(self.window)
        self.frame_signin(nb)
        self.frame_users(nb)
        self.frame_permissions(nb)
        nb.pack(expand=1, fill="both")

    # Sign-in frame
    def frame_signin(self, nb):
        signin = ttk.Frame(nb)
        signFrame = tk.Frame(signin).pack(side=tk.TOP, expand=1, fill="both")
        tk.Label(signFrame, text="Tap to sign in")\
            .pack(side=tk.TOP, expand=1, fill="both")
        nb.add(signin, text="Sign-In")

    # Users Frame
    def frame_users(self, nb):
        swiper = ttk.Frame(nb)
        addFrame = tk.Frame(swiper)
        addFrame.pack(side=tk.TOP, expand=1, fill="both")

        entries = {}
        for text, var in [('UID', self.uid),
                          ('UNI', self.uni),
                          ('First Name', self.firstname),
                          ('Last Name', self.lastname)]:
            tk.Label(addFrame, text=text)\
                .pack(side=tk.TOP, expand=1, fill="both")
            e = tk.Entry(addFrame, textvariable=var)\
                .pack(side=tk.TOP, expand=1, fill="both")
            entries[e] = var

        def add(entries):
            for k, v in entries.items():
                v.set(k)
            manage.add_user(
                uid=self.uid.get(), uni=self.uni.get(),
                lastname=self.lastname.get(), firstname=self.firstname.get())
        tk.Button(
            addFrame, text="Add User", padx=5, pady=5,
            command=lambda: add(entries)).pack(side=tk.BOTTOM)
        nb.add(swiper, text="Add User")

    # Permissions Frame
    def frame_permissions(self, nb):
        self._frame_permissions = permissions = ttk.Frame(nb)
        # Displays current UNI
        permFrame1 = tk.Frame(permissions)
        permFrame2 = tk.Frame(permissions)
        permFrame3 = tk.Frame(permissions)

        # UNI Entry and Display
        tk.Label(permFrame1, text="UNI").pack(side=tk.LEFT, expand=1, fill="x")
        tk.Entry(permFrame1, text=self.uni)\
            .pack(side=tk.LEFT, expand=1, fill="x")

        # Get and Set Buttons
        tk.Button(permFrame1, text="Get", command=self.getDataUNI, padx=5,
                  pady=5).pack(side=tk.RIGHT)
        tk.Button(permFrame2, text="Set", command=self.setDataUNI, padx=5,
                  pady=5).pack(side=tk.RIGHT)

        # All the different tool trainings
        for n, (key, var) in enumerate(chain(
                self.tools.items(), self.user_flags.items())):
            tk.Checkbutton(
                permFrame3,
                text=key,
                variable=var,
                onvalue=1,
                offvalue=0,
                padx=5,
                pady=5
            ).grid(row=n % 6 + 1, column=n // 6 + 1, sticky="W")

        permFrame1.pack(side=tk.TOP, expand=1, fill="x")
        permFrame2.pack(side=tk.TOP, expand=1, fill="x")
        permFrame3.pack(side=tk.RIGHT, expand=1, fill="both")
        nb.add(permissions, text="User Permissions")

    def getData(self, dct, uid=None):
        if uid is None:
            uid = self.uid.get()
        for dct in [self.tools, self.user_flags]:
            for key, boolean_var in self.tools.items():
                v = self.dct.get(uid, {}).get(key)
                if v is not None:
                    boolean_var.set(v)
        self.uni.set(dct.get(self.uid.get(), {}).get('uni', ''))

    def getDataUNI(self):
        self.getData(self, self.dct, uid=self.uni2uid[self.uni.get()])

    def setDataUNI(self):
        kvs = {k: self[k].get() for k in self.tools}
        kvs.update({k: self[k].get() for k in self.user_flags})
        manage.change_permissions(uni=self.uni.get(), **kvs)

    def update_ui(self, rfid, dct, uni2uid):
        self.dct = dct
        self.uni2uid = uni2uid

        self.uid.set(rfid)
        if rfid:
            self.getData(dct)
            self._frame_permissions.tkraise()
        self.window.update()

    def init_global_ui_vars(self, tools, user_flags):
        self.uid = tk.StringVar()
        self.uni = tk.StringVar()
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()

        # "user permissions"
        self.tools = {k: tk.BooleanVar() for k in tools}
        self.user_flags = {k: tk.BooleanVar() for k in user_flags}

    def __init__(self, tools, user_flags):
        self.window = tk.Tk()
        self.window.title("Card Swipe System")
        self.init_global_ui_vars(tools, user_flags)
        self.notebook()
        self.window.update()
