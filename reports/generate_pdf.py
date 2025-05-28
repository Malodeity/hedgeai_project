"""
📦 FILE: generate_pdf.py

🎯 Units:
- Unit 11: Reporting
- Unit 12: Builder Pattern

✅ Expectations:
- Render a Jinja2 HTML template and output a PDF file
"""

from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_pdf(data: dict):
    """
    Generate a PDF report using given data.

    TODO:
    - Replace hardcoded file name with dynamic naming
    - Ensure HTML template is updated for new fields
    """
    env = Environment(loader=FileSystemLoader("reports/templates"))
    template = env.get_template("report.html")
    html = template.render(data)
    pdfkit.from_string(html, "output/report.pdf")