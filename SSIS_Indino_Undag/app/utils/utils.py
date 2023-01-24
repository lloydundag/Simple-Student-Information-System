from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, inch
from app import UPLOAD_FOLDER
import os


def create_pdf(image, idno, name, college, course, yearlevel, gender):
    buffer = BytesIO()
    canvas = Canvas(buffer, pagesize=A4)
    WIDTH, HEIGHT = A4
    MARIGIN = 1.5 * cm
    canvas.translate(MARIGIN, HEIGHT-MARIGIN)
    

    # header
    canvas.drawString(0, 0, "Student Details")
    canvas.setStrokeGray(0)
    canvas.line(0, -1*cm, WIDTH - 2*MARIGIN, -1*cm)

    # footer
    canvas.drawString(0, -26.2*cm, "\u00A9 2023 SSIS")
    canvas.line(0, -26.6*cm, WIDTH - 2*MARIGIN, -26.6*cm)

    # barcode
    
    canvas.drawInlineImage(os.path.join(UPLOAD_FOLDER, image), 0 , -2.35*inch, 1.5*inch, 1.5*inch, preserveAspectRatio=True)

    # paragraphs
    txt_obj = canvas.beginText(13, -6.8* cm)
    txt_obj.setFont("Helvetica", size=14)
    txt_obj.setWordSpace(3)
    txt_lst = ["", 
                "ID No.:" + idno,
                "Name: " + name,
                "College: " + college,
                "Course: " + course,
                "Year Level: " + yearlevel,
                "Gender: " + gender]

    for line in txt_lst:
        txt_obj.textOut(line)
        txt_obj.moveCursor(0, 16)
    canvas.drawText(txt_obj)

    canvas.showPage()
    canvas.save()

    return buffer
