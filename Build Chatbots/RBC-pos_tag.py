from nltk import pos_tag
user_message = ["i", "ordered", "two", "t-shirts", "this", "past", "weekend", "when","will","my","package","be", "shipped"]

#define `tagged_user_message` here
tagged_user_message = pos_tag(user_message)
print(tagged_user_message)

def extract_nouns(tagged_message):
  message_nouns = list()
  for token in tagged_message:
    if "NN" in token[1]:
      message_nouns.append(token[0])
  return message_nouns

#define `user_message_nouns` here
user_message_nouns = extract_nouns(tagged_user_message)

print(user_message_nouns)
