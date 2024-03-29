hinglish_dict = {
    'kya', 'ho', 'nahi', 'hai', 'achha', 'aaj', 'ka', 'din', 'bura', 'tha', 'khuch', 'hua'
}

mixed_sentence = "I am sad because aaj ka din bura tha ."

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  
tokenizer = AutoTokenizer.from_pretrained("prithivida/grammar_error_correcter_v1")

model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/grammar_error_correcter_v1")


def find_indices(sentence, first_word, last_word):
    start_index = sentence.find(first_word)
    if start_index == -1:
        print(f"The word '{first_word}' is not found in the sentence.")
        return

    end_index = sentence.rfind(last_word)
    if end_index == -1:
        print(f"The word '{last_word}' is not found in the sentence.")
        return

    return start_index, end_index + len(last_word) - 1

words = mixed_sentence.split()

hinglish_part = []
in_hinglish = False

first='~'
last='~'
firstflag=1
for word in words:
    if word in hinglish_dict:
        if firstflag:
            first=word
            firstflag=0
        last=word
        hinglish_part.append(word)

(firstindex,lastindex)=find_indices(mixed_sentence, first, last)
hinglish=(' '.join(hinglish_part))


from googletrans import Translator
import spacy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import requests


nltk.download('vader_lexicon')

nlp = spacy.load('en_core_web_sm')


def hinglish_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='hi', dest='en')
    return translated.text


def analyze_text(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    tokens = [token.text for token in doc]
    return entities, tokens

entities, tokens = analyze_text(hinglish)

pure_english_sentence = hinglish_to_english(hinglish)

def extract_pos_tags(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags

pos_tags = extract_pos_tags(pure_english_sentence)

def extract_dependencies(text):
    doc = nlp(text)
    dependencies = [(token.text, token.dep_) for token in doc]
    return dependencies

dependencies = extract_dependencies(pure_english_sentence)

def lemmatize_text(text):
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return lemmas

lemmas = lemmatize_text(pure_english_sentence)

def remove_stopwords(text):
    doc = nlp(text)
    filtered_words = [token.text for token in doc if not token.is_stop]
    return filtered_words

filtered_words = remove_stopwords(pure_english_sentence)

def translate_back_to_hindi(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return translated.text

translated_back_to_hindi = translate_back_to_hindi(pure_english_sentence)

sid = SentimentIntensityAnalyzer()
sentiment_score = sid.polarity_scores(pure_english_sentence)

print("Entities:", entities)
print("Tokens:", tokens)
print("Part of speech tags:", pos_tags)
print("Dependencies:", dependencies)
print("Lemmas:", lemmas)
print("Filtered words:", filtered_words)
print("Translated back to Hindi:", translated_back_to_hindi)
print("Sentiment Score:", sentiment_score)
pure_english_sentence = hinglish_to_english(hinglish)

print("FIRST OUTPUT IS ====================================================================>>>>>")
print(pure_english_sentence)



print("SECOND OUTPUT IS ====================================================================>>>>>")
def fix_grammar(sentence):
        phrases = sentence
        tokenized_phrases = tokenizer(phrases, return_tensors='pt', padding=True)
        corrections = model.generate(**tokenized_phrases)
        corrections = tokenizer.batch_decode(corrections, skip_special_tokens=True)
        for i in range(len(corrections)):
           original, correction = phrases[i], corrections[i]
           print('correction: ', correction)
           return correction;

translated=fix_grammar(pure_english_sentence)


def replace_substring(string, new_substring, start_index, end_index):
    return string[:start_index] + new_substring + string[end_index:]

new_string = replace_substring(mixed_sentence, translated, firstindex, lastindex+1)
print(new_string)