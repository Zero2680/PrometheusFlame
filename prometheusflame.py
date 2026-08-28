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

	def Movimiento_Lluvia(self, enemigo):
		if self.check_colisiones(enemigo):
			enemigo.vidas -= 40
			self.y = -100
		if self.y < 750:
			if self.y == -100:
				self.x = randrange(1, 13) * 100
			self.y += 0.25
		if self.y >= 750:
			self.y = -100

	def Movimiento_Catarata(self, enemigo):
		global tent
		if self.check_colisiones(enemigo) == True:
			enemigo.vidas -= 1
			self.x = 1300
		if tent != 2:
			if self.direccionx == 1:
				self.x += 0.25
			if self.direccionx == 0:
				self.x -= 0.25
		if self.x > 1280 or self.x < 0:
			tent = 2

	def Movimiento_Moneda(self, enemigo):
		if self.check_colisiones(enemigo) == True:
			enemigo.puntuacion += 50
			self.x = 1300
		self.puntuacion += 1
		if self.puntuacion == 1:
			self.x = randrange(1, 13) * 100
			self.y = randrange(1, 7) * 100
		if self.puntuacion >= 5000:
			self.x = 1300

def get_font(size):
    return font.Font("menu_assets/font.ttf", size)

cave = transform.scale(image.load("prometheusflame_images/cave.png").convert(), (1280, 720))
totem1 = transform.scale(image.load("prometheusflame_images/totem1.png"), (60, 100))
totem2 = transform.scale(image.load("prometheusflame_images/totem2.png"), (60, 100))
totem3 = transform.scale(image.load("prometheusflame_images/totem3.png"), (60, 100))
totem4 = transform.scale(image.load("prometheusflame_images/totem4.png"), (60, 100))
totem5 = transform.scale(image.load("prometheusflame_images/totem5.png"), (60, 100))
totem6 = transform.scale(image.load("prometheusflame_images/totem6.png"), (60, 100))
totem7 = transform.scale(image.load("prometheusflame_images/totem7.png"), (60, 100))
totem8 = transform.scale(image.load("prometheusflame_images/totem8.png"), (60, 100))
totem9 = transform.scale(image.load("prometheusflame_images/totem9.png"), (60, 100))
ball1 = transform.scale(image.load("prometheusflame_images/ball1.png"), (52, 50))
ball2 = transform.scale(image.load("prometheusflame_images/ball2.png"), (52, 50))
ball3 = transform.scale(image.load("prometheusflame_images/ball3.png"), (52, 50))
waterfall1 = transform.scale(image.load("prometheusflame_images/waterfall1.png"), (100, 720))
waterfall2 = transform.scale(image.load("prometheusflame_images/waterfall2.png"), (100, 720))
waterfall3 = transform.scale(image.load("prometheusflame_images/waterfall3.png"), (100, 720))
coin1 = transform.scale(image.load("prometheusflame_images/coin1.png"), (24, 24))
coin2 = transform.scale(image.load("prometheusflame_images/coin2.png"), (24, 24))
coin3 = transform.scale(image.load("prometheusflame_images/coin3.png"), (24, 24))
coin4 = transform.scale(image.load("prometheusflame_images/coin4.png"), (24, 24))

def main_menu():
    while True:
        #screen.blit(BG, (0, 0))
        screen.fill((0, 0, 0)) 

        MENU_MOUSE_POS = mouse.get_pos()

        MENU_TEXT = get_font(75).render("PROMETHEUS FLAME", True, (255, 252, 46))
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
    gota1 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota2 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    catarata1 = Bola(plataforma.x-250, 0, 20, 720, 1, 0, 0, (255,0,0), 1, 1)
    catarata2 = Bola(plataforma.x-250, 0, 20, 720, 1, 0, 0, (255,0,0), 1, 1)
    moneda1 = Bola(1300, 0, 20, 20, 1, 0, 0, (255, 255, 0), 1, 1)
    timer_plataforma = 0
    timer_ball = 0
    timer_catarata = 0
    timer_catarata2 = 0
    timer_moneda = 0
    timer_moneda2 = 0
    z = -1
    while True:
        global tent
        if z == -1:
            tent = 0
            movimiento = False
            z = 0
        timer_plataforma += 1
        timer_ball += 1
        timer_catarata += 1
        screen.blit(cave, (0, 0))
        plataforma.Movimiento()
        plataforma.DibujarObjeto()
        gota1.Movimiento_Lluvia(plataforma)
        gota2.Movimiento_Lluvia(plataforma)
        gota1.DibujarObjeto()
        gota2.DibujarObjeto()

        timer_moneda += 1
        timer_moneda2 += 1
        if timer_moneda >= 5000:
            moneda1.puntuacion = 0
            timer_moneda = 0
        moneda1.Movimiento_Moneda(plataforma)
        moneda1.DibujarObjeto()
        if timer_moneda2 <= 150:
            screen.blit(coin1, (moneda1.x-2, moneda1.y-2))
        elif timer_moneda2 <= 300:
            screen.blit(coin2, (moneda1.x-2, moneda1.y-2))
        elif timer_moneda2 <= 450:
            screen.blit(coin3, (moneda1.x-2, moneda1.y-2))
        else:
            screen.blit(coin4, (moneda1.x-2, moneda1.y-2))
            if timer_moneda2 >= 600:
                timer_moneda2 = 0

        if timer_catarata == 5000: movimiento = True
        if movimiento == False and tent == 2: tent = 0
        if movimiento == True:
            timer_catarata2 += 1
            if tent == 0:
                catarata1.x = plataforma.x - 200
                catarata2.x = plataforma.x + 200
                if plataforma.x < 640:
                    catarata1.direccionx = 1
                    catarata2.direccionx = 1
                if plataforma.x >= 640:
                    catarata1.direccionx = 0
                    catarata2.direccionx = 0
                tent = 1
            if tent == 2:
                catarata1.x = 1300
                catarata2.x = 1300
                timer_catarata = 0
                timer_catarata2 = 0
                movimiento = False
            catarata1.Movimiento_Catarata(plataforma)
            catarata2.Movimiento_Catarata(plataforma)
            catarata1.DibujarObjeto()
            catarata2.DibujarObjeto()
            if timer_catarata2 <= 100:
                screen.blit(waterfall1, (catarata1.x-42.5, catarata1.y))
                screen.blit(waterfall1, (catarata2.x-42.5, catarata2.y))
            elif timer_catarata2 <= 200:
                screen.blit(waterfall2, (catarata1.x-42.5, catarata1.y))
                screen.blit(waterfall2, (catarata2.x-42.5, catarata2.y))
            else:
                screen.blit(waterfall3, (catarata1.x-42.5, catarata1.y))
                screen.blit(waterfall3, (catarata2.x-42.5, catarata2.y))
                if timer_catarata2 >= 300:
                    timer_catarata2 = 0

        if plataforma.vidas >= 66:
            if timer_plataforma <= 150:
                screen.blit(totem1, (plataforma.x-14, plataforma.y-50))
            elif timer_plataforma <= 300:
                screen.blit(totem2, (plataforma.x-14, plataforma.y-50))
            else:
                screen.blit(totem3, (plataforma.x-14, plataforma.y-50))
                if timer_plataforma >= 450:
                    timer_plataforma = 0
        elif plataforma.vidas >= 33:
            if timer_plataforma <= 150:
                screen.blit(totem4, (plataforma.x-14, plataforma.y-50))
            elif timer_plataforma <= 300:
                screen.blit(totem5, (plataforma.x-14, plataforma.y-50))
            else:
                screen.blit(totem6, (plataforma.x-14, plataforma.y-50))
                if timer_plataforma >= 450:
                    timer_plataforma = 0
        elif plataforma.vidas >= 0:
            if timer_plataforma <= 150:
                screen.blit(totem7, (plataforma.x-14, plataforma.y-50))
            elif timer_plataforma <= 300:
                screen.blit(totem8, (plataforma.x-14, plataforma.y-50))
            else:
                screen.blit(totem9, (plataforma.x-14, plataforma.y-50))
                if timer_plataforma >= 450:
                    timer_plataforma = 0

        if timer_ball <= 150:
            screen.blit(ball1, (gota1.x-14, gota1.y-25))
            screen.blit(ball1, (gota2.x-14, gota2.y-25))
        elif timer_ball <= 300:
            screen.blit(ball2, (gota1.x-14, gota1.y-25))
            screen.blit(ball2, (gota2.x-14, gota2.y-25))
        else:
            screen.blit(ball3, (gota1.x-14, gota1.y-25))
            screen.blit(ball3, (gota2.x-14, gota2.y-25))
            if timer_ball >= 450:
                timer_ball = 0

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
