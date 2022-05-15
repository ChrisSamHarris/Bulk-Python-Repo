#GUI - Graphical User Interface 
#1980's Mac Lisa - GUI Operating System : Xerox PARC first GUI; ethernet, OOP & GUI - 1999 Pirates of Silicon Valley 

#Advanced Arguements 

#Tkinter 
import tkinter

from setuptools import Command 

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width= 500, height=300)

#Label
my_label = tkinter.Label(text="I Am A Label", font=("Arial", 24, "bold"))
# my_label.pack(expand=True) # displays the label
my_label.pack() #(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Entry
input = tkinter.Entry(width=15)
input.pack()

def button_clicked():
    print("I Got Clicked")
    new_text = input.get()
    my_label.config(text=new_text)

#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack() #To appear on the screen any tkinter object needs some form of layout i.e. pack


window.mainloop() #Has to be at the end of the programme
