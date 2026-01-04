import pandas as pd
import numpy as np 

df = pd.read_csv('employees_real_world.csv')

# Replaced invalid salaries (<=0) with NaN
df.loc[df['salary']<=0 , 'salary'] = None

# Filled missing department IDs with 'unknown'
df['dept_id'].fillna('unknown',inplace=True)

# Converted join_date to datetime format
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')

# Removed duplicate employee records (keeping first occurrence)
df = df.drop_duplicates(subset='emp_id', keep='first')

#Imputed missing salary and performance values using department-level averages
df['salary'] = df.groupby('dept_id')['salary'].transform(
    lambda x:x.fillna(x.mean())
)

df['performance'] = df.groupby('dept_id')['performance'].transform(
    lambda x:x.fillna(x.mean())

)

 # Handled invalid performance ratings (outside 1–5 range)
df.loc[
    (df['performance'] < 1) | (df['performance'] > 5),
    'performance'
] = np.nan

# Removed future joining dates to maintain data integrity
today_date = pd.Timestamp.today()

df.loc[df['join_date'] > today_date , 'join_date'] = pd.NaT

print(df)

# Cleaned dataset saved as 'clean_dataset.csv'

df.to_csv('clean_dataset.csv')
