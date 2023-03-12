from cohere.classify import Example

sentiment_examples = [
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

topic_examples = [
    # Acting
    Example("The acting in this movie was simply outstanding! ", "acting"),
    Example("The actors truly brought their characters to life and delivered powerful performances that left me completely engrossed in the story", "acting"),
    Example("Unfortunately, the lackluster performances from the cast left me feeling disappointed", "acting"),
    Example("Despite a promising premise, the acting fell flat and failed to captivate me.", "acting"),
    Example("The main actor was terrible", "acting"),

    # Plot
    Example("The cinematography was undeniably stunning, but unfortunately, the script was lacking", "plot"),
    Example("Despite the impressive special effects, I found the film to be slow-paced and ultimately boring.", "plot"),
    Example("Although the film had potential, the slow pace and boring storyline left me feeling unimpressed", "plot"),
    Example("The plot of this movie was both compelling and thought-provoking, tackling complex themes and ideas in a way that was both engaging and accessible.", "plot"),
    Example("This movie had an incredibly well-crafted plot that was both original and satisfying", "plot"),

    # Special Effects
    Example("While the special effects were impressive, I couldn't help but feel underwhelmed by the plot.", "special effects"),
    Example("The special effects in this movie were absolutely stunning!", "special effects"),
    Example("The CGI was seamless and the visual design of the world was breathtaking.", "special effects"),
    Example("This movie exceeded my expectations in every way, thanks in large part to its jaw-dropping special effects.", "special effects"),
    Example("The attention to detail and the way the computer-generated images seamlessly blended with the live-action footage was truly impressive. ", "special effects"),

    # Cinematography
    Example("Overall, I would say that the graphics were good, but not quite up to the standard set by some of the industry's top films.", "cinematography"),
    Example("The attention to detail and the vivid colors made every scene feel like a work of art.", "cinematography"),
    Example("The attention to detail and the realism of the graphics made the movie a feast for the eyes.", "cinematography"),
    Example("The graphics in this movie were a mixed bag. While some scenes looked absolutely stunning, others were noticeably lacking in detail or felt a bit clunky.", "cinematography"),
    Example("The graphics in this movie were truly breathtaking.", "cinematography"),

    # Characters
    Example("I found it difficult to connect with the characters in this film. ", "character"),
    Example("I found the characters to be unlikable and the dialogue to be cheesy in this movie.", "character"),
    Example("Each one was well-developed and had their own unique personality that made them stand out.", "character"),
    Example("I found the characters in this movie to be incredibly likable and relatable.", "character"),
    Example("The characters in this movie were so well-written and well-acted that they felt like real people", "character"),

    # Soundtrack
    Example("The soundtrack in this movie was truly amazing and added so much to the overall experience.", "soundtrack"),
    Example("Each song was perfectly chosen to complement the action on screen, and it really helped to enhance the overall experience of watching the film.", "soundtrack"),
    Example("This movie had a truly incredible soundtrack that perfectly captured the mood and tone of the story.", "soundtrack"),
    Example("The music was both haunting and beautiful, and it added a whole new layer of depth to the film.", "soundtrack"),
    Example("I found myself humming the songs for days after seeing it.", "soundtrack"),

    # Other
    Example("I mean this is obviously where we just disagree.", "other"),
    Example(" If the movie was as terrible as they're saying it is, it wouldn't be doing so well.", "other"),
    Example("I had friends that watched it every day it was out in theaters, every damn day", "other"),
    Example("You’re not missing anything.", "other"),
    Example("In 2009, it was crazy to see a movie look that good in theatre", "other"),
]
