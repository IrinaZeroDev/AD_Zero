import pandas as pd

puple = {
    'Петя Петров': [5, 5, 4, 5, 3],
    'Ваня Иванов': [4, 4, 5, 5, 5],
    'Сережа Сергеев': [2, 3, 3, 5, 4],
    'Ирина Ирхина': [5, 5, 3, 3, 4],
    'Валя Валина': [2, 3, 3, 4, 3],
    'Вера Неверова': [5, 5, 3, 3, 4],
    'Кузьма Кузнецов': [4, 4, 5, 5, 5],
    'Лола Лялина': [5, 5, 3, 3, 4],
    'Петя Петухов': [2, 3, 3, 4, 5],
    'Вася Чижик': [2, 3, 3, 4, 3]
}

course = ['math', 'literature', 'phisics', 'sport', 'music']

df = pd.DataFrame(puple, index=course).T
print(df)

# 1. Средняя оценка по предмету
mean_scores = df.mean()
print('Средняя оценка по предметам:')
print(mean_scores)

# 2. Медианная оценка по предмету
median_scores = df.median()
print('\nМедианная оценка по предметам:')
print(median_scores)

# 3. Q1 по математике
Q1_math = df['math'].quantile(0.25)
print(f"\nQ1 по математике: {Q1_math}")

# 4. Q3 по математике
Q3_math = df['math'].quantile(0.75)
print(f"Q3 по математике: {Q3_math}")

# 5. IQR по математике
IQR_math = Q3_math - Q1_math
print(f"IQR по математике: {IQR_math}")

# 6. Стандартное отклонение по предмету
std_scores = df.std()
print('\nСтандартное отклонение по предметам:')
print(std_scores)