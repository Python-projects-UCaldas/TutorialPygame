import pygame,sys
from pygame.locals import *
from random import randint

#Color = (70,80,150)
ColorDos = pygame.Color(255, 255, 255)

pygame.init()
ventana = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hola mundo")

Color = (70,80,150)
# pygame.draw.line(ventana, Color, (60,80), (160,100), 8)
# pygame.draw.circle(ventana, (8,70,120), (200,200), 100, 8)
# pygame.draw.rect(ventana, Color, (50,50, 100, 30))
# pygame.draw.polygon(ventana, (80,20,240), ((300,400),(150,100),(40,80)))
pygame.draw.aaline(ventana, (80,20,240), (80,30), (90,50), 1)

Mi_imagen = pygame.image.load("truck.png")
Mi_imagen = pygame.transform.scale(Mi_imagen,(72,44))
#posX,posY = 500, 400
posX = randint(10,400)
posY = randint(10, 300)
#ventana.blit(Mi_imagen,(posX,posY))

velocidad = 2
derecha = True

rectangulo = pygame.rect.Rect(0, 0, 100, 50)
rectanguloDos = pygame.rect.Rect(500, 100, 100, 50)


mifuente = pygame.font.Font(None, 30)
miTexto = mifuente.render("Hola lindo",0,(200, 20 , 79))

mifuenteSistema = pygame.font.Font(None,30)
miTextoDos = mifuenteSistema.render("Colision",0,(200, 20 , 79))

aux = 1
while True:
	Tiempo = int(pygame.time.get_ticks()/1000)
	if aux == Tiempo:
		aux += 1
		#print(Tiempo)
	ventana.fill(ColorDos)
	ventana.blit(Mi_imagen,(posX,posY))
	pygame.draw.rect(ventana, (180, 20, 45), rectanguloDos)
	pygame.draw.rect(ventana, Color, rectangulo)
	rectangulo.left, rectangulo.top = pygame.mouse.get_pos()
	
	if rectangulo.colliderect(rectanguloDos):
		velocidad = 0
		ventana.blit(miTextoDos, (200,200))
		ventana.blit(miTexto,(100, 100))

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				posX -= velocidad
			elif event.key == K_RIGHT:
				posX += velocidad
			elif event.key == K_DOWN:
				posY += velocidad
			elif event.key == K_UP:
				posY -= velocidad
		# elif event.type == pygame.KEYUP:
		# 	if event.key == K_LEFT:
		# 		print("Teclar izquierda liberada")
		# 	elif event.key == K_RIGHT:
		# 		print("Teclar derecha liberada")
	# posX,posY = pygame.mouse.get_pos()
	# posX = posX - 100
	# posY = posY - 50
	if derecha == True:
		if posX < 550:
			posX += velocidad
			rectanguloDos.left = posX
		else:
			derecha = False
	else:
		if posX > 1:
			posX -= velocidad
			rectanguloDos.left = posX
		else:
			derecha = True
	contador = mifuente.render("Tiempo: "+str(Tiempo),0,(120,70,0))
	ventana.blit(contador,(300,400))
	pygame.display.update()
