import re

def is_conjunction_part_of_word(text, conjunction):
  return text.find(conjunction) > 0 and text.rfind(conjunction) < len(text) - 1

def process_sentence_fragments(text):
    return text.upper() 

def split_and_process_sentence(sentence):
  pattern = r"(\s*(?:and|but|or|for|nor|so|yet)\s*)|(\s*[:,\.!;?]|\s*)"
  fragments = re.split(pattern, sentence)
  fragments = [f for f in fragments if f] 

  processed_fragments = []
  for fragment in fragments:
      processed_fragments.append(process_sentence_fragments(fragment))

  return "".join(processed_fragments)

sentence = "This is a test sentence and it has some punctuation! Let's split it."
result = split_and_process_sentence(sentence)
print(result) 