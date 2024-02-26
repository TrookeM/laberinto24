import unittest
from laberinto import *
from maze import *

class TestGame(unittest.TestCase):

    def test_build_room_returns_room_with_walls(self):
        game = Game()
        room = game.build_room(1)
        self.assertIsNotNone(room.north)  # Check north wall
        self.assertIsNotNone(room.east)  # Check east wall
        self.assertIsNotNone(room.south)  # Check south wall
        self.assertIsNotNone(room.west)  # Check west wall

    def test_build_room_returns_room_with_correct_id(self):
        game = Game()
        room = game.build_room(5)
        self.assertEqual(room.id, 5)

    def test_build_room_returns_different_rooms(self):
        game = Game()
        room1 = game.build_room(1)
        room2 = game.build_room(2)
        self.assertNotEqual(room1, room2)


class TestBombedGame(unittest.TestCase):

    def test_bombed_build_room_returns_bombed_walls(self):
        game = BombedGame()
        room = game.build_room(1)
        self.assertIsInstance(room.north, BombedWall)
        self.assertIsInstance(room.east, BombedWall)
        self.assertIsInstance(room.south, BombedWall)
        self.assertIsInstance(room.west, BombedWall)
