hinglish_dict = {
    'kya', 'ho', 'nahi', 'hai', 'achha', 'aaj', 'ka', 'din', 'bura', 'tha', 'khuch', 'hua'
}

mixed_sentence = "I am sad because aaj ka din bura tha ."

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
        
        

print(find_indices(mixed_sentence, first, last))
print("Hinglish part:", ' '.join(hinglish_part))
