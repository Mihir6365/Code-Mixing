import spacy
from transformers import pipeline
from googletrans import Translator
translator = Translator()

# ... (Loading of datasets, models, dictionary)

hinglish_normalization_map = {
    "bahut": "bahut",
    "bhot": "bahut",
    "bohot": "bahut",
    "kar": "kar",
    "kr": "kar",
    "raha": "raha",
    "rha": "raha",
}

hinglish_dict = {
    "achha": "good",
    "theek": "okay", 
    "haan": "yes",
    "nahi": "no",
    "kal": "tomorrow",
    "aaj": "today",
    "kya": "what",
    "kaise": "how",
    "bahut": "very",
    "chalo": "let's go",
    "Ye": "this",
    "bahut": "very",
    "hai": "is",
    "nahi": "no",
}

ner_exceptions=["hai"]
def preprocess(text):
        tokens = text.split()  
        normalized_tokens = []
        for token in tokens:
            if token in hinglish_normalization_map: 
                normalized_tokens.append(hinglish_normalization_map[token])
            else:
                normalized_tokens.append(token)
        return normalized_tokens

def translate_word(word):
    if word in hinglish_dict:
        translation = hinglish_dict[word] 
        return translation
    else:
        return translator.translate(word, dest='en').text;

# def disambiguate(word, context):
#     pos_tag = spacy_model(word)[0].tag_ 
#     return best_translation

def process_sentence(sentence):
    tokens = preprocess(sentence)
    ner_model = spacy.load('en_core_web_sm')  # Load your NER model
    translated_tokens = []

    for token in tokens:
        if (ner_model(token).ents) and (token not in ner_exceptions): 
            print("entity is ",token)  
            translated_tokens.append(token)
        else:
            translation = translate_word(token)
            best_translation = translation
            # best_translation = disambiguate(token, tokens) 
            translated_tokens.append(best_translation) 
            print(translated_tokens)

    return " ".join((translated_tokens))

# Example usage
hinglish_sentence = "Ye video bahut funny hai "
translated_sentence = process_sentence(hinglish_sentence)
print(translated_sentence) 


