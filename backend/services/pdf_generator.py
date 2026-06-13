from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import cm
import os, datetime

def generate_pdf_report(data):
    path = 'uploads/report.pdf'
    os.makedirs('uploads', exist_ok=True)
    doc = SimpleDocTemplate(path, pagesize=A4,
                            rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    
    styles = getSampleStyleSheet()
    accent = HexColor('#6366f1')
    dark = HexColor('#09090f')
    
    title_style = ParagraphStyle('title', fontSize=24, fontName='Helvetica-Bold',
                                 textColor=accent, spaceAfter=6)
    h2_style = ParagraphStyle('h2', fontSize=14, fontName='Helvetica-Bold',
                               textColor=accent, spaceBefore=16, spaceAfter=6)
    body_style = ParagraphStyle('body', fontSize=10, spaceAfter=4,
                                textColor=HexColor('#1a1a2e'))
    
    story = []
    story.append(Paragraph("SkillyLens Career Report", title_style))
    story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%d %b %Y')}", body_style))
    story.append(Spacer(1, 0.5*cm))
    
    story.append(Paragraph(f"Target Role: {data.get('job_role', '-')}", body_style))
    story.append(Paragraph(f"Level: {data.get('level', '-')}", body_style))
    story.append(Paragraph(f"Career Readiness Score: {data.get('readiness_score', 0)}%", h2_style))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph("✅ Your Existing Skills", h2_style))
    existing = ", ".join(s.title() for s in data.get('existing_skills', []))
    story.append(Paragraph(existing or "None detected", body_style))
    
    story.append(Paragraph("🎯 Skills to Learn", h2_style))
    missing = ", ".join(s.title() for s in data.get('missing_skills', []))
    story.append(Paragraph(missing or "All required skills present!", body_style))
    
    story.append(Paragraph("🤖 Recommended AI Tools", h2_style))
    ai_tools = data.get('ai_tools', {})
    for category, tools in ai_tools.items():
        story.append(Paragraph(category.title(), ParagraphStyle('bold', fontSize=11, fontName='Helvetica-Bold')))
        for tool in tools:
            story.append(Paragraph(f"• {tool['name']}: {tool['use']}", body_style))
    
    doc.build(story)
    return path