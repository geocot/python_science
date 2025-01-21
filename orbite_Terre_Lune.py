#******************
#*Martin Couture  *
#******************
import pygame, math
#Initialisation
pygame.init()
#Constantes pour le programme.
LARGEUR = 800
HAUTEUR = 800
# Rayon des sphères
RAYON_TERRE = 100
RAYON_LUNE = 10
RAYON_TERRELUNE = 250
CENTRE_ECRAN = (LARGEUR/2, HAUTEUR/2)

#Création de l'écran
ecran = pygame.display.set_mode((LARGEUR,HAUTEUR))
#Titre
pygame.display.set_caption("Orbite de la Lune")

angle = 0
clock = pygame.time.Clock()
#Pour l'arret du jeu
arretJeu = False
while not arretJeu:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE :
                arretJeu = True

        if event.type == pygame.QUIT:
            arretJeu = True

    #Nombre d'animations par seconde
    clock.tick(60)
    ecran.fill((0, 0, 0))
    terre = pygame.draw.circle(ecran,"blue",CENTRE_ECRAN, RAYON_TERRE)
    lune = pygame.draw.circle(ecran, "white", (RAYON_TERRELUNE*math.cos(angle)+CENTRE_ECRAN[0],
                              RAYON_TERRELUNE*math.sin(angle)+CENTRE_ECRAN[1]), RAYON_LUNE)
    #Pour animer
    pygame.display.flip()
    angle += 0.005

