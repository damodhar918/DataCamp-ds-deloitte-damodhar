from tkinter import *

FONT = ("Arial", 14, "normal")


window = Tk()
window.title('MY FIRST GUI PROGRAM')
window.minsize(width=500, height=300)

#todo label
my_label = Label(text='I am a Label', font=FONT)
my_label.pack()

'''import turtle

mk = turtle.Turtle()
mk.write('Hello World')'''

#TODO: refresh
my_label['text'] = 'New Text'
my_label.config(text='New Text')

#TODO: Button
def button_clicked():
    print("I got clicked")
    entered_text = input.get()
    my_label.config(text=entered_text)

button = Button(text='Click Me', command=button_clicked)
button.pack()

#todo: Entry

input = Entry(width=50)
input.insert(END, string='Some text to begin with.')
input.pack()

#todo text box
text = Text(height=5, width=30)
#put cursor in textbox
text.focus()
text.insert(END, 'Example of multi-line text entry.')
print(text.get('1.0', END))
text.pack()


#todo: spinbox
def spinbox_used():
    #get the current value in spinbox
    print(spinbox.get())
spinbox  = Spinbox(from_ = 0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#todo: scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#todo check button
def checkbutton_used():
    print(checked_state.get())  
checked_state = IntVar()
checkbutton = Checkbutton(text='Is On?', variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#todo radio button
radio_state = IntVar()
def radio_used():
    print(radio_state.get())
radiobutton1 = Radiobutton(text='Option1', value=1, variable=radio_state, command=radio_used)   
radiobutton2 = Radiobutton(text='Option2', value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#todo list box
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
    
listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind('<<ListboxSelect>>', listbox_used)
listbox.pack()

# wait for termination
window.mainloop()