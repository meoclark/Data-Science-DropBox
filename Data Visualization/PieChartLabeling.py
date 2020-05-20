from matplotlib import pyplot as plt

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

# You can add label using Legend or including the parameter labels in the pie parameter. also use autopct to add the percentage. 0.1 for 1 decimal place.
plt.pie(payment_method_freqs,labels= payment_method_names,autopct = '%0.1f%%')
plt.axis('equal')
plt.legend(payment_method_names)
plt.show()