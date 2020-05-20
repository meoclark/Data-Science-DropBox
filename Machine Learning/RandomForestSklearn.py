def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
from cars import training_points, training_labels, testing_points, testing_labels
import warnings
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(random_state = 0,n_estimators = 2000)
classifier.fit(training_points,training_labels)
pred = classifier.predict(testing_points)
print(classifier.score(testing_points,testing_labels))