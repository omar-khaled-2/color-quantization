from PIL import Image
import numpy as np
import time
image_path = input("Enter image path: ")


image = Image.open(image_path)

width , height = image.size





color_count = int(input("Enter number of colors: "))


colors = np.zeros((color_count,3), dtype=np.uint8)







for i in range(color_count):
    rgp_color = input("Enter RGB value: ")
    rgp_colors = rgp_color.split(",")

    for j in range(3):
        colors[i][j] = int(rgp_colors[j].strip())




result = Image.new('RGB', (width, height))





for i in range(width):
    for j in range(height):
        pixel = image.getpixel((i,j))
        distances = np.linalg.norm(colors - np.array(pixel), axis=1)
        index = np.argmin(distances)
        result.putpixel((i,j), tuple(colors[index]))








result.show()

 






