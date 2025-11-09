import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_excel('lab_4_part_5.xlsx', sheet_name='Данные', skiprows=1)
df = df.drop(columns=['Unnamed: 0'])
df['Дата'] = pd.to_datetime(df['Дата'])
df['Средняя цена'] = df['Продажи'] / df['Количество']
df['Прибыль'] = df['Продажи'] - df['Себестоимость']

total_monthly = df.groupby('Дата')[['Продажи', 'Себестоимость', 'Прибыль']].sum()
plt.figure(figsize=(12, 5))
plt.plot(total_monthly.index, total_monthly['Продажи'], label='Продажи', marker='o')
plt.plot(total_monthly.index, total_monthly['Себестоимость'], label='Себестоимость', marker='s')
plt.plot(total_monthly.index, total_monthly['Прибыль'], label='Прибыль', marker='^')
plt.title('Динамика товарооборота (всего)')
plt.xlabel('Дата')
plt.ylabel('Сумма')
plt.legend()
plt.grid(True)
plt.savefig('товарооборот.png', dpi=150, bbox_inches='tight')
plt.show()

top_products = df.groupby('товар')['Продажи'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_products.plot(kind='barh', color='teal')
plt.title('ТОП-10 товаров по выручке')
plt.xlabel('Выручка')
plt.ylabel('Товар')
plt.tight_layout()
plt.savefig('топ_товаров.png', dpi=150, bbox_inches='tight')
plt.show()

sales_by_store = df.groupby('точка')['Продажи'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sales_by_store.head(10).plot(kind='barh', color='coral')
plt.title('ТОП-10 точек реализации по выручке')
plt.xlabel('Выручка')
plt.ylabel('Точка')
plt.tight_layout()
plt.savefig('топ_точек.png', dpi=150, bbox_inches='tight')
plt.show()

product_avg = df.groupby('товар').agg({
    'Средняя цена': 'mean',
    'Себестоимость': 'mean',
    'Количество': 'sum'
}).sort_values('Средняя цена', ascending=False).head(10)

first_months = df['Дата'].drop_duplicates().sort_values().head(3)
last_months = df['Дата'].drop_duplicates().sort_values().tail(3)
first_sales = df[df['Дата'].isin(first_months)].groupby('товар')['Продажи'].sum()
last_sales = df[df['Дата'].isin(last_months)].groupby('товар')['Продажи'].sum()
growth = (last_sales - first_sales).sort_values(ascending=False).head(10)

monthly = df.groupby(['товар', 'Дата'])['Продажи'].sum().reset_index()
monthly = monthly.sort_values(['товар', 'Дата'])
monthly['month_idx'] = monthly.groupby('товар').cumcount()
top3 = df.groupby('товар')['Продажи'].sum().nlargest(3).index

plt.figure(figsize=(18, 5))
for i, product in enumerate(top3, 1):
    prod_data = monthly[monthly['товар'] == product].copy()
    if len(prod_data) < 3:
        continue
    X = prod_data['month_idx'].values.reshape(-1, 1)
    y = prod_data['Продажи'].values
    model = LinearRegression()
    model.fit(X, y)
    future_idx = np.array([X.max() + 1, X.max() + 2, X.max() + 3]).reshape(-1, 1)
    future_sales = model.predict(future_idx)
    last_date = prod_data['Дата'].max()
    future_dates = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=3, freq='MS')
    plt.subplot(1, 3, i)
    plt.plot(prod_data['Дата'], y, 'o-', label='Реальные данные', linewidth=2)
    plt.plot(future_dates, future_sales, 'rx', markersize=10, label='Прогноз (3 мес)')
    all_idx = np.arange(0, X.max() + 4).reshape(-1, 1)
    all_pred = model.predict(all_idx)
    all_dates = pd.date_range(start=prod_data['Дата'].min(), periods=len(all_idx), freq='MS')
    plt.plot(all_dates, all_pred, '--', color='gray', alpha=0.7, label='Линия тренда')
    plt.title(f'Прогноз: {product}')
    plt.xlabel('Дата')
    plt.ylabel('Продажи')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('прогноз_товаров.png', dpi=150, bbox_inches='tight')
plt.show()

print("Анализ завершён!")