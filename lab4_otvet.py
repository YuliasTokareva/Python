#генерируем с помощью специальных библиотек продкуцию буфета: булочки, пирожки, смаженки, пицца, печенье
#также через генерацию генерируем: колличество которое привезли и которые продали и цену
#далее добавляем два столбцв в которых через расчет используя библиотеки расчитать скольур осталось и на какую сумму
#продали и построить по каждому продукту визуализацию сколько было и сколько продали, различные графики и все что придксаем построить
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt

fake = Faker('ru_RU')
PRODUCTS = ["булочки", "пирожки", "смаженки", "пицца", "печенье"]

def generate_buffet_data():
    data = []
    for product in PRODUCTS:
        delivered = fake.random_int(min=50, max=100)
        sold = fake.random_int(min=0, max=delivered)
        price = round(fake.pyfloat(min_value=2.0, max_value=8.5, right_digits=2), 2)
        data.append({
            "продукт": product,
            "привезли": delivered,
            "продано": sold,
            "цена": price
        })
    return pd.DataFrame(data)

def add_calculated_columns(df):
#добавление расчётных столбцов
    df_full = df.copy()
    df_full["осталось"] = df_full["привезли"] - df_full["продано"]
    df_full["выручка"] = df_full["продано"] * df_full["цена"]
    return df_full

def visualize_by_product(df):
    summary = df.set_index("продукт")

    products = summary.index
    delivered = summary["привезли"]
    sold = summary["продано"]
    revenue = summary["выручка"]
    leftovers = summary["осталось"]

    x = range(len(products))
    width = 0.35

    plt.figure(figsize=(10, 6))
    plt.bar([i - width/2 for i in x], delivered, width, label="Привезли", color="blue")
    plt.bar([i + width/2 for i in x], sold, width, label="Продано", color="orange")
    plt.xlabel("Продукт")
    plt.ylabel("Количество (шт.)")
    plt.title("Привезли и продали по каждому продукту")
    plt.xticks(x, products)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(8, 8))
    colors = ['coral', 'blue', 'green', 'gold', 'plum']
    plt.pie(revenue, labels=products, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title("Доля выручки по продуктам")
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(products, leftovers, color="green")
    plt.xlabel("Продукт")
    plt.ylabel("Остаток (шт.)")
    plt.title("Остатки по каждому продукту")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    # генерируем исходные данные
    df_initial = generate_buffet_data()
    # добавляем расчётные столбцы
    df_full = add_calculated_columns(df_initial)

    # вывод только исходных данных
    print("Исходные данные:")
    print(df_initial)

    # вывод полной таблицы со всеми столбцами и значениями
    print("\nПолная таблица со всеми данными:")
    print(df_full)

    # визуализируем
    visualize_by_product(df_full)

if __name__ == "__main__":
    main()



