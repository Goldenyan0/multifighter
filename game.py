import pygame,sys
from button import Button
from pygame import mixer
from fighter import Fighter
import random
mixer.init()
pygame.init()

screen_WIDTH = 1600
screen_HEIGHT = 900

screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
pygame.display.set_caption("Multifighter")

#nombre d'image par secondes
clock = pygame.time.Clock()
FPS = 60

#couleurs
RED = (255, 0, 0)
YELLOW = (0, 255, 0)
WHITE = (255, 255, 255)

#variables des combattants
PLAYER1SIZE = 325
PLAYER1SCALE = 2
PLAYER1OFFSET = [130, 135]
PLAYER1DATA = [PLAYER1SIZE, PLAYER1SCALE, PLAYER1OFFSET]
PLAYER2DATA = [PLAYER1SIZE, PLAYER1SCALE, PLAYER1OFFSET]
#musiques et sons
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, random.randint(0,600), 5000)
bg_image = pygame.image.load("assets/images/background/background.gif").convert_alpha()
background= pygame.image.load("assets/menu/background.jpg").convert_alpha()

def selectperso():
  global perso1
  global perso2
  global PLAYER1ANIMATION_STEPS
  global PLAYER1sheet
  global PLAYER1_victory_sheet
  PLAYER1_victory_sheet=pygame.image.load("assets/images/Sprites/what.png").convert_alpha()
  global PLAYER2ANIMATION_STEPS
  global PLAYER2sheet
  global PLAYER2_victory_sheet
  PLAYER2_victory_sheet=pygame.image.load("assets/images/Sprites/what.png").convert_alpha()
  global fighter_sound
  global fighter_sound2
  global PLAYER1_victory_sound
  global PLAYER2_victory_sound
  
  run=True
  while run:
      OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

      bg = pygame.transform.scale(background, (screen_WIDTH, screen_HEIGHT))#mettre l'arriere plan à l'écran
      screen.blit(bg, (0, 0))

      OPTIONS_TEXT = get_police(60).render("Veuillez sélectionner votre personnage", True, "White")
      OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(800, 50))
      screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

      GOKUSSBUTTON = Button(image=None, pos=(200, 200), text_input="GOKU", font=get_police(20), base_color="White", hovering_color="Blue")
      GOKUSSBUTTON2 = Button(image=None, pos=(1400, 200), text_input="GOKU", font=get_police(20), base_color="White", hovering_color="Blue")
      FREEZERBUTTON = Button(image=None, pos=(200, 300), text_input="FREEZER", font=get_police(20), base_color="White", hovering_color="Blue")
      FREEZERBUTTON2 = Button(image=None, pos=(1400, 300), text_input="FREEZER", font=get_police(20), base_color="White", hovering_color="Blue")
      BROLYBUTTON = Button(image=None, pos=(200, 400), text_input="BROLY", font=get_police(20), base_color="White", hovering_color="Blue")
      BROLYBUTTON2 = Button(image=None, pos=(1400, 400), text_input="BROLY", font=get_police(20), base_color="White", hovering_color="Blue")
      VEGETASSBUTTON = Button(image=None, pos=(200, 500), text_input="VEGETA", font=get_police(20), base_color="White", hovering_color="Blue")
      VEGETASSBUTTON2 = Button(image=None, pos=(1400, 500), text_input="VEGETA", font=get_police(20), base_color="White", hovering_color="Blue")
      LUFFYBUTTON = Button(image=None, pos=(200, 600), text_input="LUFFY", font=get_police(20), base_color="White", hovering_color="Blue")
      LUFFYBUTTON2 = Button(image=None, pos=(1400, 600), text_input="LUFFY", font=get_police(20), base_color="White", hovering_color="Blue")
      ZOROBUTTON = Button(image=None, pos=(200, 700), text_input="ZORO", font=get_police(20), base_color="White", hovering_color="Blue")
      ZOROBUTTON2 = Button(image=None, pos=(1400, 700), text_input="ZORO", font=get_police(20), base_color="White", hovering_color="Blue")
      DARKVADORBUTTON = Button(image=None, pos=(200, 800), text_input="Dark Vador", font=get_police(20), base_color="White", hovering_color="Blue")
      DARKVADORBUTTON2 = Button(image=None, pos=(1400, 800), text_input="Dark Vador", font=get_police(20), base_color="White", hovering_color="Blue")
      VALIDERBUTTON = Button(image=None, pos=(700, 850), text_input="VALIDER", font=get_police(30), base_color="White", hovering_color="Blue")
      RETOURBUTTON = Button(image=None, pos=(900, 850), text_input="RETOUR", font=get_police(30), base_color="White", hovering_color="Blue")

      GOKUSSBUTTON.changeColor(OPTIONS_MOUSE_POS)
      GOKUSSBUTTON.update(screen)
      GOKUSSBUTTON2.changeColor(OPTIONS_MOUSE_POS)
      GOKUSSBUTTON2.update(screen)
      
      VEGETASSBUTTON.changeColor(OPTIONS_MOUSE_POS)
      VEGETASSBUTTON.update(screen)
      VEGETASSBUTTON2.changeColor(OPTIONS_MOUSE_POS)
      VEGETASSBUTTON2.update(screen)
      
      FREEZERBUTTON.changeColor(OPTIONS_MOUSE_POS)
      FREEZERBUTTON.update(screen)
      FREEZERBUTTON2.changeColor(OPTIONS_MOUSE_POS)
      FREEZERBUTTON2.update(screen)

      BROLYBUTTON.changeColor(OPTIONS_MOUSE_POS)
      BROLYBUTTON.update(screen)
      BROLYBUTTON2.changeColor(OPTIONS_MOUSE_POS)
      BROLYBUTTON2.update(screen)

      LUFFYBUTTON.changeColor(OPTIONS_MOUSE_POS)
      LUFFYBUTTON.update(screen)
      LUFFYBUTTON2.changeColor(OPTIONS_MOUSE_POS)
      LUFFYBUTTON2.update(screen)

      ZOROBUTTON.changeColor(OPTIONS_MOUSE_POS)
      ZOROBUTTON.update(screen)
      ZOROBUTTON2.changeColor(OPTIONS_MOUSE_POS)
      ZOROBUTTON2.update(screen)

      DARKVADORBUTTON.changeColor(OPTIONS_MOUSE_POS)
      DARKVADORBUTTON.update(screen)
      DARKVADORBUTTON2.changeColor(OPTIONS_MOUSE_POS)
      DARKVADORBUTTON2.update(screen)

      VALIDERBUTTON.changeColor(OPTIONS_MOUSE_POS)
      VALIDERBUTTON.update(screen)

      RETOURBUTTON.changeColor(OPTIONS_MOUSE_POS)
      RETOURBUTTON.update(screen)

      screen.blit(PLAYER1_victory_sheet, (400, 300))
      screen.blit(PLAYER2_victory_sheet, (1000, 300))
      screen.blit(pygame.image.load("assets/images/Sprites/VS_logo.png").convert_alpha(), (690, 300))
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN: 
              if GOKUSSBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                perso1= "GokuSS"
                PLAYER1ANIMATION_STEPS = [4, 6, 1, 4, 6, 2, 4, 6]
                PLAYER1sheet = pygame.image.load("assets/images/Sprites/GokuSS.png").convert_alpha()
                PLAYER1_victory_sheet = pygame.image.load("assets/images/Sprites/GokuSS_Victory.png").convert_alpha()
                fighter_sound = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER1_victory_sound = pygame.mixer.Sound("assets/audio/goku_win.ogg")
                PLAYER1_victory_sound.set_volume(2)
              if GOKUSSBUTTON2.checkForInput(OPTIONS_MOUSE_POS) :
                perso2 = "GokuSS"
                PLAYER2ANIMATION_STEPS = [4, 6, 1, 4, 6, 2, 4, 6]
                PLAYER2sheet = pygame.image.load("assets/images/Sprites/GokuSS.png").convert_alpha()
                PLAYER2_victory_sheet = pygame.image.load("assets/images/Sprites/GokuSS_Victory.png").convert_alpha()
                fighter_sound2 = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER2_victory_sound = pygame.mixer.Sound("assets/audio/goku_win.ogg")
                PLAYER2_victory_sound.set_volume(2)
              if VEGETASSBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                perso1 = "VegetaSS"
                PLAYER1ANIMATION_STEPS = [4, 6, 1, 4, 5, 2, 4, 6]
                PLAYER1sheet = pygame.image.load("assets/images/Sprites/VegetaSS.png").convert_alpha()
                PLAYER1_victory_sheet = pygame.image.load("assets/images/Sprites/VegetaSS_Victory.png").convert_alpha()
                fighter_sound = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER1_victory_sound = pygame.mixer.Sound("assets/audio/vegeta_win.ogg")
                PLAYER1_victory_sound.set_volume(2)
              if VEGETASSBUTTON2.checkForInput(OPTIONS_MOUSE_POS) :
                perso2 = "VegetaSS"
                PLAYER2ANIMATION_STEPS = [4, 6, 1, 4, 5, 2, 4, 6]
                PLAYER2sheet = pygame.image.load("assets/images/Sprites/VegetaSS.png").convert_alpha()
                PLAYER2_victory_sheet = pygame.image.load("assets/images/Sprites/VegetaSS_Victory.png").convert_alpha()
                fighter_sound2 = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER2_victory_sound = pygame.mixer.Sound("assets/audio/vegeta_win.ogg")
                PLAYER2_victory_sound.set_volume(2)
              if BROLYBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                perso1 = "Broly"
                PLAYER1ANIMATION_STEPS = [10, 13, 1, 6, 6, 2, 5, 6]
                PLAYER1_victory_sheet = pygame.image.load("assets/images/Sprites/Broly_Victory.png").convert_alpha()
                PLAYER1sheet = pygame.image.load("assets/images/Sprites/Broly.png").convert_alpha()
                fighter_sound = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER1_victory_sound = pygame.mixer.Sound("assets/audio/broly_win.ogg")
                PLAYER1_victory_sound.set_volume(2)
              if BROLYBUTTON2.checkForInput(OPTIONS_MOUSE_POS) :
                perso2 = "Broly"
                PLAYER2ANIMATION_STEPS = [10, 13, 1, 6, 6, 2, 5, 6]
                PLAYER2_victory_sheet = pygame.image.load("assets/images/Sprites/Broly_Victory.png").convert_alpha()
                PLAYER2sheet = pygame.image.load("assets/images/Sprites/Broly.png").convert_alpha()
                fighter_sound2 = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER2_victory_sound = pygame.mixer.Sound("assets/audio/broly_win.ogg")
                PLAYER2_victory_sound.set_volume(2)
              if FREEZERBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                perso1="Freezer"
                PLAYER1ANIMATION_STEPS = [10, 8, 11, 7, 8, 2, 5, 5]
                PLAYER1sheet = pygame.image.load("assets/images/Sprites/Freezer.png").convert_alpha()
                PLAYER1_victory_sheet = pygame.image.load("assets/images/Sprites/Freezer_Victory.png").convert_alpha()
                fighter_sound = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER1_victory_sound = pygame.mixer.Sound("assets/audio/freezer_win.ogg")
                PLAYER1_victory_sound.set_volume(2)
              if FREEZERBUTTON2.checkForInput(OPTIONS_MOUSE_POS) :
                perso2 = "Freezer"
                PLAYER2ANIMATION_STEPS = [10, 8, 11, 7, 8, 2, 5, 5]
                PLAYER2sheet = pygame.image.load("assets/images/Sprites/Freezer.png").convert_alpha()
                PLAYER2_victory_sheet = pygame.image.load("assets/images/Sprites/Freezer_Victory.png").convert_alpha()
                fighter_sound2 = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER2_victory_sound = pygame.mixer.Sound("assets/audio/freezer_win.ogg")
                PLAYER2_victory_sound.set_volume(2)
              if LUFFYBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                perso1 = "Luffy"
                PLAYER1ANIMATION_STEPS = [4, 8, 1, 5, 6, 2, 4, 6]
                PLAYER1sheet = pygame.image.load("assets/images/Sprites/Luffy.png").convert_alpha()
                PLAYER1_victory_sheet = pygame.image.load("assets/images/Sprites/Luffy_Victory.png").convert_alpha()
                fighter_sound = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER1_victory_sound = pygame.mixer.Sound("assets/audio/luffy_win.mp3")
                PLAYER1_victory_sound.set_volume(2)
              if LUFFYBUTTON2.checkForInput(OPTIONS_MOUSE_POS) :
                perso2 = "Luffy"
                PLAYER2ANIMATION_STEPS = [4, 8, 1, 5, 6, 2, 4, 6]
                PLAYER2sheet = pygame.image.load("assets/images/Sprites/Luffy.png").convert_alpha()
                PLAYER2_victory_sheet = pygame.image.load("assets/images/Sprites/Luffy_Victory.png").convert_alpha()
                fighter_sound2 = pygame.mixer.Sound("assets/audio/punch.mp3")
                PLAYER2_victory_sound = pygame.mixer.Sound("assets/audio/luffy_win.mp3")
                PLAYER2_victory_sound.set_volume(2)
              if ZOROBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                perso1 = "Zoro"
                PLAYER1ANIMATION_STEPS = [4, 8, 1, 4, 5, 2, 4, 5]
                PLAYER1sheet = pygame.image.load("assets/images/Sprites/Zoro.png").convert_alpha()
                PLAYER1_victory_sheet = pygame.image.load("assets/images/Sprites/Zoro_Victory.png").convert_alpha()
                fighter_sound = pygame.mixer.Sound("assets/audio/sword.mp3")
                PLAYER1_victory_sound = pygame.mixer.Sound("assets/audio/zoro_win.mp3")
                PLAYER1_victory_sound.set_volume(2)
              if ZOROBUTTON2.checkForInput(OPTIONS_MOUSE_POS) :
                perso2 = "Zoro"
                PLAYER2ANIMATION_STEPS = [4, 8, 1, 4, 5, 2, 4, 5]
                PLAYER2sheet = pygame.image.load("assets/images/Sprites/Zoro.png").convert_alpha()
                PLAYER2_victory_sheet = pygame.image.load("assets/images/Sprites/Zoro_Victory.png").convert_alpha()
                fighter_sound2 = pygame.mixer.Sound("assets/audio/sword.mp3")
                PLAYER2_victory_sound = pygame.mixer.Sound("assets/audio/zoro_win.mp3")
                PLAYER2_victory_sound.set_volume(2)
              if DARKVADORBUTTON.checkForInput(OPTIONS_MOUSE_POS) :
                perso1 = "Dark Vador"
                PLAYER1ANIMATION_STEPS = [2, 4, 1, 3, 3, 2, 3, 7]
                PLAYER1sheet = pygame.image.load("assets/images/Sprites/DarkVador.png").convert_alpha()
                PLAYER1_victory_sheet = pygame.image.load("assets/images/Sprites/DarkVador_Victory.png").convert_alpha()
                fighter_sound = pygame.mixer.Sound("assets/audio/lightsaber.mp3")
                PLAYER1_victory_sound = pygame.mixer.Sound("assets/audio/vador_win.mp3")
                PLAYER1_victory_sound.set_volume(2)
              if DARKVADORBUTTON2.checkForInput(OPTIONS_MOUSE_POS) :
                perso2 = "Dark Vador"
                PLAYER2ANIMATION_STEPS = [2, 4, 1, 3, 3, 2, 3, 7]
                PLAYER2sheet = pygame.image.load("assets/images/Sprites/DarkVador.png").convert_alpha()
                PLAYER2_victory_sheet = pygame.image.load("assets/images/Sprites/DarkVador_Victory.png").convert_alpha()
                fighter_sound2 = pygame.mixer.Sound("assets/audio/lightsaber.mp3")
                PLAYER2_victory_sound = pygame.mixer.Sound("assets/audio/vador_win.mp3")
                PLAYER2_victory_sound.set_volume(2)
              if VALIDERBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                if perso1 == None or perso2 == None:
                  mainmenu()
                else:
                  game()
              if RETOURBUTTON.checkForInput(OPTIONS_MOUSE_POS):
                mainmenu()
      

      pygame.display.update()

#selection perso + sprites d'animations pour chaque personnage








def get_police(size):
    return pygame.font.Font("assets/menu/police3.ttf", size)

def options(): # la meme chose que la fonction de jeu 
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        OPTIONS_TEXT = get_police(60).render("Voici l'écran des OPTIONS.", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), text_input="RETOUR", font=get_police(75), base_color="White", hovering_color="Blue")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    mainmenu()

        pygame.display.update()

def mainmenu():
  while True:
      bg = pygame.transform.scale(background, (screen_WIDTH, screen_HEIGHT))#mettre l'arriere plan à l'écran
      screen.blit(bg, (0, 0))

      MENU_MOUSE_POS = pygame.mouse.get_pos()# position de la souris car si on veut tester si nous appuyons sur un bouton ou nous le survolons 

      MENU_TEXT = get_police(130).render("MultiFighter", True, "#f79b06")# on place le menu principale du texte sur l'écran 
      MENU_RECT = MENU_TEXT.get_rect(center=(800, 100))#          ""          ""

      # on créé nos trois bouton en utilisant la classe boutons
      PLAY_BUTTON = Button(None, pos=(800, 300),
                          text_input="JOUER", font=get_police(90), base_color="#07f7f7", hovering_color="White")
      OPTIONS_BUTTON = Button(None, pos=(800, 475), 
                          text_input="OPTIONS", font=get_police(90), base_color="#07f7f7", hovering_color="White")
      QUIT_BUTTON = Button(None, pos=(800, 650), 
                          text_input="QUITTER", font=get_police(90), base_color="#07f7f7", hovering_color="White")

      screen.blit(MENU_TEXT, MENU_RECT)

      for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:   # parcourir chaque bouton que nous avons et d'éxécuter les deux méthodes 
          button.changeColor(MENU_MOUSE_POS)
          button.update(screen)
      
      for event in pygame.event.get():    # parcourons chaque événement qui pyame a 
          if event.type == pygame.QUIT: # nous vérifions si nous quitter le jeu de la maniere traditionnelle qui consiste sur le bouton x si on le fait
              pygame.quit() #  on quitte le jeu de tarte et nous quittons 
              sys.exit()  #   ""      ""
          if event.type == pygame.MOUSEBUTTONDOWN: # on vérifie si noius avons cliqué sur le bouton de la souris 
              # si on a cliqué alors nous verifions si on a cliqué dessus 
              if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):     # si on clique sur "JOUER" nous exécutons la fonction de lecture si 
                  selectperso()
                  pygame.quit()
                  sys.exit()
              if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):    # si on clique sur le bouton d'"OPTIONS" nous exécutons la fonction d'option 
                  options()
              if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):       # si on clique sur "QUITTER" , on quitte 
                  pygame.quit()
                  sys.exit()
              
      pygame.display.update()

#afficher le texte
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#afficher le fond d'écran
def draw_bg():
  scaled_bg = pygame.transform.scale(bg_image, (screen_WIDTH, screen_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

#barre de vie
def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, RED, (x, y, 400, 30))
  pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)


#jeu:
def game():
  #créer les deux personnages
  fighter_1 = Fighter(1, 200, 500, False, PLAYER1DATA, PLAYER1sheet, PLAYER1ANIMATION_STEPS, fighter_sound)
  fighter_2 = Fighter(2, 1300, 500, True, PLAYER2DATA, PLAYER2sheet, PLAYER2ANIMATION_STEPS, fighter_sound2)
  intro_count = 3
  last_count_update = pygame.time.get_ticks()
  score = [0, 0]#scores. [P1, P2]
  round_over = False
  ROUND_OVER_COOLDOWN = 8000
  run = True
  while run:
    clock.tick(FPS)

    #afficher fond d'écran
    draw_bg()

    #statistiques de perso
    draw_health_bar(fighter_1.health, 120, 20)
    draw_health_bar(fighter_2.health, 1080, 20)
    draw_text("Joueur 1: " + str(score[0]), score_font, WHITE, 120, 60)
    draw_text("Joueur 2: " + str(score[1]), score_font, WHITE, 1080, 60)

    
    if intro_count <= 0:
      #déplacements
      fighter_1.move(screen_WIDTH, screen_HEIGHT, screen, fighter_2, round_over)
      fighter_2.move(screen_WIDTH, screen_HEIGHT, screen, fighter_1, round_over)
    else:
      
      draw_text(str(intro_count), count_font, RED, screen_WIDTH / 2, screen_HEIGHT / 3)
      
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()

    #maj des joueurs
    fighter_1.update()
    fighter_2.update()

    #affichage des perso
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #vérifie si l'un des perso est mort
    if round_over == False:
      if fighter_2.alive == False:
        victory_img=PLAYER1_victory_sheet
        PLAYER1_victory_sound.play(0)
        persowin=perso1
        score[0] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
      elif fighter_1.alive == False:
        victory_img=PLAYER2_victory_sheet
        PLAYER2_victory_sound.play(0)
        persowin=perso2
        score[1] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
    else:
      #affciahge de l'écran de victoire
      screen.blit(victory_img, (650, 200))
      draw_text(str(persowin)+ " a gagné !", score_font, WHITE, 675, 150)
      if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
        round_over = False
        intro_count = 3
        fighter_1 = Fighter(1, 200, 310, False, PLAYER1DATA, PLAYER1sheet, PLAYER1ANIMATION_STEPS, fighter_sound)
        fighter_2 = Fighter(2, 1400, 310, True, PLAYER2DATA, PLAYER2sheet, PLAYER2ANIMATION_STEPS, fighter_sound2)

    #event handler
    for event in pygame.event.get():
      if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        mainmenu()
      elif event.type == pygame.QUIT:
        run = False
        pygame.quit()


    #maj pygame
    pygame.display.update()

mainmenu()