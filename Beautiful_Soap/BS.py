""" 
Rules of Scraping
When we scrape websites, we have to make sure we are following some guidelines so that we are treating the websites and their owners with respect.

Always check a website’s Terms and Conditions before scraping. Read the statement on the legal use of data. Usually, the data you scrape should not be used for commercial purposes.

Do not spam the website with a ton of requests. A large number of requests can break a website that is unprepared for that level of traffic. As a general rule of good practice, make one request to one webpage per second.

If the layout of the website changes, you will have to change your scraping code to follow the new structure of the site."""

# Requests

import requests

webpage = requests.get('https://www.codecademy.com/articles/http-requests')
print(webpage.text)

webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
print(webpage)


# The BeautifulSoup Object
webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")
print(soup)
 # There are other options, like "lxml" and "html5lib" apart from "html.parser"


# Object Types
soup = BeautifulSoup('<div id="example">An example div</div><p>An example p tag</p>')
print(soup.div)
#Would produce output that looks like:
   #<div id="example">An example div</div>
# You can get the name of the tag using .name and a dictionary representing the attributes of the tag using .attrs:

print(soup.div.name)
print(soup.div.attrs)
  #div
  #{'id': 'example'}
# NavigableStrings are the pieces of text that are in the HTML tags on the page.
print(soup.div.string)
    # An example div
# Note pay attention to the name of the tag you want to get. it is usually in the beginning of the tag
print(soup.p)
print(soup.p.string)


# Navigating by Tags
print(soup.span)
print(soup.h1)
for child in soup.ul.children:
    print(child)

for parent in soup.li.parents:
    print(parent)

for child in soup.div.children:
  print(child)



# Find All

# If we want to find all of the occurrences of a tag, instead of just the first one, we can use .find_all().
#  With .find_all(), we can use regexes, attributes, or even functions to select HTML elements more intelligently.

# This function can take in just the name of a tag and returns a list of all occurrences of that tag.
print(soup.find_all("h1"))

# Using Regex
# What if we want every <ol> and every <ul> that the page contains? We can select both of these types of elements with a regex in our .find_all():

import re
soup.find_all(re.compile("[ou]l"))
# What if we want all of the h1 - h9 tags that the page contains? Regex to the rescue again!
import re
soup.find_all(re.compile("h[1-9]"))

# Using Lists
soup.find_all(['h1', 'a', 'p'])
# Using Attributes
soup.find_all(attrs={'class':'banner'})
soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})
# Using A Function
# If our selection starts to get really complicated, we can separate out all of the logic that we’re using to choose a tag into its own function. Then, we can pass that function into .find_all()!
def has_banner_class_and_hello_world(tag):
    return tag.attr('class') == "banner" and tag.string == "Hello world"

soup.find_all(has_banner_class_and_hello_world)

turtle_links = []
for elements in soup.find_all("a"):
  turtle_links.append(elements)

print(turtle_links)


# Select for CSS Selectors
# If we wanted to select all of the elements that have the class 'recipeLink', we could use the command
soup.select(".recipeLink")

# If we wanted to select the element that has the id 'selected', we could use the command:
soup.select("#selected")

# Let’s say we wanted to loop through all of the links to these funfetti recipes that we found from our search.

for link in soup.select(".recipeLink > a"):
  webpage = requests.get(link)
  new_soup = BeautifulSoup(webpage)

#This loop will go through each link in each .recipeLink div and create a soup object out of the webpage it links to.

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  #Add your code here:
  turtle_name = turtle.select(".name")[0]
  turtle_data[turtle_name] = []
  
print(turtle_data)


#  Reading Text
soup.get_text()
# 'Search Results for: Funfetti'
soup.get_text('|')
# 'Search Results for: |Funfetti'

import requests
from bs4 import BeautifulSoup

prefix = "https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/"
webpage_response = requests.get('https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them"
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0].get_text()
  
  stats = turtle.find("ul")
  stats_text = stats.get_text("|")
  turtle_data[turtle_name] = stats_text.split("|")
    

  
turtle_df = pd.DataFrame.from_dict(turtle_data, orient='index')

print(turtle_df.head())






















