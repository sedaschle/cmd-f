import praw
from praw.models import MoreComments
import cohere
import numpy as np
import config


# TODO: move to env file
reddit = praw.Reddit(client_id=config.praw_client_id, client_secret= config.praw_client_secret,
                              user_agent=config.praw_user_agent)
co = cohere.Client(config.praw_cohere_token)

min_comments = 10
max_comments = 90
num_threads = 5


def calculate_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def search_comments(subreddit, title):
    comments = []
    sub = reddit.subreddit(subreddit)

    for i, thread in enumerate(sub.search(query=title, sort="relevance")):
        if i == num_threads:
            break

        if thread.num_comments > min_comments:
            print(thread.title, thread.num_comments)

            phrases = [thread.title, title]
            actual, target = co.embed(phrases).embeddings

            # check returned thread from reddit is relevant to topic
            if calculate_similarity(actual, target) > 0.5:
                print("Title approved")
                for comment in thread.comments.list()[:min(thread.num_comments, max_comments)]:
                    if isinstance(comment, MoreComments):
                        continue
                    comments.append(comment.body)
                return thread.title, thread.url, comments

    return None, None, None
