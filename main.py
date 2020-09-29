import pygame
import os
from random import randrange
import time

#Luodaan peli-ikkuna
LEVEYS, KORKEUS=800,800
IKKUNA=pygame.display.set_mode((LEVEYS,KORKEUS))
pygame.display.set_caption("SpedenSpeli")




#Ladataan kuvia

SPELI_KONE=pygame.transform.scale(pygame.image.load(os.path.join("assets","pelikone_muokattu.png")),(LEVEYS,KORKEUS))


#TEHDÄÄN MAINLOOP

def main():
  ajetaan=True
  #Määritetään pelin fps
  FPS=60
  #Määritetään kello
  kello = pygame.time.Clock()

  def piirretaan():
    IKKUNA.blit(SPELI_KONE,(0,0))
    pygame.display.update()

    

  while ajetaan:
    kello.tick(FPS)
    piirretaan()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          ajetaan=False


          

      
  

  
