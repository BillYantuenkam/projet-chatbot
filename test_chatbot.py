import unittest
from src.chatbot import Chatbot

class TestChatbot(unittest.TestCase):
    def test_initialization(self):
        bot = Chatbot()
        self.assertIsNotNone(bot)

if __name__ == '__main__':
    unittest.main()
