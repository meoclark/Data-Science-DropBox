# Chocolate Scraping with Beautiful Soup
# Project Chocolate Scraping with Beautiful Soup

import seaborn as sns
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

webpage_response = requests.get("https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html")
webpage = webpage_response.content
soup = BeautifulSoup(webpage,"html.parser")
#print(soup)
soup.find_all(attrs={"class": "Rating"})

ratings = []
for elements in soup.find_all(attrs={"class": "Rating"})[1:]:
  ratings.append(float(elements.get_text()))

plt.hist(ratings)
plt.show()

soup.select(".Company")

companies = []
for company in soup.select(".Company")[1:]:
  companies.append(company.get_text())

cocoa_percents = []
cocoa_percent_tags = soup.select(".CocoaPercent")

for td in cocoa_percent_tags[1:]:
  percent = float(td.get_text().strip('%'))
  cocoa_percents.append(percent)

d = {"Company": companies, "Ratings": ratings, "CocoaPercentage":cocoa_percents}
cacao_df = pd.DataFrame.from_dict(d)

mean_vals = cacao_df.groupby("Company").Ratings.mean()
ten_best = mean_vals.nlargest(10)
print(ten_best)

plt.clf()
plt.scatter(cacao_df.CocoaPercentage, cacao_df.Ratings)

z = np.polyfit(cacao_df.CocoaPercentage, cacao_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(cacao_df.CocoaPercentage, line_function(cacao_df.CocoaPercentage), "r--")
plt.show()












