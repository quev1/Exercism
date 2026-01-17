def translate(text):
    voyels = 'aeiou'

    def translate_word(word):
        # Rule 1
        if word[0] in voyels or word.startswith("xr") or word.startswith("yt"):
            return word + "ay"
        
        # Rule 3
        if word.startswith("qu") or ("qu" in word and all(c not in voyels for c in word[:word.find("qu")])):
            split_index = word.find("qu") + 2
            return word[split_index:] + word[:split_index] + "ay"
        
        # Rule 4
        if "y" in word and word.index("y") > 0 and all(c not in voyels for c in word[:word.index("y")]):
            split_index = word.index("y")
            return word[split_index:] + word[:split_index] + "ay"
        
        # Rule 2
        for i, char in enumerate(word):
            if char in voyels:
                split_index = i
                break
        return word[split_index:] + word[:split_index] + "ay"

    # Handle multiple words
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)
