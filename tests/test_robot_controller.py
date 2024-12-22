import unittest
from src.gui.components.robot_controller import RobotController

class TestRobotController(unittest.TestCase):
    def setUp(self):
        # Initialize controller before each test
        self.controller = RobotController()

    def test_connection(self):
        # Test robot connection functionality
        self.assertFalse(self.controller.connected)
        self.controller.connect()
        self.assertTrue(self.controller.connected)

    def test_movement(self):
        # Test robot movement operations
        self.controller.connect()
        self.assertTrue(self.controller.move("forward")) 