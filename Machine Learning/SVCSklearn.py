from sklearn.svm import SVC
from graph import points, labels
classifier = SVC(kernel = "linear")
classifier.fit(points,labels)
print(classifier.predict([[2,4],[6,7]]))