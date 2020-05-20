from preprocessing import preprocess_text
# Define create_features_dictionary() below:


training_documents = ["Five fantastic fish flew off to find faraway functions.", "Maybe find another five fantastic fish?", "Find my fish with a function please!"]


def create_features_dictionary(documents):
  features_dictionary = {}
  merged = " ".join(documents)
  tokens = preprocess_text(merged)
  index = 0
  for token in tokens:
    if  not token in features_dictionary:
      features_dictionary[token] = index
      index = 1
  return features_dictionary,tokens

print(create_features_dictionary(training_documents)[0])
