from tkinter import Tk, Label, Button, Entry, messagebox, StringVar, Menu, Frame
from datetime import datetime


def program_help():
    help = Tk()
    help.title("HELP!")
    help.geometry("580x500")
    Label(help, text="HELP", font="ansi 20 bold italic", fg="blue").grid(row=0, columnspan=2)
    start_frame = Frame(help, highlightbackground="black", highlightthickness=2, width=10)
    Label(start_frame, text="Start: ", font="ansi 15 bold italic", fg="red").grid(row=1, column=0)
    Label(start_frame, text="press 'START' Button to start stopwatch.",
          font="ansi 10").grid(row=1, column=1)
    start_frame.grid(pady=5, padx=0)
    pause_frame = Frame(help, bg="", highlightbackground="black", highlightthickness=2, width=10)
    Label(pause_frame, text="Pause: ", font="ansi 15 bold italic", fg="red").grid(row=2, column=0)
    Label(pause_frame, text="Press 'PAUSE' Button to pause stopwatch. ",
          font="ansi 10").grid(row=2, column=1)
    pause_frame.grid(pady=5)
    pause_frame = Frame(help, highlightbackground="black", highlightthickness=2, width=10)
    Label(pause_frame, text="Reset: ", font="ansi 15 bold italic", fg="red").grid(row=3, column=0)
    Label(pause_frame, text="Press 'RESET' Button to pause stopwatch.\nNote that reset button will not reset 'ALARM'",
          font="ansi 10").grid(row=3, column=1)
    pause_frame.grid(pady=5)
    alarm_frame = Frame(help, highlightbackground="black", highlightthickness=2, width=10)
    Label(alarm_frame, text="Alarm: ", font="ansi 15 bold italic", fg="red").grid(row=4, column=0)
    Label(alarm_frame, text="To set alarm first of all enter time in inputbox\naccording to time of  stopwatch and then press\n'SET ALARM' Button.Format of alarm must be\nH: M: S i.e., H=Hours, M=Minutes and S=Seconds.\nFor custom Alarm Message replace 'This is Alarm'\nwith your message.", font="ansi 10").grid(row=4, column=1)
    alarm_frame.grid(pady=5)
    alarm_shortuts_frame = Frame(help, highlightbackground="black", highlightthickness=2)
    Label(alarm_shortuts_frame, text="Alarm Shortcts: ",
          font="ansi 15 bold italic", fg="red").grid(row=5, column=0)
    Label(alarm_shortuts_frame, text="Format = H:M:S\n'Types By YOU' = 'Set By Program'\nH:M:S = H:M:S\n:: = 00:00:00\n1:0:0 = 01:00:00\n0:0:90 = 0:01:30",
          font="Helvetica 18").grid(row=5, column=1)
    alarm_shortuts_frame.grid(pady=5, padx=5)
    help.mainloop()


root = Tk()
root.title("Stop Watch")
root.geometry("350x420")
root.resizable(0, 0)
alarm_var = StringVar()
alarm = ""
try:
    with open('stopwatch', 'r') as f:
        data = f.read().split('\n')
        if len(data) == 2:
            time = data[0].split(":")
            alarm = data[1]
            if alarm:
                alarm_var.set(data[1])
                print("alarm setted")
            else:
                alarm_var.set("H:M:S")
                print("alarm not setted")
        elif len(data) == 1:
            time = data[0].split(":")
            alarm_var.set("H:M:S")
            print("hey")
except IOError:
    print("super")
    time = ["0", "0", "-1"]
    alarm_var.set("H:M:S")
h, m, s = time
run = False


def timer():
    global h, m, s
    if run:
        if int(h) == 0 and int(m) == 0 and int(s) == -1:
            show = "Starting"
        else:
            if len(str(h)) == 1:
                h = "0" + str(h)
            if len(str(m)) == 1:
                m = "0" + str(m)
            if len(str(s)) == 1:
                s = "0" + str(s)
            show = "{}:{}:{}".format(h, m, s)
        mark['text'] = show
        mark.after(1000, timer)
        s = int(s) + 1
        if s == 60:
            s = 0
            m = int(m) + 1
        if m == 60:
            m = 0
            h = int(h) + 1
        with open("stopwatch", "w") as f:
            f.write(show + "\n" + alarm)
        if alarm:
            if show == alarm:
                messagebox.showerror("Alarm", alarm_message.get())


def start():
    with open('history', 'a') as f:
        f.write("STARTED AT  " + str(datetime.now()) + "\n")
    global run
    run = True
    start_button["state"] = "disable"
    pause_button['state'] = "active"
    reset_button['state'] = "active"
    timer()


def pause():
    with open('history', 'a') as f:
        f.write("Paused AT " + str(datetime.now()) + "\n")
    global run
    run = False
    start_button["state"] = "active"
    pause_button['state'] = "disable"
    reset_button['state'] = "active"


def reset():
    with open('history', 'a') as f:
        f.write("\n\t ---STOPED--- " + str(datetime.now()) + "\n")
    global h, m, s
    h, m, s = 0, 0, 0
    if not run:
        reset_button['state'] = "disable"
    else:
        reset_button['state'] = "active"
    mark['text'] = '00:00:00'
    with open('stopwatch', "w") as f:
        f.write("{}:{}:{}".format(h, m, s))


def set_alarm():
    global alarm
    alarm_checker = alarm_entry.get()
    alarm_checker = alarm_checker.split(":")
    if len(alarm_checker) == 3:
        h, m, s = alarm_checker
        if not h:
            h = "00"
        if not m:
            m = "00"
        if not s:
            s = "00"
        if not h.isdigit() or not m.isdigit() or not s.isdigit():
            messagebox.showerror(
                "Syntax Error", "What you are trying to do FOOL!\nEnter digits only ")
            return
        while int(s) >= 60:
            s = int(s) - 60
            m = int(m) + 1
        while int(m) >= 60:
            m = int(m) - 60
            h = int(h) + 1
        if len(str(h)) == 1:
            h = "0" + str(h)
        if len(str(m)) == 1:
            m = "0" + str(m)
        if len(str(s)) == 1:
            s = "0" + str(s)
        alarm = "{}:{}:{}".format(h, m, s)
        alarm_var.set(alarm)
        with open('history', "a") as f:
            f.write("\nALARM SETTED FOR " + str(datetime.now()) + "\n")
    elif len(alarm_checker) == 1 and not alarm_checker[0]:
        alarm = ""
        alarm_var.set('H:M:S')
        return
    else:
        messagebox.showerror("Syntax Error", "Invalid Syntax FOOL!")
        print(alarm_checker)


menubar = Menu(root)
menubar.add_command(label="HELP!", command=program_help)
root.config(menu=menubar)

alarm_message_var = StringVar()
alarm_message_var.set('This is Alarm')
HMS = Label(font=("Helvetica", 20), text="H : M : S", bg="#387823",
            fg="white", borderwidth=2, relief="groove")
HMS.grid(row=0, columnspan=2, pady=2, padx=60)
mark = Label(font=("Helvetica", 20), text="Welcome", bg="#387823",
             fg="white", borderwidth=2, relief="groove")
mark.grid(row=1, columnspan=2, pady=6, padx=60)

start_button = Button(text="Start", command=start, width=10, font=("Helvetica", 15), border=10)
start_button.grid(row=2, column=1, padx=60)

pause_button = Button(text="Pause", command=pause, width=10, font=(
    "Helvetica", 15), state='disable', border=10)
pause_button.grid(row=3, column=1, padx=60)

reset_button = Button(text="Reset", command=reset, width=10, font=(
    "Helvetica", 15), state='disable', border=10)
reset_button.grid(row=4, column=1, padx=60)
if h != "0" and m != "0" and s != "0":
    mark['text'] = "{}:{}:{}".format(h, m, s)
    reset_button['state'] = "active"
alarm_entry = Entry(font=("Helvetica", 15), border=10, textvariable=alarm_var)
alarm_entry.grid(row=5, column=1, padx=60)
alarm_message = Entry(font=("Helvetica", 15), border=10, textvariable=alarm_message_var)
alarm_message.grid(row=6, column=1, padx=60)
Button(text="Set Alarm", command=set_alarm, width=10, font=("Helvetica", 15),
       state='active', border=10).grid(row=7, column=1, padx=60)
# Button(text="Help", command=program_help, font=(
#     "Helvetica", 15), state='active', border=10).grid(row=7, column=1, padx=60)
root.mainloop()
