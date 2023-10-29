
from tkinter import *
from tkinter import messagebox
import time
# ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
path=r"C:\Users\jdamodhar\Desktop\python_essential-\python-100\day-28 tomato timer\tomato.png"
count = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global count
    count = 0
    canvas.itemconfig(timer_text, text=f'00:00')
    t_label.config(text="Timer", fg=RED)
    check_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global count
    count +=1
    
    if count % 8 == 0:
        #if count 8
        t_label.config(text="Walk Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
        messagebox.showinfo(title='Walk Break', message=f"Get out from sitting position")
        
    # elif count > 8:
    #     print("Done",count)
    #     reset_timer()
    elif not count % 2 :
        #if count the 1,3,5,7
        t_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
        messagebox.showinfo(title='Break', message=f"Breat in and out")

    elif count % 2:
        #if count 2,4,6
        t_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(coun):
    count_min = coun // 60
    count_sec = coun % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
        
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if coun>0:
        global  timer
        timer = window.after(1000, count_down, coun-1)
    else:
        start_timer()
        check_label.config(text='✔'*(count // 2))
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)




t_label = Label(text='Timer', font=(FONT_NAME, 50), bg=YELLOW, fg=RED)
t_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=path)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

st_button = Button(text='Start', highlightthickness=0,command=start_timer)
st_button.grid(column=0, row=2)

rst_button = Button(text='Reset', highlightthickness=0,command=reset_timer)
rst_button.grid(column=2, row=2)

check_label = Label(text='', font=(FONT_NAME, 18), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)


window.mainloop()
