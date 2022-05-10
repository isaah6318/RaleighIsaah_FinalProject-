from tkinter import *


root = Tk()
root.title("Ezeke's Pub - POS")
root.configure(bg="LightSkyBlue4")
root.eval('tk::PlaceWindow . top')
root.geometry("930x520")



#Formatting the application for spacing out the Entry box plus the grid to lay out the buttons and such!

e = Entry(root, width=50, bg="black", fg="green", borderwidth=15, font=55,  justify=CENTER)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


#e.insert(0,"")

#When clicking the buttons/functional buttons

def button_click(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


    #######################################

def button_clear():
    e.delete(0, END)

    #######################################

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

    #######################################

def button_equal():
#second_number = e.get()  --- Removing this code because having error with check mark not loading up after total
#e.delete(0, END)   --- Removing this code because having error with check mark not loading up up after total
    newWindow = Toplevel(root)
    newWindow.title("Submitting Order")
    newWindow.geometry("300x550")
    newWindow.configure(bg="LightSkyBlue4")
    #Row1
    Label(newWindow, text="-----ORDER IS SUBMITTED!-----", font=25, bg="black", fg="white").pack(pady=95)
    #row2 for image to be in middle between label 1 and 2
    checkmark = PhotoImage(file="checkmark.png", width=125, height=125)
    Label(newWindow, image=checkmark).pack()
    #row3
    Label(newWindow, text="-------Ezeke's Pub-------", font=25, bg="black", fg="white").pack(pady=95)


    # burger = PhotoImage(file="Burger.png", width=75, height=60)
    # logo = Label(root, image=burger).grid(row=3, column=3)


    ########################################

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


#Defining the buttons

button_1 = Button(root, bg="blue", fg="White", text="Vanilla Cake - $3.75", padx=39, pady=20, command=lambda: button_click(3.75))
button_2 = Button(root, bg="blue", fg="White", text="Medium Drink - $2.25", padx=15, pady=20, command=lambda: button_click(2.25))
button_3 = Button(root, bg="blue", fg="White", text="Cheeseburger N' Fries - $6.35", padx=23, pady=20, command=lambda: button_click(2.25))
button_4 = Button(root, bg="blue", fg="White", text="Chocolate Cake - $3.75", padx=30, pady=20, command=lambda: button_click(3.75))
button_5 = Button(root, bg="blue", fg="White", text="Large Drink - $3.00", padx=23, pady=20, command=lambda: button_click(3.00))
button_6 = Button(root, bg="blue", fg="White", text= "Hotdog N' Fries - $5.35", padx=40, pady=20, command=lambda: button_click(5.35))
button_7 = Button(root, font=25, bg="black", fg="White", text="---Deserts----", padx=90, pady=20, command=lambda: button_click(0))
button_8 = Button(root, font=25, bg="black", fg="White", text="---Drinks---", padx=90, pady=20, command=lambda: button_click(0))
button_9 = Button(root, font=25, bg="black", fg="White", text="---Food---", padx=90, pady=20, command=lambda: button_click(0))
button_0 = Button(root,  bg="purple4", fg="White", text="Military Discount (Broken)", padx=5, pady=20, command=lambda: button_click(-1))
button_add = Button(root, bg="green", fg="White", text="Add to Order", padx=39, pady=20, command=button_add)
button_equal = Button(root, bg="green", fg="white", text="Total", padx=87.5, pady=20, command=button_equal)
button_clear = Button(root, bg="red", fg="White", text="Restart Order", padx=66.5, pady=20, command=button_clear)


# Add this code to add a subtract button- button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
#I am not using these buttons. These are just fillers to describe my program
button_subtract = Button(root, text="Version: 1.5", padx=28, pady=20, command=button_subtract)
button_multiply = Button(root, text="By: Isaah Raleigh", padx=14, pady=16, command=button_multiply)
button_divide = Button(root, text="Ezeke's Pub", padx=27, pady=15, command=button_divide)


###

# Put the buttons on the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=1)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=1)

#Reference for white buttons on where they are. Now I do not use the functions for these buttons so they are fillers
button_subtract.grid(row=5, column=3)
button_multiply.grid(row=6, column=3)
button_divide.grid(row=7, column=3)


#images per each item

burger = PhotoImage(file="Burger.png", width=75, height=60)
logo = Label(root, image=burger).grid(row=3, column=3)

hotdog = PhotoImage(file="hotdog.png", width=75, height=50)
logo = Label(root, image=hotdog).grid(row=2, column=3)






root.mainloop()