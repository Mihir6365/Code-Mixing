import nltk
nltk.download('wordnet')


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


word = "sona"
context = ["expensive", "rich",]
translations = ["gold", "sleep"]

disambiguated_word = disambiguate(word, context, translations)
print(disambiguated_word)  
