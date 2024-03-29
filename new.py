import torch
from transformers import MarianMTModel, MarianTokenizer

# Replace this with a suitable model name if you find one better
model_name = "facebook/m2m100_418M"

# Load the model and tokenizer
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Function for translation
def translate_hinglish(text):
  input_ids = tokenizer.encode(text, return_tensors="pt")
  output = model.generate(input_ids)
  decoded_text = tokenizer.decode(output[0], skip_special_tokens=True)
  return decoded_text

# Example usage
hinglish_sentence = "Aaj ka din bohot acha tha."
translation = translate_hinglish(hinglish_sentence)
print(translation)
