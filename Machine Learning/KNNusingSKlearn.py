#So i will use this for reference. This how u use KNN with SKlearn
#Import your data set and labels
from movies import movie_dataset, labels
#import KNN from  SKlearn
from sklearn.neighbors import KNeighborsClassifier
#set up your classifier and your number of k
classifier = KNeighborsClassifier(n_neighbors=5)
#train your classifier using the .fit() it takes two parameters,your datapoints and your label associated with it.
classifier.fit(movie_dataset, labels)
#introduce the new or unknown points you want to predict.
unknown = [.45, .2, .5], [.25, .8, .9],[.1, .1, .9]
#predict the unknown point using the .predict
guess = classifier.predict(unknown)
print(guess)

# Egbo Moses aka MEO