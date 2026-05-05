from PIL import Image
import os
for file in os.listdir():
    if file.endswith((".jpg", ".png")):
        img = Image.open(file)
        print(f"Размер: {img.size}")
        print(f"Формат: {img.format}")
        print(f"Цветовая модель: {img.mode}")
        img.show()
