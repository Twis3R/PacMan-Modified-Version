import pygame
from pygame.locals import *
from constante import*
from creation_fond_niveau import*
pygame.init()

#chargement et affichage de l'image du niveau
fond_niveau(L)
image_niveau = "images/niveau-hamilton.bmp"
fond_niveau = pygame.image.load(image_niveau).convert_alpha()
fenetre.blit(fond_niveau,(0,0))
pygame.display.flip()

#affichage Pac Man
pac=pygame.image.load(image_icone).convert_alpha()
pac=pygame.transform.scale(pac,(40,40)) ## redimensionne l'image
position_perso = pac.get_rect() ##récupère les coord du personnage
position_perso = position_perso.move(40,40) ##deplacer perso en (30,30)
fenetre.blit(pac,position_perso)
pygame.display.flip() ##actualisation de l'affichage

#chragement victoire
fond_win=pygame.image.load(image_bravo).convert()
##fond_win=pygame.transform.scale(fond_win,(450,240))

#affichage sprite noir quand nourriture mangée
sprite_noir=pygame.image.load(image_sprite_noir).convert()
sprite_noir=pygame.transform.scale(sprite_noir,(40,40))
#i et j compteurs pour parcourir la liste de listes L ->savoir si mur ?
i=1
j=1
L[i][j]='V' #case est vide

#affichage objet win
w=pygame.image.load(image_bonus).convert()
w=pygame.transform.scale(w,(40,40))
objet=0
affichage=0
L[4][18]='w'
fenetre.blit(w,(720,160))


#initialisation boucle principale infinie
continuer=True
compteur_nourriture=0
while continuer==True:
    if objet==5:
        fenetre.blit(fond_win,(240,100))
        print ("Bravo vous avez gagnez !")

    for event in pygame.event.get():
        if event.type==pygame.QUIT or objet==5:
            continuer=False
            break
        #gérer le déplacement au clavier
        if event.type==KEYDOWN :
            if event.key==K_s : #s
                if 1<=i<=(nbr_sprite_largeur-2) and L[i+1][j]!='m':
                    fenetre.blit(sprite_noir,position_perso)
                    position_perso=position_perso.move(0,taille_sprite)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i+1][j]=='N':
                        compteur_nourriture=compteur_nourriture+1
                        L[i+1][j]='V'
                    elif L[i+1][j]=='w':
                        objet=objet+1
                        L[i+1][j]='V'
                    i=i+1
            if event.key==K_w : #z
                if 1<=i<=(nbr_sprite_largeur-2)  and L[i-1][j]!='m':
                    fenetre.blit(sprite_noir,position_perso)
                    position_perso=position_perso.move(0,-taille_sprite)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i-1][j]=='N':
                        compteur_nourriture+=1
                        L[i-1][j]='V'
                    elif L[i-1][j]=='w':
                        objet=objet+1
                        L[i-1][j]='V'
                    i=i-1
            if event.key == K_d:	#Si "d"
                if 1<=j<=(nbr_sprite_longueur-2)  and L[i][j+1]!='m':
                    fenetre.blit(sprite_noir,position_perso)
                    position_perso = position_perso.move(taille_sprite,0)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i][j+1]=='N':
                        compteur_nourriture+=1
                        L[i][j+1]='V'
                    elif L[i][j+1]=='w':
                        objet=objet+1
                        L[i][j+1]='V'
                    j=j+1
            if event.key == K_a:   #Si 'q"
                if 1<=j<=(nbr_sprite_longueur-2)  and L[i][j-1]!='m':
                    fenetre.blit(sprite_noir,position_perso)
                    position_perso=position_perso.move(-taille_sprite,0)
                    fenetre.blit(pac,position_perso)
                    pygame.display.flip()
                    if L[i][j-1]=='N':
                        compteur_nourriture+=1
                        L[i][j-1]='V'
                    elif L[i][j-1]=='w':
                        objet=objet+1
                        L[i][j-1]='V'
                    j=j-1
        print(compteur_nourriture)
        print("Vous avez ramassez",objet,"objets, plus que",5-objet,"objets à ramassez pour gagner.")
        #Suite affichage win
        if objet==1:
            L[8][1]='w'
            fenetre.blit(w,(40,320))
        if objet==2:
            L[14][22]='w'
            fenetre.blit(w,(880,560))
        if objet==3:
            L[8][7]='w'
            fenetre.blit(w,(280,320))
        if objet==4:
            L[14][1]='w'
            fenetre.blit(w,(40,560))


#fermeture fenetre
pygame.display.update()
pygame.time.wait(5000) # attend 3000 ms avant de terminer
pygame.quit()