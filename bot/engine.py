from typing import Dict, Any
from .knowledge import templates, syntax_references
from .models import CodeSession

class CodeHelperBot:
    def __init__(self):
        self.sessions: Dict[str, CodeSession] = {}

    def start_session(self, session_id: str):
        if session_id not in self.sessions:
            self.sessions[session_id] = CodeSession(session_id)

    def get_template(self, language: str, template_name: str) -> str:
        return templates.get(language, {}).get(template_name, 'Template not found')

    def get_syntax_reference(self, language: str) -> str:
        return syntax_references.get(language, 'Syntax reference not available')

    def process_message(self, session_id: str, message: str) -> str:
        # Simulated processing logic
        return f'Processed message: {message}'

bot_instance = CodeHelperBot()
