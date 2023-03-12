import cohere as cohere
from cohere.classify import Example
co = cohere.Client('S4kgh2LIaQL0b8FFV0KI9KnguLR89eIpUSfaIrPA')

examples = [
Example("The acting was incredible and the story was gripping", "positive"),
Example("The special effects were top-notch but the plot was weak", "neutral"),
Example("I was disappointed by the lackluster performances", "negative"),
Example("This is a must-see movie, I highly recommend it!", "positive"),
Example("The film was slow-paced and boring", "negative"),
Example("The soundtrack was amazing and really added to the movie", "positive"),
Example("The movie was just okay, nothing special", "neutral"),
Example("I found the characters to be unlikable and the dialogue was cheesy", "negative"),
Example("This movie exceeded my expectations, I was blown away", "positive"),
Example("The cinematography was stunning but the script was lacking", "neutral")
]



prompt = "my favourite colour is orange, but I don't like it very much anymore. I prefer green now"
text = "A hackathon is an event where participants, usually software developers, come together to collaborate on solving a specific problem or creating a new product or service. The purpose of a hackathon is to encourage creativity, innovation, and teamwork, while providing an opportunity for participants to learn new skills and technologies. The event typically involves intense, focused work over a short period of time, with the goal of producing a functioning prototype or proof of concept. Hackathons are often sponsored by companies or organizations seeking to foster innovation and identify talent."

# input is a list of reddit comments
def ai(input):

    impression = impressions(input)
    summary = summarize(input[1])

    return resultData(impression, summary)

def impressions(prompt):
    response = co.classify(
        inputs=prompt,
        examples=examples,
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
    result = ["Positive Reviews: " + positiveCount, "Neutral Reviews: " + neutralCount, "Negative Reviews: " + negativeCount]
    return result

def generate(prompt):
    response = co.generate( 
        model='xlarge', 
        prompt = prompt,
        max_tokens=40, 
        temperature=0.8,
        stop_sequences=["--"])

    return response.generations[0].text

def summarize(prompt):
    response = co.summarize(         
        text= prompt,
        model='summarize-xlarge', 
        extractiveness='medium',
        length='medium',
        temperature='0.3'
    )

    return response.summary

print(generate(prompt))
print(summarize(text))


def ai(data):
    return 5

class resultData:
    def init(self, impression, summary):
        self.impression = impression
        self.summary = summary