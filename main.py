"""
Jeu Pac-Man crée par Paul FERREIRA. Programmée sur Python avec Pygame.
"""

import pygame
from pygame.locals import *
import random
import time

fps = 60
gains = 10
vitesse = 2.5
temps_direction = (30 / vitesse) * 4

pygame.init()


def level_initialisation_convertisation():
    level_liste = []
    with open("level_1", "r") as fichier:
        for ligne in fichier:
            level_ligne = []
            for detail in ligne:
                if detail == "0":
                    level_ligne.append(0)
                if detail == "1":
                    level_ligne.append(1)
                if detail == "2":
                    level_ligne.append(2)
                if detail == "3":
                    level_ligne.append(3)
                if detail == "4":
                    level_ligne.append(4)
                if detail == "v":
                    level_ligne.append("v")
            level_liste.append(level_ligne)
    return level_liste


def level_affichage(level_l):
    y = 0
    for ligne in level_l:
        x = 0
        for detail in ligne:
            if detail == 0 or detail == 2 or detail == 3 or detail == 4:
                fenetre.blit(rect_noir, (x, y))
            if detail == "v":
                fenetre.blit(rect_noir, (x, y))
            if detail == 1:
                fenetre.blit(rect_viollet, (x, y))
            x += 30
        y += 30


def level_affichage_pastille(level_l):
    y = 15
    for ligne in level_l:
        x = 15
        for detail in ligne:
            if detail == 2:
                pygame.draw.circle(fenetre, (255, 255, 255), (x, y), 4)
            x += 30
        y += 30


def affichage_niveau():
    level_affichage(level_list)
    level_affichage_pastille(level_list)
    fenetre.blit(texte_titre_object, (60, 30))


def condition_avancer_haut(liste, x, y):
    if liste[y - 1][x] == 0 or liste[y - 1][x] == 2:
        return True
    else:
        return False


def condition_avancer_bas(liste, x, y):
    if liste[y + 1][x] == 0 or liste[y + 1][x] == 2:
        return True
    else:
        return False


def condition_avancer_gauche(liste, x, y):
    if liste[y][x - 1] == 0 or liste[y][x - 1] == 2 or liste[y][x - 1] == 3 or liste[y][x - 1] == 4:
        return True
    else:
        return False


def condition_avancer_droite(liste, x, y):
    if liste[y][x + 1] == 0 or liste[y][x + 1] == 2 or liste[y][x + 1] == 3 or liste[y][x + 1] == 4:
        return True
    else:
        return False


def choix_direction(liste, x, y):
    continuer = 1
    choix = random.choice(["haut", "bas", "gauche", "droite"])
    while continuer:
        choix = random.choice(["haut", "bas", "gauche", "droite"])
        if choix == "haut":
            if condition_avancer_haut(liste, x, y):
                continuer = 0
        elif choix == "bas":
            if condition_avancer_bas(liste, x, y):
                continuer = 0
        elif choix == "gauche":
            if condition_avancer_gauche(liste, x, y):
                continuer = 0
        elif choix == "droite":
            if condition_avancer_droite(liste, x, y):
                continuer = 0
    return choix


def deplacement_fantomme(coordonee_fan, modif_f, v, liste):
    if coordonee_fan[0][0] * 30 == coordonee_fan[1][0] and coordonee_fan[0][1] * 30 == \
            coordonee_fan[1][1]:
        if coordonee_fan[2] == "haut":
            if condition_avancer_haut(liste, coordonee_fan[0][0], coordonee_fan[0][1]):
                coordonee_fan[0][1] -= 1
                coordonee_fan[1][1] -= v
                modif_f = "haut"
            else:
                coordonee_fan[2] = choix_direction(liste, coordonee_fan[0][0], coordonee_fan[0][1])
        elif coordonee_fan[2] == "bas":
            if condition_avancer_bas(liste, coordonee_fan[0][0], coordonee_fan[0][1]):
                coordonee_fan[0][1] += 1
                coordonee_fan[1][1] += v
                modif_f = "bas"
            else:
                coordonee_fan[2] = choix_direction(liste, coordonee_fan[0][0], coordonee_fan[0][1])
        elif coordonee_fan[2] == "gauche":
            if condition_avancer_gauche(liste, coordonee_fan[0][0], coordonee_fan[0][1]):
                coordonee_fan[0][0] -= 1
                coordonee_fan[1][0] -= v
                modif_f = "gauche"
            else:
                coordonee_fan[2] = choix_direction(liste, coordonee_fan[0][0], coordonee_fan[0][1])
        elif coordonee_fan[2] == "droite":
            if condition_avancer_droite(liste, coordonee_fan[0][0], coordonee_fan[0][1]):
                coordonee_fan[0][0] += 1
                coordonee_fan[1][0] += v
                modif_f = "droite"
            else:
                coordonee_fan[2] = choix_direction(liste, coordonee_fan[0][0], coordonee_fan[0][1])
    else:
        if modif_f == "haut":
            coordonee_fan[1][1] -= v
        elif modif_f == "bas":
            coordonee_fan[1][1] += v
        elif modif_f == "gauche":
            coordonee_fan[1][0] -= v
        elif modif_f == "droite":
            coordonee_fan[1][0] += v
    return modif_f, coordonee_fan


def contact_fantomme(x_f, y_f, x_p, y_p, vie):
    if x_f == x_p and y_f == y_p:
        vie -= 1
        return 1, vie
    else:
        return 0, vie


"""intiitalisation de la fenêtre"""

fenetre = pygame.display.set_mode((690, 900))
pygame.display.set_caption("Pac-man")

"""initialisation des image"""

image_menu = pygame.image.load("menu.png").convert()
level_suivant_image = pygame.image.load("level_suivant.png").convert()
option_image = pygame.image.load("option.png").convert()
valide_option_image = pygame.image.load("valide.png").convert_alpha()
game_over_image = pygame.image.load("gameover.png").convert()
rect_noir = pygame.image.load("rectangle_noir.png").convert()
rect_viollet = pygame.image.load("rectangle_viollet.png").convert()
pac_man = pygame.image.load("pac_man.png").convert_alpha()
fan_bleu = pygame.image.load("fantomme_bleu.png").convert_alpha()
fan_jaune = pygame.image.load("fantomme_jaune.png").convert_alpha()
fan_rose = pygame.image.load("fantomme_rose.png").convert_alpha()
fan_rouge = pygame.image.load("fantomme_rouge.png").convert_alpha()

"""initialisation des texte"""
texte_titre = pygame.font.Font(None, 60)
points_titre = pygame.font.Font(None, 35)
vie_titre = pygame.font.Font(None, 35)
game_over_points_titre = pygame.font.Font(None, 40)
record_titre = pygame.font.Font(None, 36)
game_over_record = pygame.font.Font(None, 40)
level_titre = pygame.font.Font(None, 72)
texte_titre_object = texte_titre.render("Pac Man", True, (255, 255, 255))

print("Jeu Pac-Man crée sur Python avec Pygame par Paul FERREIRA")

"""Boucle principale"""

boucle_niveau = 0
boucle_menu = 1
boucle_jeu = 1
boucle_option = 0
boucle_gameover = 0
while boucle_jeu:
    count_animation = 0
    while boucle_menu:
        pygame.time.Clock().tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                boucle_menu = 0
                boucle_jeu = 0
            if event.type == MOUSEBUTTONUP and event.button == 1:
                if 550 < event.pos[0] < 680 and 20 < event.pos[1] < 80:
                    boucle_option = 1
                    boucle_menu = 0
                if 190 < event.pos[0] < 390 and 415 < event.pos[1] < 510:
                    """Lancement du jeux et initialisation de toute les variables"""
                    boucle_niveau = 1
                    level_list = level_initialisation_convertisation()
                    vie_p = 3
                    x_pac_man_i = 6
                    y_pac_man_i = 21
                    x_pac_man = x_pac_man_i
                    y_pac_man = y_pac_man_i
                    x_pac_man_coordonee = x_pac_man * 30
                    y_pac_man_coordonee = y_pac_man * 30
                    direction = ""
                    modif = ""
                    recommencer = 0
                    coordonee_fan_bleu = [[16, 12], [14 * 30 + 60, 7 * 30 + 150], "haut"]
                    coordonee_fan_jaune = [[6, 13], [4 * 30 + 60, 8 * 30 + 150], "haut"]
                    coordonee_fan_rose = [[10, 20], [8 * 30 + 60, 15 * 30 + 150], "haut"]
                    coordonee_fan_rouge = [[11, 9], [9 * 30 + 60, 4 * 30 + 150], "haut"]
                    modif_rouge = ""
                    modif_bleu = ""
                    modif_jaune = ""
                    modif_rose = ""
                    points = 0
                    level = 1
                    boucle_menu = 0

        fenetre.blit(image_menu, (0, 0))
        fichier = open("record", "r")
        record = fichier.read()
        fichier.close()
        record_titre_obj = record_titre.render(record, True, (255, 255, 255))
        fenetre.blit(record_titre_obj, (254, 160))
        pygame.display.flip()

    while boucle_option:
        pygame.time.Clock().tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                boucle_option = 0
                boucle_jeu = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    boucle_menu = 1
                    boucle_option = 0

            if event.type == MOUSEBUTTONUP and event.button == 1:
                if 100 < event.pos[0] < 165 and 275 < event.pos[1] < 325:
                    vitesse = 2.5
                if 435 < event.pos[0] < 500 and 275 < event.pos[1] < 325:
                    vitesse = 5
                if 100 < event.pos[0] < 165 and 640 < event.pos[1] < 700:
                    fps = 30
                if 435 < event.pos[0] < 500 and 640 < event.pos[1] < 700:
                    fps = 60

        fenetre.blit(option_image, (0, 0))
        if vitesse == 2.5:
            fenetre.blit(valide_option_image, (109, 284))
        else:
            fenetre.blit(valide_option_image, (444, 284))
        if fps == 30:
            fenetre.blit(valide_option_image, (109, 649))
        else:
            fenetre.blit(valide_option_image, (444, 649))

        pygame.display.flip()

    while boucle_niveau:
        pygame.time.Clock().tick(fps)
        affichage_niveau()

        """Gestion des touche"""
        for event in pygame.event.get():
            if event.type == QUIT:
                boucle_jeu = 0
                boucle_niveau = 0
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = "gauche"
                if event.key == K_RIGHT:
                    direction = "droite"
                if event.key == K_UP:
                    direction = "haut"
                if event.key == K_DOWN:
                    direction = "bas"
                if event.key == K_a:
                    direction = "gauche"
                if event.key == K_d:
                    direction = "droite"
                if event.key == K_w:
                    direction = "haut"
                if event.key == K_s:
                    direction = "bas"

        """deplacement du personnage"""
        if y_pac_man * 30 == y_pac_man_coordonee and x_pac_man * 30 == x_pac_man_coordonee:
            if direction == "haut":
                if condition_avancer_haut(level_list, x_pac_man, y_pac_man):
                    y_pac_man_coordonee -= vitesse
                    y_pac_man -= 1
                    modif = "haut"
            elif direction == "gauche":
                if condition_avancer_gauche(level_list, x_pac_man, y_pac_man):
                    x_pac_man -= 1
                    if level_list[y_pac_man][x_pac_man] == 3:
                        x_pac_man = 19
                        y_pac_man = 15
                        x_pac_man_coordonee = x_pac_man * 30
                        y_pac_man_coordonee = y_pac_man * 30
                    else:
                        x_pac_man_coordonee -= vitesse
                        modif = "gauche"
            elif direction == "droite":
                if condition_avancer_droite(level_list, x_pac_man, y_pac_man):
                    x_pac_man += 1
                    if level_list[y_pac_man][x_pac_man] == 4:
                        x_pac_man = 4
                        y_pac_man = 15
                        x_pac_man_coordonee = x_pac_man * 30
                        y_pac_man_coordonee = y_pac_man * 30
                    else:
                        x_pac_man_coordonee += vitesse
                        modif = "droite"
            elif direction == "bas":
                if condition_avancer_bas(level_list, x_pac_man, y_pac_man):
                    y_pac_man_coordonee += vitesse
                    y_pac_man += 1
                    modif = "bas"
        else:
            if modif == "haut":
                y_pac_man_coordonee -= vitesse
            elif modif == "gauche":
                x_pac_man_coordonee -= vitesse
            elif modif == "droite":
                x_pac_man_coordonee += vitesse
            elif modif == "bas":
                y_pac_man_coordonee += vitesse
        fenetre.blit(pac_man, (x_pac_man_coordonee, y_pac_man_coordonee))

        """gestion des points du jeux"""
        if level_list[y_pac_man][x_pac_man] == 2:
            level_list[y_pac_man][x_pac_man] = 0
            points += gains

        points_var_titre = str(points)
        points_titre_objet = points_titre.render("Points :" + points_var_titre + "points", True, (255, 255, 255))
        fenetre.blit(points_titre_objet, (420, 90))

        """gestion des directions des fantomme"""
        if temps_direction == (30 / vitesse) * 4:
            temps_direction = 0
            coordonee_fan_rouge[2] = choix_direction(level_list, coordonee_fan_rouge[0][0], coordonee_fan_rouge[0][1])
            coordonee_fan_rose[2] = choix_direction(level_list, coordonee_fan_rose[0][0], coordonee_fan_rose[0][1])
            coordonee_fan_jaune[2] = choix_direction(level_list, coordonee_fan_jaune[0][0], coordonee_fan_jaune[0][1])
            coordonee_fan_bleu[2] = choix_direction(level_list, coordonee_fan_bleu[0][0], coordonee_fan_bleu[0][1])
        temps_direction += 1

        """gestion des déplacement des fantommes et des affichage"""
        modif_rouge, coordonee_fan_rouge = deplacement_fantomme(coordonee_fan_rouge, modif_rouge, vitesse, level_list)
        fenetre.blit(fan_rouge, (coordonee_fan_rouge[1][0], coordonee_fan_rouge[1][1]))

        modif_bleu, coordonee_fan_bleu = deplacement_fantomme(coordonee_fan_bleu, modif_bleu, vitesse, level_list)
        fenetre.blit(fan_bleu, (coordonee_fan_bleu[1][0], coordonee_fan_bleu[1][1]))

        modif_jaune, coordonee_fan_jaune = deplacement_fantomme(coordonee_fan_jaune, modif_jaune, vitesse, level_list)
        fenetre.blit(fan_jaune, (coordonee_fan_jaune[1][0], coordonee_fan_jaune[1][1]))

        modif_rose, coordonee_fan_rose = deplacement_fantomme(coordonee_fan_rose, modif_rose, vitesse, level_list)
        fenetre.blit(fan_rose, (coordonee_fan_rose[1][0], coordonee_fan_rose[1][1]))

        """contact avec fantomme"""
        recommencer, vie_p = contact_fantomme(coordonee_fan_rouge[0][0], coordonee_fan_rouge[0][1], x_pac_man,
                                              y_pac_man, vie_p)
        if recommencer == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordonee = x_pac_man * 30
            y_pac_man_coordonee = y_pac_man * 30
            coordonee_fan_bleu_i = coordonee_fan_bleu
            coordonee_fan_jaune_i = coordonee_fan_jaune
            coordonee_fan_rose_i = coordonee_fan_rose
            coordonee_fan_rouge_i = coordonee_fan_rouge
        else:
            recommencer, vie_p = contact_fantomme(coordonee_fan_bleu[0][0], coordonee_fan_bleu[0][1], x_pac_man,
                                                  y_pac_man, vie_p)
        if recommencer == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordonee = x_pac_man * 30
            y_pac_man_coordonee = y_pac_man * 30
            coordonee_fan_bleu_i = coordonee_fan_bleu
            coordonee_fan_jaune_i = coordonee_fan_jaune
            coordonee_fan_rose_i = coordonee_fan_rose
            coordonee_fan_rouge_i = coordonee_fan_rouge
        else:
            recommencer, vie_p = contact_fantomme(coordonee_fan_jaune[0][0], coordonee_fan_jaune[0][1], x_pac_man,
                                                  y_pac_man, vie_p)
        if recommencer == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordonee = x_pac_man * 30
            y_pac_man_coordonee = y_pac_man * 30
            coordonee_fan_bleu_i = coordonee_fan_bleu
            coordonee_fan_jaune_i = coordonee_fan_jaune
            coordonee_fan_rose_i = coordonee_fan_rose
            coordonee_fan_rouge_i = coordonee_fan_rouge
        else:
            recommencer, vie_p = contact_fantomme(coordonee_fan_rose[0][0], coordonee_fan_rose[0][1], x_pac_man,
                                                  y_pac_man, vie_p)
        if recommencer == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordonee = x_pac_man * 30
            y_pac_man_coordonee = y_pac_man * 30
            coordonee_fan_bleu_i = coordonee_fan_bleu
            coordonee_fan_jaune_i = coordonee_fan_jaune
            coordonee_fan_rose_i = coordonee_fan_rose
            coordonee_fan_rouge_i = coordonee_fan_rouge

        vie_titre_var = str(vie_p)
        vie_titre_obj = vie_titre.render("Vies restantes : " + vie_titre_var + " vies", True, (255, 255, 255))
        fenetre.blit(vie_titre_obj, (60, 840))

        if vie_p == 0:
            record_int = int(record)
            if points > record_int:
                record_int = points
            boucle_gameover = 1
            boucle_niveau = 0

        if points == (level * 1890) and vie_p != 0:
            """Affichage de l'écran pause"""
            fenetre.blit(level_suivant_image, (0, 0))
            vie_titre_var = str(vie_p)
            points_var_titre = str(points)
            level_var_titre = str(level)
            vie_titre_obj = vie_titre.render(vie_titre_var + " vies", True, (255, 255, 255))
            points_titre_objet = points_titre.render(points_var_titre + "points", True, (255, 255, 255))
            record_titre_obj = record_titre.render(record + "points", True, (255, 255, 255))
            level_titre_obj = level_titre.render(level_var_titre, True, (255, 255, 255))
            fenetre.blit(vie_titre_obj, (271, 591))
            fenetre.blit(points_titre_objet, (231, 64))
            fenetre.blit(record_titre_obj, (273, 210))
            fenetre.blit(level_titre_obj, (437, 405))

            pygame.display.flip()
            time.sleep(5)

            """renitialisation du niveau"""

            level += 1
            level_list = level_initialisation_convertisation()
            x_pac_man_i = 6
            y_pac_man_i = 21
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordonee = x_pac_man * 30
            y_pac_man_coordonee = y_pac_man * 30
            direction = ""
            modif = ""
            recommencer = 0
            coordonee_fan_bleu = [[16, 12], [14 * 30 + 60, 7 * 30 + 150], "haut"]
            coordonee_fan_jaune = [[6, 13], [4 * 30 + 60, 8 * 30 + 150], "haut"]
            coordonee_fan_rose = [[10, 20], [8 * 30 + 60, 15 * 30 + 150], "haut"]
            coordonee_fan_rouge = [[11, 9], [9 * 30 + 60, 4 * 30 + 150], "haut"]
            modif_rouge = ""
            modif_bleu = ""
            modif_jaune = ""
            modif_rose = ""

        pygame.display.flip()

    while boucle_gameover:
        pygame.time.Clock().tick(fps)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    boucle_gameover = 0
                    boucle_menu = 1
                if event.key == K_ESCAPE:
                    boucle_gameover = 0
                    boucle_jeu = 0
            if event.type == QUIT:
                boucle_gameover = 0
                boucle_jeu = 0

        fenetre.blit(game_over_image, (0, 0))
        points_var_titre_gameover = str(points)
        points_var_titre_gameover_obj = game_over_points_titre.render(points_var_titre_gameover, True,
                                                                      (255, 255, 255))
        fenetre.blit(points_var_titre_gameover_obj, (290, 710))

        record = str(record_int)
        fichier = open("record", "w")
        fichier.write(record)
        fichier.close()
        game_over_record_obj = game_over_record.render(record, True, (255, 255, 255))
        fenetre.blit(game_over_record_obj, (257, 753))
        pygame.display.flip()
