#1. Iterate over each item in the dictionary
def match_reply(self, reply):
  for key, values in self.matching_phrases.items():
    for regex_pattern in values:

#2. Check if user utterance matches a regular expression pattern
 def match_reply(self, reply):
  for key, values in self.matching_phrases.items():
    for regex_pattern in values:

      found_match = re.match(regex_pattern, reply)
# 3. Respond if a match was made

def match_reply(self, reply):
 for key, values in self.matching_phrases.items():
	for regex_pattern in values:
  	found_match = re.match(regex_pattern, reply)

  if found_match:
    reply = input("Great! I found a matching regular expression. Isn't that cool?")
    return reply

#4. Respond if a match was not made
def match_reply(self, reply):
  for key, values in self.matching_phrases.items():
    for regex_pattern in values:
      found_match = re.match(regex_pattern, reply)
      if found_match:
        reply = input("Great! I found a matching regular expression. Isn't that cool?")
        return reply

    return input("Can you please ask your questions a different way? ")

 #5. Call .match_reply() after every user response
 def handle_conversation(self, reply):
  while not make_exit(reply):
    reply = match_reply(reply)