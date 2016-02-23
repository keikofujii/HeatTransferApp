#!/usr/bin/python3.5

"""
This is an app that will serve as a tool for a lab for Mike Foster's
heat transfer class.
"""

from tkinter import *
import os

def updateCommand():
    """
    Method that controls what the update button does
    """
    print("Update!")

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def main():
    """
    The main method that is called when this application is run
    """
    PT_DROPDOWN_ROW = 0
    FLUID_DROPDOWN_ROW = 1
    IMAGE_ROW = 2
    IMAGE_COLUMN_SPAN = 6
    P_ROW = 3
    T_ROW = 4
    UPDATE_BUTTON_ROW = 5
    ALIGN_LEFT = W
    ALIGN_RIGHT = E
    INITAL_COLUMN = 0
    INITAL_ENTRY_COLUMN = 1
    INITAL_LABEL_COLUMN = 2
    EXIT_COLUMN = 3
    EXIT_ENTRY_COLUMN = 4
    EXIT_LABEL_COLUMN = 5
    UPDATE_BUTTON_ROW = 5
    
    #create the window
    root = Tk()
    root.title("Heat Transfer Lab - Temp vs. Energy")

    systemImage = PhotoImage(file="System.gif")

    # create the labels
    Label(root, text="Units for pressure:").grid(row=PT_DROPDOWN_ROW, column=INITAL_COLUMN, sticky=ALIGN_RIGHT)
    Label(root, text="Units for temperature:").grid(row=FLUID_DROPDOWN_ROW, column=INITAL_COLUMN, sticky=ALIGN_RIGHT)
    Label(root, text="Select a fluid:").grid(row=PT_DROPDOWN_ROW, column=EXIT_ENTRY_COLUMN, sticky=ALIGN_RIGHT)
    Label(root, image=systemImage).grid(row=IMAGE_ROW, columnspan=IMAGE_COLUMN_SPAN)
    Label(root, text="Pi =").grid(row=P_ROW, column=INITAL_COLUMN, sticky=ALIGN_RIGHT)
    Label(root, text="Ti =").grid(row=T_ROW, column=INITAL_COLUMN, sticky=ALIGN_RIGHT)
    Label(root, text="Pe =").grid(row=P_ROW, column=EXIT_COLUMN, sticky=ALIGN_RIGHT)
    Label(root, text="Te =").grid(row=T_ROW, column=EXIT_COLUMN, sticky=ALIGN_RIGHT)

    # Create and place the entry boxes
    pi = Entry(root)
    ti = Entry(root)
    pe = Entry(root)
    te = Entry(root)

    pi.grid(row=P_ROW, column=INITAL_ENTRY_COLUMN, sticky = ALIGN_RIGHT)
    ti.grid(row=T_ROW, column=INITAL_ENTRY_COLUMN, sticky = ALIGN_RIGHT)
    pe.grid(row=P_ROW, column=EXIT_ENTRY_COLUMN, sticky = ALIGN_RIGHT)
    te.grid(row=T_ROW, column=EXIT_ENTRY_COLUMN, sticky = ALIGN_RIGHT)

    # Create and place the dropdown selectors
    pressureChoice = StringVar(root)
    pressureChoice.set("kPa")   #default choice
    pressureOptionList = ["kPa", "psia", "atm"]
    pressureDropdown = OptionMenu(root, pressureChoice, *pressureOptionList)
    pressureDropdown.grid(row=PT_DROPDOWN_ROW, column=INITAL_ENTRY_COLUMN, sticky=ALIGN_LEFT)
    pressureDropdown.configure(width=10)

    tempChoice = StringVar(root)
    tempChoice.set("K")     #default choice
    tempOptionList = ["K", "C", "F", "R"]
    tempDropdown = OptionMenu(root, tempChoice, *tempOptionList)
    tempDropdown.grid(row=FLUID_DROPDOWN_ROW, column=INITAL_ENTRY_COLUMN, sticky=ALIGN_LEFT)
    tempDropdown.configure(width=10)

    fluidChoice = StringVar(root)
    fluidChoice.set("Nitrogen")     #default choice
    fluidOptionList = ["Nitrogen", "Carbon Dioxide", "Helium", "Argon"]
    fluidDropdown = OptionMenu(root, fluidChoice, *fluidOptionList)
    fluidDropdown.grid(row=PT_DROPDOWN_ROW, column=EXIT_LABEL_COLUMN, sticky=ALIGN_LEFT)
    fluidDropdown.configure(width=20)    

    # Create the unit labels
    # Need to update based on what is entered for pressure and temperature
    # Labels are based on the dropdown selectors that correspond and will
    # update when the dropdown selectors are changed
    Label(root, textvariable=pressureChoice).grid(row=P_ROW, column=INITAL_LABEL_COLUMN, sticky=ALIGN_LEFT)
    Label(root, textvariable=tempChoice).grid(row=T_ROW, column=INITAL_LABEL_COLUMN, sticky=ALIGN_LEFT)
    Label(root, textvariable=pressureChoice).grid(row=P_ROW, column=EXIT_LABEL_COLUMN, sticky=ALIGN_LEFT)
    Label(root, textvariable=tempChoice).grid(row=T_ROW, column=EXIT_LABEL_COLUMN, sticky=ALIGN_LEFT)

    Button(root, text='Update', command=updateCommand).grid(row=UPDATE_BUTTON_ROW, column=0, sticky=W, pady=4)
    
    #kick off the main event loop
    mainloop()

if __name__ == '__main__':
    main()
