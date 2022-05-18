from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time

t = Tk()
t.title('Reminder Application')
t.geometry("500x300")
img = Image.open("label1.png")
image = ImageTk.PhotoImage(img)
img_label = Label(t, image=image).grid()

# get details
def get_Details():
    get_Title = title.get()
    get_Msg = msg.get()
    get_Hrs = hrs.get()
    get_Min = min.get()
    get_Sec = sec.get()

    if get_Title == "" or get_Msg == "" or (get_Hrs == "" and get_Min == "" and get_Sec == ""):
        messagebox.showerror("Alert", "All the fields are required!")
    else:
        int_Hrs = int(get_Hrs)
        int_Min = int(get_Min)
        int_Sec = int(get_Sec)
        time_in_sec = ((int_Hrs * 60) * 60) + (int_Min * 60) + int_Sec
        messagebox.showinfo("Set Reminder", "Confirm Reminder ?")
        t.destroy()
        time.sleep(time_in_sec)

        notification.notify(title=get_Title,
                            message=get_Msg,
                            app_name="Reminder Application",
                            app_icon="reminder.ico",
                            timeout=10)


# Label - Title
t_label = Label(t, text="Title", font=("Avenir", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25", font=("Avenir", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Message", font=("Avenir", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("Avenir", 13))
msg.place(x=123, height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("Avenir", 10))
time_label.place(x=12, y=175)

# ENTRY - Time_hrs
hrs = Entry(t, width="5", font=("Avenir", 13))
hrs.place(x=123, y=175)

# Label - Hrs
time_hrs_label = Label(t, text="Hrs", font=("Avenir", 10))
time_hrs_label.place(x=175, y=180)

# Entry - min
min = Entry(t, width="5", font=("Avenir", 13))
min.place(x=205, y=175)

# Label - min
time_min_label = Label(t, text="Min", font=("Avenir", 10))
time_min_label.place(x=256, y=180)

# Entry - Sec
sec = Entry(t, width="5", font=("Avenir", 13))
sec.place(x=285, y=175)

# Label - Sec
time_sec_label = Label(t, text="Sec", font=("Avenir", 10))
time_sec_label.place(x=335, y=180)


# Button
button = Button(t, text="SET REMINDER", font=("Avenir", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised", cursor="hand2",
             command=get_Details)
button.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()





