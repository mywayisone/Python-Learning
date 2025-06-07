def greet_user(name):
    return f"Hello, {name.capitalize()}! Welcome back."

def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())