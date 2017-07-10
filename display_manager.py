# -----------------------------------------------------------
# GUI tool for keeping track of users & the user_privileges they are
# trained on in Columbia's student run Makerspace
# Written for the 2017 Columbia Makerspace swipe system
# - Yonah Elorza 2017, with database assistance from Max Alto
#
# Dependencies:
#   * swig 3.0.12
#       ** PCRE
# -----------------------------------------------------------

try:
    import Tkinter as tk
except:
    import tkinter as tk
import ttk


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
            self.db.add_user(
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
        tk.Button(permFrame1, text="Get", command=self.getData, padx=5,
                  pady=5).pack(side=tk.RIGHT)
        tk.Button(permFrame2, text="Set", command=self.setDataUNI, padx=5,
                  pady=5).pack(side=tk.RIGHT)

        # All the different tool trainings
        for n, (key, var) in enumerate(self.user_privileges_dct.items()):
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

    def getData(self):
        for key, val in self.db.fetch_user_profile_data(
                uid=self.uid.get(), uni=self.uni.get()):
            if val is not None:
                var = self.user_privileges_dct[key]
                var.set(val)

    def setDataUNI(self):
        kvs = {k: self[k].get() for k in self.user_privileges_dct}
        self.db.change_permissions(uni=self.uni.get(), **kvs)

    def update_ui(self, rfid):
        self.uid.set(rfid)
        if rfid:
            self.getData()
            self._frame_permissions.tkraise()
        self.window.update()

    def init_global_ui_vars(self, user_privileges):
        self.uid = tk.StringVar()
        self.uni = tk.StringVar()
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()

        # "user permissions"
        self.user_privileges_dct = {k: tk.BooleanVar() for k in user_privileges}

    def __init__(self, db, user_privileges):
        self.db = db
        self.window = tk.Tk()
        self.window.title("Card Swipe System")
        self.init_global_ui_vars(user_privileges)
        self.notebook()
        self.window.update()
