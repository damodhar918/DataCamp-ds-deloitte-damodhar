from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
def bye():
    return '<b>Bye World!</b>'

@app.route('/wraper')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Bye World!'

# @app.route('/<name>')
# def greet(name):
#     return f'Hello there {name}!'

# @app.route('/<name>')
# def greet(name):
#     return f'Hello there {name+"22"}!' #name _22 will be error

@app.route('/hello/<name>/<int:age>')
def greet(name,age):
    return f'Hello there {name}! You are {age} years old.'
# end def

if __name__ == '__main__':
    app.run(debug=True)