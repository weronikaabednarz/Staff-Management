import tkinter
from tkinter import ttk

def enter_data():
    # user info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    print("First name: ", firstname, "\tLast name: ", lastname)

    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    gender = gender_spinbox.get()
    print("Title: ", title, "\tAge: ", age, "\tNationality: ", nationality, "\tGender: ", gender)

    # course info
    registrationstatus = reg_status_var.get()
    numcourses = numcourses_spinbox.get()
    numsemesters = numsemesters_spinbox.get()
    print("Registration status: ", registrationstatus, "\nCourses: ", numcourses, "\tSemesters: ", numsemesters)
    print("-----------------------------------------------------------------------")

def cancel():
    window.destroy()

window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# saving user info
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

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
gender_spinbox = ttk.Combobox(user_info_frame, values = ["woman", "man"])
gender_spinbox.grid(row = 3, column = 2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# saving course info                            sticky - expand
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

registered_label = tkinter.Label(courses_frame, text = "Registration Status")
registered_label.grid(row = 0, column = 0)
reg_status_var = tkinter.StringVar(value = "not registered")
registered_check = tkinter.Checkbutton(courses_frame, text = "Currently Registered",
                                       variable = reg_status_var, onvalue = "registered",
                                       offvalue = "not registered")
registered_check.grid(row = 1, column = 0)

numcourses_label = tkinter.Label(courses_frame, text = "Completed Courses")
numcourses_label.grid(row = 0, column = 1)
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numcourses_spinbox.grid(row = 1, column = 1)

numsemesters_label = tkinter.Label(courses_frame, text = "Semesters")
numsemesters_label.grid(row = 0, column = 2)
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_ = 0, to = "infinity")
numsemesters_spinbox.grid(row = 1, column = 2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

# accept terms
terms_frame = tkinter.LabelFrame(frame, text = "Terms & Conditions")
terms_frame.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)
terms_check = tkinter.Checkbutton(terms_frame, text = "I accept all terms and conditions.")
terms_check.grid(row = 0, column = 0)

# button
button_enter = tkinter.Button(frame, text = "Enter data", command = enter_data)
button_enter.grid(row = 3, column = 0, sticky = "e", padx = 20, pady = 10)

button_cancel = tkinter.Button(frame, text = "Cancel", command = cancel)
button_cancel.grid(row = 3, column = 0, sticky = "w", padx = 20, pady = 10)
window.mainloop()