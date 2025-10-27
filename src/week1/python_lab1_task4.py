"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))

def count_words(text):
    """Count number of words in a string."""
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    num = []
    for word in text.split():
        if word.isdigit():
            num.append(int(word))
    return num

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char = count_characters(text)
    words = count_words(text)
    num = extract_numbers(text)
    total = sum(num)
    average = total / len(num) if num else 0
    return char, words, num, total, average

if __name__ == "__main__":
    text = input("Enter a text: ")
    char, words, num, total, average = analyze_text(text)
    print(f"Non-space characters: {char}")
    print(f"Word count: {words}")
    print(f"Numbers found: {num}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {average:.2f}")
