#Term frequency-inverse document frequency is a numerical statistic used to indicate how important a word is to each document in a collection of documents, or a corpus.
#When applying tf-idf to a corpus, each word is given a tf-idf score for each document, representing the relevance of that word to the particular document.
# A higher tf-idf score indicates a term is more important to the corresponding document.

import seaborn as sns 
from preprocessing import preprocess_text
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# sample documents
document_1 = "This is a sample sentence!"
document_2 = "This is my second sentence."
document_3 = "is this my third sentence?"

# corpus of documents
corpus = [document_1, document_2, document_3]

# preprocess documents
processed_corpus = [preprocess_text(doc) for doc in corpus]

# initialize and fit TfidfVectorizer
vectorizer = TfidfVectorizer(norm=None)
tf_idf_scores = vectorizer.fit_transform(processed_corpus)

# get vocabulary of terms
feature_names = vectorizer.get_feature_names()
corpus_index = [n for n in processed_corpus]

# create pandas DataFrame with tf-idf scores
df_tf_idf = pd.DataFrame(tf_idf_scores.T.todense(), index=feature_names, columns=corpus_index)
print(df_tf_idf)