import random

LANGUAGES = ['Python', 'JavaScript', 'Java', 'C++']

def detect_language(code: str) -> str:
    # Simple heuristics to detect code language
    if 'def ' in code:
        return 'Python'
    elif 'function ' in code:
        return 'JavaScript'
    return random.choice(LANGUAGES)
