from fpdf import FPDF
import ast
import os
from typing import List, Dict, Any
import webbrowser
from datetime import datetime


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(190, 10, '"Mercado de Karen"', ln=True, align='C')
        self.set_font('Arial', 'I', 10)
        self.cell(190, 10, 'Abasto de comestibles y productos varios',
                  ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-30)
        self.set_font('Arial', 'I', 9)
        self.multi_cell(0, 10, 'Esta factura fue emitida digitalmente por SysMarket.\n'
                        'Contacto: +58 424-4961877', align='C')


def generar_factura_pdf(DatosRecibo: List[Any], lista_detalles_dics: Dict[str, Any]) -> None:

    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%d/%m/%Y")

    # Información del cliente y factura
    pdf.cell(100, 10, f'Cliente: {DatosRecibo[4]} {DatosRecibo[5]}', 0)
    pdf.cell(0, 10, f'Fecha: {fecha_actual}', 0, ln=True)
    pdf.cell(100, 10, f'CI o RIF: {DatosRecibo[6]}', 0)
    pdf.cell(0, 10, f'Tipo Fact.: factura digital', 0, ln=True)
    pdf.ln(10)

    # Tabla de productos
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(80, 10, 'Producto', 1)
    pdf.cell(30, 10, 'Cantidad', 1, align='C')
    pdf.cell(40, 10, 'Valor Unit.', 1, align='R')
    pdf.cell(40, 10, 'Valor Total', 1, ln=True, align='R')

    pdf.set_font('Arial', '', 12)
    for key, producto in lista_detalles_dics.items():
        producto_nombre = producto['Nombre']
        cantidad = producto['Cantidad']
        valor_unit = producto['Precio Unit. $']
        valor_total = producto['Precio']
        pdf.cell(80, 10, producto_nombre, 1)
        pdf.cell(30, 10, str(cantidad), 1, align='C')
        pdf.cell(40, 10, f'${valor_unit:.2f}', 1, align='R')
        pdf.cell(40, 10, f'${valor_total:.2f}', 1, ln=True, align='R')

    # Totales
    pdf.ln(5)
    pdf.cell(150, 10, 'Total $:', 0, align='R')
    pdf.cell(40, 10, f'${DatosRecibo[2]:.2f}', 0, ln=True, align='R')
    pdf.cell(150, 10, 'Total BS:', 0, align='R')
    pdf.cell(40, 10, f'BS {DatosRecibo[3]:.2f}', 0, ln=True, align='R')

    # Guardar y abrir PDF
    file_name = f'factura_{DatosRecibo[0]}.pdf'
    pdf.output(file_name)

    webbrowser.open(file_name)  # Abre el archivo PDF automáticamente
