let chatHistory = [];

async function sendMessage() {
  const input = document.getElementById('chatInput');
  const message = input.value.trim();
  if (!message) return;
  input.value = '';
  appendMessage(message, 'user');
  chatHistory.push({ role: 'user', content: message });

  const typingEl = appendTyping();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, history: chatHistory })
    });
    const data = await res.json();
    typingEl.remove();
    appendMessage(data.response, 'ai');
    chatHistory.push({ role: 'assistant', content: data.response });
  } catch {
    typingEl.remove();
    appendMessage('Connection error. Please try again.', 'ai');
  }
}

function appendMessage(text, role) {
  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = `chat-bubble bubble-${role}`;
  div.textContent = text;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
  return div;
}

function appendTyping() {
  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'chat-bubble bubble-ai';
  div.innerHTML = '<span class="typing-dots">●●●</span>';
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
  return div;
}

function sendSuggestion(text) {
  document.getElementById('chatInput').value = text;
  sendMessage();
}