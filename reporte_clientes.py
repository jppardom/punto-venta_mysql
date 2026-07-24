from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from conexion import conexion
from datetime import datetime
from tkinter import *
import fitz  
from PIL import Image as PIL_Image, ImageTk

class reporte_clientes:
    def __init__(self, ventanaPrincipal):
        #Eliminar el reporte
        reporte_clientes.generar_reporte(self)
        self.ventanaReporte = Toplevel(ventanaPrincipal)
        self.ventanaReporte.title("Reporte de Clientes")
        self.ventanaReporte.geometry("1000x700")
            
        self.ventanaReporte.focus_set()
        self.ventanaReporte.grab_set()
        self.ventanaReporte.transient(master=ventanaPrincipal)
        reporte_clientes.mastrar_pdf(self)

    def generar_reporte(self, nombre_archivo="reporte/reporte_clientes.pdf"):
        doc = SimpleDocTemplate(
            nombre_archivo,
            pagesize=landscape(letter),
            rightMargin=36,
            leftMargin=36,
            topMargin=36,
            bottomMargin=36
        )
        elementos = []
        estilos = getSampleStyleSheet()
    
        # Estilos
        estilo_titulo = ParagraphStyle(
            'TituloReporte',
            parent=estilos['Heading1'],
            fontSize=18,
            leading=22,
            textColor=colors.HexColor('#1A365D'),
            spaceAfter=4
        )
        estilo_celda = ParagraphStyle(
            'CeldaTabla',
            parent=estilos['Normal'],
            fontSize=9,
            leading=11,
            textColor=colors.HexColor('#2D3748')
        )
    
        estilo_cabecera = ParagraphStyle(
            'CabeceraTabla',
            parent=estilos['Normal'],
            fontSize=9,
            leading=11,
            textColor=colors.white,
            fontName='Helvetica-Bold'
        )
        MESES = {
            1: "enero", 2: "febrero", 3: "marzo", 4: "abril",
            5: "mayo", 6: "junio", 7: "julio", 8: "agosto",
            9: "septiembre", 10: "octubre", 11: "noviembre", 12: "diciembre"
        }
        ahora = datetime.now()
        fecha_formateada = f"{ahora.day} de {MESES[ahora.month]} de {ahora.year}"

        textos_encabezado = [
            Paragraph("Reporte de Lista de Clientes", estilo_titulo),
            Paragraph(f"Fecha de generación: {fecha_formateada}", estilos['Italic'])
        ]

        
        try:
            logo = Image("logo.png", width=50, height=40)
            logo.hAlign = 'RIGHT'
        except Exception:
            logo = Paragraph("", estilos['Normal'])

        tabla_encabezado = Table([[textos_encabezado, logo]], colWidths=[520, 200])
        tabla_encabezado.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 0),
        ]))
    
        elementos.append(tabla_encabezado)
        elementos.append(Spacer(1, 15))

        data = [('ID', 'CÉDULA', 'NOMBRES', 'APELLIDOS', 'GÉNERO', 'TELÉFONO', 'CORREO','DIRRECCIÓN')]
        query = 'SELECT * FROM clientes ORDER BY id_cliente DESC'
        db_rows = conexion.ejecutarSQL(query)
    
        for row in db_rows:
            data.append((row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        datos_tabla = []
        for i, fila in enumerate(data):
            fila_formateada = []
            for celda in fila:
                texto_celda = str(celda) if celda is not None else ""
                if i == 0:
                    fila_formateada.append(Paragraph(texto_celda, estilo_cabecera))
                else:
                    fila_formateada.append(Paragraph(texto_celda, estilo_celda))
            datos_tabla.append(fila_formateada)
        anchos_columnas = [30, 70, 100, 100, 60, 90, 130, 150]
        tabla = Table(datos_tabla, colWidths=anchos_columnas, repeatRows=1)

        estilo_tabla = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2B6CB0')),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 0), (-1, 0), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            ('TOPPADDING', (0, 1), (-1, -1), 6),
            ('LINEBELOW', (0, 1), (-1, -1), 0.5, colors.HexColor('#E2E8F0')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F7FAFC')])
        ])
    
        tabla.setStyle(estilo_tabla)
        elementos.append(tabla)

        # Crear PDF
        doc.build(elementos)

    def mastrar_pdf(self):
        try:
            # Cargar el PDF con PyMuPDF
            doc = fitz.open("reporte/reporte_clientes.pdf")
            pagina = doc.load_page(0)  # Cargar primera página
            
            # Convertir página a imagen de alta definición
            pix = pagina.get_pixmap(matrix=fitz.Matrix(1.3, 1.3))
            img = PIL_Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Guardar referencia en la instancia para que no la borre el Garbage Collector
            self.photo = ImageTk.PhotoImage(img)

            # Canvas con barras de desplazamiento para ver el documento
            canvas = Canvas(self.ventanaReporte, bg="#525659")
            scroll_y = Scrollbar(self.ventanaReporte, orient=VERTICAL, command=canvas.yview)
            scroll_x = Scrollbar(self.ventanaReporte, orient=HORIZONTAL, command=canvas.xview)

            frame_contenedor = Frame(canvas, bg="#525659")
            frame_contenedor.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )

            canvas.create_window((0, 0), window=frame_contenedor, anchor="nw")
            canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

            # Insertar la imagen del PDF
            lbl_pdf = Label(frame_contenedor, image=self.photo, bg="#525659")
            lbl_pdf.pack(padx=20, pady=20)

            # Empaquetado
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.pack(side=BOTTOM, fill=X)
            canvas.pack(side=LEFT, fill=BOTH, expand=True)

        except Exception as e:
            print(f"Error al visualizar PDF: {e}")