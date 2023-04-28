import random

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

        self.spawn_snake((self.width//2, self.height//2))

        self.current_dir = Direction.LEFT

        self.gen_food()

    #################################################
    def spawn_snake(self, pos:tuple[int, int]):
        self.snake =  [pos,(pos[0]+1, pos[1]),(pos[0]+2, pos[1])]

    def gen_food(self):
        self.food_pos = (random.randint(0, self.width), random.randint(0, self.height))
        if self.food_pos in self.snake:
            self.gen_food() # Get a Valid food position until....

    def update_snake(self, direction: Direction):
        cell = self.snake[0]
        if direction != None and direction != opposite_dir(self.current_dir):
            self.current_dir = direction

        match self.current_dir:
            case Direction.UP:
                new_cell = (cell[0], cell[1] - 1)
            case Direction.DOWN:
                new_cell = (cell[0], cell[1] + 1)
            case Direction.LEFT:
                new_cell = (cell[0] - 1, cell[1])
            case Direction.RIGHT:
                new_cell = (cell[0] + 1, cell[1])

        # Wrapping the snake within the bound
        if new_cell[0] < 0 :
            new_cell =( self.width - 1, new_cell[1])
        
        if new_cell[1] < 0 :
            new_cell = (new_cell[0] , self.height - 1)

        if new_cell[0] > self.width :
            new_cell =( 0, new_cell[1])
        
        if new_cell[1] > self.height :
            new_cell = (new_cell[0] , 0)

        # This makes Snake Grow
        if new_cell == self.food_pos:
            self.snake = [new_cell] + self.snake
        else:
            self.snake = [new_cell] + self.snake[:-1]
        

    #################################################

    @property
    def width(self) -> int:
        return (self.bound[-2] - self.bound[0] ) // self.cell_size
    
    @property
    def height(self) -> int:
        return (self.bound[-1]-self.bound[1]) // self.cell_size
    
    def to_rect(self, g:tuple[int, int]) -> Rect:
        return Rect(g[0]*self.cell_size,g[1]*self.cell_size, self.cell_size, self.cell_size)
    
    #################################################

    def update(self, new_direction:Direction):
        self.update_snake(new_direction)
    
    def draw(self):

        # Snake Head
        snake_head = self.snake[0]
        draw.rect(self.surf, Color(255,255,255), self.to_rect(snake_head))
        # Snake Body
        for rect in self.snake[1:]:
            draw.rect(self.surf, Color(255,255,255,20),self.to_rect(rect))

        # Draw Food
        draw.rect(self.surf, Color(255, 0,0), self.to_rect(self.food_pos) )
       

