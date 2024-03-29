def translate_hinglish(hinglish_text):
    hinglish_dict = {
        "Kya": "what",
        "haan": "yes",
        "nahi": "no",
        "Theek": "okay",
        "achcha": "good",
        "hai":"is",
        "haal":"state",
        "hu":"am",
        "aaj":"today",
        "din":"day",
        "bura":"bad",
        "tha":"was"
    }

    words = hinglish_text.split()
    translated_words = []

    for word in words:
        if word in hinglish_dict:
            translated_words.append(hinglish_dict[word])
        else:
            translated_words.append(word)  

    return " ".join(translated_words)

hinglish_sentence = "aaj ka din bura tha ."
translated_sentence = translate_hinglish(hinglish_sentence)
print(translated_sentence) 
