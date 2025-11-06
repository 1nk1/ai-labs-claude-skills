---
name: resume-manager
description: This skill should be used when managing professional resumes, tracking work projects and achievements, or tailoring resumes for specific job applications. It provides structured resume data management, project tracking capabilities, and automated PDF resume generation tailored to job requirements.
---

# Resume Manager

## Overview

This skill enables comprehensive resume and career portfolio management. It maintains structured resume data, tracks projects and achievements, and generates tailored PDF resumes optimized for specific job roles. The skill combines data management with automated document generation to streamline the job application process.

## Core Capabilities

### 1. Resume Data Management

Maintain a structured database of resume information in `references/resume_data.md`. This includes:

- **Contact information** - Name, location, phone, email, LinkedIn, portfolio
- **Professional summary** - High-level career overview with keywords
- **Experience history** - Detailed work history with achievements and impact metrics
- **Skills taxonomy** - Categorized skills with tags for easy filtering
- **Education and certifications** - Academic credentials and professional certifications
- **Project database** - Detailed project descriptions with challenges, solutions, and results

**When to update resume data:**
- Adding new work experience or achievements
- Completing significant projects
- Earning new certifications
- Updating contact information or professional summary
- Adding new skills or technologies

### 2. Project Tracking

Track detailed project information in `assets/project_template.json`. Each project includes:

- Project name and context (company, role, duration)
- Challenge statement (what problem was being solved)
- Solution approach (how it was addressed)
- Measurable results (quantified impact)
- Technologies and tools used
- Relevant tags for filtering (e.g., "e-commerce", "mobile", "analytics")
- Relevance scores for different job categories

**Project tracking workflow:**
1. Create a new project entry when starting significant work
2. Document the challenge and approach during the project
3. Record measurable results after completion
4. Tag the project with relevant keywords
5. Assign relevance scores for different job types

### 3. Resume Tailoring for Job Applications

When tailoring a resume for a specific job:

**Step 1: Analyze the job description**
- Identify key requirements, skills, and keywords
- Note specific technologies, methodologies, or domains mentioned
- Determine the role type (e.g., senior, lead, specialist)

**Step 2: Select relevant experience**
- Review `references/resume_data.md` for matching experience
- Prioritize achievements that align with job requirements
- Select 2-3 most relevant achievements per role (max 3 bullets per role)
- Ensure selected items include quantifiable results when possible

**Step 3: Customize the professional summary**
- Emphasize skills and experience relevant to the job
- Include keywords from the job description naturally
- Keep it concise (2-3 sentences)

**Step 4: Tailor skills section**
- Prioritize skills mentioned in the job description
- Group related skills together
- Remove or de-emphasize less relevant skills

**Step 5: Adjust education and certifications**
- Highlight relevant certifications
- Include GPA only if specifically requested or if recent graduate

### 4. PDF Resume Generation

Generate professional PDF resumes using the `scripts/generate_resume.py` script.

**Prerequisites:**
```bash
pip install -r scripts/requirements.txt
```

**Usage workflow:**

1. **Create a tailored JSON file** with selected resume content:
   - Use `assets/resume_template.json` as a starting point
   - Customize sections based on job requirements
   - Include only relevant achievements and skills
   - Save as a new file (e.g., `resume_tailored_ux_lead.json`)

2. **Generate the PDF:**
   ```bash
   python scripts/generate_resume.py resume_tailored_ux_lead.json output_resume.pdf
   ```

3. **Review the output:**
   - Check formatting and layout
   - Verify all information is accurate
   - Ensure the resume fits on 1-2 pages
   - Confirm visual hierarchy is clear

**Script capabilities:**
- Professional formatting with custom styles
- Consistent branding (colors, fonts, layout)
- Section headers with visual separation
- Bullet points for achievements
- Two-column layout for experience dates
- Contact information header
- Automatic page breaking

## Tailoring Strategy by Role Type

### For Senior/Lead Positions
- Emphasize leadership, mentorship, and strategic impact
- Highlight projects with business-level results (revenue, efficiency)
- Include design system or process improvement achievements
- Show cross-functional collaboration and stakeholder management

### For Specialist Positions (e.g., Accessibility, Mobile)
- Prioritize deep expertise in the specialty area
- Include relevant certifications prominently
- Highlight specific technical skills and tools
- Show impact in the specialized domain

### For Individual Contributor Positions
- Focus on hands-on execution and deliverables
- Emphasize collaboration with cross-functional teams
- Highlight user research and data-driven decision making
- Include diverse project types and methodologies

### For E-commerce Focused Roles
- Prioritize conversion optimization and business impact
- Include checkout, cart, or payment flow experience
- Show analytics and A/B testing capabilities
- Quantify revenue or conversion improvements

### For Startup/Fast-Paced Roles
- Emphasize versatility and wearing multiple hats
- Show rapid iteration and MVP development
- Highlight autonomy and initiative
- Include examples of 0-to-1 product work

## Best Practices

### Resume Content
- **Quantify achievements** - Use specific numbers, percentages, or dollar amounts
- **Use action verbs** - Start bullets with strong verbs (Redesigned, Conducted, Created, Developed)
- **Show impact** - Connect work to business or user outcomes
- **Be concise** - Keep bullets to 1-2 lines maximum
- **Avoid jargon** - Use clear language that non-designers can understand
- **Stay current** - Update regularly, not just when job hunting

### Resume Formatting
- **Length** - Aim for 1 page for <5 years experience, 2 pages for more
- **Consistency** - Use consistent formatting for dates, locations, and sections
- **White space** - Ensure adequate spacing for readability
- **Hierarchy** - Make section headers and job titles visually distinct
- **Professional design** - Use subtle color and professional fonts

### Keyword Optimization
- **Match job description** - Use similar terminology to the job posting
- **Include tools** - List specific software and platforms used
- **Certifications** - Highlight relevant credentials
- **Soft skills** - Include collaboration, communication, leadership where demonstrated
- **Domain knowledge** - Mention specific industries or product types

## Common Use Cases

### "Tailor my resume for this UX Lead position at an e-commerce company"

**Workflow:**
1. Read and analyze the job description
2. Load `references/resume_data.md`
3. Select achievements emphasizing:
   - E-commerce experience (checkout redesign project)
   - Leadership (design system creation, team collaboration)
   - Business impact (conversion rates, revenue)
4. Create tailored JSON with professional summary emphasizing leadership and e-commerce
5. Generate PDF with `generate_resume.py`

### "Add this new project to my resume database"

**Workflow:**
1. Read `assets/project_template.json`
2. Create new project entry with:
   - Project name and context
   - Challenge, solution, results
   - Technologies and tags
   - Relevance scores
3. Update `references/resume_data.md` with a condensed achievement bullet
4. Save both files

### "Update my professional summary to emphasize accessibility"

**Workflow:**
1. Read `references/resume_data.md`
2. Revise professional summary to lead with accessibility expertise
3. Mention CPACC certification prominently
4. Include accessibility-related achievements
5. Update the summary in both `resume_data.md` and `resume_template.json`

### "Create a resume focused on my mobile design experience"

**Workflow:**
1. Load `references/resume_data.md`
2. Filter achievements by "mobile" tag
3. Prioritize:
   - Fitness app project (3M downloads)
   - Mobile-first design skills
   - Responsive design experience
4. Adjust professional summary to emphasize mobile expertise
5. Generate tailored JSON and PDF

## Resources

### scripts/
**generate_resume.py** - Python script that generates professional PDF resumes from JSON data
- Requires: `reportlab` library (see `requirements.txt`)
- Input: JSON file with resume data
- Output: Formatted PDF resume
- Customizable styling (colors, fonts, layout)

**requirements.txt** - Python dependencies for the resume generation script

### references/
**resume_data.md** - Comprehensive structured resume database
- Contact information
- Professional summary with keywords
- Detailed work history with tagged achievements
- Skills taxonomy organized by category
- Education and certifications
- Project database with templates for expansion

Use this file as the source of truth for all resume content. Load it when tailoring resumes or updating career information.

### assets/
**resume_template.json** - JSON template for PDF generation
- Contains the full resume in JSON format
- Used as input for `generate_resume.py`
- Copy and customize for each job application
- Maintains consistent structure for the PDF generator

**project_template.json** - Structured project tracking template
- Detailed project database with challenges, solutions, and results
- Relevance scoring for different job types
- Work summaries by role
- Use for tracking ongoing projects and portfolio management

## Examples

### Example 1: Tailoring for a Senior UX Designer role at a SaaS company

Job requirements emphasize: design systems, user research, cross-functional collaboration, B2B experience

**Selected achievements:**
- "Created a responsive design system in Figma used across three product teams, cutting design time by 40%"
- "Conducted 30+ user interviews and usability tests that led to critical design changes, improving user satisfaction scores by 25%"
- "Collaborated with developers to refine UI components, decreasing user-reported bugs by 60% after launch"

**Professional summary adjusted:**
"Senior UX Designer with 5+ years of experience building scalable design systems and conducting user research for B2B and e-commerce products. Expert in cross-functional collaboration, translating user insights into intuitive interfaces that drive measurable business results."

### Example 2: Adding a new project

New project completed: "Dashboard Redesign for Analytics Platform"

**Information to capture:**
```json
{
  "name": "Analytics Dashboard Redesign",
  "company": "Hive Digital Products",
  "role": "UX Designer",
  "duration": "Q3 2024",
  "challenge": "Complex analytics dashboard overwhelmed users with data, leading to low adoption",
  "solution": "Redesigned information architecture, created customizable views, added progressive disclosure",
  "results": [
    "Increased dashboard adoption by 45%",
    "Reduced support tickets by 30%",
    "Improved user satisfaction from 3.2 to 4.5/5"
  ],
  "technologies": ["Figma", "Amplitude", "Maze"],
  "tags": ["analytics", "dashboard", "data visualization", "B2B", "SaaS"]
}
```

Add condensed bullet to resume_data.md:
"Redesigned analytics dashboard with customizable views and progressive disclosure, increasing adoption by 45% and user satisfaction from 3.2 to 4.5/5"

## Maintenance

**Regular updates (monthly):**
- Review and add recent achievements
- Update skills with newly learned tools or technologies
- Add completed projects to project database
- Refresh professional summary if role or focus changes

**Before job search:**
- Verify all dates and information are accurate
- Ensure contact information is current
- Review for any outdated technologies or achievements
- Create fresh baseline template with all current information

**After each application:**
- Save tailored JSON file with descriptive name (e.g., `resume_2024_ux_lead_shopify.json`)
- Note which achievements resonated in interviews
- Track which customizations led to responses
- Refine tailoring strategy based on results
