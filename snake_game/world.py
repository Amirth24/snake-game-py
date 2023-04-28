from pygame import Surface, Rect, draw,Color


from enum import Enum

class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2 
    RIGHT = 3

def opposite_dir(dir: Direction) -> Direction:
    match dir:
        case Direction.UP:
            return Direction.DOWN
        
        case Direction.DOWN:
            return Direction.UP
        
        case Direction.RIGHT:
            return Direction.LEFT
        
        case Direction.LEFT:
            return Direction.RIGHT


class World:
    def __init__(self, dim: tuple[int, int], cell_size: int, surf: Surface) -> None:
        self.bound = (0,0, *dim)
        self.cell_size = cell_size

        self.surf = surf

        self.rects = [] # Store the rect in (x, y) tuple where x (row) and y(col) are grid index.

    @property
    def width(self) -> int:
        return (self.bound[-2] - self.bound[0] ) // self.cell_size
    
    @property
    def height(self) -> int:
        return (self.bound[-1]-self.bound[1]) // self.cell_size
    
    def to_rect(self, g) -> Rect:
        return Rect(g[0]*self.cell_size,g[1]*self.cell_size, self.cell_size, self.cell_size)
    
    def draw(self):
        # Draw all the rectangle in buffer
        for rect in self.rects:
            draw.rect(self.surf, Color(255,255,255), self.to_rect(rect))
