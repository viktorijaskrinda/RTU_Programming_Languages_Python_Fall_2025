"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    total_char = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()
    return total_char, word_count, contains_python

if __name__ == "__main__":
    sentence = input("Write a sentence: ")
    char, words, has_python = analyze_sentence(sentence)
    print(f"Total characters: {char}")
    print(f"Word count: {words}")
    print(f"Contains the word 'Python': {has_python}")
