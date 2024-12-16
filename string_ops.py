# string_ops.py

def reverse_string(s):
    """Reverses a given string."""
    return s[::-1]

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    s = s.lower().replace(" ", "")  # Make it case and space insensitive
    return s == s[::-1]

def count_vowels_and_consonants(s):
    """Counts vowels and consonants in a string."""
    vowels = "aeiouAEIOU"
    s = s.replace(" ", "")
    vowels_count = sum(1 for char in s if char in vowels)
    consonants_count = len(s) - vowels_count
    return {"vowels": vowels_count, "consonants": consonants_count}
