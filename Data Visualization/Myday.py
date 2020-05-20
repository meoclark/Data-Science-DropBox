from matplotlib import pyplot as plt
# This Pie Chart will describe my activities in a day during the lockdown

activities = ["Learning","Chores","Sleep","TV : news,movies","Mobile Games","Food","Social Media & Surfing the Net","Others"]
hours_spent = [11,0.3,5,1,4,0.2,2,0.5]

plt.pie(hours_spent,labels = activities,autopct = "%0.1f%%")
#plt.legend(activities)
plt.title("My Activities within 24Hrs of a Day.{MEO}")
plt.show()