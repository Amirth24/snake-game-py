import pygame as pg

class Game:
    def __init__(self) -> None:
        pg.init()

        self.fps = 60

        self.surface = pg.display.set_mode((600, 400))

        self.clock = pg.time.Clock()

        # For Debug Info
        self.dbg_font = pg.font.SysFont('Verdana', 14)
        self.dbg_rect = pg.rect.Rect(0,0,30 , 140)

    def update(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit_game()
            


    def draw(self) -> None:
        self.surface.fill(0)


    def disp_dbg(self) -> None:
        dbg_text = f'FPS: {self.clock.get_fps():.1f}'

        dbg_info = self.dbg_font.render(dbg_text, True, pg.Color(255,255,255,126))

        self.surface.blit(dbg_info, self.dbg_rect)

    def run(self) -> None:
        while 1:
            
            self.update()
            self.draw()

            self.disp_dbg() # For Debug purpose

            pg.display.update()


    def exit_game(self) -> None:
        print('bye')

        pg.quit()
        quit()

