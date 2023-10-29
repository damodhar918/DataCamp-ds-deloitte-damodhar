from email.mime import image
import pandas as pd
import turtle 

data = pd.read_csv(r"day-25 pandas\us-states-game-start\50_states.csv")

screen = turtle.Screen()
screen.title('U.S. States Game')
img = r'day-25 pandas\us-states-game-start\blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)


guess_ans =[]
ans = ''
while ans != 'Exit' and len(guess_ans)<=50 :
    ans = screen.textinput(title=f'{len(guess_ans)}/50 Guess the State', prompt="What's another state").title()
    if ans in data.state.to_list():
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans]
        t.goto(int(state_data.x), int(state_data.y))
        print(state_data.state.item())
        t.write(str(state_data.state.item()))
        print(state_data.x, state_data.y)
        guess_ans.append(ans)


miss_state=[ state for state in data.state.to_list() if state not in guess_ans]   
print(miss_state)
pd.DataFrame(miss_state).to_csv(r'day-25 pandas\us-states-game-start\miss_state.csv', index=False, header=['state'])
        

def get_mouse_click(x,y):
    print(x,y)
    
screen.onclick(get_mouse_click)
screen.mainloop()