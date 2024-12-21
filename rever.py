def reverse_words(s: str) -> str:
    words = s.split()
    return " ".join(reversed(words))

# Example
print(reverse_words("Hello World"))  # "World Hello"
print(reverse_words("Python is fun"))  # "fun is Python"