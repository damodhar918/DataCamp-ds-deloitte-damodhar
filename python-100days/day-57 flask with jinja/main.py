from sqlite3 import Timestamp
from urllib import response
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    randdom_number = random.randint(1,10)
    current_yaer= datetime.datetime.now().year  
    return render_template("index.html", num=randdom_number,year = current_yaer)

@app.route('/guess/<name>')
def guess(name):
    gender_url = f"https://api.genderize.io/?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']
    
    age_url = f"https://api.agify.io/?name={name}"
    age_data = requests.get(age_url).json()
    age = age_data['age']
    return render_template("guess.html",person_name=name,gender = gender,age = age, gender_data=gender_data)

@app.route('/blog/<int:num>')
def get_blog(num):
    blog_url = r"https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts = all_posts,num=(num))

if __name__ == "__main__":
    app.run(debug=True)
    
    


