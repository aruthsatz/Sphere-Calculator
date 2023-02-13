""" Sphere Calculator User Interface.

Description: This program creates a graphical user interface
for the calculation of a Sphere

Programmer: Aiden Ruthsatz
"""

import tkinter
from algorithmic_classes import homework5_unittest

def leave():
    """Method for exiting out of the interface"""
    window.destroy()

def callback():
    """Contains Error Checking and runs the calculations from the homework5_unittest module"""
    pi_value = entry_field.get()
    radius_value = entry_field2.get()
    try:
        int_input = int(pi_value)
    except ValueError:
        output.configure(text = "You've entered an invalid value. \n Please enter a posative number.", fg='red')               
    else:
        if int_input <=0:
            
            output.configure(text = "You've entered an invalid value. \n Please enter a posative number.", fg='red')
        else:   
            sphere_object = homework5_unittest.Sphere(int_input)
            try:
                float_rad = float(radius_value)
            except ValueError:
                output.configure(text = "You've entered an invalid value. \n Please enter a posative number.", fg='red')
            else:
                if float_rad <=0:
                    output.configure(text = "You've entered an invalid value. \n Please enter a posative number.", fg='red')
                else:
                    sphere_object.radius(float_rad)
                    sphere_object.diameter(float_rad)
                    sphere_object.circumference(float_rad)
                    sphere_object.surface_area(float_rad)
                    sphere_object.volume(float_rad)
                    sphere_object.mass(float_rad)
                    
                                      
                    output.configure(text=sphere_object.valuelist, fg='green') 

# Window
window = tkinter.Tk()
window.title('Sphere Measurement Calculator')
window.geometry('400x160')
# Label for the prompts
label = tkinter.Label(window,
                         text='How many numbers would you like to pass? ')
label.place(x=10, y=10)

label_2 = tkinter.Label(window,
                         text='What is the radius value? ')
label_2.place(x=10, y=40)

# Values passed entry field
entry_field = tkinter.Entry(window, width=10)
entry_field.place(x=260, y=10)
entry_field.focus()

# Radius entry field
entry_field2 = tkinter.Entry(window, width=10)
entry_field2.place(x=260, y=45)
entry_field2.focus()

# Enter button
button = tkinter.Button(window, text='GO!',font =('Bold', 10), command=callback)
button.place(x=340, y=45)

# Label for results
results = tkinter.Label(window,
                            text='Results:')
results.place(x=10, y=80)

# Empty results label
output = tkinter.Label(window, text=' ')
output.place(x=60, y=80)

info = tkinter.Label(window, text="Calculations are delimited by a space.\n (Radius, Diameter, Circumference, Surface Area, Volume, Mass)", font =('Helvetica', 8))
info.place(x= 10, y=115)

# Exit button
exit_button = tkinter.Button(window, text='EXIT', font=('Bold', 10), command=leave)
exit_button.place(x=340, y=100)

window.mainloop()
