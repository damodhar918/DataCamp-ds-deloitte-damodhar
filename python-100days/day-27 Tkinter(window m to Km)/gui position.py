from tkinter import *


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)


#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.config(padx=50, pady=10)
my_label.grid(column=0, row=0)#left top corner

# my_label.pack(side='left')  # left corner
# my_label.place(x=0,y=0) #left top corner

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=1)
button.grid(padx=50, pady=10)

new_button = Button(text="New Button")
new_button.grid(column=0, row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=0, row=2)









window.mainloop()