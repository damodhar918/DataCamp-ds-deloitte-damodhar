from flask import Flask
from random import randint

app = Flask(__name__)

msg = ['Too low, try again!', 'Too high, try again!', 'You found me!']
links = ['https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif',
         'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif',
         'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif',]


def render(case):  # the rendering function with random RGB colors
    return f'<h1 style="color: #{randint(0, 0xFFFFFF):06x}">{msg[case]}</h1>' \
           f'<img src="{links[case]}" width=300 alt="{msg[case]}">'


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300 alt="numbers">'


number = randint(0, 9)


@app.route('/<int:guess_num>')
def compare(guess_num):
    global number
    if guess_num < number:
        return render(0)
    elif guess_num > number:
        return render(1)
    elif guess_num == number:
        number = randint(0, 9)  # change the number when it is guessed
        return render(2)


if __name__ == '__main__':
    app.run(debug=True)
