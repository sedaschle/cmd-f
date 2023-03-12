import cohere as cohere
from .examples import sentiment_examples, topic_examples
import config

co = cohere.Client(config.cohere_token)

topics = ["special effects", "cinematography", "soundtrack", "plot", "acting", "character"]


def sentiment_analysis(prompt):
    response = co.classify(
        inputs=prompt,
        examples=sentiment_examples,
    )
    positiveCount = 0
    negativeCount = 0
    neutralCount = 0

    for x in response.classifications:
        if x.prediction == 'positive':
            positiveCount += 1
        elif x.prediction == 'negative':
            negativeCount += 1
        else:
            neutralCount += 1

    print("pos:", positiveCount, "neutral:", neutralCount, "neg:", negativeCount)
    return positiveCount, neutralCount, negativeCount


def topic_analysis(prompt):
    response = co.classify(
        inputs=prompt,
        examples=topic_examples,
    )

    sorted_topics = {topic: [] for topic in topics}

    for i, x in enumerate(response.classifications):
        if x.prediction in topics:
            sorted_topics[x.prediction].append(prompt[i])

    print(sorted_topics)
    return sorted_topics


def summarize(comments):

    """
    :param comments: comments from reddit in list
    """

    prompt = '\n'.join(comments)
    response = co.summarize(
        text=prompt,
        model='summarize-xlarge',
        extractiveness='medium',
        length='medium',
        temperature='0.3'
    )

    print(response.summary)
    return response.summary


class resultData:
    def init(self, data):
        self.sentiment = sentiment_analysis(data)
        self.topic = topic_analysis(data)
        self.summary = summarize(data)