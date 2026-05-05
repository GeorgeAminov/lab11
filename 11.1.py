from PIL import Image, ImageFilter
import os
os.mkdir("gotovoe")
for file in os.listdir("negotovoe"):
    path_file = os.path.join("negotovoe", file)
    img = Image.open(path_file)
    img_filter = img.filter(ImageFilter.CONTOUR)
    img_filter.save(f"gotovoe/{file}")