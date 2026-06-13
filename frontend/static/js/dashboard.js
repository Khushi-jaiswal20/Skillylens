function initDashboard(data) {
  renderRadarChart(data.career_dna);
  renderRoadmap(data.roadmap);
  renderAITools(data.ai_tools);
}

function renderRadarChart(dna) {
  const ctx = document.getElementById('radarChart');
  if (!ctx || !dna) return;
  new Chart(ctx, {
    type: 'radar',
    data: {
      labels: Object.keys(dna),
      datasets: [{
        label: 'Your Career DNA',
        data: Object.values(dna),
        backgroundColor: 'rgba(99,102,241,0.15)',
        borderColor: '#6366f1',
        borderWidth: 2,
        pointBackgroundColor: '#a855f7',
        pointRadius: 4
      }]
    },
   // NAYA
options: {
  scales: {
    r: {
      min: 0, max: 100,
      ticks: { display: false },
      grid: {
        color: document.documentElement.getAttribute('data-theme') === 'light'
          ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.05)'
      },
      pointLabels: {
        color: document.documentElement.getAttribute('data-theme') === 'light'
          ? '#374151' : '#94a3b8',
        font: { size: 11 }
      }
    }
  },
  plugins: { legend: { display: false } }
}
  });
}

function renderRoadmap(roadmap) {
  const container = document.getElementById('roadmap-container');
  if (!roadmap || Object.keys(roadmap).length === 0) {
    container.innerHTML = '<p style="color:#64748b">Roadmap could not be generated. Please try again.</p>';
    return;
  }
  const phases = [
    { key: 'phase1', label: 'Phase 1 — Foundations', cls: '' },
    { key: 'phase2', label: 'Phase 2 — Build Up', cls: 'phase-2' },
    { key: 'phase3', label: 'Phase 3 — Master', cls: 'phase-3' }
  ];
  let html = '';
  phases.forEach(p => {
    const phase = roadmap[p.key];
    if (!phase) return;
    const tasks = (phase.tasks || []).map(t => `
      <div style="background:var(--bg-elevated);padding:0.75rem;border-radius:8px;margin:0.5rem 0">
        <div style="display:flex;justify-content:space-between">
          <strong>${t.skill || t.task}</strong>
          <span style="color:#6366f1;font-size:0.8rem">${t.hours || '?'}h</span>
        </div>
        <p style="color:#94a3b8;font-size:0.8rem;margin-top:0.25rem">${t.task || ''}</p>
        ${t.resource_name ? `<a href="${t.resource_url || '#'}" target="_blank" 
          style="color:#a855f7;font-size:0.75rem">📚 ${t.resource_name}</a>` : ''}
      </div>`).join('');
    html += `<div class="phase-card ${p.cls}">
      <h4 style="margin-bottom:0.5rem">${p.label}</h4>
      <p style="color:#64748b;font-size:0.8rem">${phase.duration || ''}</p>
      ${tasks}
    </div>`;
  });
  container.innerHTML = html;
}

function renderAITools(aiTools) {
  const renderTools = (tools, containerId) => {
    const el = document.getElementById(containerId);
    if (!el || !tools) return;
    el.innerHTML = tools.map(t => `
      <a href="${t.link}" target="_blank" class="tool-card">
        <div class="tool-name">${t.name}</div>
        <div class="tool-use">${t.use}</div>
      </a>`).join('');
  };
  renderTools(aiTools?.famous, 'famous-tools');
  renderTools(aiTools?.underrated, 'underrated-tools');
}

async function downloadReport() {
    const btn = document.querySelector('[onclick="downloadReport()"]');
    btn.textContent = '⏳ Generating...';
    btn.disabled = true;
    
    const res = await fetch('/download-report');
    if (res.status === 401) {
        btn.textContent = '⬇ Download PDF';
        btn.disabled = false;
        // Show login popup
        const popup = document.createElement('div');
        popup.id = 'signup-popup';
        popup.innerHTML = `
            <div class="popup-backdrop" onclick="this.parentElement.remove()"></div>
            <div class="popup-box">
                <h2>Login to Download 📄</h2>
                <p>Create a free account or login to download your Career DNA PDF report.</p>
                <div class="popup-btns">
                    <a href="/signup" class="btn-primary">Create Free Account</a>
                    <a href="/login" class="btn-outline">Login</a>
                    <button onclick="document.getElementById('signup-popup').remove()" 
                        class="btn-skip">Cancel</button>
                </div>
            </div>`;
        document.body.appendChild(popup);
        return;
    }
    
    // Download the blob
    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'SkillyLens_Report.pdf';
    a.click();
    btn.textContent = '⬇ Download PDF';
    btn.disabled = false;
}