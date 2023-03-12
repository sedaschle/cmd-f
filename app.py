from flask import Flask, render_template, request, url_for, redirect, session
from datetime import datetime
from .cohereTemp import resultData
from .reddit_scrape import search_comments

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/result", methods=['POST'])
def result():
    if request.method == 'POST':
        subreddit = request.form.get("subreddit")[2:]
        print(subreddit)
        title = request.form.get("title")
        thread_title, url, comments = search_comments(subreddit, title)

        if thread_title is not None:
            print(thread_title)
            result = resultData(comments)
            return render_template('results.html',
                                   user_title=title,
                                   title=thread_title,
                                   url=url, result=result,
                                   subreddit=subreddit)

        else:
            error = 'Error: Subreddit could not be found.'
            return render_template('index.html', error=error)


@app.route("/about")
def about():
    return render_template('about.html')
