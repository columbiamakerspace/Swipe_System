try:
    import Tkinter
    from Tkinter import *
except:
    import tkinter as Tkinter
    from tkinter import *
import ttk


class DisplayManager(object):
    def notebook(self):
        nb = ttk.Notebook(self.window)

        self.frame_signin(nb)
        self.frame_users(nb)
        self.frame_permissions(nb)
        nb.pack(expand=1, fill="both")


    # Sign-in frame
    def frame_signin(self, nb):
        signin = ttk.Frame(nb)
        signFrame = Frame(signin)
        signFrame.pack(side=TOP, expand=1, fill="both")
        Z0 = Label(signFrame, text="Tap to sign in")
        Z0.pack(side=TOP, expand=1, fill="both")
        nb.add(signin, text="Sign-In")


    # Users Frame
    def frame_users(self, nb):
        def add(*args):
            self.uid.set(args[0])
            self.uni.set(args[1])
            self.lastname.set(args[2])
            self.firstname.set(args[3])
            manage.add_user(
                uid=self.uid.get(), uni=self.uni.get(),
                lastname=self.lastname.get(), firstname=self.firstname.get())

        swiper = ttk.Frame(nb)
        addFrame = Frame(swiper)
        addFrame.pack(side=TOP, expand=1, fill="both")
        B1 = Label(addFrame, text="UID")
        C1 = Entry(addFrame, textvariable=self.uid)
        B2 = Label(addFrame, text="UNI")
        C2 = Entry(addFrame, textvariable=self.uni)
        B3 = Label(addFrame, text="First Name")
        C3 = Entry(addFrame, textvariable=self.firstname)
        B4 = Label(addFrame, text="Last Name")
        C4 = Entry(addFrame, textvariable=self.lastname)
        A0 = Button(
            addFrame, text="Add User", padx=5, pady=5,
            command=lambda: add(C1.get(), C2.get(), C3.get(), C4.get()))
        B1.pack(side=TOP, expand=1, fill="both")
        C1.pack(side=TOP, expand=1, fill="both")
        B2.pack(side=TOP, expand=1, fill="both")
        C2.pack(side=TOP, expand=1, fill="both")
        B3.pack(side=TOP, expand=1, fill="both")
        C3.pack(side=TOP, expand=1, fill="both")
        B4.pack(side=TOP, expand=1, fill="both")
        C4.pack(side=TOP, expand=1, fill="both")
        A0.pack(side=TOP, expand=1, fill="both")
        nb.add(swiper, text="Add User")

    # Permissions Frame
    def frame_permissions(self, nb):
        permissions = ttk.Frame(nb)
        # Displays current UNI
        permFrame1 = Frame(permissions)
        permFrame2 = Frame(permissions)
        permFrame3 = Frame(permissions)
        permFrame1.pack(side=TOP, expand=1, fill="x")
        permFrame2.pack(side=TOP, expand=1, fill="x")
        permFrame3.pack(side=RIGHT, expand=1, fill="both")

        # UNI Entry and Display
        L1 = Label(permFrame1, text="UNI")
        E1 = Entry(permFrame1, text=self.uni)

        L1.pack(side=LEFT, expand=1, fill="x")
        E1.pack(side=LEFT, expand=1, fill="x")

        # Get and Set Buttons
        B1 = Button(
            permFrame1, text="Get", command=self.getDataUNI, padx=5, pady=5)
        B2 = Button(
            permFrame2, text="Set", command=self.setDataUNI, padx=5, pady=5,
            state=DISABLED)
        B1.pack(side=RIGHT)
        B2.pack(side=RIGHT)

        # All the different tool trainings
        T0 = Checkbutton(
            permFrame3,
            text="User",
            variable=self.user,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T1 = Checkbutton(
            permFrame3,
            text="3D Printer",
            variable=self.printer,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T2 = Checkbutton(
            permFrame3,
            text="Laser Cutter",
            variable=self.laser,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T3 = Checkbutton(
            permFrame3,
            text="CNC Mill",
            variable=self.mill,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T4 = Checkbutton(
            permFrame3,
            text="Vinyl Cutter",
            variable=self.vinyl,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T5 = Checkbutton(
            permFrame3,
            text="Soldering",
            variable=self.solder,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T6 = Checkbutton(
            permFrame3,
            text="Drill Press",
            variable=self.drill,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T7 = Checkbutton(
            permFrame3,
            text="Sewing Machine",
            variable=self.sewing,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T8 = Checkbutton(
            permFrame3,
            text="Hand Tools",
            variable=self.hand,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T9 = Checkbutton(
            permFrame3,
            text="Oscilloscope",
            variable=self.osc,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T10 = Checkbutton(
            permFrame3,
            text="superusruser",
            variable=self.superusr,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)
        T11 = Checkbutton(
            permFrame3,
            text="Banned",
            variable=self.ban,
            onvalue=1,
            offvalue=0,
            state=DISABLED,
            padx=5,
            pady=5)

        T0.grid(row=1, column=1, sticky="W")
        T1.grid(row=2, column=1, sticky="W")
        T2.grid(row=3, column=1, sticky="W")
        T3.grid(row=4, column=1, sticky="W")
        T4.grid(row=5, column=1, sticky="W")
        T5.grid(row=6, column=1, sticky="W")
        T6.grid(row=1, column=2, sticky="W")
        T7.grid(row=2, column=2, sticky="W")
        T8.grid(row=3, column=2, sticky="W")
        T9.grid(row=4, column=2, sticky="W")
        T10.grid(row=5, column=2, sticky="W")
        T11.grid(row=6, column=2, sticky="W")
        nb.add(permissions, text="User Permissions")

    def raise_frame(frame):
        frame.tkraise()

    # Swipe Data Get


    def getData(dct):
        self.uni.set(dct.get(self.uid.get(), {}).get('uni', ''))
        self.user.set(dct.get(self.uid.get(), {}).get('user', False))

        self.printer.set(dct.get(self.uid.get(), {}).get('printer', False))
        self.laser.set(dct.get(self.uid.get(), {}).get('laser', False))
        self.mill.set(dct.get(self.uid.get(), {}).get('mill', False))
        self.vinyl.set(dct.get(self.uid.get(), {}).get('vinyl', False))
        self.solder.set(dct.get(self.uid.get(), {}).get('solder', False))
        self.drill.set(dct.get(self.uid.get(), {}).get('drill', False))
        self.sewing.set(dct.get(self.uid.get(), {}).get('sewing', False))

        self.osc.set(dct.get(self.uid.get(), {}).get('oscope', False))
        self.superusr.set(dct.get(self.uid.get(), {}).get('superusr', False))
        self.ban.set(dct.get(self.uid.get(), {}).get('banned', False))


    def getDataUNI(self):
        self.dct[self.uni2uid[self.uni.get()]]['user']
        self.user.set(dct[uni2uid[self.uni.get()]]['user'])
        self.printer.set(dct[uni2uid[self.uni.get()]]['printer'])
        self.laser.set(dct[uni2uid[self.uni.get()]]['laser'])
        self.mill.set(dct[uni2uid[self.uni.get()]]['mill'])
        self.vinyl.set(dct[uni2uid[self.uni.get()]]['vinyl'])
        self.solder.set(dct[uni2uid[self.uni.get()]]['solder'])
        self.drill.set(dct[uni2uid[self.uni.get()]]['drill'])
        self.sewing.set(dct[uni2uid[self.uni.get()]]['sewing'])
        self.osc.set(dct[uni2uid[self.uni.get()]]['oscope'])
        self.superusr.set(dct[uni2uid[uni.get()]]['superusr'])
        self.ban.set(dct[uni2uid[self.uni.get()]]['banned'])


    def setDataUNI(self):
        manage.change_permissions_uni(self.uni.get(), 'user', self.user.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'printer', self.printer.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'laser', self.laser.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'mill', self.mill.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'vinyl', self.vinyl.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'solder', self.solder.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'drill', self.drill.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'sewing', self.sewing.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'osmanage.cope', self.osmanage.c.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'superusr', self.superusr.get(), dmanage.ct)
        manage.change_permissions_uni(self.uni.get(), 'banned', self.ban.get(), dmanage.ct)

    def update_ui(self, rfid, dct, uni2uid):
        self.dct = dct
        self.uni2uid = uni2uid

        self.window.update()
        self.uid.set(rfid)
        if rfid:
            raise_frame(permissions)
            getData(dct)


    def __init__(self):

        # Main self.window
        self.window = Tkinter.Tk()
        self.window.title("Card Swipe System")

        # "add user" screen
        self.uid = StringVar()
        self.uni = StringVar()
        self.firstname = StringVar()
        self.lastname = StringVar()

        # "user permissions" screen
        self.user = StringVar()
        self.printer = BooleanVar()
        self.laser = BooleanVar()
        self.mill = BooleanVar()
        self.vinyl = BooleanVar()
        self.solder = BooleanVar()
        self.drill = BooleanVar()
        self.sewing = BooleanVar()
        self.hand = BooleanVar()
        self.osc = BooleanVar()
        self.superusr = BooleanVar()
        self.ban = BooleanVar()

        flag = 0
        self.notebook()

        # Establish dctionary of users
