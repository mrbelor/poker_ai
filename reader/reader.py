from PIL import ImageGrab

# Захват экрана
image = ImageGrab.grab()

# Получение цвета пикселя в координатах (x,y)
x = 100
y = 200
pixel_color = image.getpixel((x,y))

# Вывод цвета в формате RGB
print(f"RGB color: {pixel_color}")

input(". . .")