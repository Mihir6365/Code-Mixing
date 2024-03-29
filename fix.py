from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  
tokenizer = AutoTokenizer.from_pretrained("prithivida/grammar_error_correcter_v1")

model = AutoModelForSeq2SeqLM.from_pretrained("prithivida/grammar_error_correcter_v1")

phrases = [
  'How is you doing?',
  'We is on the supermarket.',
  'Hello you be in school for lecture.'
]

# Tokenize text
tokenized_phrases = tokenizer(phrases, return_tensors='pt', padding=True)

# Perform corrections and decode the output
corrections = model.generate(**tokenized_phrases)
corrections = tokenizer.batch_decode(corrections, skip_special_tokens=True)

# Print correction
for i in range(len(corrections)):
  original, correction = phrases[i], corrections[i]
  print(f'{correction}')