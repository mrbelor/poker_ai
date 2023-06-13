import pyautogui, time

time.sleep(2)

print("take_screenshot")
loca = pyautogui.locateOnScreen('3.png')
if loca: loca = pyautogui.center(loca) # точка в центре

try:
	#print(loca)
	pyautogui.moveTo(loca.left, loca.top, 0.1)
except:
	print("cant find")

input('exit')