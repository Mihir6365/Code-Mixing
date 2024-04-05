import transformers

# Load BERT model and tokenizer
model_name = "bert-base-uncased"  
tokenizer = transformers.BertTokenizer.from_pretrained(model_name)
model = transformers.BertForMaskedLM.from_pretrained(model_name) 

def rearrange_with_bert(jumbled_sentence):
    words = jumbled_sentence.split()

    best_rearrangement = jumbled_sentence  # Initialize 
    best_score = -float('inf')  # Track the best score so far

    # Generate rearrangements (simple example, you can get more sophisticated)
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            rearrangement = words.copy()
            rearrangement[i], rearrangement[j] = rearrangement[j], rearrangement[i]
            rearrangement_str = " ".join(rearrangement)

            # Mask a word and get BERT's suggestions
            masked_sentence = rearrangement_str.replace(words[i], "<mask>", 1) 
            suggestions = get_bert_suggestion(masked_sentence)

            # Calculate score (heuristic, you might improve this)
            score = suggestions.index(words[i]) if words[i] in suggestions else 0

            if score > best_score:
                best_score = score
                best_rearrangement = rearrangement_str

    return best_rearrangement

def get_bert_suggestion(sentence, masked_token="<mask>"):
    inputs = tokenizer(sentence, return_tensors="pt")
    masked_index = inputs['input_ids'][0].tolist().index(tokenizer.mask_token_id)
    outputs = model(**inputs)
    predictions = outputs.logits[0, masked_index].softmax(dim=0)
    top_prediction_tokens = tokenizer.convert_ids_to_tokens(predictions.topk(5).indices.tolist())
    return top_prediction_tokens

# Example usage
jumbled_sentence = "very I hungry am"
result = rearrange_with_bert(jumbled_sentence)
print(f"Original: {jumbled_sentence}")
print(f"Rearrangement Suggestion: {result}") 
