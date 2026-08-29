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
				self.y -= 0.75
		if keys[K_s]:
			self.direcciony = 0
			if y < 700:
				self.y += 0.75
		if keys[K_a]==1:
			self.direccionx = 0
			self.direcciony = 2
			if x > 0:
				self.x -= 0.75
		if keys[K_d]:
			self.direccionx = 1
			self.direcciony = 2
			if x < 1260:
				self.x += 0.75

	def Movimiento_Lluvia(self, enemigo):
		if self.check_colisiones(enemigo):
			enemigo.vidas -= 1
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
			enemigo.puntuacion += 5000 - self.puntuacion
			self.x = 1300
		self.puntuacion += 1
		if self.puntuacion == 1:
			self.x = randrange(1, 13) * 100
			self.y = randrange(1, 7) * 100
		if self.puntuacion >= 5000:
			self.x = 1300
    
	def Movimiento_Tornado(self, enemigo):
		if self.check_colisiones(enemigo) == True:
			enemigo.vidas -= 1
			if self.x <= 640:
				self.x = -1280
			elif self.x > 640:
				self.x = 2560
			if self.y <= 360:
				self.y = -720
			elif self.y > 360:
				self.y = 1440
		if self.direccionx == 0:
			self.x -= 0.5
		if self.direccionx == 1:
			self.x += 0.5
		if self.direcciony == 0:
			self.y -= 0.5
		if self.direcciony == 1:
			self.y += 0.5
		if self.x <= 0:
			self.direccionx = 1
		if self.x >= 1260:
			self.direccionx = 0
		if self.y <= 0:
			self.direcciony = 1
		if self.y >= 700:
			self.direcciony = 0
    
	def Movimiento_Trampa(self, enemigo):
		if self.puntuacion >= 4500:
			self.color = (125, 125, 125)
			if self.check_colisiones(enemigo) == True:
				enemigo.vidas -= 1
				self.x = 1300
		self.puntuacion += 1
		if self.puntuacion == 1:
			self.x = randrange(1, 13) * 100
			self.y = randrange(1, 7) * 100
		if self.puntuacion >= 5000:
			self.color = (0, 125, 255)
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
twister1 = transform.scale(image.load("prometheusflame_images/twister1.png"), (75, 75))
twister2 = transform.scale(image.load("prometheusflame_images/twister2.png"), (75, 75))
twister3 = transform.scale(image.load("prometheusflame_images/twister3.png"), (75, 75))
tramp1 = transform.scale(image.load("prometheusflame_images/tramp1.png"), (64, 18))
tramp2 = transform.scale(image.load("prometheusflame_images/tramp2.png"), (64, 18))
tramp3 = transform.scale(image.load("prometheusflame_images/tramp3.png"), (64, 18))
tramp4 = transform.scale(image.load("prometheusflame_images/tramp4.png"), (64, 80))
tramp5 = transform.scale(image.load("prometheusflame_images/tramp5.png"), (64, 80))
tramp6 = transform.scale(image.load("prometheusflame_images/tramp6.png"), (64, 80))

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
    plataforma = Bola(625, 350, 30, 30, 1, 1, 0, (0,0,255), 3, 0)
    gota1 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota2 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota3 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota4 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota5 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota6 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota7 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    gota8 = Bola(0, -100, 20, 20, 0, 0, 0, (255, 125, 255), 1, 1)
    catarata1 = Bola(plataforma.x-250, 0, 20, 720, 1, 0, 0, (255,0,0), 1, 1)
    catarata2 = Bola(plataforma.x-250, 0, 20, 720, 1, 0, 0, (255,0,0), 1, 1)
    moneda1 = Bola(1300, 0, 20, 20, 1, 0, 0, (255, 255, 0), 1, 1)
    moneda2 = Bola(1300, 0, 20, 20, 1, 0, 0, (255, 255, 0), 1, 1)
    moneda3 = Bola(1300, 0, 20, 20, 1, 0, 0, (255, 255, 0), 1, 1)
    tornado1 = Bola(-1280, -720, 20, 30, 1, 0, 0, (0, 255, 255), 1, 1)
    tornado2 = Bola(-1280, -720, 20, 30, 1, 0, 0, (0, 255, 255), 1, 1)
    tornado3 = Bola(2560, 1440, 20, 30, 1, 0, 0, (0, 255, 255), 1, 1)
    tornado4 = Bola(-1280, -720, 20, 30, 1, 0, 0, (0, 255, 255), 1, 1)
    tornado5 = Bola(2560, 1440, 20, 30, 1, 0, 0, (0, 255, 255), 1, 1)
    tornado6 = Bola(-1280, -720, 20, 30, 1, 0, 0, (0, 255, 255), 1, 1)
    tornado7 = Bola(2560, 1440, 20, 30, 1, 0, 0, (0, 255, 255), 1, 1)
    trampa1 = Bola(1300, 0, 40, 40, 1, 0, 0, (0, 125, 255), 1, 1)
    trampa2 = Bola(1300, 0, 40, 40, 1, 0, 0, (0, 125, 255), 1, 1)
    trampa3 = Bola(1300, 0, 40, 40, 1, 0, 0, (0, 125, 255), 1, 1)
    trampa4 = Bola(1300, 0, 40, 40, 1, 0, 0, (0, 125, 255), 1, 1)
    trampa5 = Bola(1300, 0, 40, 40, 1, 0, 0, (0, 125, 255), 1, 1)
    trampa6 = Bola(1300, 0, 40, 40, 1, 0, 0, (0, 125, 255), 1, 1)
    trampa7 = Bola(1300, 0, 40, 40, 1, 0, 0, (0, 125, 255), 1, 1)
    timer_plataforma = 0
    timer_ball = 0
    timer_catarata = 0
    timer_catarata2 = 0
    timer_moneda = 0
    timer_moneda2 = 0
    timer_tornado = 0
    z = -1
    while True:
        global tent
        if z == -1:
            tent = 0
            movimiento = False
            z = 0
        timer_plataforma += 1
        screen.blit(cave, (0, 0))
        plataforma.Movimiento()

        #MONEDA
        timer_moneda += 1
        timer_moneda2 += 1
        if timer_moneda >= 5000:
            moneda1.puntuacion = 0
            moneda2.puntuacion = 0
            moneda3.puntuacion = 0
            trampa1.puntuacion = 0
            trampa2.puntuacion = 0
            trampa3.puntuacion = 0
            trampa4.puntuacion = 0
            trampa5.puntuacion = 0
            trampa6.puntuacion = 0
            trampa7.puntuacion = 0
            timer_moneda = 0
        moneda1.Movimiento_Moneda(plataforma)
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
        
        if plataforma.puntuacion >= 30000:
            moneda2.Movimiento_Moneda(plataforma)
            if timer_moneda2 <= 150:
                screen.blit(coin1, (moneda2.x-2, moneda2.y-2))
            elif timer_moneda2 <= 300:
                screen.blit(coin2, (moneda2.x-2, moneda2.y-2))
            elif timer_moneda2 <= 450:
                screen.blit(coin3, (moneda2.x-2, moneda2.y-2))
            else:
                screen.blit(coin4, (moneda2.x-2, moneda2.y-2))
                if timer_moneda2 >= 600:
                    timer_moneda2 = 0
        
        if plataforma.puntuacion >= 60000:
            moneda3.Movimiento_Moneda(plataforma)
            if timer_moneda2 <= 150:
                screen.blit(coin1, (moneda3.x-2, moneda3.y-2))
            elif timer_moneda2 <= 300:
                screen.blit(coin2, (moneda3.x-2, moneda3.y-2))
            elif timer_moneda2 <= 450:
                screen.blit(coin3, (moneda3.x-2, moneda3.y-2))
            else:
                screen.blit(coin4, (moneda3.x-2, moneda3.y-2))
                if timer_moneda2 >= 600:
                    timer_moneda2 = 0

        #TORNADO
        if plataforma.puntuacion >= 10000:
            timer_tornado += 1
            tornado1.Movimiento_Tornado(plataforma)
            if timer_tornado <= 150:
                screen.blit(twister1, (tornado1.x-28, tornado1.y-25))
            elif timer_tornado <= 300:
                screen.blit(twister2, (tornado1.x-28, tornado1.y-25))
            else:
                screen.blit(twister3, (tornado1.x-28, tornado1.y-25))
                if timer_tornado >= 450:
                    timer_tornado = 0
        
        if plataforma.puntuacion >= 50000:
            tornado2.Movimiento_Tornado(plataforma)
            tornado3.Movimiento_Tornado(plataforma)
            if timer_tornado <= 150:
                screen.blit(twister1, (tornado2.x-28, tornado2.y-25))
                screen.blit(twister1, (tornado3.x-28, tornado3.y-25))
            elif timer_tornado <= 300:
                screen.blit(twister2, (tornado2.x-28, tornado2.y-25))
                screen.blit(twister2, (tornado3.x-28, tornado3.y-25))
            else:
                screen.blit(twister3, (tornado2.x-28, tornado2.y-25))
                screen.blit(twister3, (tornado3.x-28, tornado3.y-25))
                if timer_tornado >= 450:
                    timer_tornado = 0
        
        if plataforma.puntuacion >= 100000:
            tornado4.Movimiento_Tornado(plataforma)
            tornado5.Movimiento_Tornado(plataforma)
            if timer_tornado <= 150:
                screen.blit(twister1, (tornado4.x-28, tornado4.y-25))
                screen.blit(twister1, (tornado5.x-28, tornado5.y-25))
            elif timer_tornado <= 300:
                screen.blit(twister2, (tornado4.x-28, tornado4.y-25))
                screen.blit(twister2, (tornado5.x-28, tornado5.y-25))
            else:
                screen.blit(twister3, (tornado4.x-28, tornado4.y-25))
                screen.blit(twister3, (tornado5.x-28, tornado5.y-25))
                if timer_tornado >= 450:
                    timer_tornado = 0
        
        if plataforma.puntuacion >= 200000:
            tornado6.Movimiento_Tornado(plataforma)
            tornado7.Movimiento_Tornado(plataforma)
            if timer_tornado <= 150:
                screen.blit(twister1, (tornado6.x-28, tornado6.y-25))
                screen.blit(twister1, (tornado7.x-28, tornado7.y-25))
            elif timer_tornado <= 300:
                screen.blit(twister2, (tornado6.x-28, tornado6.y-25))
                screen.blit(twister2, (tornado7.x-28, tornado7.y-25))
            else:
                screen.blit(twister3, (tornado6.x-28, tornado6.y-25))
                screen.blit(twister3, (tornado7.x-28, tornado7.y-25))
                if timer_tornado >= 450:
                    timer_tornado = 0
        
        #TRAMPA
        if plataforma.puntuacion >= 20000:
            trampa1.Movimiento_Trampa(plataforma)
            if trampa1.puntuacion <= 4300:
                screen.blit(tramp1, (trampa1.x-14, trampa1.y+25))
            elif trampa1.puntuacion <= 4400:
                screen.blit(tramp2, (trampa1.x-14, trampa1.y+25))
            elif trampa1.puntuacion <= 4500:
                screen.blit(tramp3, (trampa1.x-14, trampa1.y+25))
            elif trampa1.puntuacion <= 4700:
                screen.blit(tramp4, (trampa1.x-14, trampa1.y-35))
            elif trampa1.puntuacion <= 4900:
                screen.blit(tramp5, (trampa1.x-14, trampa1.y-35))
            elif trampa1.puntuacion <= 5000:
                screen.blit(tramp6, (trampa1.x-14, trampa1.y-35))
        
        if plataforma.puntuacion >= 60000:
            trampa2.Movimiento_Trampa(plataforma)
            trampa3.Movimiento_Trampa(plataforma)
            if trampa1.puntuacion <= 4300:
                screen.blit(tramp1, (trampa2.x-14, trampa2.y+25))
                screen.blit(tramp1, (trampa3.x-14, trampa3.y+25))
            elif trampa1.puntuacion <= 4400:
                screen.blit(tramp2, (trampa2.x-14, trampa2.y+25))
                screen.blit(tramp2, (trampa3.x-14, trampa3.y+25))
            elif trampa1.puntuacion <= 4500:
                screen.blit(tramp3, (trampa2.x-14, trampa2.y+25))
                screen.blit(tramp3, (trampa3.x-14, trampa3.y+25))
            elif trampa1.puntuacion <= 4700:
                screen.blit(tramp4, (trampa2.x-14, trampa2.y-35))
                screen.blit(tramp4, (trampa3.x-14, trampa3.y-35))
            elif trampa1.puntuacion <= 4900:
                screen.blit(tramp5, (trampa2.x-14, trampa2.y-35))
                screen.blit(tramp5, (trampa3.x-14, trampa3.y-35))
            elif trampa1.puntuacion <= 5000:
                screen.blit(tramp6, (trampa2.x-14, trampa2.y-35))
                screen.blit(tramp6, (trampa3.x-14, trampa3.y-35))
        
        if plataforma.puntuacion >= 100000:
            trampa4.Movimiento_Trampa(plataforma)
            trampa5.Movimiento_Trampa(plataforma)
            if trampa1.puntuacion <= 4300:
                screen.blit(tramp1, (trampa4.x-14, trampa4.y+25))
                screen.blit(tramp1, (trampa5.x-14, trampa5.y+25))
            elif trampa1.puntuacion <= 4400:
                screen.blit(tramp2, (trampa4.x-14, trampa4.y+25))
                screen.blit(tramp2, (trampa5.x-14, trampa5.y+25))
            elif trampa1.puntuacion <= 4500:
                screen.blit(tramp3, (trampa4.x-14, trampa4.y+25))
                screen.blit(tramp3, (trampa5.x-14, trampa5.y+25))
            elif trampa1.puntuacion <= 4700:
                screen.blit(tramp4, (trampa4.x-14, trampa4.y-35))
                screen.blit(tramp4, (trampa5.x-14, trampa5.y-35))
            elif trampa1.puntuacion <= 4900:
                screen.blit(tramp5, (trampa4.x-14, trampa4.y-35))
                screen.blit(tramp5, (trampa5.x-14, trampa5.y-35))
            elif trampa1.puntuacion <= 5000:
                screen.blit(tramp6, (trampa4.x-14, trampa4.y-35))
                screen.blit(tramp6, (trampa5.x-14, trampa5.y-35))

        if plataforma.puntuacion >= 200000:
            trampa6.Movimiento_Trampa(plataforma)
            trampa7.Movimiento_Trampa(plataforma)
            if trampa1.puntuacion <= 4300:
                screen.blit(tramp1, (trampa6.x-14, trampa6.y+25))
                screen.blit(tramp1, (trampa7.x-14, trampa7.y+25))
            elif trampa1.puntuacion <= 4400:
                screen.blit(tramp2, (trampa6.x-14, trampa6.y+25))
                screen.blit(tramp2, (trampa7.x-14, trampa7.y+25))
            elif trampa1.puntuacion <= 4500:
                screen.blit(tramp3, (trampa6.x-14, trampa6.y+25))
                screen.blit(tramp3, (trampa7.x-14, trampa7.y+25))
            elif trampa1.puntuacion <= 4700:
                screen.blit(tramp4, (trampa6.x-14, trampa6.y-35))
                screen.blit(tramp4, (trampa7.x-14, trampa7.y-35))
            elif trampa1.puntuacion <= 4900:
                screen.blit(tramp5, (trampa6.x-14, trampa6.y-35))
                screen.blit(tramp5, (trampa7.x-14, trampa7.y-35))
            elif trampa1.puntuacion <= 5000:
                screen.blit(tramp6, (trampa6.x-14, trampa6.y-35))
                screen.blit(tramp6, (trampa7.x-14, trampa7.y-35))

        #CATARATA
        if plataforma.puntuacion >= 30000:
            timer_catarata += 1
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

        #TOTEM
        if plataforma.vidas >= 3:
            if timer_plataforma <= 150:
                screen.blit(totem1, (plataforma.x-14, plataforma.y-50))
            elif timer_plataforma <= 300:
                screen.blit(totem2, (plataforma.x-14, plataforma.y-50))
            else:
                screen.blit(totem3, (plataforma.x-14, plataforma.y-50))
                if timer_plataforma >= 450:
                    timer_plataforma = 0
        elif plataforma.vidas >= 2:
            if timer_plataforma <= 150:
                screen.blit(totem4, (plataforma.x-14, plataforma.y-50))
            elif timer_plataforma <= 300:
                screen.blit(totem5, (plataforma.x-14, plataforma.y-50))
            else:
                screen.blit(totem6, (plataforma.x-14, plataforma.y-50))
                if timer_plataforma >= 450:
                    timer_plataforma = 0
        else:
            if timer_plataforma <= 150:
                screen.blit(totem7, (plataforma.x-14, plataforma.y-50))
            elif timer_plataforma <= 300:
                screen.blit(totem8, (plataforma.x-14, plataforma.y-50))
            else:
                screen.blit(totem9, (plataforma.x-14, plataforma.y-50))
                if timer_plataforma >= 450:
                    timer_plataforma = 0

        #LLUVIA
        if plataforma.puntuacion > 0:
            timer_ball += 1
            gota1.Movimiento_Lluvia(plataforma)
            gota2.Movimiento_Lluvia(plataforma)
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
        
        if plataforma.puntuacion >= 40000:
            gota3.Movimiento_Lluvia(plataforma)
            gota4.Movimiento_Lluvia(plataforma)
            if timer_ball <= 150:
                screen.blit(ball1, (gota3.x-14, gota3.y-25))
                screen.blit(ball1, (gota4.x-14, gota4.y-25))
            elif timer_ball <= 300:
                screen.blit(ball2, (gota3.x-14, gota3.y-25))
                screen.blit(ball2, (gota4.x-14, gota4.y-25))
            else:
                screen.blit(ball3, (gota3.x-14, gota3.y-25))
                screen.blit(ball3, (gota4.x-14, gota4.y-25))
                if timer_ball >= 450:
                    timer_ball = 0

        if plataforma.puntuacion >= 100000:
            gota5.Movimiento_Lluvia(plataforma)
            gota6.Movimiento_Lluvia(plataforma)
            if timer_ball <= 150:
                screen.blit(ball1, (gota5.x-14, gota5.y-25))
                screen.blit(ball1, (gota6.x-14, gota6.y-25))
            elif timer_ball <= 300:
                screen.blit(ball2, (gota5.x-14, gota5.y-25))
                screen.blit(ball2, (gota6.x-14, gota6.y-25))
            else:
                screen.blit(ball3, (gota5.x-14, gota5.y-25))
                screen.blit(ball3, (gota6.x-14, gota6.y-25))
                if timer_ball >= 450:
                    timer_ball = 0
        
        if plataforma.puntuacion >= 200000:
            gota7.Movimiento_Lluvia(plataforma)
            gota8.Movimiento_Lluvia(plataforma)
            if timer_ball <= 150:
                screen.blit(ball1, (gota7.x-14, gota7.y-25))
                screen.blit(ball1, (gota8.x-14, gota8.y-25))
            elif timer_ball <= 300:
                screen.blit(ball2, (gota7.x-14, gota7.y-25))
                screen.blit(ball2, (gota8.x-14, gota8.y-25))
            else:
                screen.blit(ball3, (gota7.x-14, gota7.y-25))
                screen.blit(ball3, (gota8.x-14, gota8.y-25))
                if timer_ball >= 450:
                    timer_ball = 0
        
        if plataforma.vidas <= 0:
            final(plataforma.puntuacion)

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

def final(score):
    while True:
        SCORE_MOUSE_POS = mouse.get_pos()

        FS_TEXT = get_font(45).render("FINAL SCORE:", True, (255, 252, 46))
        FS_RECT = FS_TEXT.get_rect(center=(640, 100))
        screen.blit(FS_TEXT, FS_RECT)

        SCORE_TEXT = get_font(45).render(str(score), True, (255, 252, 46))
        SCORE_RECT = SCORE_TEXT.get_rect(center=(640, 200))
        screen.blit(SCORE_TEXT, SCORE_RECT)

        if score < 100000:
            SENTENCE_TEXT = get_font(45).render("That's a terrible score", True, (255, 252, 46))
            SENTENCE_RECT = SENTENCE_TEXT.get_rect(center=(640, 300))
            screen.blit(SENTENCE_TEXT, SENTENCE_RECT)
        elif score < 200000:
            SENTENCE_TEXT = get_font(45).render("Nice! You're pretty good!", True, (255, 252, 46))
            SENTENCE_RECT = SENTENCE_TEXT.get_rect(center=(640, 300))
            screen.blit(SENTENCE_TEXT, SENTENCE_RECT)
        else:
            SENTENCE_TEXT = get_font(45).render('Wow! You’re in the top 10%', True, (255, 252, 46))
            SENTENCE_RECT = SENTENCE_TEXT.get_rect(center=(640, 300))
            screen.blit(SENTENCE_TEXT, SENTENCE_RECT)

        SCORE_RETRY = Button(image=None, pos=(640, 450), 
                            text_input="RETRY", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        SCORE_RETRY.changeColor(SCORE_MOUSE_POS)
        SCORE_RETRY.update(screen)

        SCORE_BACK = Button(image=None, pos=(640, 600), 
                            text_input="BACK", font=get_font(75), base_color=(215, 252, 212), hovering_color=(255, 255, 255))

        SCORE_BACK.changeColor(SCORE_MOUSE_POS)
        SCORE_BACK.update(screen)

        for evento in event.get():
            if evento.type == QUIT:
                quit()
                exit()
            if evento.type == MOUSEBUTTONDOWN:
                if SCORE_RETRY.checkForInput(SCORE_MOUSE_POS):
                    play()
                if SCORE_BACK.checkForInput(SCORE_MOUSE_POS):
                    main_menu()
            if evento.type==KEYDOWN:
                if evento.key == K_1 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() - 0.1)
                if evento.key == K_2 and mixer.music.get_volume() > 0.0:
                    mixer.music.set_volume(mixer.music.get_volume() + 0.1)
                if evento.key == K_ESCAPE:
                    quit()
                    exit()

        display.update()

main_menu()
