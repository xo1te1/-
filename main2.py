import json
from _datetime import datetime
import csv


with open('[ПР №2] sales_data_large.json', 'r', encoding='utf-8') as file:
    sales_data = json.load(file)

start_date_str = input("Введіть дату початку періоду(YYYY-MM-DD): ")
end_date_str = input("Введіть дату кінця періоду: ")

start_date_str = datetime.strptime(start_date_str, '%Y-%m-%d')
end_date_str = datetime.strptime(end_date_str, '%Y-%m-%d')

min_price = float(input("Введіть мінімальну ціну товару: "))

filtered_sales = [
    sale for sale in sales_data
    if start_date_str <= datetime.strptime(sale["date"], '%Y-%m-%d') <= end_date_str and sale['price'] >= min_price
]

headers = ['product', 'price', 'quantity', 'date']
with open('filtered_sales.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(filtered_sales)