import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
class Gerente:
    def __init__(self):
        # Inicializar cualquier estado necesario
        pass

    def generar_informe(self, tipo, fecha):
        informe = self._generar_informe_base(tipo, fecha)
        self._guardar_informe_pdf(informe)
        return True

    def _generar_informe_base(self, tipo, fecha):
        # Lógica para generar el informe base
        informe = f"Informe de ventas para el tipo {tipo} y la fecha {fecha}"
        return informe

    def _guardar_informe_pdf(self, informe):
        # Lógica para guardar el informe en un archivo PDF
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = f"Informe_Ventas_{fecha_actual}.pdf"

        # Crear el lienzo para el PDF
        c = canvas.Canvas(nombre_archivo, pagesize=letter)

        # Escribir el informe en el lienzo
        c.drawString(100, 750, informe)

        # Guardar el PDF
        c.save()


# Ejemplo de uso
gerente = Gerente()
gerente.generar_informe("diario", "2024-05-21")
