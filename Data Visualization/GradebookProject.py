last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]
gradebook = list(zip(subjects,grades))
#print(gradebook)
subjects.append("computer science")
grades.append(100)
gradebook.append(("visual arts", 93))
#print(gradebook)
full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)


#List Comprehension
temperatures = [-5, 29, 26, -7, 1, 18, 12, 31]
temperatures_adjusted = [temp + 20 for temp in temperatures]
# temperatures_adjusted is now [15, 49, 46, 13, 21, 38, 32, 51]

x_values_1 = [2*index for index in range(5)]
# [0.0, 2.0, 4.0, 6.0, 8.0] 
x_values_2 = [2*index + 0.8 for index in range(5)]
# [0.8, 2.8, 4.8, 6.8, 8.8]

x_values_midpoints = [(x1 + x2)/2.0 for (x1, x2) in zip(x_values_1, x_values_2)]
# [0.4, 2.4, 4.4, 6.4, 8.4]

zip([1, 2, 3], [4, 6, 8])
#yields:

[(1, 4), (2, 6), (3, 8)]



