let chatHistory = [];

async function sendMessage() {
  const input = document.getElementById('chatInput');
  const msg = input.value.trim();
  if (!msg) return;
  input.value = ''; input.style.height = 'auto';
  appendBubble(msg, 'user');
  chatHistory.push({ role: 'user', content: msg });
  await getAIResponse();
}

function sendQuick(btn) {
  const msg = btn.textContent;
  btn.closest('div').remove();
  document.getElementById('chatInput').value = msg;
  sendMessage();
}

function handleChatKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
}

function autoResize(el) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 120) + 'px';
}

function appendBubble(text, role) {
  const wrap = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = `bubble bubble-${role}`;
  div.textContent = text;
  wrap.appendChild(div);
  wrap.scrollTop = wrap.scrollHeight;
  return div;
}

function showTyping() {
  const wrap = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'bubble bubble-ai bubble-typing';
  div.id = 'typingIndicator';
  div.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
  wrap.appendChild(div);
  wrap.scrollTop = wrap.scrollHeight;
}

function removeTyping() {
  document.getElementById('typingIndicator')?.remove();
}

async function getAIResponse() {
  document.getElementById('sendBtn').disabled = true;
  showTyping();
  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: chatHistory[chatHistory.length-1].content, history: chatHistory })
    });
    const data = await res.json();
    removeTyping();
    const bubble = appendBubble('', 'ai');
    // Typewriter effect
    const text = data.response || 'Sorry, I could not generate a response.';
    chatHistory.push({ role: 'assistant', content: text });
    let i = 0;
    const typer = setInterval(() => {
      bubble.textContent = text.slice(0, i);
      i += 2;
      document.getElementById('chatMessages').scrollTop = 999999;
      if (i > text.length) { bubble.textContent = text; clearInterval(typer); }
    }, 12);
  } catch(e) {
    removeTyping();
    appendBubble('Connection error. Please try again.', 'ai');
  } finally {
    document.getElementById('sendBtn').disabled = false;
    document.getElementById('chatInput').focus();
  }
}
function sendSuggestion(text) {
    document.getElementById('chatInput').value = text;
    sendMessage();
}