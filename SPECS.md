# Portfolio Redesign Specifications

## Goal
Create a refreshed one-page portfolio experience inspired by the OpenAI Engineering blog design while preserving GitHub Pages compatibility through the existing MkDocs static site setup.

## Primary Objectives
- Present Dimas Jackson as a Deep Learning Architect at AWS focused on Financial Service Institutions.
- Use a minimalist, modern engineering-blog aesthetic like https://openai.com/news/engineering/.
- Keep the site buildable with MkDocs and deployable to GitHub Pages.
- Leverage existing content from `profile.md` and the current `docs/index.md`.

## Audience
- Hiring managers and technical leaders in AI, cloud, and financial services.
- Enterprise customers and partners evaluating AI architect experience.
- Recruiters looking for senior architecture, AWS, and deep learning expertise.

## Design Principles
- Clean structural hierarchy with wide readable content blocks.
- Strong emphasis on professional summary, impact stories, and technical leadership.
- Neutral palette with refined typography, subtle cards, and consistent spacing.
- Simple top navigation and a prominent hero section.
- Mobile-first responsiveness.

## Required Pages and Sections

### 1. Home / Portfolio Page
This will be the core page and should include:
- Hero header with title, subtitle, location, and current role.
- Quick contact / social links.
- Summary section with current role and value proposition.
- Impact highlights / metrics.
- Career timeline or experience summary.
- Core technical skills and certifications.
- Publications and research.
- Call-to-action / contact section.

### 2. Supporting Content Pages
Maintain existing pages for:
- Projects (`projetos.md`)
- Publications (`publicacoes.md`)
- Certifications (`certificacoes.md`)
- Book Reviews (`resenhas_livros.md`)
- Contact (`contato.md`)

## Content Source Mapping
Use data from `profile.md` for the following:
- Name: Dimas Jackson, PhD
- Current role: Deep Learning Architect @ Amazon | AWS Gen AI Innovation Center
- Location: São Paulo, São Paulo, Brasil
- Summary and disclaimer
- Key accomplishments (AWS GenAI, Financial Services, $2M ARR conversational AI, code remediation agent, speech recognition architecture, pilots with Amazon Q, A2A, MCP, Bedrock, Copilot, Databricks)
- Technical competencies and certifications
- Publications list
- Experience timeline
- Education
- Contact details

## Visual and Interaction Requirements
- Modern hero block with concise title, subtitle, and highlight badges.
- Section headings using strong typographic contrast.
- Use cards or panels for "Skills," "Experience," and "Highlights." 
- Keep navigation minimal and fixed for ease of access.
- Simple footer with deploy/branding note if desired.

## Technical Constraints
- Continue using MkDocs Material theme.
- Add or update `docs/index.md` to implement the new homepage layout.
- Keep `mkdocs.yml` compatible with GitHub Pages deployment.
- Use existing `extra_css` and `extra_javascript` if needed.
- Avoid server-side components; site must remain static.

## Implementation Notes
- Keep the existing repo structure and build flow: `mkdocs build` → `site/` output.
- If additional styling is required, create or update `docs/styles/custom.css`.
- Consider one clean homepage design instead of a multi-panel landing page.

## Next Step
- Refactor `docs/index.md` to match the new OpenAI-like portfolio layout.
- Use `profile.md` content to update the hero, summary, experience, skills, and contact sections.
- Optionally add a small visual accent or custom CSS to emulate the OpenAI engineering blog tone.
