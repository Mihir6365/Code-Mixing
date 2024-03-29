from googletrans import Translator
import spacy
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import ttk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from modules import math_preprocess


tokenizer = AutoTokenizer.from_pretrained(
    "prithivida/grammar_error_correcter_v1")
model = AutoModelForSeq2SeqLM.from_pretrained(
    "prithivida/grammar_error_correcter_v1")
nlp = spacy.load('en_core_web_sm')


hinglish_dict = set()
with open('hinglish_words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        hinglish_dict.add(word)


def find_indices(sentence, first_word, last_word):
    start_index = sentence.find(first_word)
    if start_index == -1:
        return

    end_index = sentence.rfind(last_word)
    if end_index == -1:
        return

    return start_index, end_index + len(last_word) - 1


def hinglish_to_english(text):
    translator = Translator()
    translated = translator.translate(text, src='hi', dest='en')
    return translated.text


def analyze_text(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    tokens = [token.text for token in doc]
    return entities, tokens


def extract_pos_tags(text):
    doc = nlp(text)
    pos_tags = [(token.text, token.pos_) for token in doc]
    return pos_tags


def extract_dependencies(text):
    doc = nlp(text)
    dependencies = [(token.text, token.dep_) for token in doc]
    return dependencies


def lemmatize_text(text):
    doc = nlp(text)
    lemmas = [token.lemma_ for token in doc]
    return lemmas


def remove_stopwords(text):
    doc = nlp(text)
    filtered_words = [token.text for token in doc if not token.is_stop]
    return filtered_words


def translate_back_to_hindi(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='hi')
    return translated.text


def fix_grammar(sentence):
    phrases = sentence
    tokenized_phrases = tokenizer(phrases, return_tensors='pt', padding=True)
    corrections = model.generate(**tokenized_phrases)
    corrections = tokenizer.batch_decode(corrections, skip_special_tokens=True)
    for i in range(len(corrections)):
        original, correction = phrases[i], corrections[i]
        print('original: ', original)
        print('correction: ', correction)
        return (f'{correction}')


def replace_substring(string, new_substring, start_index, end_index):
    return string[:start_index] + new_substring + string[end_index:]


root = tk.Tk()
root.title("CODE MIXING FIX")
root.geometry("1000x1000")


def perform_operation():
    user_input = input_text.get("1.0", "end-1c")
    mixed_sentence = user_input
    words = mixed_sentence.split()

    hinglish_part = []
    in_hinglish = False

    first = '~'
    last = '~'
    firstflag = 1
    for word in words:
        if word in hinglish_dict:
            if firstflag:
                first = word
                firstflag = 0
            last = word
            hinglish_part.append(word)

    (firstindex, lastindex) = find_indices(mixed_sentence, first, last)
    hinglish = (' '.join(hinglish_part))
    # nltk.download('vader_lexicon')
    entities, tokens = analyze_text(hinglish)
    pure_english_sentence = hinglish_to_english(hinglish)
    pos_tags = extract_pos_tags(pure_english_sentence)
    dependencies = extract_dependencies(pure_english_sentence)
    lemmas = lemmatize_text(pure_english_sentence)
    filtered_words = remove_stopwords(pure_english_sentence)
    translated_back_to_hindi = translate_back_to_hindi(pure_english_sentence)
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(pure_english_sentence)
    pure_english_sentence = hinglish_to_english(hinglish)
    translated = fix_grammar(pure_english_sentence)
    new_string = replace_substring(
        mixed_sentence, translated, firstindex, lastindex+1)
    temp_answer = (math_preprocess.process(user_input))
    if temp_answer != 0:
        print(temp_answer)
        output_label2.config(text=f"{temp_answer}")
    else:
        print(new_string)
        output_label2.config(text=f"{new_string}")


style = ttk.Style(root)
style.theme_use("clam")

label = ttk.Label(root, text="Enter input:")
label.pack(pady=10)

input_text = tk.Text(root, height=5, width=40)
input_text.pack()

button = ttk.Button(root, text="Perform Operation", command=perform_operation)
button.pack(pady=10)

output_label = ttk.Label(root, text="Sample Output: ")
output_label.pack(pady=10)
output_label2 = ttk.Label(root)
output_label2.pack(pady=10)

root.mainloop()

