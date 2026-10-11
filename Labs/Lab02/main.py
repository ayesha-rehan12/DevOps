
def greet(name):
    return f"Hello, {name}!"


def add_numbers(a, b):
    return a + b


def format_greeting(name):
    """Return a personalized greeting."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name must be a non-empty string.")
    return f"Hello, {name.strip()}! Welcome to the code review demo."
