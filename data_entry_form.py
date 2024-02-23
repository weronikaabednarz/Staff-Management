import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# saving user info
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row = 0, column = 0, padx = 20, pady = 20)

first_name_label = tkinter.Label(user_info_frame, text = "First name")
first_name_label.grid(row = 0, column = 0)
last_name_label = tkinter.Label(user_info_frame, text = "Last name")
last_name_label.grid(row = 0, column = 1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row = 1, column = 1)

title_label = tkinter.Label(user_info_frame, text = "Title")
title_label.grid(row = 0, column = 2)
title_combobox = ttk.Combobox(user_info_frame, values = ["", "Mr.", "Mrs.", "Dr.", "Engr.", "MSc."])
title_combobox.grid(row = 1, column = 2)

age_label = tkinter.Label(user_info_frame, text = "Age")
age_label.grid(row = 2, column = 0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_= 18, to = 70)
age_spinbox.grid(row = 3, column = 0)

nationality_label = tkinter.Label(user_info_frame, text = "Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Poland", "Spain", "Italy", "Greece", "Portugal", "France", "United Kingdom", "Germany"])
nationality_label.grid(row = 2, column = 1)
nationality_combobox.grid(row = 3, column = 1)

gender_label = tkinter.Label(user_info_frame, text = "Gender")
gender_label.grid(row = 2, column = 2)
gender_spinbox = tkinter.Spinbox(user_info_frame, values = ["woman", "man"])
gender_spinbox.grid(row = 3, column = 2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)


window.mainloop()