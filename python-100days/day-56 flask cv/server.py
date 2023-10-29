from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/index')
# def index():
#     return 'Hello World'


if __name__ =="__main__":
    app.run(debug=True)