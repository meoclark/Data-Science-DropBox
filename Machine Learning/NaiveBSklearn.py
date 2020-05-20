from reviews import counter, training_counts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

review = "This crib was perfect great excellent amazing great"
review_counts = counter.transform([review])
classifier = MultinomialNB()
training_labels =  [0] * 1000 + [1] * 1000 
classifier.fit(training_counts,training_labels)
pred = classifier.predict(review_counts)
print(pred)
print(classifier.predict_proba(review_counts))