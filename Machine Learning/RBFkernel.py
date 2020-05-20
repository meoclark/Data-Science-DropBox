from data import points, labels
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

training_data, validation_data, training_labels, validation_labels = train_test_split(points, labels, train_size = 0.8, test_size = 0.2, random_state = 100)
#rbf is the default kernel if you dont set any initial kernel.
# An rbf kernel transforms two-dimensional points into points with an infinite number of dimensions!
#We won’t get into how the kernel does this — it involves some fairly complicated linear algebra. 
#However, it is important to know about the rbf kernel’s gamma parameter.



classifier = SVC(kernel='rbf',gamma = 1)
classifier.fit(training_data,training_labels)
#the .score() method is used to test the classifier's accuracy
print(classifier.score(validation_data,validation_labels))