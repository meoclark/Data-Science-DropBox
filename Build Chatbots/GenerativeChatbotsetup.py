class ChatBot:
  
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")

  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop")
  
  def start_chat(self):
    user_response = input("Hi, I'm a chatbot trained on dialog from The Princess Bride. Would you like to chat with me?\n")
    
    if user_response in self.negative_responses:
      print("Ok, have a great day!")
      return
    
    self.chat(user_response)
  
  def chat(self, reply):
    while not self.make_exit(reply):
      # change this line below:
      reply = input(self.generate_response(reply))
    
  # define .generate_response():
  def generate_response(self, user_input):
    return "Cool!\n"
  
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if exit_command in reply:
        print("Ok, have a great day!")
        return True
      
    return False
  
# instantiate your ChatBot below:
chatty_mcchatface = ChatBot()
print(chatty_mcchatface.generate_response("I'd love to chat."))