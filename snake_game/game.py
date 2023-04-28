from dataclasses import dataclass
import pygame as pg

from .world import World, Direction

@dataclass
class GameConfig:
    win_dim : tuple[int, int] = (600, 480)

    # debug settings
    dbg_font_size:int = 14
    dbg_text_wrap: int = 30

    # World Settings
    world_cell_size: int = 10

    # Key Maps
    u_k = pg.K_w
    d_k = pg.K_s
    l_k = pg.K_a
    r_k = pg.K_d



class Game:
    def __init__(self) -> None:
        pg.init()
        self.config = GameConfig()

        self.fps = 60
        self.surface = pg.display.set_mode(self.config.win_dim) # Create Display
        self.clock = pg.time.Clock() # Clock for fps

        self.key_map = {
            self.config.u_k : Direction.UP,
            self.config.d_k : Direction.DOWN,
            self.config.l_k : Direction.LEFT,
            self.config.r_k : Direction.RIGHT,
        }


        # For Debug Info
        self.dbg_font = pg.font.SysFont('Verdana', self.config.dbg_font_size)
        self.dbg_rect = pg.rect.Rect(0,0,self.config.dbg_text_wrap, self.config.dbg_font_size*10)


        self.world = World(self.config.win_dim, self.config.world_cell_size, self.surface)



    def update(self) -> None:
        new_dir = None
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.exit_game()

            elif event.type == pg.KEYDOWN:
                match event.dict.get('key'):
                    # Other Keys than control ..


                    # Snake Control
                    case x:
                        new_dir = self.key_map.get(x, None)


        self.world.update(new_dir) 

            


    def draw(self) -> None:
        self.surface.fill(0)
        self.world.draw()


    def disp_dbg(self) -> None:
        dbg_text = f'FPS: {self.clock.get_fps():.1f}'

        dbg_info = self.dbg_font.render(dbg_text, True, pg.Color(255,255,255,126))

        self.surface.blit(dbg_info, self.dbg_rect)

    def run(self) -> None:
        while 1:
            self.clock.tick(self.fps)
            
            self.update()
            self.draw()

            self.disp_dbg() # For Debug purpose

            pg.display.update()


    def exit_game(self) -> None:
        print('bye')

        pg.quit()
        quit()

