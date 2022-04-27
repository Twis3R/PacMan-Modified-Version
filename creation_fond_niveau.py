"""
    Ce fichier permet de créer le fond d'un niveau
    à l'aide des listes Ligne1, Ligne2, ...
"""

#importation des bibliothèques
import pygame
from pygame.locals import *
from constante import*
pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((longueur_fenetre, largeur_fenetre))

#chargement du fond
fond=pygame.image.load(image_fond).convert()
fenetre.blit(fond,(0,0))

#Titre
pygame.display.set_caption("Pac Man")


#Chargement des images
mur = pygame.image.load(image_mur).convert()
mur = pygame.transform.scale(mur,(taille_sprite,taille_sprite))
nourriture=pygame.image.load(image_nourriture).convert()
nourriture =pygame.transform.scale(nourriture,(taille_sprite,taille_sprite)) ## redimensionne l'image


Ligne1=['m' for i in range(0,nbr_sprite_longueur)]
Ligne2=['m']+['N' for i in range(0,nbr_sprite_longueur-2)]+['m']
Ligne3=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne4=list('mNmBBBmNmBBBmNmmNmNNNNNmmBBmNm')
Ligne5=list('mNmBBBmNmBBBmNmmNmNmmmNmmBBmNm')
Ligne6=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne7=['m']+['N' for i in range(0,nbr_sprite_longueur-2)]+['m']
Ligne8=list('mmmmmNmmmmmmNmmmmNmmmmmmmmmmmm')
Ligne9=list('mNmmmNmNNNNNNNNNNNNNNNNmmmBBBm')
Ligne10=list('mNmmmNmNmmmmmNmmNmmmmmNmmmBBBm')
Ligne11=list('mNNmmNmNmmmmmNmmNmmmmmNmmmBBBm')
Ligne12=list('mmNNNNmNNNNNNNNNNNNNNNNmmmBBBm')
Ligne13=list('mmmmmNmmmmmmNmmmmNmmmmmmmmmmmm')
Ligne14=['m']+['N' for i in range(0,nbr_sprite_longueur-2)]+['m']
Ligne15=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne16=['m' for i in range(0,nbr_sprite_longueur)]
Ligne17=list('mNmBBBmNmBBBmNmmNmBBBmNmBBBmNm')
Ligne18=list('mNmmmmmNmmmmmNmmNmmmmmNmmmmmNm')
Ligne19=['m']+['N' for i in range(0,nbr_sprite_longueur-2)]+['m']
Ligne20=['m' for i in range(0,nbr_sprite_longueur)]

L=[Ligne1,Ligne2,Ligne3,Ligne4,Ligne5,Ligne6,Ligne7,Ligne8,Ligne9,Ligne10,\
Ligne11,Ligne12,Ligne13,Ligne14,Ligne15,Ligne16,Ligne17,Ligne18,Ligne19,Ligne20]

def fond_niveau(L):
    numero_ligne=0
    for ligne in L:
        numero_case=0
        #parcours de la ième Ligne
        for sprite in ligne:
            x=numero_case*taille_sprite
            y=numero_ligne*taille_sprite
            if sprite=="N" :
                fenetre.blit(nourriture,(x,y))
            elif sprite=="m" :
                fenetre.blit(mur,(x,y))
            numero_case=numero_case+1
        numero_ligne=numero_ligne+1
    pygame.image.save(fenetre,'images/niveau-hamilton.bmp')

##fond_niveau(L)
##pac=pygame.image.load(image_icone).convert_alpha()
##pac=pygame.transform.scale(pac,(30,30)) ## redimensionne l'image
##fenetre.blit(pac,(30,30))


###fermeture fenetre
##pygame.display.update()
##pygame.time.wait(3000) # attend 3000 ms avant de terminer
##pygame.quit()




