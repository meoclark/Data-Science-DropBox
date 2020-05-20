import re
import random

class SupportBot:
  negative_responses = ("nothing", "don't", "stop", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

  def __init__(self):
    self.matching_phrases = {'how_to_pay_bill': [r'.*how.*pay bills.*', r'.*how.*pay my bill.*'], r'pay_bill': [r'.*want.*pay my bill.*', r'.*need.*pay my bill.*']}

  def welcome(self):
    name = input("Hi, I'm a customer support representative. Welcome to Codecademy Bank. Before we can help you, I need some information from you. What is your first name and last name? ")
    
    will_help = input(f"Ok {name}, what can I help you with? ")
    
    if will_help in self.negative_responses:
      print("Ok, have a great day!")
      return
    
    self.handle_conversation(will_help)
  
  def handle_conversation(self, reply):
    while not self.make_exit(reply):
      reply = self.match_reply(reply)
      
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("Ok, have a great day!")
        return True
      
    return False
  
  def match_reply(self, reply):
    for key, values in self.matching_phrases.items():
      for regex_pattern in values:
        found_match = re.match(regex_pattern, reply)
        if found_match:
          return input(f"We matched your utterance to {key}")
    
    return input("I did not understand you. Can you please ask your question differently?")
  
    
  
# Create a SupportBot instance
SupportConversation = SupportBot()
# Call the .welcome() method
SupportConversation.welcome()