import spacy
from transformers import pipeline
from googletrans import Translator
translator = Translator()
import nltk

punc=['.',',','?','!',';',':']
sentence="this is a test, and I hope it words. this is another test."
temp=''
final=''

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
    "sona":["sleep","gold"],
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

def disambiguate(word, context, translations):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    context = [lemmatizer.lemmatize(w) for w in context]  

    from nltk.corpus import wordnet as wn
    best_translation = None
    max_similarity = 0

    for translation in translations:
        translation_synsets = wn.synsets(translation)
        for context_word in context:
            context_synsets = wn.synsets(context_word)

            for translation_synset in translation_synsets:
                for context_synset in context_synsets:                     
                    similarity = translation_synset.path_similarity(context_synset) 

                    if similarity and similarity > max_similarity:  
                        max_similarity = similarity
                        best_translation = translation 

    return best_translation if best_translation else translations[0] 

def process_sentence(sentence):
    tokens = preprocess(sentence)
    ner_model = spacy.load('en_core_web_sm')  
    translated_tokens = []

    for token in tokens:
        if (ner_model(token).ents) and (token not in ner_exceptions): 
            translated_tokens.append(token)
        else:
            translation = translate_word(token)
            if isinstance(translation, str):
                best_translation = translation
            else:
                best_translation = token

            translated_tokens.append(best_translation) 
    

    new_translated_tokens = []
    for token in translated_tokens:
        if (not ner_model(token).ents) or (token in ner_exceptions): 
            translation = translate_word(token)
            if not isinstance(translation, str):
                best_translation = disambiguate(token, translated_tokens, translation)
            else:
                best_translation = token

            new_translated_tokens.append(best_translation) 



    final_translation=" ".join((new_translated_tokens))
    return final_translation


hinglish_sentence = "Ye video bahut funny hai, but mujhe sona hai because I am tired and want to rest."


for char in hinglish_sentence:
    if char in punc:
        final+=process_sentence(temp);
        temp='';
        final+=char;
        final+=' ';
    else:
        temp=temp+char;

print(final) 



#fixing grammar and also using conjunction last part