import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Load the dataset
file_path = r"C:\Users\user\Downloads\myexcel - myexcel.csv.csv"
data = pd.read_csv(file_path)

# Preprocessing: Replace the 'Height' column with random numbers between 150 and 180
np.random.seed(42)  # For reproducibility
data['Height'] = np.random.randint(150, 181, size=len(data))

# Task 1: Distribution of employees across teams
team_distribution = data['Team'].value_counts()
team_percentage = (team_distribution / len(data)) * 100

# Combine into a DataFrame
team_stats = pd.DataFrame({
    'Team': team_distribution.index,
    'Count': team_distribution.values,
    'Percentage': team_percentage.values
}).reset_index(drop=True)

# Visualization for Task 1
plt.figure(figsize=(12, 8))
team_stats_sorted = team_stats.sort_values(by='Count', ascending=False)
plt.bar(team_stats_sorted['Team'], team_stats_sorted['Count'], color='skyblue')
plt.xticks(rotation=90)
plt.xlabel('Teams')
plt.ylabel('Number of Employees')
plt.title('Distribution of Employees Across Teams')
plt.tight_layout()
plt.show()

# Task 2: Segregation of employees by position
position_distribution = data['Position'].value_counts()

# Create a DataFrame
position_stats = pd.DataFrame({
    'Position': position_distribution.index,
    'Count': position_distribution.values
}).reset_index(drop=True)

# Visualization for Task 2
plt.figure(figsize=(8, 6))
plt.bar(position_stats['Position'], position_stats['Count'], color='orange')
plt.xlabel('Position')
plt.ylabel('Number of Employees')
plt.title('Segregation of Employees by Position')
plt.tight_layout()
plt.show()

# Task 3: Predominant age group among employees
bins = [0, 25, 30, 35, 100]
labels = ['<25', '25-30', '31-35', '>35']
data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)
age_group_distribution = data['Age Group'].value_counts()

# Create a DataFrame
age_group_stats = pd.DataFrame({
    'Age Group': age_group_distribution.index,
    'Count': age_group_distribution.values
}).reset_index(drop=True)

# Visualization for Task 3
plt.figure(figsize=(8, 6))
plt.bar(age_group_stats['Age Group'], age_group_stats['Count'], color='green')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees')
plt.title('Predominant Age Group Among Employees')
plt.tight_layout()
plt.show()

# Task 4: Highest salary expenditure by team and position
team_salary = data.groupby('Team')['Salary'].sum().sort_values(ascending=False)
position_salary = data.groupby('Position')['Salary'].sum().sort_values(ascending=False)

# Visualization for salary expenditure by team
plt.figure(figsize=(12, 8))
team_salary_sorted = team_salary.sort_values(ascending=False)
plt.bar(team_salary_sorted.index, team_salary_sorted.values, color='purple')
plt.xticks(rotation=90)
plt.xlabel('Teams')
plt.ylabel('Total Salary Expenditure ($)')
plt.title('Salary Expenditure by Team')
plt.tight_layout()
plt.show()

# Visualization for salary expenditure by position
plt.figure(figsize=(8, 6))
plt.bar(position_salary.index, position_salary.values, color='red')
plt.xlabel('Position')
plt.ylabel('Total Salary Expenditure ($)')
plt.title('Salary Expenditure by Position')
plt.tight_layout()
plt.show()

# Task 5: Correlation between age and salary
plt.figure(figsize=(8, 6))
plt.scatter(data['Age'], data['Salary'], alpha=0.7, color='blue')
plt.xlabel('Age')
plt.ylabel('Salary ($)')
plt.title('Correlation Between Age and Salary')
plt.tight_layout()
plt.show()
