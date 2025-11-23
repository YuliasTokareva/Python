import argparse
import csv
import os
import re
import time

import requests
from bs4 import BeautifulSoup


def clean_number(text):
    if not text:
        return None
    # оставляем только цифры
    digits = re.sub(r'[^\d]', '', text)
    return int(digits) if digits else None

def ensure_cache_dir():
    if not os.path.expanduser("cache"):
        os.makedirs("cache")

def get_country_data(country_name):
    # подготавливаем URL
    url_name = country_name.replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{url_name}"

    cache_path = os.path.join("cache", f"{url_name}.html")
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)

    # попытка загрузить из кэша
    if os.path.exists(cache_path):
        print(f"Беру из кэша: {country_name}")
        with open(cache_path, "r", encoding="utf-8") as f:
            html = f.read()
    else:
        # загрузка с сайта
        print(f"Загружаю с Википедии: {country_name}")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
        }
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            html = response.text
            # сохраняем в кэш
            with open(cache_path, "w", encoding="utf-8") as f:
                f.write(html)
            time.sleep(1)  # пауза между запросами
        except Exception as e:
            print(f"Ошибка при загрузке {country_name}: {e}")
            return {
                "country": country_name,
                "city": None,
                "area": None,
                "population": None
            }

    # парсим HTML
    soup = BeautifulSoup(html, "lxml")

    # столица
    city = None
    capital_th = soup.find("th", string=re.compile(r"Capital", re.IGNORECASE))
    if capital_th:
        td = capital_th.find_next("td")
        if td:
            a_tag = td.find("a")
            city = a_tag.get_text(strip=True) if a_tag else td.get_text(strip=True)

    # площадь
    area = None
    area_th = soup.find("th", string=re.compile(r"Area", re.IGNORECASE))
    if area_th:
        td = area_th.find_next("td")
        if td:
            match = re.search(r"[\d,]+", td.get_text())
            if match:
                area = clean_number(match.group())

    # население
    population = None
    # Ищем "Population" в заголовке ИЛИ в тексте ближайших ячеек
    pop_th = soup.find("th", string=re.compile(r"Population", re.IGNORECASE))
    if pop_th:
        td = pop_th.find_next("td")
        if td:
            # Иногда население в подсписке — ищем первое число
            match = re.search(r"[\d,]+", td.get_text())
            if match:
                population = clean_number(match.group())
    else:
        # альтернатива: ищем таблицу с населением в другом месте
        demographics = soup.find("span", {"id": re.compile(r"Demographics|Population", re.IGNORECASE)})
        if demographics:
            table = demographics.find_parent("table")
            if table:
                # Ищем первое число в таблице
                match = re.search(r"[\d,]+", table.get_text())
                if match:
                    population = clean_number(match.group())

    return {
        "country": country_name,
        "city": city,
        "area": area,
        "population": population
    }


def main():
    parser = argparse.ArgumentParser(description="Парсер данных о странах с английской Википедии")
    parser.add_argument("-i", "--input", default="countries.txt", help="Входной файл со списком стран")
    parser.add_argument("-o", "--output", default="countries_data.csv", help="Выходной CSV-файл")
    args = parser.parse_args()

    # проверка входного файла
    if not os.path.exists(args.input):
        print(f"Файл '{args.input}' не найден!")
        return

    # чтение стран
    with open(args.input, "r", encoding="utf-8") as f:
        countries = [line.strip() for line in f if line.strip()]

    if not countries:
        print("Нет стран в файле.")
        return

    # сбор данных
    results = []
    for country in countries:
        data = get_country_data(country)
        results.append(data)

    # запись в CSV
    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["country", "city", "area", "population"])
        writer.writeheader()
        writer.writerows(results)

    print(f"Данные сохранены в '{args.output}'")


if __name__ == "__main__":
    main()