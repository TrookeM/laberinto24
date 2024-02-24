class Game:
    def __init__(self):
        self.maze = None

    def construct_wall(self):
        return Wall()

    def create_door(self, room1, room2):
        return Door(room1, room2)

    def build_room(self, room_id):
        room=Room(room_id)
        room.north=self.construct_wall()
        room.east=self.construct_wall()
        room.south=self.construct_wall()
        room.west=self.construct_wall()
        return room

    def generate_2_room_maze(self):
        maze = Maze()
        self.maze = maze
        room1 = self.build_room(1)
        room2 = self.build_room(2)
        door = self.create_door(room1, room2)
        room1.set_south_wall(door)  # More descriptive wall placement
        room2.set_north_wall(door)
        maze.add_room(room1)
        maze.add_room(room2)

    def create_2_room_maze_fm(self):
        room1 = self.build_room(1)
        room2 = self.build_room(2)
        door = self.create_door(room1, room2)
        maze = Maze()
        maze.add_room(room1)
        maze.add_room(room2)
        room1.set_south_wall(door)
        room2.set_north_wall(door)
        return maze


class BombedGame(Game):
    def construct_wall(self):
        return BombedWall()


class MapElement:
    def __init__(self):
        pass


class Container(MapElement):
    # Composite
    def __init__(self):
        self.components = []  # More descriptive name for children

    def add_component(self, component):  # More descriptive method name
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)


class Leaf(MapElement):
    def __init__(self):
        super().__init__()


class Decorator(Leaf):
    def __init__(self, component):
        self.component = component


class Bomb(Decorator):
    pass


class Maze(Container):
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)


class Room(MapElement):
    def __init__(self, id):
        self.id = id
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def set_walls(self, direction, wall):
        if direction == 'north':
            self.north = wall
        elif direction == 'east':
            self.east = wall
        elif direction == 'south':
            self.south = wall
        elif direction == 'west':
            self.west = wall

    def set_north_wall(self, wall):
        self.set_walls('north', wall)

    def set_east_wall(self, wall):
        self.set_walls('east', wall)

    def set_south_wall(self, wall):
        self.set_walls('south', wall)

    def set_west_wall(self, wall):
        self.set_walls('west', wall)

class Wall(MapElement):
    def __init__(self):
        pass


class BombedWall(Wall):
    def __init__(self):
        super().__init__()
        self.active = False


class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2


# Usage examples (unchanged)
game = Game()
game.generate_2_room_maze()

bgame = BombedGame()
bgame.generate_2_room_maze()

game = Game()
game.create_2_room_maze_fm()
