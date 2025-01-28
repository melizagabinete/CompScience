import numpy as np
import matplotlib.pyplot as plt

# datas
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  
grades = np.array([50, 60, 65, 70, 80, 85, 90, 95, 98, 100])

# calculations
N = len(hours_studied)
sumH = np.sum(hours_studied)
sumG = np.sum(grades)
sumHH = np.sum(hours_studied**2)
sumHG = np.sum(hours_studied * grades)

# calculate slope and intercept
m = (N * sumHG - sumH * sumG) / (N * sumHH - sumH**2)
b = (sumG - m * sumH) / N

#regression line
r_line = m * hours_studied + b

#plotting the data
plt.scatter(hours_studied, grades, color='violet', label='Data points')
plt.plot(hours_studied, r_line, color='black', linestyle='--',label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Grades')
plt.title('Linear Regression Model: Hours Studied vs Grades')
plt.legend()
plt.grid(True)
plt.show()
