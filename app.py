from flask import Flask, render_template, request, url_for, redirect, session
from datetime import datetime
import cohere_temp
from .reddit_scrape import search_comments

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/result")
def result():
    if request.method == 'POST':
        subreddit = request.form.get("subreddit")
        title = request.form.get("title")
        data = search_comments(subreddit, title)

        result = cohere_temp.ai(data)

        return render_template('result.html', dataToRender=result)

    return redirect(url_for('index'))


@app.route("/about")
def about():
    return render_template('about.html')
