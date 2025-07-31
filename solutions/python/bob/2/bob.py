def response(hey_bob):
    sentence = hey_bob.strip()
    if sentence.endswith("?") and sentence.isupper():
        return "Calm down, I know what I'm doing!"
    
    if sentence.endswith("?"):
        return "Sure."

    if sentence.isupper():
        return "Whoa, chill out!"
    
    if sentence == "":
        return "Fine. Be that way!"
    
    return "Whatever."