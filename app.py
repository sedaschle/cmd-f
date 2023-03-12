from flask import Flask, render_template, request, url_for, redirect, session
from datetime import datetime
import cohere
import praw
import pickle


app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form.get("title")
        subreddit = request.form.get("subreddit")
        return redirect(url_for('results'))
    return render_template('index.html')

@app.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        length = request.form.get("time")
        difficulty = request.form.get("difficulty")
        location = request.form.get("location")
        coords = gmaps.geocode(location)[0]['geometry']['viewport']['northeast']
        data = (coords["lat"],coords["lng"],length)
        if difficulty=="Relaxed":
            level1.append(data)
            file1 = open('level1', 'wb')
            pickle.dump(level1, file1)
            file1.close()
        elif difficulty == "Active":
            level2.append(data)
            file2 = open('level2', 'wb')
            pickle.dump(level2, file2)
            file2.close()
        elif difficulty == "Intense":
            level3.append(data)
            file3 = open('level3', 'wb')
            pickle.dump(level3, file3)
            file3.close()

        
        
    

    return render_template('signup.html')

@app.route("/result")
def result():
    data = praw.scrape_reddit(session['difficulty'],session['location'], session['length'])

    result = cohere.ai(data)

    return render_template('result.html',dataToRender=result)

@app.route("/about")
def about():
    return render_template('about.html')



