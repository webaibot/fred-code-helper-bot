import unittest
from bot.engine import bot_instance

class TestCodeHelperBot(unittest.TestCase):
    def test_start_session(self):
        bot_instance.start_session('test_session')
        self.assertIn('test_session', bot_instance.sessions)

    def test_get_template(self):
        template = bot_instance.get_template('Python', 'hello_world')
        self.assertEqual(template, 'print("Hello, World!")')

    def test_process_message(self):
        response = bot_instance.process_message('test_session', 'Hello, Fred!')
        self.assertIn('Processed message', response)

if __name__ == '__main__':
    unittest.main()
