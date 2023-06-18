from tkinter import *
import calendar

def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar")
    gui.geometry("550x600")
    year = int(year_field.get())
    cal_content = calendar.calendar(year)
    cal_year = Label(gui, text=cal_content, font=("Courier New", 10, "bold"))
    cal_year.grid(row=5, column=1, padx=20)
    gui.mainloop()

gui = Tk()
gui.config(background='grey')
gui.title("Calendar")
gui.geometry("250x140")
cal = Label(gui, text="Calendar", bg="grey", font=("Helvetica", 28))
cal.grid(row=0, column=1)
year = Label(gui, text="Enter Year", bg="grey", font=("Helvetica", 16))
year.grid(row=1, column=0)
year_field = Entry(gui)
year_field.grid(row=1, column=1)
button = Button(gui, text="Show Calendar", fg="Black", bg="light grey", command=showCalender)
button.grid(row=4, column=1)

gui.mainloop()
