def b1():
	import pytesseract
	from PIL import ImageGrab

	# картинку в текст
	image = Image.open('fnord.tif') # Open image object using PIL

	print(image_to_string(image)) # Run tesseract.exe on image

	# файл в текст
	print(image_file_to_string('fnord.tif'))

def b2():
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	from PIL import ImageGrab
	left = 0
	top = 0
	right = 772
	bottom = 34

	image = ImageGrab.grab(bbox=(left, top, right, bottom))

	text = pytesseract.image_to_string(image, config='outputbase digits')
	print(text)

def b3():
	import pyautogui
	import easyocr
	from PIL import Image
	# задаем координаты углов области экрана, которую нужно сделать скриншот
	left, top, width, height = 0, 0, 300, 300

	# делаем скриншот заданной области экрана и сохраняем его в файл
	screenshot = pyautogui.screenshot(region=(left, top, width, height))
	screenshot.save('img/screenshot.png')

	# загружаем скриншот из файла и производим сканирование с помощью библиотеки easyocr
	reader = easyocr.Reader(['en'])
	image = Image.open('img/screenshot.png')
	result = reader.readtext(image)

	# выводим найденный текст в консоль
	text = ' '.join(map(lambda res: res[1], result))
	print(text)

def b4():
	import pyautogui
	import easyocr
	from PIL import Image
	# задаем координаты левого верхнего и правого нижнего углов желаемой области экрана
	left_x, top_y, right_x, bottom_y = 0, 0, 772, 34
	width, height = right_x - left_x, bottom_y - top_y

	# делаем скриншот заданной области экрана и сохраняем его в файл
	#screenshot = pyautogui.screenshot(region=(left_x, top_y, width, height))
	#screenshot.save('img/screenshot.png')

	# загружаем скриншот из файла и производим сканирование с помощью библиотеки easyocr
	reader = easyocr.Reader(['en'])
	image = Image.open('img/screenshot.png')
	result = reader.readtext(image)

	# выводим найденный текст в консоль
	text = ' '.join(map(lambda res: res[1], result))
	print(text)

def b5():
	import cv2
	import pytesseract
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

	img = cv2.imread('img/screenshot.png')
	img = cv2.resize(img, None, fx=9, fy=9)  # Увеличение изображения в 9 раз

	# Распознавание, допустимы только цифры
	balance = pytesseract.image_to_string(img, config='outputbase digits')
	print(balance)

def b6(x1:int, y1:int,
	x2:int, y2:int,
	onlyNumbers = False,
	isCords_OrSize = True):

	if isCords_OrSize:
		width = x2-x1
		height = y2-y1
	else:
		width = x2
		height = y2

		x2 = x1 + width
		y2 = y1 + height
	
	#import pytesseract
	#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	#from PIL import ImageGrab


	image = ImageGrab.grab(bbox=(x1, y1, x2, y2))

	if onlyNumbers:
		text = pytesseract.image_to_string(image, config='outputbase digits')
		return text
	else:
		text = pytesseract.image_to_string(image)
		return text
	


if __name__ == '__main__':
	import time

	# b2 and b5 is work
	# b6 best

	start = time.time()
	x = b6(0, 0, 772, 34)
	end = time.time()

	print(x)
	print("work time:", end-start,'\n')
	

	start = time.time()
	x = b6(0, 0, 772, 34, True)
	end = time.time()

	print(x)
	print("work time:", end-start,'\n')

	input("exit")


