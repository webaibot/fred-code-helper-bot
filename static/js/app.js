document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatContainer = document.getElementById('chat-container');

    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const message = chatInput.value;
        if (message.trim() !== '') {
            addMessageToChat('You', message);
            chatInput.value = '';
            fetch('/api/chat', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({session_id: 'default', message: message})
            })
            .then(response => response.json())
            .then(data => {
                addMessageToChat('Fred', data.response);
            });
        }
    });

    function addMessageToChat(sender, message) {
        const messageBubble = document.createElement('div');
        messageBubble.classList.add('chat-bubble');
        messageBubble.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatContainer.appendChild(messageBubble);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
});
