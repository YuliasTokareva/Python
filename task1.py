import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from faker import Faker

fake = Faker('ru_RU')

# параметры
years = [2020, 2021, 2022, 2023, 2024]
forms = ['очная', 'заочная']
specialties = [
    'Радиофизика и информационные технологии',
    'Прикладная информатика',
    'Кибербезопасность',
    'Интеллектуальная электроника',
    'Аэрокосмические радиоэлектронные и информационные системы и технологии',
    'Физическая электроника'
]

students = []
print("Генерация данных...")

for _ in range(150):
    year = np.random.choice(years)
    form = np.random.choice(forms)
    specialty = np.random.choice(specialties, p=[0.35, 0.25, 0.15, 0.1, 0.1, 0.05])

    # средний балл аттестата
    diploma_avg = round(np.random.normal(loc=7.0, scale=2.8), 1)
    diploma_avg = np.clip(diploma_avg, 4.0, 10.0)

    base_score = diploma_avg * 8

    # баллы ЦТ
    ct_math = round(np.random.normal(loc=base_score, scale=30), 1)
    ct_physics = round(np.random.normal(loc=base_score, scale=28), 1)
    ct_language = round(np.random.normal(loc=base_score, scale=20), 1)

    ct_math = np.clip(ct_math, a_min=20, a_max=100)
    ct_physics = np.clip(ct_physics, a_min=20, a_max=100)
    ct_language = np.clip(ct_language, a_min=25, a_max=100)

    # щкольный балл = аттестат * 10
    school_score = round(diploma_avg * 10, 1)

    # общий балл = сумма трёх ЦТ + школьный балл
    total_score = ct_math + ct_physics + ct_language + school_score

    students.append({
        'Год поступления': year,
        'Форма обучения': form,
        'Специальность': specialty,
        'ЦТ Математика': ct_math,
        'ЦТ Физика': ct_physics,
        'ЦТ Язык': ct_language,
        'Балл аттестата': diploma_avg,
        'Школьный балл': school_score,
        'Общий балл': round(total_score, 1),
        'ФИО': fake.name(),
        'Адрес': fake.address(),
        'Телефон': fake.phone_number()
    })

# таблицу
df = pd.DataFrame(students)

# ВИЗУАЛИЗАЦИЯ
#  динамика среднего балла по предметам ЦТ
plt.figure(figsize=(10, 5))
subjects = ['ЦТ Математика', 'ЦТ Физика', 'ЦТ Язык']
for subject in subjects:
    yearly = df.groupby('Год поступления')[subject].median()
    plt.plot(yearly.index, yearly.values, marker='o', label=subject)
    plt.xticks(years)
plt.title('Динамика среднего балла по предметам ЦТ')
plt.xlabel('Год')
plt.ylabel('Средний балл')
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.show()

# динамика среднего балла аттестата
plt.figure(figsize=(8, 4))
diploma_trend = df.groupby('Год поступления')['Балл аттестата'].median()
plt.plot(diploma_trend.index, diploma_trend.values, marker='s', color='green')
plt.xticks(years)
plt.title('Динамика среднего балла аттестата')
plt.xlabel('Год')
plt.ylabel('Балл')
plt.ylim(0, 10)
plt.grid(True)
plt.show()

# динамика проходного балла
plt.figure(figsize=(8, 4))
passing = df.groupby('Год поступления')['Общий балл'].quantile(0.8)
plt.plot(passing.index, passing.values, marker='D', color='red')
plt.xticks(years)
plt.title('Динамика проходного балла')
plt.xlabel('Год')
plt.ylabel('Балл')
plt.ylim(0, 400)
plt.grid(True)
plt.show()

# количество поступивших по специальностям
plt.figure(figsize=(11, 5))
spec_counts = df['Специальность'].value_counts()
plt.barh(spec_counts.index, spec_counts.values, color='coral')
plt.title('Количество поступивших по специальностям')
plt.xlabel('Число студентов')
plt.tight_layout()
plt.show()

# статистика по формам обучения
plt.figure(figsize=(6, 6))
form_data = df['Форма обучения'].value_counts()
plt.pie(form_data.values, labels=form_data.index, autopct='%1.1f%%', startangle=140)
plt.title('Распределение по формам обучения')
plt.show()

print("Генерация и визуализация завершены.")