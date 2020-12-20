from tkinter import *
from tkinter import messagebox
import timeit
import time

from PIL import ImageTk, Image

import os

root = Tk()

root.title('GUI')

root.iconbitmap('icon.ico')

root.geometry("400x500")

root.eval('tk::PlaceWindow {} center'
          .format(root.winfo_toplevel()))


# Add local server time
def clock():
    timeLocation = time.strftime('%I:%M:%S', time.localtime())

    if timeLocation != '':
        label1.config(text=timeLocation, font='times 15')
    root.after(100, clock)


label1 = Label(root, justify='center')

label1.pack()

clock()

# Create Frame
Frame1 = LabelFrame(root, text="Array Sorter", padx=50, pady=50)
Frame1.pack(padx=10, pady=10)

# Create input box
e = Entry(Frame1, width=50)
e.grid(row=0, column=1)
e.insert(0, "Enter an Array of numbers")

sorted_array = 0


def reverse():
    global sorted_array

    array = e.get()
    array.split()
    sorted_array = array[::-1]
    sort = "Reversed array is" + sorted_array

    if sorted_array == type(int):
        sort = "Please Enter a list of numbers to sort!"

    print(array[::-1])

    label1 = Label(root, text=sort)
    label1.pack()


sorted1 = 0


def sort():
    global sorted1

    array = e.get()
    list_array = list(array)
    sorted1 = sorted(list_array)

    _array = "The sorted list is ", str(sorted1)
    label2 = Label(root, text=_array)
    label2.pack()


# Define Buttons
button1 = Button(Frame1, text="Sort", command=sort)
button2 = Button(Frame1, text="Reverse", command=reverse)

# Grid buttons
button2.grid(row=1, column=1)
button1.grid(row=2, column=1)

# NEw LAbel
# new_Label

new_Label = Label(root, text="Would you like to save a log ? Y/N")
new_Label.pack()

# Creating a log 

newEntry = Entry(root, width=30)

newEntry.pack()


def saveLog():
    count = 0
    while True and count < 1:

        if newEntry.get() == "N":
            messagebox.showinfo('Message', 'Are you sure?', icon="warning")
            break

        while newEntry.get() == "Y":
            f = open('dataForList.txt', 'a')
            f.write("The sorted array is {} the reversed array is {} \n".format(sorted1, sorted_array))

            f.close()

            break

        messagebox.showinfo('Message', 'File has succesfully been saved')
        count += 1


entryButton = Button(root, text='Save', command=saveLog)
entryButton.pack()


# Quit
def quit():
    root.quit()


quitButton = Button(root, text="Quit Program", command=quit)
quitButton.pack(side=BOTTOM)

root.mainloop()
