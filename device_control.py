import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Add title
    elements.append(Paragraph("Device Control", style='Title'))
    elements.append(Spacer(1, 0.25*inch))

    # Add device information
    device_info = [['Property', 'Value'],
                   ['Device Name', 'WhiteRabbitNeo'],
                   ['Device Model', 'AI-01'],
                   ['Device Serial', '123456789'],
                   ['Device Location', 'Living Room']]
    table = Table(device_info, colWidths=[1.5*inch, 2.5*inch])
    table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), colors.lightgrey),
                                ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                                ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    elements.append(table)
    elements.append(Spacer(1, 0.5*inch))

    # Add control buttons
    elements.append(Paragraph("Control Buttons", style='Heading'))
    elements.append(Spacer(1, 0.25*inch))
    elements.append(Paragraph("<b>Power On</b> - Turns the device on", style='Normal'))
    elements.append(Paragraph("<b>Power Off</b> - Turns the device off", style='Normal'))
    elements.append(Paragraph("<b>Restart</b> - Restarts the device", style='Normal'))
    elements.append(Paragraph("<b>Shutdown</b> - Shuts down the device", style='Normal'))
    elements.append(Spacer(1, 0.5*inch))

    # Generate PDF file
    doc.build(elements)

# Create PDF file
filename = 'device_control.pdf'
create_pdf(filename)

# Open PDF file
os.system(f'open {filename}')