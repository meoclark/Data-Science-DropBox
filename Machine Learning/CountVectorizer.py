#To begin, we need to create a CountVectorizer and teach it the vocabulary of the training set. This is done by calling the .fit() method.
vectorizer = CountVectorizer()

vectorizer.fit(["Training review one", "Second review"])

#The .transform() method takes a list of strings and will transform those strings into counts of the trained words
counts = vectorizer.transform(["one review two review"])

#But how did we know that the 2 corresponded to review? You can print vectorizer.vocabulary_ to see the index that each word corresponds to. It might look something like this:
{'one': 1, 'Training': 2, 'review': 0, 'Second': 3}



from reviews import neg_list, pos_list
from sklearn.feature_extraction.text import CountVectorizer

review = "This crib was amazing"

counter = CountVectorizer()
counter.fit(neg_list + pos_list)
print(counter.vocabulary_)

review_counts = counter.transform([review])
print(review_counts.toarray())

training_counts = counter.transform(neg_list + pos_list)