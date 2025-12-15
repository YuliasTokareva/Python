import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10.0, 6.0)
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

#PDF-ФАЙЛА
pdf = PdfPages('отчет_авиабилеты.pdf')

# Статистика в виде текста
fig, ax = plt.subplots(figsize=(10, 8))
stats_text = df['REVENUE_AMOUNT'].describe().round(2).to_string()
ax.text(0.1, 0.95, "Описательная статистика:", fontsize=14, fontweight='bold', transform=ax.transAxes)
ax.text(0.1, 0.85, stats_text, fontsize=11, fontfamily='monospace', transform=ax.transAxes, verticalalignment='top')
ax.axis('off')
pdf.savefig(fig, bbox_inches='tight')
plt.close()

# Описательная статистика
print("1. Описательная статистика ")
print(df['REVENUE_AMOUNT'].describe().round(2))

# Аэропорты
fig, ax = plt.subplots(1, 2, figsize=(16.0, 6.0))
top_orig = df['ORIG_CITY_CODE'].value_counts().head(10)
top_dest = df['DEST_CITY_CODE'].value_counts().head(10)

sns.barplot(x=top_orig.index, y=top_orig.values, ax=ax[0], color='blue')
ax[0].set_title('Топ-10 городов отправления')
ax[0].set_xlabel('Код аэропорта')
ax[0].tick_params(axis='x', rotation=45)
ax[0].set_ylabel('Число билетов')
ax[0].tick_params(axis='y', rotation=90)

sns.barplot(x=top_dest.index, y=top_dest.values, ax=ax[1], color='coral')
ax[1].set_title('Топ-10 городов назначения')
ax[1].set_xlabel('Код аэропорта')
ax[1].tick_params(axis='x', rotation=45)
ax[1].set_ylabel('Число билетов')
ax[1].tick_params(axis='y', rotation=90)
plt.tight_layout()
pdf.savefig(bbox_inches='tight')
plt.close()

#Сезонность и количество перелётов

monthly = df.groupby('Месяц').agg(
    перелетов= ('REVENUE_AMOUNT', 'size'),
    выручка=('REVENUE_AMOUNT', 'sum'),
    средний_чек=('REVENUE_AMOUNT', 'mean')
).reset_index()

fig, ax = plt.subplots(1, 3, figsize=(16.0, 6.0))
sns.lineplot(data=monthly, x='Месяц', y='перелетов', marker='o', ax=ax[0])
ax[0].set_title('Сезонность: колл. перелетов')
sns.lineplot(data=monthly, x='Месяц', y='выручка', marker='s', ax=ax[1])
ax[1].set_title('Сезонность: выручка')
sns.lineplot(data=monthly, x='Месяц', y='средний_чек', marker='D', ax=ax[2])
ax[2].set_title('Сезонность: средний_чек')
plt.tight_layout()
pdf.savefig(bbox_inches='tight')
plt.close()

# 4. Пассажиры и лояльность
fig, ax = plt.subplots(1, 2, figsize=(14.0, 6.0))
sns.countplot(data=df, y='Тип пассажира', ax=ax[0], color='green')
ax[0].set_title('Распределение типов пассажиров')

sns.countplot(data=df, y='Лояльность', ax=ax[1], color='green')
ax[1].set_title('Участие в программе лояльности')
plt.tight_layout()
pdf.savefig(bbox_inches='tight')
plt.close()

# 5. Способы оплаты
plt.figure(figsize=(10, 8))
sns.countplot(data=df, y='Способ оплаты', color='steelblue')  # горизонтальный график
plt.title('Распределение способов оплаты')
plt.xlabel('Количество транзакций')
plt.tight_layout()  # автоматически подгоняет подписи
pdf.savefig(bbox_inches='tight')
plt.close()

#  6. Способы оплаты
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, y='Способ оплаты',x='REVENUE_AMOUNT', showfliers=False, color='coral')  # горизонтальный график
plt.title('Цена билета по способу оплаты', fontsize=14, pad=20)
plt.xlabel('Цена', fontsize=12)
plt.ylabel('Способ оплаты', fontsize=12)
plt.tight_layout()  # автоматически подгоняет подписи
pdf.savefig(bbox_inches='tight')
plt.close()

from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(monthly['Месяц'], monthly['выручка'])
monthly['trend'] = intercept + slope * monthly['Месяц']
monthly['forecast'] = monthly['trend']

plt.figure(figsize=(10, 6))
plt.plot(monthly['Месяц'], monthly['выручка'], 'o-', label='Факт')
plt.plot(monthly['Месяц'], monthly['trend'], 'r--', label='Тренд')

next_month = 1
forecast_val = intercept + slope * next_month
plt.plot([12, next_month], [monthly['trend'].iloc[-1], forecast_val], 'r--', alpha=0.7)
plt.scatter(next_month, forecast_val, color='red', s=100, zorder=5, label=f'Прогноз (мес. {next_month})')
plt.title('Прогноз выручки на следующий месяц')
plt.xlabel('Месяц')
plt.ylabel('Выручка')
plt.legend()
plt.grid(True)
plt.tight_layout()
pdf.savefig(bbox_inches='tight')
plt.close()
pdf.close()

print(" Анализ завершён!")