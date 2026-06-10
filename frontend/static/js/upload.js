let selectedFile = null;

// Drag and drop
const dropZone = document.getElementById('dropZone');
dropZone.addEventListener('dragover', (e) => {
  e.preventDefault();
  dropZone.classList.add('dragover');
});
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
dropZone.addEventListener('drop', (e) => {
  e.preventDefault();
  dropZone.classList.remove('dragover');
  const file = e.dataTransfer.files[0];
  if (file && file.type === 'application/pdf') setFile(file);
  else alert('Please drop a PDF file only.');
});

function handleFileSelect(input) {
  if (input.files[0]) setFile(input.files[0]);
}

function setFile(file) {
  selectedFile = file;
  const nameEl = document.getElementById('file-name');
  nameEl.textContent = '✅ ' + file.name;
  nameEl.style.display = 'block';
}

function setLevel(btn, value) {
  document.querySelectorAll('.level-pill').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  document.getElementById('levelInput').value = value;
}

const loadingMessages = [
  "Extracting skills from PDF...",
  "Comparing with industry requirements...",
  "Building your Career DNA...",
  "Generating 90-day roadmap with AI...",
  "Almost there..."
];

async function submitResume() {
  if (!selectedFile) { alert('Please upload your resume PDF first!'); return; }

  const jobRole = document.getElementById('jobRole').value;
  const level = document.getElementById('levelInput').value;

  const formData = new FormData();
  formData.append('resume', selectedFile);
  formData.append('job_role', jobRole);
  formData.append('level', level);

  // Show loading
  const overlay = document.getElementById('loadingOverlay');
  overlay.classList.add('active');
  document.getElementById('analyzeBtn').disabled = true;

  // Cycle messages
  let i = 0;
  const interval = setInterval(() => {
    document.getElementById('loading-step').textContent = loadingMessages[i % loadingMessages.length];
    i++;
  }, 2500);

  try {
    const res = await fetch('/analyze', { method: 'POST', body: formData });
    const data = await res.json();
    clearInterval(interval);
    // Existing submitResume() ke andar, data.success block replace karo:
if (data.success) {
    // Check if logged in
    const loginStatus = await fetch('/check-login');
    const loginData = await loginStatus.json();
    
    if (!loginData.logged_in) {
        overlay.classList.remove('active');
        document.getElementById('analyzeBtn').disabled = false;
        showSignupPopup(data.redirect);
    } else {
        window.location.href = data.redirect;
    }
}
  } catch (err) {
    clearInterval(interval);
    overlay.classList.remove('active');
    document.getElementById('analyzeBtn').disabled = false;
    alert('Network error. Make sure the server is running.');
  }
}
function showSignupPopup(redirectUrl) {
    // Create popup
    const popup = document.createElement('div');
    popup.id = 'signup-popup';
    popup.innerHTML = `
        <div class="popup-backdrop" onclick="closePopup()"></div>
        <div class="popup-box">
            <h2>Save Your Analysis 💾</h2>
            <p>Create a free account to save your Career DNA report, chat history, and track your progress.</p>
            <div class="popup-btns">
                <a href="/signup?next=${redirectUrl}" class="btn-primary">Create Free Account</a>
                <a href="/login?next=${redirectUrl}" class="btn-outline">Login</a>
                <button onclick="skipToAnalysis('${redirectUrl}')" class="btn-skip">Continue without login →</button>
            </div>
        </div>
    `;
    document.body.appendChild(popup);
}

function skipToAnalysis(url) {
    document.getElementById('signup-popup')?.remove();
    window.location.href = url;
}

function closePopup() {
    document.getElementById('signup-popup')?.remove();
}