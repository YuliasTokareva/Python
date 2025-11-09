import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_excel('s7_data_sample_rev4_50k.xlsx', sheet_name='DATA')

df['ISSUE_DATE'] = pd.to_datetime(df['ISSUE_DATE'])
df['Месяц'] = df['ISSUE_DATE'].dt.month

pax_type_names = {
    'AD': 'Взрослый',
    'CHD': 'Ребёнок',
    'INF': 'Младенец',
    'FIM': 'Семейный'
}

fop_names = {
    'AH': 'Корп. счёт',
    'AI': 'Корп. счёт',
    'BN': 'Бонусы',
    'CA': 'Наличные',
    'CC': 'Кредитная карта',
    'DP': 'Динамическое ценообразование',
    'EX': 'Прочее',
    'FF': 'Оплата милями',
    'FS': 'Частично милями',
    'IN': 'Корп. счёт',
    'LS': 'Скидка 10%',
    'MC': 'Прочее',
    'PS': 'Подарок',
    'VO': 'Ваучер'
}

ffp_names = {
    'FFP': 'Да',
    np.nan: 'Нет'
}

#  перевод
df['Тип пассажира'] = df['PAX_TYPE'].map(pax_type_names).fillna('Неизвестно')
df['Способ оплаты'] = df['FOP_TYPE_CODE'].map(fop_names).fillna('Прочее')
df['Лояльность'] = df['FFP_FLAG'].map(ffp_names).fillna('Нет')

print("Данные подготовлены.")

# Описательная статистика
print("1. Описательная статистика ")
stats = df['REVENUE_AMOUNT'].describe()
print(f"Средняя цена билета: {stats['mean']:.2f} руб.")
print(f"Медиана: {stats['50%']:.2f} руб.")
print(f"Минимум: {stats['min']:.2f} руб.")
print(f"Максимум: {stats['max']:.2f} руб.")
print(f"Стандартное отклонение: {stats['std']:.2f} руб.")

# Аэропорты
plt.figure(figsize=(14, 5))
top_orig = df['ORIG_CITY_CODE'].value_counts().head(10)
top_dest = df['DEST_CITY_CODE'].value_counts().head(10)

plt.subplot(1, 2, 1)
top_orig.plot(kind='bar', color='skyblue')
plt.title('Топ-10 городов отправления')
plt.xlabel('Код аэропорта')
plt.ylabel('Число билетов')
plt.xticks(rotation=45, ha='right')

plt.subplot(1, 2, 2)
top_dest.plot(kind='bar', color='lightcoral')
plt.title('Топ-10 городов назначения')
plt.xlabel('Код аэропорта')
plt.ylabel('Число билетов')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

#Сезонность и количество перелётов

monthly_flights = df.groupby('Месяц').size()
monthly_revenue = df.groupby('Месяц')['REVENUE_AMOUNT'].sum()

plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
monthly_flights.plot(marker='o', color='purple')
plt.title('Количество перелётов по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Число перелётов')
plt.grid(True)

plt.subplot(1, 2, 2)
monthly_revenue.plot(marker='s', color='green')
plt.title('Выручка по месяцам')
plt.xlabel('Месяц')
plt.ylabel('Выручка')
plt.grid(True)

plt.tight_layout()
plt.show()

# 4. Пассажиры и лояльность
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
pax_counts = df['Тип пассажира'].value_counts()
pax_counts.plot(kind='bar', color='mediumseagreen')
plt.title('Распределение типов пассажиров')
plt.xlabel('Тип пассажира')
plt.ylabel('Количество')
plt.xticks(rotation=45, ha='right')

plt.subplot(1, 2, 2)
ffp_counts = df['Лояльность'].value_counts()
ffp_counts.plot(kind='bar', color='goldenrod')
plt.title('Участие в программе лояльности')
plt.xlabel('Участие')
plt.ylabel('Количество')
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# 5. Способы оплаты

fop_counts = df['Способ оплаты'].value_counts()

plt.figure(figsize=(10, 6))
fop_counts.plot(kind='barh', color='steelblue')  # горизонтальный график
plt.title('Распределение способов оплаты')
plt.xlabel('Количество транзакций')
plt.ylabel('Способ оплаты')
plt.tight_layout()  # автоматически подгоняет подписи
plt.show()

#  6. Предсказание
avg_by_month = df.groupby('Месяц')['REVENUE_AMOUNT'].mean()

plt.figure(figsize=(10, 5))
avg_by_month.plot(marker='D', color='red', linewidth=2)
plt.title('Средний чек по месяцам (прогноз на основе данных)')
plt.xlabel('Месяц')
plt.ylabel('Средний чек')
plt.grid(True)
plt.show()

print(" Анализ завершён!")