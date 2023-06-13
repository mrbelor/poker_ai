from PIL import ImageGrab
import pyautogui, time, pygame


def WitC(cord: tuple = None):
	
	if not cord:
		cord = pyautogui.position()
		cord = (cord.x, cord.y)

	image = ImageGrab.grab() # Скрин
	pixel_color = image.getpixel(cord)

	return pixel_color, cord

def main():
	pygame.init()

	screen = pygame.display.set_mode((100, 100)) #создаём окно с размерами
	time.sleep(1)

	#основной цикл
	running = True
	while running: 
	    for event in pygame.event.get(): 
	        if event.type == pygame.QUIT:
	            pygame.quit()

	    color, pos = WitC()
	    screen.fill(color)
	    print(f"\npos: {pos}\ncolor: {color}")
	    
	    pygame.display.flip()

	pygame.quit()



if __name__ == "__main__":
	main()
