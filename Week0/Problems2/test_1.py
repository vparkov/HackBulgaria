import unittest
from count_words import count_words


class hue(unittest.TestCase):

    def test_with_3_variables(self):
        result = {'apple': 2, 'pie': 1, 'banana': 1}
        inputt = count_words(["apple", "banana", "apple", "pie"])
        self.assertEqual(inputt, result)

    def test_with_3_variables1(self):
        result = {'ruby': 1, 'python': 3}
        inputt = count_words(["python", "python", "python", "ruby"])
        self.assertEqual(inputt, result)

    def test_with_no_variables(self):
        result = {'':1}
        inputt = count_words([""])
        self.assertEqual(inputt, result)

if __name__ == "__main__":
    unittest.main()