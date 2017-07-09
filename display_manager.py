try:
    import Tkinter
    from Tkinter import *
except:
    import tkinter as Tkinter
    from tkinter import *
import ttk

def notebook():
    nb = ttk.Notebook(window)

    frame_signin(nb)
    frame_users(nb)
    frame_superuser_auth(nb)
    nb.pack(expand=1, fill="both")


# Sign-in frame
def frame_signin(nb):
    signin = ttk.Frame(nb)
    signFrame = Frame(signin)
    signFrame.pack(side=TOP, expand=1, fill="both")
    Z0 = Label(signFrame, text="Tap to sign in")
    Z0.pack(side=TOP, expand=1, fill="both")
    nb.add(signin, text="Sign-In")


# Users Frame
def frame_users(nb):
    def add(*args):
        uid.set(args[0])
        uni.set(args[1])
        lastname.set(args[2])
        firstname.set(args[3])
        manage.add_user(
            uid=uid.get(), uni=uni.get(),
            lastname=lastname.get(), firstname=firstname.get(),
            dct=dct)  # TODO: remove dct or clean up.

    swiper = ttk.Frame(nb)
    addFrame = Frame(swiper)
    addFrame.pack(side=TOP, expand=1, fill="both")
    B1 = Label(addFrame, text="UID")
    C1 = Entry(addFrame, textvariable=uid)
    B2 = Label(addFrame, text="UNI")
    C2 = Entry(addFrame, textvariable=uni)
    B3 = Label(addFrame, text="First Name")
    C3 = Entry(addFrame, textvariable=firstname)
    B4 = Label(addFrame, text="Last Name")
    C4 = Entry(addFrame, textvariable=lastname)
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

# superusruser Authentication Frame
def frame_superuser_auth(nb):
    superusrUserAuth = ttk.Frame(nb)
    authFrame = Frame(superusrUserAuth)
    authFrame.pack(side=TOP, expand=1, fill="both")
    D0 = Checkbutton(
        authFrame,
        text="Unlock on superusruser Swipe",
        variable=unlocked,
        onvalue=1,
        offvalue=0,
        padx=5,
        pady=5)
    D0.pack(side=TOP, expand=1, fill="both")
    nb.add(superusrUserAuth, text="superusruser Authentication")

# Permissions Frame
def frame_permissions(nb):
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
    E1 = Entry(permFrame1, text=uni)

    L1.pack(side=LEFT, expand=1, fill="x")
    E1.pack(side=LEFT, expand=1, fill="x")

    # Get and Set Buttons
    B1 = Button(permFrame1, text="Get", command=getDataUNI, padx=5, pady=5)
    B2 = Button(
        permFrame2,
        text="Set",
        command=setDataUNI,
        padx=5,
        pady=5,
        state=DISABLED)
    B1.pack(side=RIGHT)
    B2.pack(side=RIGHT)

    # All the different tool trainings
    T0 = Checkbutton(
        permFrame3,
        text="User",
        variable=user,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T1 = Checkbutton(
        permFrame3,
        text="3D Printer",
        variable=printer,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T2 = Checkbutton(
        permFrame3,
        text="Laser Cutter",
        variable=laser,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T3 = Checkbutton(
        permFrame3,
        text="CNC Mill",
        variable=mill,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T4 = Checkbutton(
        permFrame3,
        text="Vinyl Cutter",
        variable=vinyl,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T5 = Checkbutton(
        permFrame3,
        text="Soldering",
        variable=solder,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T6 = Checkbutton(
        permFrame3,
        text="Drill Press",
        variable=drill,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T7 = Checkbutton(
        permFrame3,
        text="Sewing Machine",
        variable=sewing,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T8 = Checkbutton(
        permFrame3,
        text="Hand Tools",
        variable=hand,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T9 = Checkbutton(
        permFrame3,
        text="Oscilloscope",
        variable=osc,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T10 = Checkbutton(
        permFrame3,
        text="superusruser",
        variable=superusr,
        onvalue=1,
        offvalue=0,
        state=DISABLED,
        padx=5,
        pady=5)
    T11 = Checkbutton(
        permFrame3,
        text="Banned",
        variable=ban,
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


def getData():
    uni.set(dct.get(uid.get(), {}).get('uni', ''))
    user.set(dct.get(uid.get(), {}).get('user', False))

    printer.set(dct.get(uid.get(), {}).get('printer', False))
    laser.set(dct.get(uid.get(), {}).get('laser', False))
    mill.set(dct.get(uid.get(), {}).get('mill', False))
    vinyl.set(dct.get(uid.get(), {}).get('vinyl', False))
    solder.set(dct.get(uid.get(), {}).get('solder', False))
    drill.set(dct.get(uid.get(), {}).get('drill', False))
    sewing.set(dct.get(uid.get(), {}).get('sewing', False))

    osc.set(dct.get(uid.get(), {}).get('oscope', False))
    superusr.set(dct.get(uid.get(), {}).get('superusr', False))
    ban.set(dct.get(uid.get(), {}).get('banned', False))


def getDataUNI():
    dct[uni2uid[uni.get()]]['user']
    user.set(dct[uni2uid[uni.get()]]['user'])
    printer.set(dct[uni2uid[uni.get()]]['printer'])
    laser.set(dct[uni2uid[uni.get()]]['laser'])
    mill.set(dct[uni2uid[uni.get()]]['mill'])
    vinyl.set(dct[uni2uid[uni.get()]]['vinyl'])
    solder.set(dct[uni2uid[uni.get()]]['solder'])
    drill.set(dct[uni2uid[uni.get()]]['drill'])
    sewing.set(dct[uni2uid[uni.get()]]['sewing'])
    osc.set(dct[uni2uid[uni.get()]]['oscope'])
    superusr.set(dct[uni2uid[uni.get()]]['superusr'])
    ban.set(dct[uni2uid[uni.get()]]['banned'])


def setDataUNI():
    manage.change_permissions_uni(uni.get(), 'user', user.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'printer', printer.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'laser', laser.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'mill', mill.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'vinyl', vinyl.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'solder', solder.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'drill', drill.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'sewing', sewing.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'osmanage.cope', osmanage.c.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'superusr', superusr.get(), dmanage.ct)
    manage.change_permissions_uni(uni.get(), 'banned', ban.get(), dmanage.ct)

def update_ui(rfid):
    window.update()
    uid.set(rfid)
    if rfid:
        raise_frame(permissions)
        getData()


# Main Window
window = Tkinter.Tk()
window.title("Card Swipe System")

# "add user" screen
uid = StringVar()
uni = StringVar()
firstname = StringVar()
lastname = StringVar()

# "superuser authentication"
unlocked = BooleanVar()

# "user permissions" screen
user = StringVar()
printer = BooleanVar()
laser = BooleanVar()
mill = BooleanVar()
vinyl = BooleanVar()
solder = BooleanVar()
drill = BooleanVar()
sewing = BooleanVar()
hand = BooleanVar()
osc = BooleanVar()
superusr = BooleanVar()
ban = BooleanVar()

flag = 0
notebook()

# Establish dctionary of users
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


