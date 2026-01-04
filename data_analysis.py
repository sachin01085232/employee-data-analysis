import pandas as pd
import numpy as np

df = pd.read_csv('clean_dataset.csv')

# Q Dept-wise avg salary
avg_salary = df[df['dept_id'] != 'Unknown'].groupby('dept_id')['salary'].mean()

print('Here we Have the average salary by department wise',avg_salary)

# Q Top 3 highest paid employees

top_3 = df.sort_values(by='salary',ascending=False).head(3)
print(top_3)

# INSIGHTS
# I analyzed salary data and identifyed employess  with the highest compensation .
# We have karan malhotra with highest salary so it indicate a senior level position 
# with reponsibility

# Q Employees joined after 2022
df['join_date'] = pd.to_datetime(df['join_date'],errors='coerce')
join_2022 = df[df['join_date']>pd.Timestamp('2022-01-01')]
print(join_2022)
 
 # iNSIGHTS
 # The Analysis shows employees who joined organisation after 2022 , representing the recent hires.

# Best performance employees

Best_performance = df.sort_values(by='performance',ascending=False).head(3)
print(Best_performance)
 
 # This employees is the top performer and has made a strong contribution to the organization

 # Q lowest #paid employees

lowest = df.sort_values('salary',ascending=True).head(3)
print(lowest)

# This analysis shows the  lowest 3  paid employees, indicating entry level or junior level role
# within the organization




