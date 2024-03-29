import unittest
import tkinter as tk
from unittest.mock import Mock
from GUI import My_thirdUI, My_secondUI  # Suppose you have a My_secondUI class

class TestGUI(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.title("Test Window")
        self.root.geometry("800x600")
        self.root.withdraw()

        # For testing purposes, simulate the My_secondUI class
        class MockMySecondUI:
            def __init__(self, root, value):
                self.root = root
                self.value = value

        self.mock_my_second_ui = MockMySecondUI
        self.my_second_ui = self.mock_my_second_ui  # Use self. to indicate that it is an instance property

    def tearDown(self):
        # Restore the original My_secondUI class after testing
        self.my_second_ui = My_secondUI
        self.root.destroy()

    def test_change(self):
        third_ui = My_thirdUI(self.root)
        third_ui.overframe.destroy = Mock()

        third_ui.change()

        third_ui.overframe.destroy.assert_called_once()

    def test_end(self):
        third_ui = My_thirdUI(self.root)
        third_ui.root.destroy = Mock()

        third_ui.end()

        third_ui.root.destroy.assert_called_once()

if __name__ == '__main__':
    unittest.main()
