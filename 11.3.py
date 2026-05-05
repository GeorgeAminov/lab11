import csv
total = 0
print("Нужно купить:")
with open("products.csv", "r", encoding = "utf-8") as products:
    reader = csv.DictReader(products)
    for row in reader:
        product = row["Продукт"]
        kol = int(row["Количество"])
        price = int(row["Цена"])
        print(f"{product} - {kol} шт. за {price} руб.")
        total += price * kol
    print(f"Итоговая сумма: {total} руб.")