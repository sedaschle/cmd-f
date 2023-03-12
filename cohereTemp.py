import cohere as cohere
from .examples import sentiment_examples, topic_examples
from collections import Counter

co = cohere.Client('S4kgh2LIaQL0b8FFV0KI9KnguLR89eIpUSfaIrPA')

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

    return [positiveCount, neutralCount, negativeCount]


def topic_analysis(prompt):
    response = co.classify(
        inputs=prompt,
        examples=topic_examples,
    )

    sorted_topics = {topic: [] for topic in topics}

    for i, x in enumerate(response.classifications):
        if x.prediction in topics:
            sorted_topics[x.prediction].append(prompt[i])

    topic_comments = {topic: len(sorted_topics[topic]) for topic in sorted_topics}

    k = Counter(topic_comments)
    top3 = k.most_common(3)

    result = {}
    for i in range(3):
        topic = top3[i][0]
        l = len(sorted_topics[topic])
        result[i] = [topic, sorted_topics[topic][:min(5,l)]]

    return result


def summarize(comments):

    """
    :param comments: comments from reddit in list
    """

    prompt = "".join(comments)
    response = co.summarize(
        text=prompt,
        model='summarize-xlarge',
        extractiveness='medium',
        length='medium',
    )

    summary = response.summary
    return summary


class resultData:
    def __init__(self,data):
        self.sentiment = sentiment_analysis(data)
        self.topic = topic_analysis(data)
        self.summary = summarize(data)