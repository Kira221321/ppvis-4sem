import json
from os import path

import pygame

from config.Clouds import *
from config.enemies import *
from config.lowPlatform import *
from config.platforms import *
from menu.menu import EndMenu, MainMenu, LeaderboardMenu, HelpMenu
vec = pygame.math.Vector2


class GamSettings:
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()

    def __init__(self, settings_file, game):
        self.game = game
        self.settings = GamSettings.load_settings(settings_file)
        # main controls
        self.load_main_controls()
        # window
        self.laod_window(
            w=self.settings[0]["display_w"],
            h=self.settings[0]["display_h"],
            caption=self.settings[1]["caption"],
            icon=self.settings[1]["icon"],
            background=self.settings[1]["background"]
        )
        # game time
        self.load_game_time(fps=self.settings[0]["fps"])
        # menus
        self.load_menus()
        # fonts
        self.load_fonts()
        # elements
        self.load_elements(
            paddle_speed=self.settings[0]["paddle_speed"],
            ball_speed=self.settings[0]["ball_speed"],
        )
        # sounds
        self.load_sounds(
            self.settings[2]["bad_bonus_sound"],
            self.settings[2]["good_bonus_sound"],
            self.settings[2]["end_or_next_sound"],
            self.settings[2]["ball_block_sound"],
            self.settings[2]["paddle_sound"],
            self.settings[2]["gray_block_sound"]
        )
        # level
        self.load_level()

    @staticmethod
    def load_settings(sfile: str):
        try:
            with open(sfile, 'r') as f:
                settings = json.load(f)
        except Exception as e:
            print(e.__str__())
            print("Error to open file!")
        return settings

    def load_main_controls(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def laod_window(self, w, h, caption, icon, background):
        self.DISPLAY_W, self.DISPLAY_H = w, h
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H), pygame.SCALED)
        self.caption = pygame.display.set_caption(caption)

    def load_game_time(self, fps):
        self.clock = pygame.time.Clock()
        self.FPS = fps

    def load_level(self):
        pass

    def load_menus(self):
        self.main_menu = MainMenu(self)
        self.leaderboard = LeaderboardMenu(self, max_leaders=10)
        self.help = HelpMenu(self)
        self.end = EndMenu(self)
        self.curr_menu = self.main_menu

    def load_elements(self, paddle_speed, ball_speed):
        pass

    def load_fonts(self):
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.font_end = pygame.font.SysFont('Arial', 40, bold=True)
        self.font_score = pygame.font.SysFont('Arial', 20, bold=True)

    def load_sounds(self, *sounds):
        self.bad_bonus_sound = pygame.mixer.Sound(sounds[0])
        self.good_bonus_sound = pygame.mixer.Sound(sounds[1])
        self.end_or_next_sound = pygame.mixer.Sound(sounds[2])
        self.ball_block_sound = pygame.mixer.Sound(sounds[3])
        self.paddle_sound = pygame.mixer.Sound(sounds[4])
        self.gray_block_sound = pygame.mixer.Sound(sounds[5])


class Game:
    def __init__(self):  # initialize game window and other things for the game.
        pygame.init()
        self.settings = GamSettings('settings.json', self)

        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        self.gameDisplay.fill(white)
        pygame.display.set_caption("Doodle Jump!")
        self.clock = pygame.time.Clock()
        self.img_pikachu = pygame.sprite.Sprite()
        self.img_pikachu.image = pygame.image.load('images/pikachu.png').convert_alpha()
        self.img_pikachu.rect = self.img_pikachu.image.get_rect()
        self.background = pygame.image.load('images/blue_back.jpg').convert()
        self.font = pygame.font.SysFont(None, 25)
        self.gameExit = False
        self.pos = vec(display_width - 100, display_height)
        self.img_pikachu.rect.topleft = [self.pos.x, self.pos.y]
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.platforms = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.playerSprite = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.playerSprite.add(self.img_pikachu)
        p1 = lowPlatform(0, display_height - 40, display_width, 40)
        platform_obj = Platform(self)
        self.platform_images = platform_obj.getImages()
        p2 = Platform(self)
        p2.getPlatform(display_width / 2 - 50, display_height - 150, self.platform_images)
        p3 = Platform(self)
        p3.getPlatform(display_width / 2 - 100, display_height - 300, self.platform_images)
        p4 = Platform(self)
        p4.getPlatform(display_width / 2, display_height - 450, self.platform_images)
        p5 = Platform(self)
        p5.getPlatform(0, display_height - 600, self.platform_images)
        self.platforms.add(p1)
        self.platforms.add(p2)
        self.platforms.add(p3)
        self.platforms.add(p4)
        self.platforms.add(p5)
        self.score = 0
        self.font_name = pygame.font.match_font(Font_Name)
        self.load_data()
        self.enemies_timer = 0

        for i in range(8):
            c = Cloud(self)
            c.rect.y += 600


    def load_data(self):
        # load cloud images
        self.dir = path.dirname(__file__)
        cloud_dir = path.join(self.dir, 'clouds_img')
        self.cloud_images = []
        for i in range(1, 4):
            self.cloud_images.append(pygame.image.load(path.join(cloud_dir, 'cloud{}.png'.format(i))).convert())

        # load sounds
        self.sound_dir = path.join(self.dir, 'sound')
        self.jump_sound = pygame.mixer.Sound(path.join(self.sound_dir, 'jump.ogg'))
        self.jump_sound.set_volume(0.1)
        self.pow_sound = pygame.mixer.Sound(path.join(self.sound_dir, 'pow.wav'))

    def updateScreen(self):

        now_time = pygame.time.get_ticks()
        if now_time - self.enemies_timer > 5000 + random.choice([-1000, -500, 0, 500, 1000]):
            self.enemies_timer = now_time
            if random.randint(1, 2) == random.randint(1, 2):
                Enemies(self)
            else:
                BlackHole(self)

        enemies_hits = pygame.sprite.spritecollide(self.img_pikachu, self.enemies, False, pygame.sprite.collide_mask)
        if enemies_hits:
            self.gameOver = True

        # Updating the sprite's position
        self.img_pikachu.rect.midbottom = [self.pos.x, self.pos.y]
        # Checking for collision between the player and the sprites.
        powerup_hits = pygame.sprite.spritecollide(self.img_pikachu, self.powerups, False)
        for x in powerup_hits:
            self.pow_sound.play()
            self.vel.y = power_up_boost

        if self.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.img_pikachu, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit

                if self.pos.x < lowest.rect.right + 30 and self.pos.x > lowest.rect.left - 30:
                    if self.pos.y < lowest.rect.centery:
                        self.pos.y = lowest.rect.top
                        self.vel.y = 0

        # Scrolling the screen upwards as the player moves upward. Killing the platforms which are not futher required.
        if self.img_pikachu.rect.top <= display_height / 4:

            if random.randrange(100) < 99:
                Cloud(self)

            self.pos.y += abs(self.vel.y)

            for cloud in self.clouds:
                cloud.rect.y += max(abs(self.vel.y / 2), 2)

            for platform in self.platforms:
                platform.rect.y += abs(self.vel.y)
                if platform.rect.top >= display_height:
                    platform.kill()
                    self.score += 10

            for enemy in self.enemies:
                enemy.rect.y += abs(self.vel.y)

        # GAME OVER CHECK.
        if self.img_pikachu.rect.bottom > display_height:
            self.gameOver = True;
            for sprite in self.platforms:
                sprite.rect.y -= max(self.vel.y, 10)

        # Creating new platforms.
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(self)
            p.getPlatform(random.randrange(0, display_width - width), random.randrange(-50, -30), self.platform_images)
            self.platforms.add(p)

        for x in self.powerups:  # updating powerup sprites positions according to the change in platform position.
            x.update()

        self.gameDisplay.fill(black)
        self.enemies.update()
        self.powerups.update()
        self.platforms.update()
        self.clouds.update()
        self.playerSprite.update()
        self.gameDisplay.blit(self.background, (0, 0))
        self.clouds.draw(self.gameDisplay)
        self.platforms.draw(self.gameDisplay)
        self.powerups.draw(self.gameDisplay)
        self.enemies.draw(self.gameDisplay)

        self.playerSprite.draw(self.gameDisplay)
        self.messageToScreen("SCORE : " + (str)(self.score), 25, white, display_width / 2, 15)
        pygame.display.update()

    def waitForKeyPress(self):
        waiting = True
        while waiting:
            self.clock.tick(fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.gameExit = True
                if event.type == pygame.KEYUP:
                    waiting = False
                    self.gameOver = False
                    self.gameExit = False

    def run(self):
        while self.settings.playing:
            self.score = 0
            self.gameOver = False
            while not self.gameExit:
                self.checkEvent()
                self.acc.x += self.vel.x * player_Fric
                self.vel += self.acc
                self.pos += self.vel + 0.5 * self.acc
                self.checkHorizontalCrossing()
                self.updateScreen()
                self.clock.tick(fps)
                if self.gameOver == True:
                    self.gameOverScreen()
                    self.gameOver == False
                    break
            pygame.mixer.music.fadeout(500)

    def checkHorizontalCrossing(self):
        if self.pos.x > display_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = display_width
        if self.pos.y == display_height:
            self.gameOver = True
        if self.pos.y == -50:
            self.pos.y = display_height

    def checkEvent(self):
        self.acc = vec(0, gravity)
        self.jump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if not self.settings.playing:
                    if event.key == pygame.K_BACKSPACE:
                        self.settings.end.user_text = self.settings.end.user_text[:-1]
                    else:
                        self.settings.end.user_text += event.unicode
                if event.key == pygame.K_LEFT:
                    self.acc.x = -player_Acc
                if event.key == pygame.K_RIGHT:
                    self.acc.x = player_Acc
                if event.key == pygame.K_SPACE:
                    self.jump()
                if event.key == pygame.K_RETURN:
                    self.settings.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.settings.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.settings.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.settings.UP_KEY = True

    def messageToScreen(self, msg, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(msg, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.gameDisplay.blit(text_surface, text_rect)

    def jump(self):

        # We check if the player sprite is standing on a platform on or not.
        if self.vel.y > 0:
            self.img_pikachu.rect.y += 1
            hits = pygame.sprite.spritecollide(self.img_pikachu, self.platforms, False)
            self.img_pikachu.rect.y -= 1
            if hits:
                self.jump_sound.play()
                self.vel.y = -10

    def startScreen(self):
        self.gameDisplay.fill(orange)
        self.messageToScreen("DOODLE JUMP MP PROJECT - II", 40, white, display_width / 2, display_height / 2)
        self.messageToScreen("Press any key to continue...", 25, white, display_width / 2 + 50, display_height / 2 + 50)
        self.messageToScreen("High Score: " + str(self.highscore), 25, white, display_width / 2, 35)
        pygame.display.update()
        self.waitForKeyPress()
        g.run()

    def gameOverScreen(self):
        self.close_game(self.score, "GAME OVER", "red")

    def close_game(self, score: int, end_label: str, end_color: str, score_label: str = "SCORE: ", score_color: str = "orange"):
        pygame.mouse.set_visible(True)
        self.settings.end = EndMenu(self.settings)
        self.settings.curr_menu = self.settings.end
        self.settings.playing = False
        self.settings.curr_menu.display_menu(score, end_label, end_color)
        pygame.display.update()
        g.__init__()

    def draw_game_style(self):
        self.settings.display.fill(self.settings.BLACK)
        self.settings.display.blit(self.settings.background, (0, 0))
        self.draw_level(path=str(self.settings.level) + '.yaml')
        pygame.draw.rect(self.settings.display, pygame.Color("blue"), self.settings.paddle.figure)
        pygame.draw.circle(self.settings.display, pygame.Color("white"), self.settings.ball.figure.center,
                           self.settings.ball.radius)
        # show score
        render_score = self.settings.font_score.render(f'SCORE: {self.settings.score}', 1, pygame.Color('orange'))
        self.settings.display.blit(render_score, (5, 5))

    def win_or_game_over(self):
        if self.settings.ball.figure.bottom > self.settings.DISPLAY_H:
            self.close_game(score=self.settings.score, end_label='GAME OVER', end_color="red")
        elif not len(self.settings.blocks.block_list):
            self.settings.blocks = None
            if self.settings.level < 10:
                self.settings.level += 1
                self.draw_level(path=str(self.settings.level) + '.yaml')
                self.settings.paddle = Paddle(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H)
                self.settings.ball = Ball(WIDTH=self.settings.DISPLAY_W, HEIGHT=self.settings.DISPLAY_H)
            else:
                self.close_game(score=self.settings.score, end_label='YOU WIN!', end_color="green")

    def update_game_screen(self):
        self.settings.window.blit(self.settings.display, (0, 0))
        pygame.display.update()
        self.settings.clock.tick(self.settings.FPS)

    def reset_keys(self):
        self.settings.UP_KEY, self.settings.DOWN_KEY, self.settings.START_KEY, self.settings.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, color, x, y, font='8bit_wonder/8-BIT WONDER.TTF'):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, pygame.Color(color))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.settings.display.blit(text_surface, text_rect)


if __name__ == '__main__':
    g = Game()
    while g.settings.running:
        g.settings.curr_menu.display_menu()
        g.run()
