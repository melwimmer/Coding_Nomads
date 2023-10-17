def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    sentence = f"{greeting}, {name}! How are you?"
    return sentence

print(greet("hi!", "melanie"))