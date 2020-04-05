import unittest
import cap

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cat_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_word(self):
        text = 'python text'
        result = cap.cat_text(text)
        self.assertEqual(result, 'Python Text')

    def test_asd_word(self):
        text = 'python'
        result = cap.cat_text(text)
        self.assertEqual(result, 'Python')


if __name__ == '__main__':
    unittest.main()
