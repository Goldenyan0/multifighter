import pygame

class Fighter():
  def __init__(self, player, x, y, flip, data, sprite_sheet, animation_steps, sound):
    self.player = player
    self.size = data[0]
    self.image_scale = data[1]
    self.offset = data[2]
    self.flip = flip
    self.animation_list = self.load_images(sprite_sheet, animation_steps)
    self.action = 0#0:base #1:courir #2:sauter #3:attack1 #4: attack2 #5:touché #6:mort
    self.frame_index = 0
    self.image = self.animation_list[self.action][self.frame_index]
    self.update_time = pygame.time.get_ticks()
    self.rect = pygame.Rect((x, y, 120, 240))
    self.vel_y = 0
    self.running = False
    self.jump = False
    self.attacking = False
    self.attack_type = 0
    self.attack_cooldown = 0
    self.attack_sound = sound
    self.hit = False
    self.health = 100
    self.alive = True


  def load_images(self, sprite_sheet, animation_steps):
    #gestion des images et animations
    animation_list = []
    for y, animation in enumerate(animation_steps):
      temp_img_list = []
      for x in range(animation):
        temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
        temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
      animation_list.append(temp_img_list)
    return animation_list


  def move(self, screen_width, screen_height, surface, target, round_over):
    SPEED = 10
    GRAVITY = 2
    dx = 0
    dy = 0
    self.running = False
    self.attack_type = 0

    
    key = pygame.key.get_pressed()

    if self.attacking == False and self.alive == True and round_over == False:
      if self.player == 1:
        #déplacements
        if key[pygame.K_q]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_d]:
          dx = SPEED
          self.running = True
        #saut
        if key[pygame.K_z] and self.jump == False:
          self.vel_y = -40
          self.jump = True
        #attaque
        if key[pygame.K_r] or key[pygame.K_t] or key[pygame.K_f]:
          #quel type d'attaque
          if key[pygame.K_r]:
            self.attack_type = 1
          if key[pygame.K_t]:
            self.attack_type = 2
          if key[pygame.K_f]:
            self.attack_type = 3
          self.attack(target,self.attack_type)


      if self.player == 2:
        #déplacement
        if key[pygame.K_LEFT]:
          dx = -SPEED
          self.running = True
        if key[pygame.K_RIGHT]:
          dx = SPEED
          self.running = True
        #saut
        if key[pygame.K_UP] and self.jump == False:
          self.vel_y = -40
          self.jump = True
        #attaque
        if key[pygame.K_KP1] or key[pygame.K_KP2] or key[pygame.K_KP3]:
          #determine which attack type was used
          if key[pygame.K_KP1]:
            self.attack_type = 1
          if key[pygame.K_KP2]:
            self.attack_type = 2
          if key[pygame.K_KP3]:
            self.attack_type = 3
          self.attack(target,self.attack_type)


    #gravité
    self.vel_y += GRAVITY
    dy += self.vel_y

    
    if self.rect.left + dx < 0:
      dx = -self.rect.left
    if self.rect.right + dx > screen_width:
      dx = screen_width - self.rect.right
    if self.rect.bottom + dy > screen_height - 110:
      self.vel_y = 0
      self.jump = False
      dy = screen_height - 110 - self.rect.bottom

    #vérification que chaque perso se regarde
    if target.rect.centerx > self.rect.centerx:
      self.flip = False
    else:
      self.flip = True

    #cooldown d'attaque
    if self.attack_cooldown > 0:
      self.attack_cooldown -= 1

    #mise à jour de position
    self.rect.x += dx
    self.rect.y += dy


  #mise à jour des animations
  def update(self):
    if self.health <= 0:
      self.health = 0
      self.alive = False
      self.update_action(6)#6:mort
    elif self.hit == True:
      self.update_action(5)#5:touché
    elif self.attacking == True:
      if self.attack_type == 1:
        self.update_action(3)#3:attack1
      elif self.attack_type == 2:
        self.update_action(4)#4:attack2
      elif self.attack_type == 3:
        self.update_action(7)#7:attack3
    elif self.jump == True:
      self.update_action(2)#2:saut
    elif self.running == True:
      self.update_action(1)#1:courir
    else:
      self.update_action(0)#0:base

    animation_cooldown = 50
    self.image = self.animation_list[self.action][self.frame_index]
    #vérifie si le temps entre chaque animation a bien été executé
    if pygame.time.get_ticks() - self.update_time > animation_cooldown:
      self.frame_index += 1
      self.update_time = pygame.time.get_ticks()
    #vérifie si l'animétion est terminée
    if self.frame_index >= len(self.animation_list[self.action]):
      #si le personnage meurt
      if self.alive == False:
        self.frame_index = len(self.animation_list[self.action]) - 1
      else:
        self.frame_index = 0
        #si une attaque est executée
        if self.action == 3 or self.action == 4 or self.action == 7:
          self.attacking = False
          self.attack_cooldown = 20
        #si le personnage est touché
        if self.action == 5:
          self.hit = False
          #si le personnage attaque mais se fait toucher
          self.attacking = False
          self.attack_cooldown = 20


  def attack(self, target, attack_type):
    if attack_type==1:
      if self.attack_cooldown == 0:
        self.attacking = True
        self.attack_sound.play()
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
          target.health -= 5
          target.hit = True
    if attack_type==2:
      if self.attack_cooldown == 0:
        self.attacking = True
        self.attack_sound.play()
        attacking_rect = pygame.Rect(self.rect.centerx - ( self.rect.width * self.flip), self.rect.centery - (2 * self.rect.width), self.rect.width/2, self.rect.height/2)
        if attacking_rect.colliderect(target.rect):
          target.health -= 10
          target.hit = True
    if attack_type==3:
      if self.attack_cooldown == 0:
        self.attacking = True
        self.attack_sound.play()
        attacking_rect = pygame.Rect(self.rect.centerx - (self.rect.width * self.flip), self.rect.centery + (self.rect.width), 1 * self.rect.width/2, self.rect.height/2)
        if attacking_rect.colliderect(target.rect):
          target.health -= 15
          target.hit = True
      


  def update_action(self, new_action):
    #met à jour les actions
    if new_action != self.action:
      self.action = new_action
      #met à jour les animations
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks()

  def draw(self, surface):
    img = pygame.transform.flip(self.image, self.flip, False)
    surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
