from pygame import *
init()
from random import *
from button import Button
screen = display.set_mode((1280, 720), FULLSCREEN)
display.set_caption('Fire Game')
screen.fill((0, 0, 0)) 

class Objeto(sprite.Sprite):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion, color, vidas, team):
		sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.ancho = ancho
		self.largo = largo
		self.direccionx = direccionx
		self.direcciony = direcciony
		self.puntuacion = puntuacion
		self.color = color
		self.vidas = vidas
		self.team = team

	def DibujarObjeto(self):
		draw.rect(screen, self.color, (self.x,self.y,self.ancho,self.largo))

	def check_colisiones(sprite1, sprite2):
		xsprite1 = sprite1.x
		ysprite1 = sprite1.y
		anchosprite1 = sprite1.ancho
		largosprite1 = sprite1.largo
		xsprite2 = sprite2.x
		ysprite2 = sprite2.y
		anchosprite2 = sprite2.ancho
		largosprite2 = sprite2.largo
		if (ysprite1 + largosprite1) > ysprite2 and ysprite1 < (ysprite2 + largosprite2) and (xsprite1 + anchosprite1) > xsprite2 and xsprite1 < (xsprite2 + anchosprite2):
			return True

class Bola(Objeto):
	def __init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion, color, vidas, team):
		Objeto.__init__(self, x, y, ancho, largo, direccionx, direcciony, puntuacion, color, vidas, team)
	
	def Movimiento(self):
		x = self.x
		y = self.y
		keys = key.get_pressed()
		if keys[K_w]==1:
			self.direcciony = 1
			if y > 0:
				self.y -= 1
		if keys[K_s]:
			self.direcciony = 0
			if y < 700:
				self.y += 1
		if keys[K_a]==1:
			self.direccionx = 0
			self.direcciony = 2
			if x > 0:
				self.x -= 1
		if keys[K_d]:
			self.direccionx = 1
			self.direcciony = 2
			if x < 1260:
				self.x += 1

def get_font(size):
    return font.Font("menu_assets/font.ttf", size)

cave = transform.scale(image.load("firegame_images/cave.png").convert(), (1280, 720))
totem1 = transform.scale(image.load("firegame_images/totem1.png"), (60, 100))
totem2 = transform.scale(image.load("firegame_images/totem2.png"), (60, 100))
totem3 = transform.scale(image.load("firegame_images/totem3.png"), (60, 100))

def main_menu():
    while True:
        #screen.blit(BG, (0, 0))
        screen.fill((0, 0, 0)) 

        MENU_MOUSE_POS = mouse.get_pos()

        MENU_TEXT = get_font(75).render("FIRE GAME", True, (178, 64, 182))
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=image.load("menu_assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        OPTIONS_BUTTON = Button(image=image.load("menu_assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))
        QUIT_BUTTON = Button(image=image.load("menu_assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for evento in event.get():
            if evento.type == QUIT:
                quit()
                exit()
            if evento.type == MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    quit()
                    exit()
            if evento.type==KEYDOWN:
                if evento.key == K_1 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                if evento.key == K_2 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() + 0.1)
                if evento.key == K_ESCAPE:
                    quit()
                    exit()

        display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = mouse.get_pos()

        #screen.blit(BG, (0, 0))
        screen.fill((0, 0, 0)) 

        OPTIONS_TEXT = get_font(45).render("OPTIONS", True, (178, 64, 182))
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        DECREASE_TEXT = get_font(45).render("1 : Decrease Volume", True, (215, 252, 212))
        DECREASE_RECT = DECREASE_TEXT.get_rect(center=(640, 250))
        screen.blit(DECREASE_TEXT, DECREASE_RECT)

        INCREASE_TEXT = get_font(45).render("2 : Increase Volume", True, (215, 252, 212))
        INCREASE_RECT = INCREASE_TEXT.get_rect(center=(640, 400))
        screen.blit(INCREASE_TEXT, INCREASE_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 550), 
                            text_input="BACK", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for evento in event.get():
            if evento.type == QUIT:
                quit()
                exit()
            if evento.type == MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
            if evento.type==KEYDOWN:
                if evento.key == K_1 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                if evento.key == K_2 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() + 0.1)

        display.update()

def play():
    plataforma = Bola(625, 350, 30, 30, 1, 1, 0, (0,0,255), 100, 0)
    timer_plataforma = 0
    while True:
        timer_plataforma += 1
        screen.blit(cave, (0, 0))
        plataforma.Movimiento()
        plataforma.DibujarObjeto()
        if timer_plataforma <= 150:
            screen.blit(totem1, (plataforma.x-14, plataforma.y-50))
        elif timer_plataforma <= 300:
            screen.blit(totem2, (plataforma.x-14, plataforma.y-50))
        else:
            screen.blit(totem3, (plataforma.x-14, plataforma.y-50))
            if timer_plataforma >= 450:
                timer_plataforma = 0
        display.update()
        for evento in event.get():
            if evento.type == QUIT:
                quit()
                exit()
            if evento.type==KEYDOWN:
                if evento.key == K_1 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                if evento.key == K_2 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() + 0.1)
                if evento.key == K_ESCAPE:
                    quit()
                    exit()

main_menu()