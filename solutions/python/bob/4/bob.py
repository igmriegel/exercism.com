def response(hey_bob):
    sentence = hey_bob.strip()

    if sentence.endswith("?") and sentence.isupper():
        return "Calm down, I know what I'm doing!"
    elif sentence.endswith("?"):
        return "Sure."
    elif sentence.isupper():
        return "Whoa, chill out!"
    
    if sentence == "":
        return "Fine. Be that way!"
    
    return "Whatever."