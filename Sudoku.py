from tkinter import *
from idlelib.tooltip import Hovertip
tk = Tk()
tk.geometry("600x385")
tk.resizable(width=False, height=False)
tk.title("PySudoku")
#defining menu commands:
def ChangeBoard():
    pass
def SetDefault():
    pass
def ClearBoard():
    pass
#Menu:
menu = Menu(tk) #making Menu
tk.config(menu=menu) #set tks menu as "menu".
BoardMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Board", menu=BoardMenu)
BoardMenu.add_command(label="Change Board", command=ChangeBoard)
BoardMenu.add_command(label="Set Default Board", command=SetDefault)
BoardMenu.add_command(label="Clear Board", command=ClearBoard)
first = Frame(border=3, relief=GROOVE)
first.grid(row=0, column=0, padx=2, pady=2)
#square number, entry number
firstOne = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstTwo = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstThree = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstFour = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstFive = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstSix = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstSeven = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstEight = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstNine = Entry(first, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
firstOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [firstOne, firstTwo, firstThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [firstFour, firstFive, firstSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [firstSeven, firstEight, firstNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
#second:
sec = Frame(border=3, relief=GROOVE)
sec.grid(row=0, column=1, padx=2, pady=2)
#square number, entry number
secOne = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secTwo = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secThree = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secFour = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secFive = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secSix = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secSeven = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secEight = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secNine = Entry(sec, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
secOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [secOne, secTwo, secThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [secFour, secFive, secSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [secSeven, secEight, secNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
third = Frame(border=3, relief=GROOVE)
third.grid(row=0, column=2, padx=2, pady=2)
#square number, entry number
thirdOne = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdTwo = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdThree = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdFour = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdFive = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdSix = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdSeven = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdEight = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdNine = Entry(third, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
thirdOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [thirdOne, thirdTwo, thirdThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [thirdFour, thirdFive, thirdSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [thirdSeven, thirdEight, thirdNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
fourth = Frame(border=3, relief=GROOVE)
fourth.grid(row=1, column=0, padx=2, pady=2)
#fourth:
fourthOne = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthTwo = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthThree = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthFour = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthFive = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthSix = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthSeven = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthEight = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthNine = Entry(fourth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fourthOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [fourthOne, fourthTwo, fourthThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [fourthFour, fourthFive, fourthSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [fourthSeven, fourthEight, fourthNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
fifth = Frame(border=3, relief=GROOVE)
fifth.grid(row=1, column=1, padx=2, pady=2)
#fifth
fifthOne = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthTwo = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthThree = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthFour = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthFive = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthSix = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthSeven = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthEight = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthNine = Entry(fifth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
fifthOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [fifthOne, fifthTwo, fifthThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [fifthFour, fifthFive, fifthSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [fifthSeven, fifthEight, fifthNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
sixth = Frame(border=3, relief=GROOVE)
sixth.grid(row=1, column=2, padx=2, pady=2)
#sixth:
sixthOne = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthTwo = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthThree = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthFour = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthFive = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthSix = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthSeven = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthEight = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthNine = Entry(sixth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
sixthOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [sixthOne, sixthTwo, sixthThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [sixthFour, sixthFive, sixthSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [sixthSeven, sixthEight, sixthNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
seventh = Frame(border=3, relief=GROOVE)
seventh.grid(row=2, column=0, padx=2, pady=2)
#seventh
seventhOne = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhTwo = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhThree = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhFour = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhFive = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhSix = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhSeven = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhEight = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhNine = Entry(seventh, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
seventhOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [seventhOne, seventhTwo, seventhThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [seventhFour, seventhFive, seventhSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [seventhSeven, seventhEight, seventhNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
eighth = Frame(border=3, relief=GROOVE)
eighth.grid(row=2, column=1, padx=2, pady=2)
#eighth
eighthOne = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthTwo = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthThree = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthFour = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthFive = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthSix = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthSeven = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthEight = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthNine = Entry(eighth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
eighthOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [eighthOne, eighthTwo, eighthThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [eighthFour, eighthFive, eighthSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [eighthSeven, eighthEight, eighthNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
ninth = Frame(border=3, relief=GROOVE)
ninth.grid(row=2, column=2, padx=2, pady=2)
#ninth
ninthOne = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthTwo = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthThree = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthFour = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthFive = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthSix = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthSeven = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthEight = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthNine = Entry(ninth, width=2, font=("Alako-Bold", 15), relief=RAISED, border=3)
ninthOne.grid(row=0, column=0, padx=5, pady=5)
r = 0
for x in [ninthOne, ninthTwo, ninthThree]:
    r += 1
    x.grid(row=r, column=0, padx=2, pady=2)
r = 0
for x in [ninthFour, ninthFive, ninthSix]:
    r += 1
    x.grid(row=r, column=1, padx=2, pady=2)
r = 0
for x in [ninthSeven, ninthEight, ninthNine]:
    r += 1
    x.grid(row=r, column=2, padx=2, pady=2)
#insert:
for x in [(firstFour, 9), (firstSix, 7), (firstEight, 4), (secOne, 2), (secSix, 6), (secEight, 8), (secSeven, 1), (secNine, 9), (thirdFive, 7), (thirdNine, 8), (fourthOne, 1), (fourthFour, 4), (fourthFive, 6), (fourthNine, 8), (fifthThree, 6), (fifthSeven, 5), (sixthOne, 8), (sixthFive, 2), (sixthSix, 4), (sixthNine, 7), (seventhOne, 2), (seventhFive, 3), (eighthOne, 3), (eighthTwo, 1), (eighthThree, 8), (eighthFour, 4), (eighthNine, 2), (ninthTwo, 7), (ninthFour, 6), (ninthSix, 1)]:
    x[0].insert(1, x[1])
    x[0].configure({"disabledforeground": "#272727"})
    x[0].config(state="disabled")
#Check:
def Check_cell_duplicate():
    global duplicate
    duplicate = False
    numbers = [firstOne.get(), firstTwo.get(), firstThree.get(), firstFour.get(), firstFive.get(), firstSix.get(), firstSeven.get(), firstEight.get(), firstNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #second:
    del numbers
    numbers = [secOne.get(), secTwo.get(), secThree.get(), secFour.get(), secFive.get(), secSix.get(), secSeven.get(), secEight.get(), secNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #third:
    del numbers
    numbers = [thirdOne.get(), thirdTwo.get(), thirdThree.get(), thirdFour.get(), thirdFive.get(), thirdSix.get(), thirdSeven.get(), thirdEight.get(), thirdNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #fourth:
    del numbers
    numbers = [fourthOne.get(), fourthTwo.get(), fourthThree.get(), fourthFour.get(), fourthFive.get(), fourthSix.get(), fourthSeven.get(), fourthEight.get(), fourthNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #fifth:
    del numbers
    numbers = [fifthOne.get(), fifthTwo.get(), fifthThree.get(), fifthFour.get(), fifthFive.get(), fifthSix.get(), fifthSeven.get(), fifthEight.get(), fifthNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #sixth:
    del numbers
    numbers = [sixthOne.get(), sixthTwo.get(), sixthThree.get(), sixthFour.get(), sixthFive.get(), sixthSix.get(), sixthSeven.get(), sixthEight.get(), sixthNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #seventh:
    del numbers
    numbers = [seventhOne.get(), seventhTwo.get(), seventhThree.get(), seventhFour.get(), seventhFive.get(), seventhSix.get(), seventhSeven.get(), seventhEight.get(), seventhNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #eighth:
    del numbers
    numbers = [eighthOne.get(), eighthTwo.get(), eighthThree.get(), eighthFour.get(), eighthFive.get(), eighthSix.get(), eighthSeven.get(), eighthEight.get(), eighthNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    #ninth:
    del numbers
    numbers = [ninthOne.get(), ninthTwo.get(), ninthThree.get(), ninthFour.get(), ninthFive.get(), ninthSix.get(), ninthSeven.get(), ninthEight.get(), ninthNine.get()]
    while '' in numbers: #remove every empty strings
        numbers.remove('')
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        duplicate = True
    duplicate_check.config(state="active")
    if duplicate:
        duplicate_check.deselect()
    else:
        duplicate_check.select()
    duplicate_check.config(state="disabled")
def Check_are_Numbers():
    global areNums
    areNums = True
    numbers = [firstOne.get(), firstTwo.get(), firstThree.get(), firstFour.get(), firstFive.get(), firstSix.get(), firstSeven.get(), firstEight.get(), firstNine.get(), secOne.get(), secTwo.get(), secThree.get(), secFour.get(), secFive.get(), secSix.get(), secSeven.get(), secEight.get(), secNine.get(), thirdOne.get(), thirdTwo.get(), thirdThree.get(), thirdFour.get(), thirdFive.get(), thirdSix.get(), thirdSeven.get(), thirdEight.get(), thirdNine.get(),fourthOne.get(), fourthTwo.get(), fourthThree.get(), fourthFour.get(), fourthFive.get(), fourthSix.get(), fourthSeven.get(), fourthEight.get(), fourthNine.get(), fifthOne.get(), fifthTwo.get(), fifthThree.get(), fifthFour.get(), fifthFive.get(), fifthSix.get(), fifthSeven.get(), fifthEight.get(), fifthNine.get(), sixthOne.get(), sixthTwo.get(), sixthThree.get(), sixthFour.get(), sixthFive.get(), sixthSix.get(), sixthSeven.get(), sixthEight.get(), sixthNine.get(), seventhOne.get(), seventhTwo.get(), seventhThree.get(), seventhFour.get(), seventhFive.get(), seventhSix.get(), seventhSeven.get(), seventhEight.get(), seventhNine.get(), eighthOne.get(), eighthTwo.get(), eighthThree.get(), eighthFour.get(), eighthFive.get(), eighthSix.get(), eighthSeven.get(), eighthEight.get(), eighthNine.get(), ninthOne.get(), ninthTwo.get(), ninthThree.get(), ninthFour.get(), ninthFive.get(), ninthSix.get(), ninthSeven.get(), ninthEight.get(), ninthNine.get()]
    for x in numbers: #remove all empty enteries like ''
        try:
            numbers.remove('')
        except:
            pass
    while '' in numbers:
        numbers.remove('')
    for x in numbers:
        print(x, end=", ")
    print("\n")
    try:
        for x in numbers:
            int(x)
    except:
        areNums = False #if something is not an intiger areNums will be set to False.
    #change
    are_numbers_check.config(state="active")
    if areNums:
        are_numbers_check.select()
    else:
        are_numbers_check.deselect()
    are_numbers_check.config(state="disabled")
def Check_vertical():
    global vertical_duplicates
    vertical_duplicates = "duplicates in columns:"
    vertical1 = [firstOne.get(), firstFour.get(), firstSeven.get(), secOne.get(), secFour.get(), secSeven.get(), thirdOne.get(), thirdFour.get(), thirdSeven.get()]
    vertical2 = [firstTwo.get(), firstFive.get(), firstEight.get(), secTwo.get(), secFive.get(), secEight.get(), thirdTwo.get(), thirdFive.get(), thirdEight.get()]
    vertical3 = [firstThree.get(), firstSix.get(), firstNine.get(), secThree.get(), secSix.get(), secNine.get(), thirdThree.get(), thirdSix.get(), thirdNine.get()]
    vertical4 = [fourthOne.get(), fourthFour.get(), fourthSeven.get(), fifthOne.get(), fifthFour.get(), fifthSeven.get(), sixthOne.get(), sixthFour.get(), sixthSeven.get()]
    vertical5 = [fourthTwo.get(), fourthFive.get(), fourthEight.get(), fifthTwo.get(), fifthFive.get(), fifthEight.get(), sixthTwo.get(), sixthFive.get(), sixthEight.get()]
    vertical6 = [fourthThree.get(), fourthSix.get(), fourthNine.get(), fifthThree.get(), fifthSix.get(), fifthNine.get(), sixthThree.get(), sixthSix.get(), sixthNine.get()]
    vertical7 = [seventhOne.get(), seventhFour.get(), seventhSeven.get(), eighthOne.get(), eighthFour.get(), eighthSeven.get(), ninthOne.get(), ninthFour.get(), ninthSeven.get()]
    vertical8 = []
    for x in [vertical1, vertical2, vertical3, vertical4, vertical5, vertical6, vertical7]:
        while '' in x:
            x.remove('')
    print(vertical7)
    for x in [(vertical1, "column 1"), (vertical2, "column 2"), (vertical3, "column 3"), (vertical4, "column 4"), (vertical5, "column 5"), (vertical6, "column 6"), (vertical7, "column 7")]: #for all verticals check if there are duplicates
        vertical_x_set = set(x[0])
        if len(vertical_x_set) != len(x[0]):
            vertical_duplicates += " "+x[1]+", "
    if vertical_duplicates == "duplicates in columns:": #if there are nothing added to this string:
        vertical_duplicates = "No duplicates in any columns."
    else:
        vertical_duplicates = vertical_duplicates[0:-2] #remove ", "
    duplicate_vertical_label.config(text=vertical_duplicates)
    Hovertip(duplicate_vertical_label, text=vertical_duplicates, hover_delay=0) #incase the text does not fit, someone could hover their mouse over the label to view complete text.
def Check_horizantal():
    pass
def Check():
    Check_cell_duplicate()
    Check_are_Numbers()
    Check_vertical()
    Check_vertical()

StateFrame = LabelFrame(tk, text="Status", font=("Dosis", 14, "bold italic"), width=200, height=100)
StateFrame.grid(row=1, column=5)
CheckbuttonFrame = Frame(StateFrame)
CheckbuttonFrame.pack()
duplicate_check = Checkbutton(CheckbuttonFrame, text="No duplicates", disabledforeground="#000000", state="disabled", )
are_numbers_check = Checkbutton(CheckbuttonFrame, text="Everything are Intigers", disabledforeground="#000000", state="disabled")
duplicate_vertical_label = Label(StateFrame, text="No duplicates in any columns.", relief="ridge")
duplicate_horizantal_label = Label(StateFrame, text="No duplicates in any rows.", relief="ridge")
duplicate_check.pack(side="left")
are_numbers_check.pack(side="left")
duplicate_vertical_label.pack()
duplicate_horizantal_label.pack()
Button(StateFrame, text="Check", command=Check, font=("Calibri", 13), bg="#808080", fg="#e6e6e6", relief=GROOVE).pack()
tk.mainloop()