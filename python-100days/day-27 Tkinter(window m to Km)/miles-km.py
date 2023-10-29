from tkinter import *

window  = Tk()
window.title("Miles to Km Converter")
window.minsize(width=220, height=100)

miles_input = Entry(width=10)
miles_input.grid(column=1,row=0, padx=0, pady=10)
# miles_input.pack()

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)
miles_label.grid(padx=5, pady=10)

is_equal_label = Label(text = 'is equal to', font=('Arial', 10, 'bold'))
is_equal_label.grid(column=0,row=1,padx=10,pady=10)

km_results = Label(text='0',font=('Arial', 10, 'bold'))
km_results.grid(column=1,row=1)

km_label = Label(text='Km')
km_label.grid(column=2,row=1)

def mToKm():
    miles = float(miles_input.get())
    km = miles*1.689
    km_results.config(text=f'{km:.2f}')
    

calculate_button = Button(text = 'Calculate', command = mToKm)
calculate_button.grid(column=1,row=2, padx=10, pady=10)
window.mainloop()