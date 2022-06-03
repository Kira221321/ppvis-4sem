import pygame

from .database import DataBase


class Menu:
    pygame.init()
    pygame.mixer.music.load('sounds/menu-music.mp3')
    pygame.mixer.music.play(-1)

    def __init__(self, game):
        self.settings = game
        self.mid_w, self.mid_h = self.settings.DISPLAY_W / 2, self.settings.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.settings.game.draw_text('*', 15, 'white', self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.settings.window.blit(self.settings.display, (0, 0))
        pygame.display.update()
        self.settings.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.leaderboardx, self.leaderboardy = self.mid_w, self.mid_h + 50
        self.helpx, self.helpy = self.mid_w, self.mid_h + 70
        self.exitx, self.exity = self.mid_w, self.mid_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.settings.game.checkEvent()
            self.check_input()
            self.settings.display.fill(self.settings.BLACK)
            self.settings.game.draw_text('Main Menu', 20, 'white', self.settings.DISPLAY_W / 2,
                                         self.settings.DISPLAY_H / 2 - 20)
            self.settings.game.draw_text("Start Game", 20, 'white', self.startx, self.starty)
            self.settings.game.draw_text("Leaders", 20, 'white', self.leaderboardx, self.leaderboardy)
            self.settings.game.draw_text("Help", 20, 'white', self.helpx, self.helpy)
            self.settings.game.draw_text("Exit", 20, 'white', self.exitx, self.exity)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.settings.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (self.helpx + self.offset, self.helpy)
                self.state = 'Help'
            elif self.state == 'Help':
                self.cursor_rect.midtop = (self.    exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.settings.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Leaderboard':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Help':
                self.cursor_rect.midtop = (self.leaderboardx + self.offset, self.leaderboardy)
                self.state = 'Leaderboard'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (self.helpx + self.offset, self.helpy)
                self.state = 'Help'

    def check_input(self):
        self.move_cursor()
        if self.settings.START_KEY:
            if self.state == 'Start':
                pygame.mixer.music.pause()
                self.settings.curr_menu = None
                self.settings.playing = True
            elif self.state == 'Leaderboard':
                self.settings.curr_menu = self.settings.leaderboard
                print("leaderboard")
            elif self.state == 'Help':
                self.settings.curr_menu = self.settings.help
                print("help")
            elif self.state == 'Exit':
                exit()
            self.run_display = False


class LeaderboardMenu(Menu):

    def __init__(self, game, max_leaders):
        self.max_leaders = max_leaders
        # self.leaders = DataBase.get_leaders()
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        self.leaders = DataBase.get_leaders()
        while self.run_display:
            self.settings.game.checkEvent()
            if self.settings.START_KEY or self.settings.BACK_KEY:
                self.settings.curr_menu = self.settings.main_menu
                self.run_display = False
            self.settings.display.fill(self.settings.BLACK)

            text_size = 10
            padding = text_size

            self.settings.game.draw_text('Leaderboard', text_size * 3, 'darkorange', self.settings.DISPLAY_W / 2,
                                         padding * 2)
            padding += text_size * 5
            space = 20
            for i in range(len(self.leaders)):
                if i == 0:
                    space *= 2
                    self.draw_player(position=i, spacing=space, player=self.leaders[i], text_size=text_size * 2,
                                     text_color='yellow', padding=padding)
                elif i == 1:
                    space *= 3 / 2
                    self.draw_player(position=i, spacing=int(space), player=self.leaders[i],
                                     text_size=text_size * 3 / 2, text_color='gray', padding=padding)
                else:
                    self.draw_player(position=i, spacing=space, player=self.leaders[i], text_size=text_size,
                                     text_color='white', padding=padding)
                padding += text_size * 3
            self.blit_screen()

    def draw_player(self, position, spacing, player, text_size, text_color, padding):
        self.settings.game.draw_text(f"{position + 1}" + " " * 5 + player[0] + " " * 5 + str(player[1]), int(text_size),
                                     text_color, self.settings.DISPLAY_W / 2, padding)


class HelpMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.settings.game.checkEvent()
            if self.settings.START_KEY or self.settings.BACK_KEY:
                self.settings.curr_menu = self.settings.main_menu
                self.run_display = False
            self.settings.display.fill(self.settings.BLACK)
            text_size = 10
            padding = text_size

            self.settings.game.draw_text('Rules of the game Doodle Jump', text_size, 'white', self.settings.DISPLAY_W / 2,
                                         padding)
            padding += text_size * 5 / 2
            self.settings.game.draw_text('Purpose of the game', text_size, 'darkorange', self.settings.DISPLAY_W / 2,
                                         padding)
            padding += text_size * 3 / 2
            self.settings.game.draw_text('To guide a creature called the Doodler up without falling',
                                         int(text_size - 2), 'orange', self.settings.DISPLAY_W / 2, padding)
            padding += text_size * 5 / 2
            self.settings.game.draw_text('How to play', text_size, 'darkorange', self.settings.DISPLAY_W / 2, padding)
            padding += text_size * 3 / 2
            for i in ['To play Doodle Jump move left to right to reach the platforms',
                      'The gameplay is endless jump for as long as possible']:
                self.settings.game.draw_text(i, int(text_size - 2), 'orange', self.settings.DISPLAY_W / 2, padding)
                padding += text_size * 3 / 2
            self.settings.game.draw_text('to achieve your greatest score', int(text_size - 2), 'orange',
                                         self.settings.DISPLAY_W / 2, padding)
            padding += text_size * 5 / 2
            self.settings.game.draw_text('Obstacles', text_size, 'darkorange', self.settings.DISPLAY_W / 2, padding)
            padding += text_size * 3 / 2
            self.settings.game.draw_text('Along with boosters to propel your alien to new heights',
                                         int(text_size - 2), 'red', self.settings.DISPLAY_W / 2, padding)

            self.blit_screen()


class EndMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.font_end = pygame.font.SysFont('Arial', 40, bold=True)
        self.font_score = pygame.font.SysFont('Arial', 20, bold=True)
        self.base_font = pygame.font.SysFont('Arial', 20)
        self.record_font = pygame.font.SysFont('Arial', 32, bold=True)
        self.user_text = ''
        self.new_record = False

    def display_menu(self, score: int, end_label: str, end_color: str, score_label: str = "SCORE: ",
                     score_color: str = "orange"):
        self.run_display = True
        self.settings.display.fill(self.settings.BLACK)
        self.blit_screen()
        while self.run_display:
            self.settings.game.checkEvent()
            # exits
            if self.settings.BACK_KEY:
                pygame.mixer.music.unpause()
                self.settings.curr_menu = self.settings.main_menu
                self.run_display = False
            if self.settings.START_KEY:
                pygame.mixer.music.unpause()
                if self.new_record:
                    DataBase.add_new_record(self.user_text[:-1], score)
                self.settings.curr_menu = self.settings.main_menu
                self.settings.playing = False
                self.run_display = False

            render_end = self.font_end.render(end_label, 0, pygame.Color(end_color))
            render_score = self.font_score.render(score_label + str(score), 0, pygame.Color(score_color))
            self.settings.window.blit(render_end, render_end.get_rect(
                center=(self.settings.DISPLAY_W // 2, self.settings.DISPLAY_H // 2)))
            self.settings.window.blit(render_score, render_score.get_rect(
                center=(self.settings.DISPLAY_W // 2, self.settings.DISPLAY_H // 2 + 30)))

            if score > DataBase.get_leader_score():
                new_record_surface = self.record_font.render("NEW RECORD!", True, (255, 215, 0))
                text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
                self.settings.window.blit(text_surface,
                                          (self.settings.DISPLAY_W // 2 - 35, self.settings.DISPLAY_H // 2 + 60))
                self.settings.window.blit(new_record_surface, new_record_surface.get_rect(
                    center=(self.settings.DISPLAY_W // 2, self.settings.DISPLAY_H // 2 - 90)))
                self.new_record = True

            pygame.display.flip()


if __name__ == "__main__":
    cursor = DataBase.connect_database()
    cursor.execute('''DELETE FROM leaders WHERE score > 0''')
    DataBase.conn.commit()
    DataBase.conn.close()
