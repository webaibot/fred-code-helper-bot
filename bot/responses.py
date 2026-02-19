def get_greeting() -> str:
    return "Hello! I'm Fred, your friendly code helper bot. How can I assist you today?"

def get_error_message() -> str:
    return "Oops! Something went wrong. Can you try again?"

def get_help_text() -> str:
    return "I can help with code templates, syntax references, and more. Just ask!"

def build_dynamic_response(template: str) -> str:
    return f"Here's a useful template for you: {template}"
