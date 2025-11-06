#!/usr/bin/env python3
"""
Resume PDF Generator

This script generates a tailored PDF resume based on a JSON input file.
It uses ReportLab for PDF generation and can customize the resume
based on job requirements.

Usage:
    python generate_resume.py <input_json> <output_pdf>

Example:
    python generate_resume.py resume_data.json tailored_resume.pdf
"""

import json
import sys
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT


class ResumeGenerator:
    """Generate a tailored PDF resume from structured data."""

    def __init__(self, output_filename):
        self.output_filename = output_filename
        self.doc = SimpleDocTemplate(
            output_filename,
            pagesize=letter,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
            leftMargin=0.75*inch,
            rightMargin=0.75*inch
        )
        self.story = []
        self.styles = self._create_styles()

    def _create_styles(self):
        """Create custom paragraph styles for the resume."""
        styles = getSampleStyleSheet()

        # Header name style
        styles.add(ParagraphStyle(
            name='HeaderName',
            parent=styles['Heading1'],
            fontSize=24,
            textColor=HexColor('#8B0000'),  # Dark red
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))

        # Contact info style
        styles.add(ParagraphStyle(
            name='ContactInfo',
            parent=styles['Normal'],
            fontSize=9,
            textColor=HexColor('#000000'),
            spaceAfter=12,
            alignment=TA_CENTER
        ))

        # Section header style
        styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=styles['Heading2'],
            fontSize=14,
            textColor=HexColor('#8B0000'),
            spaceBefore=12,
            spaceAfter=6,
            fontName='Helvetica-Bold',
            borderWidth=2,
            borderColor=HexColor('#8B0000'),
            borderPadding=5
        ))

        # Professional summary style
        styles.add(ParagraphStyle(
            name='Summary',
            parent=styles['Normal'],
            fontSize=10,
            leading=14,
            spaceAfter=12,
            alignment=TA_LEFT
        ))

        # Job title style
        styles.add(ParagraphStyle(
            name='JobTitle',
            parent=styles['Normal'],
            fontSize=11,
            fontName='Helvetica-Bold',
            spaceAfter=2
        ))

        # Company/dates style
        styles.add(ParagraphStyle(
            name='CompanyDates',
            parent=styles['Normal'],
            fontSize=10,
            fontName='Helvetica-Oblique',
            spaceAfter=6
        ))

        # Bullet point style
        styles.add(ParagraphStyle(
            name='ResumeBullet',
            parent=styles['Normal'],
            fontSize=10,
            leading=13,
            leftIndent=20,
            bulletIndent=10,
            spaceAfter=4
        ))

        return styles

    def add_header(self, data):
        """Add the header section with name and contact info."""
        contact = data.get('contact', {})

        # Name
        name = Paragraph(
            contact.get('name', 'Name Missing'),
            self.styles['HeaderName']
        )
        self.story.append(name)

        # Contact info line
        contact_parts = []
        if contact.get('location'):
            contact_parts.append(contact['location'])
        if contact.get('phone'):
            contact_parts.append(contact['phone'])
        if contact.get('email'):
            contact_parts.append(contact['email'])
        if contact.get('linkedin'):
            contact_parts.append(contact['linkedin'])
        if contact.get('portfolio'):
            contact_parts.append(contact['portfolio'])

        contact_line = Paragraph(
            ' | '.join(contact_parts),
            self.styles['ContactInfo']
        )
        self.story.append(contact_line)

    def add_summary(self, data):
        """Add professional summary section."""
        summary = data.get('summary', '')
        if summary:
            summary_para = Paragraph(summary, self.styles['Summary'])
            self.story.append(summary_para)
            self.story.append(Spacer(1, 0.1*inch))

    def add_section_header(self, title):
        """Add a section header."""
        header = Paragraph(title, self.styles['SectionHeader'])
        self.story.append(header)

    def add_experience(self, experiences):
        """Add professional experience section."""
        self.add_section_header('Professional Experience')

        for exp in experiences:
            # Job title
            title = Paragraph(
                exp.get('title', 'Position Title'),
                self.styles['JobTitle']
            )
            self.story.append(title)

            # Company and dates
            company = exp.get('company', '')
            location = exp.get('location', '')
            dates = exp.get('dates', '')

            company_line = f"{company}, {location}" if location else company
            if dates:
                company_line = f"<b>{company_line}</b>"
                dates_line = f"<i>{dates}</i>"

                # Create a table for company and dates alignment
                data_table = [[
                    Paragraph(company_line, self.styles['Normal']),
                    Paragraph(dates_line, self.styles['Normal'])
                ]]

                table = Table(data_table, colWidths=[4.5*inch, 2*inch])
                table.setStyle(TableStyle([
                    ('ALIGN', (0, 0), (0, 0), 'LEFT'),
                    ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
                    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Oblique'),
                    ('FONTSIZE', (0, 0), (-1, -1), 10),
                ]))
                self.story.append(table)

            # Achievements
            achievements = exp.get('achievements', [])
            for achievement in achievements:
                bullet = Paragraph(
                    f"• {achievement}",
                    self.styles['ResumeBullet']
                )
                self.story.append(bullet)

            self.story.append(Spacer(1, 0.15*inch))

    def add_skills(self, skills):
        """Add skills section."""
        if not skills:
            return

        self.add_section_header('Key Skills')

        # Create bullet points for skills
        if isinstance(skills, list):
            for skill in skills:
                bullet = Paragraph(f"• {skill}", self.styles['ResumeBullet'])
                self.story.append(bullet)
        elif isinstance(skills, dict):
            for category, skill_list in skills.items():
                if isinstance(skill_list, list):
                    skills_text = ', '.join(skill_list)
                    bullet = Paragraph(
                        f"• <b>{category}:</b> {skills_text}",
                        self.styles['ResumeBullet']
                    )
                    self.story.append(bullet)

        self.story.append(Spacer(1, 0.1*inch))

    def add_education(self, education):
        """Add education section."""
        if not education:
            return

        self.add_section_header('Education')

        for edu in education:
            degree = edu.get('degree', '')
            institution = edu.get('institution', '')
            location = edu.get('location', '')
            date = edu.get('date', '')

            edu_line = f"<b>{degree}</b>"
            if date:
                edu_line += f" - {date}"

            edu_para = Paragraph(edu_line, self.styles['Normal'])
            self.story.append(edu_para)

            inst_line = f"{institution}"
            if location:
                inst_line += f", {location}"

            inst_para = Paragraph(inst_line, self.styles['Normal'])
            self.story.append(inst_para)
            self.story.append(Spacer(1, 0.1*inch))

    def add_certifications(self, certifications):
        """Add certifications section."""
        if not certifications:
            return

        self.add_section_header('Certifications')

        for cert in certifications:
            name = cert.get('name', '')
            date = cert.get('date', '')

            cert_line = f"<b>{name}</b>"
            if date:
                cert_line += f" - {date}"

            cert_para = Paragraph(cert_line, self.styles['Normal'])
            self.story.append(cert_para)
            self.story.append(Spacer(1, 0.05*inch))

    def generate(self, data):
        """Generate the complete resume PDF."""
        # Add all sections
        self.add_header(data)
        self.add_summary(data)

        if 'experience' in data:
            self.add_experience(data['experience'])

        if 'skills' in data:
            self.add_skills(data['skills'])

        if 'education' in data:
            self.add_education(data['education'])

        if 'certifications' in data:
            self.add_certifications(data['certifications'])

        # Build the PDF
        self.doc.build(self.story)
        print(f"✅ Resume generated successfully: {self.output_filename}")


def main():
    """Main function to run the resume generator."""
    if len(sys.argv) != 3:
        print("Usage: python generate_resume.py <input_json> <output_pdf>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        # Load resume data
        with open(input_file, 'r') as f:
            resume_data = json.load(f)

        # Generate PDF
        generator = ResumeGenerator(output_file)
        generator.generate(resume_data)

    except FileNotFoundError:
        print(f"❌ Error: Input file '{input_file}' not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in input file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error generating resume: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
