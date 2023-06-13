import pyautogui, time, sys
from PIL import ImageGrab, ImageDraw
from OCR import b6

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def binared(x:str):
	y = bin(int.from_bytes(x.encode(), byteorder='big'))
	return y

def unbinared(x:str):
	y = int(x, 2)
	return y.to_bytes((y.bit_length() + 7) // 8, byteorder='big').decode()

class table(object):
	"""docstring for table"""
	def __init__(self, 
		window_pos = None,
		settings = {
			
			#'playersImgPos':((224,148), (575,148), (991,148)),
			#'playersNametagPos':()
			#'playersImgNametagPos':(((224,148),()), (575,148), (991,148))
			'playersItemPos':(
				{'img':(224,148),'nametag':(0,0), 'chips':(0,0)}, 
				{'img':(575,148),'nametag':(0,0), 'chips':(0,0)},
				{'img':(991,148),'nametag':(0,0), 'chips':(0,0)}
				),
			'playersImgSize':(53,71),
			'playersNametagSize':(0,0),
			'playersChipsSize':(0,0),

			#'cardsY':210,
			#'cardsX':(195, 237, 278, 320, 360),
			#'cards':(
			#	{'pos':(195,210),'nametag':(), 'chips':()}, 
			#	{'pos':(237,210),'nametag':(), 'chips':()},
			#	{'pos':(278,210),'nametag':(), 'chips':()},
			#	{'pos':(320,210),'nametag':(), 'chips':()},
			#	{'pos':(360,210),'nametag':(), 'chips':()}
			#	),
			'cards':{
				'pos':((195,210), (237,210), (278,210), (320,210), (360,210)), # левого верхнего угла
				'size':(0,0),
				'colorPos':(0,0), # точка в которой rgb карты относительно угла карты
				'suitPos':(0,0), # координаты угла области, где нужно сканировать масть карты относительно угла карты
				'suitSize':(0,0) # ширина и высота облати масти
			},
			
			'myCards':{
				'pos':((266,382), (307,382)),
				'size':(0,0),
				'colorPos':(0,0),
				'suitPos':(0,0),
				'suitSize':(0,0)
			},

			'myChipsPos':(0,0),
			'myChipsSize':(0,0)
		}):
		self.window_pos = window_pos
		self.window_size = (pyautogui.size().width, pyautogui.size().height)
		self.settings = settings
		self.players = list()
	
	def settingsCheck(self):
		image = ImageGrab.grab()
		draw = ImageDraw.Draw(image)
		window_pos =  self.window_pos

		#draw.line((0, 0, 100, 100), fill=(255, 0, 0), width=2)
		#draw.rectangle((200, 50, 300, 150), outline=(255, 0, 0), width=2)
		#draw.ellipse((0, 0, 150, 150), outline=(0, 0, 255), width=2)

		imgSize = self.settings['playersImgSize']
		nametagSize = self.settings['playersNametagSize']
		chipsSize = self.settings['playersChipsSize']

		for i in self.settings['playersItemPos']:
			Px1, Py1 = i['img'][0] + window_pos[0], i['img'][1] + window_pos[1]
			Px2, Py2 = Px1 + imgSize[0], Py1 + imgSize[1]
			draw.rectangle((Px1, Py1, Px2, Py2), outline=(255, 0, 0), width=3)


			Nx1, Ny1 = i['nametag'][0] + window_pos[0], i['nametag'][1] + window_pos[1]
			Nx2, Ny2 = Nx1 + nametagSize[0], Ny1 + nametagSize[1]
			draw.rectangle((Nx1, Ny1, Nx2, Ny2), outline=(255, 0, 0), width=3)

			CHx1, CHy1 = i['chips'][0] + window_pos[0], i['chips'][1] + window_pos[1]
			CHx2, CHy2 = CHx1 + chipsSize[0], CHy1 + chipsSize[1]
			draw.rectangle((CHx1, CHy1, CHx2, CHy2), outline=(255, 0, 0), width=3)

		cardSize = self.settings['cards']['size']
		colorPos = self.settings['cards']['colorPos']
		suitPos = self.settings['cards']['suitPos']
		suitSize = self.settings['cards']['suitSize']

		for i in self.settings['cards']['pos']:
			Cx1, Cy1 = i[0] + window_pos[0], i[1] + window_pos[1]
			Cx2, Cy2 = Cx1 + cardSize[0], Cy1 + cardSize[1]
			draw.rectangle((Cx1, Cy1, Cx2, Cy2), outline=(255, 0, 0), width=2)

			colorX = i[0] + colorPos[0] + window_pos[0]
			colorY = i[1] + colorPos[1] + window_pos[1]
			draw.ellipse((colorX-1, colorY-1, colorX+1, colorY+1), outline=(0, 0, 255), width=2)

			Sx1, Sy1 = suitPos[0] + window_pos[0], suitPos[1] + window_pos[1]
			Sx2, Sy2 = Sx1 + suitSize[0], Sy1 + suitSize[1]
			draw.rectangle((Sx1, Sy1, Sx2, Sy2), outline=(255, 0, 0), width=2)


		image.show()

	def waitPoint(self, waitt = 4):
		print('Требуется определить левый верхний угол программы')
		print(f'Указывайте на него в течении {waitt} секунд..')
		#time.sleep(3)

		mpos_old = (None, None)
		pastt_old = None
		WINDOW_POS = None
		startt = time.time()

		while not WINDOW_POS:
			mpos = pyautogui.position()
			pastt = round(time.time() - startt, 1)
			remaint = round(waitt - pastt, 1)

			if mpos == mpos_old:

				if remaint <= 0:
					WINDOW_POS = (mpos.x, mpos.y)
					for i in range(3): print(f"Точка {WINDOW_POS} зафиксирована!")

				elif remaint < waitt-1 and pastt != pastt_old:
						print(f"Эта точка будет выбрана через {remaint} секунд")
						#print(f"Отсутствие движений мышки {round(pastt, 1)} секунд")

			else:
				startt = time.time()

			mpos_old = mpos
			pastt_old = pastt

		self.window_pos = WINDOW_POS
		return WINDOW_POS

	def locatePlayers(self):
		'''
		[
			{
				'img':image = ImageGrab.grab(x1,y1,x2,y2) # None
				'name':b6(x1,y1,width,height, False, True)
				'id':(imageRGBpos and name)
				'chips':b6(x1,y1,width,height,True,False)
			}
		]
		'''
		image = ImageGrab.grab() # Скрин


		for i in self.settings['playersImgPos']:
			
			window_x, window_y = self.window_pos[0], self.window_pos[1]
			cord = (i[0]+window_x+10, i[1]+window_y+10)
			
			pixel = image.getpixel(cord)
			
			# проверка на отсутствие игрока
			if pixel == (255,255,255):
				self.players.append(None)
				continue

			# делаем playerId
			#plid = int(f'{pixel[0]}{pixel[1]}{pixel[2]}')
			plid = f'{pixel[0]} {pixel[1]} {pixel[2]}'
			self.players.append(plid)
				
	def report(self):
		print('settings:', self.settings)
		print('window_pos:', self.window_pos)
		print('players:', self.players)

	



def main():
	x = table()
	'''
	y = binared(input(">"))
	print(y)
	print(unbinared(y))

	'''
	

	#pyautogui.alert(title="Window", text="Расположите окно игры так, чтобы было видно всю необходимую информацию",  button="OK")
	print('\nРасположите окно игры как вам удобно, \nчтобы было видно всю необходимую информацию, \nи не в коем случае не передвигайте его во время работы нейросети')
	input('далее ->')
	x.waitPoint()

	#pyautogui.alert(title="Window", text="\nДалее проверка на правильность располжения триггеров\nНажмите enter",  button="OK")
	input("\nДалее проверка на правильность располжения триггеров\nсделайте так, чтобы окно игры ничего не перекрывало\nНажмите enter по готовности")
	x.settingsCheck()
	while True:
		i = input('\nПравильно ли были определены триггеры?\n(y/n) ')
		if i == ('y' or 'Y'):
			break
		elif i == ('n' or 'N'):
			input("жаль. придётся делать всё сначала ")
			sys.exit(0)
		else:
			print('нужно ввести "y" или "n"')



	'''
	x.locatePlayers()
	x.report()
	'''




if __name__ == '__main__':
	main()
	input("exit")
