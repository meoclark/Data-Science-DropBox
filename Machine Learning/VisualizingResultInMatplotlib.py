import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]

y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

lm = LinearRegression()

model=lm.fit(x_train, y_train)

y_predict = lm.predict(x_test)

plt.scatter(y_test , y_predict, alpha = 0.4)
plt.xlabel("Prices: $" + str(x_train))
plt.ylabel("Predicted prices: " + str(y_train))
plt.title("Actual Rent vs Predicted Rent")
plt.show()

# Comment the code below before running this script

#steps below
# Create a scatter plot
plt.scatter(x, y, alpha=0.4)

# Create x-axis label and y-axis label
plt.xlabel("the x-axis label")
plt.ylabel("the y-axis label")

# Create a title
plt.title("title!")

# Show the plot
plt.show()

#SScatter plots
plt.scatter(df[['size_sqft']], df[['rent']], alpha = 0.4)
plt.scatter(df[['min_to_subway']], df[['rent']], alpha=0.4)
plt.scatter(df[['bedrooms']], df[['rent']], alpha=0.4)
plt.scatter(df[['no_fee']], df[['rent']], alpha=0.4)