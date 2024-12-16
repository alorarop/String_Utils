import unittest
from string_utils.string_ops import reverse_string, is_palindrome, count_vowels_and_consonants

class TestStringOps(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("A Santa at NASA"))
        self.assertFalse(is_palindrome("hello"))

    def test_count_vowels_and_consonants(self):
        self.assertEqual(count_vowels_and_consonants("hello"), {"vowels": 2, "consonants": 3})

if __name__ == "__main__":
    unittest.main()
