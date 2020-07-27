import spacy

nlp = spacy.load('en_core_web_sm')

sent = nlp("set a reminder to wash dishes at 3 am")
# iterating over tokens
print("TOKENS: ")
for token in sent:
    print(token.text, token.pos_, token.has_vector)
    # print(token.text, token.pos_, token.dep_, token.head.text)

# iterating over tokens
print("ENTITIES: ")
for ent in sent.ents:
    print(ent.text, ent.label_)

# iterating over noun chunks
print("NOUN CHUNKS: ")
for chunk in sent.noun_chunks:
    print(chunk.text)
