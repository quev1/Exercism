def response(hey_bob):
    text = hey_bob.strip()
    
    if not text:
        return "Fine. Be that way!"

    is_question = text.endswith("?")
    has_letters = any(c.isalpha() for c in text)
    is_yelling = has_letters and text.isupper()

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."

