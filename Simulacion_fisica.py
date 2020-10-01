import pygame
from pygame.locals import *
import math

canvas = pygame.display.set_mode((1000,1000))
pygame.init()
runnig = True

aceleracion_gravitatoria = 10
radio = 300
desfase = 0 # rad
velocidad_inicial = 0 # rad/s
masa = 1 # kg

class pendulo():
    def __init__(self,radio,desfase,velocidad_inicial,masa):
        self.radio = radio
        self.angulo = desfase
        self.velocidad_angular = velocidad_inicial
        self.acceleracion = 0
        self.masa = masa
    def update(self):
        self.fuerza_tangencial = math.cos(-self.angulo)*(aceleracion_gravitatoria*self.masa)
        self.acceleracion = self.fuerza_tangencial/self.masa
        self.velocidad_angular += (self.acceleracion/radio)
        self.angulo = self.angulo - self.velocidad_angular/1000 # el 10000 es para ajustar la velocidad de la simulacion (mas es mas lento)
        if self.angulo > 0:
            print(self.angulo)
    def draw(self,canvas):
        pygame.draw.circle(canvas,(255,255,255),(500,500),(self.radio))
        pygame.draw.circle(canvas,(255,0,255),(int(math.cos(self.angulo)*self.radio)+500,int(500-math.sin(self.angulo)*self.radio)),(50))

Pendulo = pendulo(radio,desfase,velocidad_inicial,masa)

while runnig:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnig = False
    
    canvas.fill((0,0,0))
            
    Pendulo.update()
    Pendulo.draw(canvas)
    pygame.display.flip()

pygame.quit()
        
