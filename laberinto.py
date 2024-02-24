class Game:
    def __init__(self):
        self.maze = None

    def create_wall(self):
        return Wall()

    def create_door(self, side1, side2):
        door = Door(side1, side2)
        return door

    def create_room(self, room_id):
        room = Room(room_id)
        room.north = self.create_wall()
        room.east = self.create_wall()
        room.south = self.create_wall()
        room.west = self.create_wall()
        return room

    def create_maze(self):
        return Maze()

    def make_2_rooms_maze_fm(self):
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        door = self.create_door(room1, room2)
        room1.south = door
        room2.north = door
        self.maze.add_room(room1)
        self.maze.add_room(room2)
        return self.maze

    def make_2_rooms_maze(self):
        self.maze = self.create_maze()
        room1 = self.create_room(1)
        room2 = self.create_room(2)
        self.maze.add_room(room1)
        self.maze.add_room(room2)

        door = self.create_door(room1, room2)
        room1.south = door
        room2.north = door
        return self.maze


class BombedGame(Game):
    def create_wall(self):
        return BombedWall()


class MapElement:
    def __init__(self):
        pass

    def enter(self):
        pass


class Container(MapElement):
    def __init__(self):
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)


class Leaf(MapElement):
    def accept(self, visitor):
        visitor.visit_leaf(self)


class Decorator(Leaf):
    def __init__(self, component):
        self.component = component


class Maze(Container):
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def enter(self):
        self.rooms[0].enter()


class Room(Container):
    def __init__(self, room_id):
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.id = room_id

    def enter(self):
        print("Has entrado a la habitación", self.id)


class Door(MapElement):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        self.opened = False

    def enter(self):
        if self.opened:
            self.side2.enter()
        else:
            print("La pueera esta cerrada.")


class Wall(MapElement):
    def __init__(self):
        pass  # Walls don't need additional attributes

    def enter(self):
        print("No puedes atravesaar paredes...")


class BombedWall(Wall):
    def __init__(self):
        self.active = False

    def enter(self):
        if self.active:
            print("La bomba ha explotado!")
        else:
            return super().enter()


# Usage examples
game = Game()
game.make_2_rooms_maze()
game.maze.enter()

game = Game()
game.make_2_rooms_maze_fm()
game.maze.enter()

game = BombedGame()
game.make_2_rooms_maze_fm()
game.maze.enter()
