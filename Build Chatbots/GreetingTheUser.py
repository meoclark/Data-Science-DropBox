import re
import random

class SupportBot:
  negative_responses = ("nothing", "don't", "stop", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

  def __init__(self):
    pass

  def welcome(self):
    name = input("Hi, I'm a customer support representative. Welcome to Codecademy Bank. Before we can help you, I need some information from you. What is your first name and last name? ")
    
    will_help = input(f"Okay {name}, what can I help you with?")
    
    if will_help in self.negative_responses:
      print("Okay, have a great day!")
      return
    
    return will_help

# Create a SupportBot instance
SupportConversation = SupportBot()
# Call the .welcome() method
SupportConversation.welcome()