import spacy

# load word embedding model
nlp = spacy.load("en")

# define word embedding vectors
happy_vec = nlp('happy').vector
sad_vec = nlp('sad').vector
angry_vec = nlp('angry').vector
print(happy_vec,sad_vec,angry_vec)
vector_length = len(happy_vec)



# find vector length here

