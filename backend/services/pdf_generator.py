from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, 
                                 Table, TableStyle, HRFlowable)
from reportlab.lib.units import cm
from reportlab.lib import colors
import os, json, datetime

INDIGO = HexColor('#6366f1')
PURPLE = HexColor('#a855f7')
GREEN = HexColor('#22c55e')
RED = HexColor('#ef4444')
AMBER = HexColor('#f59e0b')
DARK = HexColor('#1e1e2e')
LIGHT_BG = HexColor('#f8fafc')
GRAY = HexColor('#64748b')

def make_styles():
    return {
        'title': ParagraphStyle('title', fontSize=26, fontName='Helvetica-Bold',
                                textColor=INDIGO, spaceAfter=4),
        'subtitle': ParagraphStyle('subtitle', fontSize=11, fontName='Helvetica',
                                   textColor=GRAY, spaceAfter=16),
        'h2': ParagraphStyle('h2', fontSize=14, fontName='Helvetica-Bold',
                              textColor=INDIGO, spaceBefore=18, spaceAfter=8),
        'h3': ParagraphStyle('h3', fontSize=11, fontName='Helvetica-Bold',
                              textColor=HexColor('#1e293b'), spaceBefore=10, spaceAfter=4),
        'body': ParagraphStyle('body', fontSize=10, fontName='Helvetica',
                               textColor=HexColor('#334155'), spaceAfter=4, leading=16),
        'small': ParagraphStyle('small', fontSize=9, fontName='Helvetica',
                                textColor=GRAY, spaceAfter=3),
        'tag_pass': ParagraphStyle('tag_pass', fontSize=9, fontName='Helvetica-Bold',
                                   textColor=GREEN),
        'tag_fail': ParagraphStyle('tag_fail', fontSize=9, fontName='Helvetica-Bold',
                                   textColor=RED),
        'tag_warn': ParagraphStyle('tag_warn', fontSize=9, fontName='Helvetica-Bold',
                                   textColor=AMBER),
    }

def generate_pdf_report(data):
    path = 'uploads/SkillyLens_Report.pdf'
    os.makedirs('uploads', exist_ok=True)
    
    doc = SimpleDocTemplate(path, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    s = make_styles()
    story = []

    # ── HEADER ──
    story.append(Paragraph("SkillyLens", s['title']))
    story.append(Paragraph(f"Career DNA Report · {datetime.datetime.now().strftime('%d %b %Y')}", s['subtitle']))
    story.append(HRFlowable(width="100%", thickness=1, color=INDIGO, spaceAfter=12))

    # ── INFO TABLE ──
    info_data = [
        ["Target Role", data.get('job_role', '-'), "Level", data.get('level', '-')],
        ["Career Readiness", f"{data.get('readiness_score', 0)}%",
         "ATS Score", f"{data.get('ats_score', 0)}/100"],
    ]
    info_table = Table(info_data, colWidths=[3.5*cm, 6.5*cm, 3.5*cm, 3.5*cm])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME', (2,0), (2,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('TEXTCOLOR', (0,0), (0,-1), GRAY),
        ('TEXTCOLOR', (2,0), (2,-1), GRAY),
        ('TEXTCOLOR', (1,0), (1,-1), HexColor('#1e293b')),
        ('TEXTCOLOR', (3,0), (3,-1), INDIGO),
        ('FONTNAME', (3,0), (3,-1), 'Helvetica-Bold'),
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('ROWBACKGROUNDS', (0,0), (-1,-1), [LIGHT_BG, white]),
        ('GRID', (0,0), (-1,-1), 0.5, HexColor('#e2e8f0')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.4*cm))

    # ── SKILLS SECTION ──
    story.append(Paragraph("Skills Analysis", s['h2']))
    
    existing = data.get('existing_skills', [])
    missing = data.get('missing_skills', [])
    
    if existing:
        story.append(Paragraph("✅  Your Existing Skills", s['h3']))
        skills_text = "  ·  ".join(s_item.title() for s_item in existing)
        story.append(Paragraph(skills_text, s['body']))
    
    if missing:
        story.append(Paragraph("🎯  Skills to Learn", s['h3']))
        miss_text = "  ·  ".join(s_item.title() for s_item in missing)
        story.append(Paragraph(miss_text, ParagraphStyle('miss', fontSize=10,
                               fontName='Helvetica', textColor=RED, spaceAfter=4)))

    good = data.get('good_to_have', [])
    if good:
        story.append(Paragraph("⭐  Good to Have", s['h3']))
        story.append(Paragraph("  ·  ".join(good), s['body']))

    # ── ATS SECTION ──
    story.append(Paragraph("ATS Analysis", s['h2']))
    ats_friendly = data.get('is_ats_friendly', False)
    ats_score = data.get('ats_score', 0)
    
    verdict_color = GREEN if ats_friendly else RED
    verdict_text = "✅  ATS FRIENDLY" if ats_friendly else "❌  NOT ATS FRIENDLY"
    story.append(Paragraph(f"{verdict_text}  —  Score: {ats_score}/100",
                           ParagraphStyle('verdict', fontSize=12, fontName='Helvetica-Bold',
                                         textColor=verdict_color, spaceAfter=8)))
    
    ats_fb = data.get('ats_feedback', [])
    if ats_fb:
        fb_data = [["Check", "Status", "Details"]]
        for fb in ats_fb:
            status = fb.get('status', '')
            color = GREEN if status == 'pass' else (RED if status == 'fail' else AMBER)
            icon = "✅" if status == 'pass' else ("❌" if status == 'fail' else "⚠️")
            fb_data.append([fb.get('check', ''), f"{icon} {status.upper()}", fb.get('msg', '')])
        
        fb_table = Table(fb_data, colWidths=[4*cm, 3*cm, 10*cm])
        fb_table.setStyle(TableStyle([
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('BACKGROUND', (0,0), (-1,0), INDIGO),
            ('TEXTCOLOR', (0,0), (-1,0), white),
            ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT_BG, white]),
            ('GRID', (0,0), (-1,-1), 0.5, HexColor('#e2e8f0')),
            ('PADDING', (0,0), (-1,-1), 7),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(fb_table)
    
    ats_tips = data.get('ats_tips', [])
    if ats_tips:
        story.append(Spacer(1, 0.3*cm))
        story.append(Paragraph("How to Make Your Resume ATS-Ready:", s['h3']))
        for tip in ats_tips:
            story.append(Paragraph(f"• {tip}", s['body']))

    # ── ROADMAP SECTION ──
    roadmap = data.get('roadmap', {})
    if roadmap:
        story.append(Paragraph("90-Day Learning Roadmap", s['h2']))
        phase_colors = {'phase1': INDIGO, 'phase2': PURPLE, 'phase3': GREEN}
        phase_labels = {'phase1': 'Phase 1 — Foundations (Days 1-30)',
                       'phase2': 'Phase 2 — Build Up (Days 31-60)',
                       'phase3': 'Phase 3 — Master (Days 61-90)'}
        
        for phase_key in ['phase1', 'phase2', 'phase3']:
            phase = roadmap.get(phase_key, {})
            if not phase:
                continue
            color = phase_colors[phase_key]
            story.append(Paragraph(phase_labels[phase_key],
                                   ParagraphStyle(f'ph_{phase_key}', fontSize=12,
                                                  fontName='Helvetica-Bold',
                                                  textColor=color, spaceBefore=12, spaceAfter=6)))
            
            tasks = phase.get('tasks', [])
            if tasks:
                task_data = [["Skill", "Task", "Hours", "Resource"]]
                for t in tasks:
                    task_data.append([
                        str(t.get('skill', '')),
                        str(t.get('task', ''))[:60],
                        str(t.get('hours', '?')) + 'h',
                        str(t.get('resource_name', ''))[:25]
                    ])
                task_table = Table(task_data, colWidths=[3.5*cm, 8*cm, 1.5*cm, 4*cm])
                task_table.setStyle(TableStyle([
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0,0), (-1,-1), 9),
                    ('BACKGROUND', (0,0), (-1,0), color),
                    ('TEXTCOLOR', (0,0), (-1,0), white),
                    ('ROWBACKGROUNDS', (0,1), (-1,-1), [LIGHT_BG, white]),
                    ('GRID', (0,0), (-1,-1), 0.5, HexColor('#e2e8f0')),
                    ('PADDING', (0,0), (-1,-1), 6),
                    ('VALIGN', (0,0), (-1,-1), 'TOP'),
                ]))
                story.append(task_table)

    # ── AI TOOLS ──
    ai_tools = data.get('ai_tools', {})
    if ai_tools:
        story.append(Paragraph("Recommended AI Tools", s['h2']))
        for category, tools in ai_tools.items():
            if not tools: continue
            label = "🔥 Famous Tools" if category == 'famous' else "💎 Underrated but Powerful"
            story.append(Paragraph(label, s['h3']))
            for tool in tools:
                story.append(Paragraph(
                    f"<b>{tool['name']}</b> — {tool['use']}",
                    s['body']))

    # ── FOOTER ──
    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width="100%", thickness=0.5, color=HexColor('#e2e8f0')))
    story.append(Paragraph("Generated by SkillyLens · Your AI Career Mentor · skillylens.app",
                           ParagraphStyle('footer', fontSize=8, textColor=GRAY,
                                         alignment=1, spaceBefore=6)))
    
    doc.build(story)
    return path