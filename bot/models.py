from dataclasses import dataclass

@dataclass
class CodeSession:
    session_id: str
    language: str = ''
    code_snippets: list = None

class DifficultyLevel:
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
