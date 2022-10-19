import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertRaises(english_to_french(None), ValueError)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertRaises(french_to_english(None), ValueError)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()