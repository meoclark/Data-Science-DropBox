from cars import training_points, training_labels, testing_points, testing_labels
from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(random_state = 0)
classifier.fit(training_points, training_labels)
print(classifier.score(testing_points, testing_labels))
#Can be used to check the tree depth
print(classifier.tree_.max_depth)
#Max depth can be used to prune the tree to a needed depth 
classifier = DecisionTreeClassifier(random_state = 0, max_depth = 11)