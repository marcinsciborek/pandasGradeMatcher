import pandas as pd

df = pd.DataFrame({
    'name': ['Andrew', 'Beth', 'Carol', 'John', 'Larry', 'Lucas', 'Rick'],
    'points': [42, 35, 50, 60, 75, 85, 100]
})

print(df, '\n')

point_range = [0, 20, 40, 60, 75, 85, 101]
labels = ['F', 'E', 'D', 'C', 'B', 'A']

df['grade'] = pd.cut(df['points'], bins=point_range, labels=labels, right=False)
print(df)

df.to_csv('StudentsScores.csv')
