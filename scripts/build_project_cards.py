"""Render consistent, self-hosted SVG cards for selected public work."""

from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1] / "assets" / "cards"
ROOT.mkdir(parents=True, exist_ok=True)

CARDS = [
    ("reliefrail", "01 / RELIEFRAIL", "Coordination with an auditable money trail", "PayPal Sandbox · FastAPI · React", "#72e1c5", "PAYMENTS / HUMAN REVIEW"),
    ("blackbox", "02 / BLACKBOX", "Road incident evidence, organized for review", "FastAPI · Next.js · Celery", "#bca5ff", "EVIDENCE / UNCERTAINTY"),
    ("wallsense", "03 / WALLSENSE", "Reproducible experiments on recorded CSI", "Python · Dataset validation · Evaluation", "#6cb8ff", "RESEARCH / DATA INTEGRITY"),
    ("dilcare", "04 / DILCARE MOBILE", "A health app exploring connected workflows", "React Native · TypeScript · APIs", "#ff9fb2", "MOBILE / PRODUCT"),
]

for filename, title, subtitle, tech, accent, tag in CARDS:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="560" height="220" viewBox="0 0 560 220" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc>
  <defs><linearGradient id="bg" x2="1" y2="1"><stop stop-color="#101a29"/><stop offset="1" stop-color="#182d3e"/></linearGradient></defs>
  <rect width="560" height="220" rx="17" fill="url(#bg)"/>
  <rect x="1" y="1" width="558" height="218" rx="16" fill="none" stroke="#355169"/>
  <rect x="30" y="30" width="6" height="158" rx="3" fill="{accent}"/>
  <text x="59" y="64" fill="{accent}" font-family="Arial,Helvetica,sans-serif" font-size="13" font-weight="700" letter-spacing="2">{escape(title)}</text>
  <text x="59" y="104" fill="#f1f7fb" font-family="Arial,Helvetica,sans-serif" font-size="19" font-weight="600">{escape(subtitle)}</text>
  <text x="59" y="140" fill="#a9bdcb" font-family="Arial,Helvetica,sans-serif" font-size="15">{escape(tech)}</text>
  <line x1="59" y1="162" x2="515" y2="162" stroke="#355169"/>
  <text x="59" y="191" fill="{accent}" font-family="Arial,Helvetica,sans-serif" font-size="12" letter-spacing="1.5">{escape(tag)}</text>
  <path d="M504 178h20m-8-8 8 8-8 8" stroke="{accent}" fill="none" stroke-width="2"/>
</svg>'''
    (ROOT / f"{filename}.svg").write_text(svg + "\n", encoding="utf-8")
