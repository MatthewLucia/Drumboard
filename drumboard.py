import pygame, curses

# Initialize pygame mixer
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Audio files
a1 = pygame.mixer.Sound('beats/01.wav')
a2 = pygame.mixer.Sound('beats/02.wav')
a3 = pygame.mixer.Sound('beats/03.wav')
a4 = pygame.mixer.Sound('beats/04.wav')
a5 = pygame.mixer.Sound('beats/05.wav')
a6 = pygame.mixer.Sound('beats/06.wav')
a7 = pygame.mixer.Sound('beats/07.wav')
a8 = pygame.mixer.Sound('beats/08.wav')
a9 = pygame.mixer.Sound('beats/09.wav')

# Initialize curses screen
screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.clear()

while True:
	screen.addstr(1, 0, "Press the letters w - p on your keyboard to play! Press q to quit!")

	event = screen.getch()

	screen.clear()

	if event == ord('q'):
		break
	elif event == ord('w'):
		a1.play()
	elif event == ord('e'):
		screen.clear()
		a2.play()
	elif event == ord('r'):
		screen.clear()
		a3.play()
	elif event == ord('t'):
		screen.clear()
		a4.play()
	elif event == ord('y'):
		screen.clear()
		a5.play()
	elif event == ord('u'):
		screen.clear()
		a6.play()
	elif event == ord('i'):
		screen.clear()
		a7.play()
	elif event == ord('o'):
		screen.clear()
		a8.play()
	elif event == ord('p'):
		screen.clear()
		a9.play()
	else:
		screen.clear()
		screen.addstr(0, 0, "That key doesn't do anything!")

curses.endwin()
