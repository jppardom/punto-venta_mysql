from reportlab.pdfgen import canvas
c = canvas.Canvas("hola-mundo.pdf")
c.drawString(50, 50, "¡Hola, mundo!")
c.save()
