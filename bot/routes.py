from flask import Blueprint, jsonify, request
from flask_cors import CORS
from .engine import bot_instance

bp = Blueprint('routes', __name__)
CORS(bp)

@bp.route('/', methods=['GET'])
def index():
    return '<h1>Welcome to Fred the Code Helper</h1>'

@bp.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    session_id = data.get('session_id')
    message = data.get('message')
    bot_instance.start_session(session_id)
    response = bot_instance.process_message(session_id, message)
    return jsonify({'response': response})

@bp.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

@bp.route('/api/stats', methods=['GET'])
def stats():
    return jsonify({'total_sessions': len(bot_instance.sessions)})
