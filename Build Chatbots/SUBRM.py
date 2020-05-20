import re 

text = "<p>    This is a paragraph</p>" 

result = re.sub(r'<.?p>', '', text)

print(result) 
#    This is a paragraph


#let’s remove the whitespace from the beginning of the text. The whitespace consists of four spaces.

import re 

text = "    This is a paragraph" 

result = re.sub(r'\s{4}', '', text)

print(result)