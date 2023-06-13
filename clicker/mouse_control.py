import pyautogui, time

def where_cycle():
	cord = pyautogui.position()
	while True:
		cord_old = cord
		cord = pyautogui.position()

		if cord != cord_old:
			print(cord)

time.sleep(4)

where_cycle()

# перемещение курсора на координаты в течении 4 секунд
# pyautogui.moveTo(100, 200, 4)

# перетаскивание
# pyautogui.dragTo(737, 544, 2, button='left') 

# нажатие
# pyautogui.click()

# двойное нажатие
# pyautogui.doubleClick()

# нажатие на определённой координате
# pyautogui.click(x=100, y=200)

# тройное нажатие с итервалом
# pyautogui.click(x=100, y=200, clicks=3, interval=0.5)

# колёсико
# pyautogui.scroll(10)

# написание текста
# pyautogui.write('Hello world!', interval=0.25)

# нажатия на клавиши
# pyautogui.press('esc')

# нажатие z 3 раза при зажатом ctrl
# with pyautogui.hold('ctrl'):
#       pyautogui.press(['z', 'z', 'z'])