import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
import ast
from modelos import ventas_modelo
from modulos import ventas, factura_pdf
import main as app


def cerrar_recibo(frame, module):
    app.show_module(frame, module)


def modulo_recibo(frame, IDVenta):

    DatosRecibo = ventas_modelo.mostrar_recibo(IDVenta)
    lista_detalles = DatosRecibo[1]
    lista_detalles_dics = ast.literal_eval(lista_detalles)

    # Añadir elementos de interfaz para las acciones
    titulo_frame = tk.Frame(frame)
    titulo_frame.pack(fill=tk.X)
    titulo_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    titulo = tk.Label(titulo_frame, text=f"Recibo No. {DatosRecibo[0]}",
                      font=("Helvetica", 16, "bold"))
    titulo.grid(row=0, column=0, pady=15)

    # Informacion del cliente
    cliente_frame = tk.Frame(frame)
    cliente_frame.pack(fill=tk.X)
    cliente_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    cliente = tk.Label(cliente_frame, text=f"{DatosRecibo[4]} {DatosRecibo[5]}, {DatosRecibo[6]}",
                       font=("Helvetica", 12, "normal"))
    cliente.grid(row=0, column=0, pady=10)

    def mostrar_datos_recibo(data):

        recibo_frame = tk.Frame(frame)
        recibo_frame.pack(fill=tk.X, side=tk.TOP)

        # Crear Treeview para la tabla
        recibo_tabla = ttk.Treeview(recibo_frame, columns=(
            "IDProducto", "Nombre", "Cantidad", "PrecioUnit$", "Precio$", "PrecioBS"), show='headings')

        # Crear un estilo personalizado
        estilo = ttk.Style()
        estilo.theme_use("alt")
        estilo.configure("Treeview", font=("Verdana", 14), rowheight=30)
        estilo.configure("Treeview.Heading", font=("Verdana", 14, "bold"))
        estilo.configure("Treeview",
                         background="#CACACA",
                         foreground="black",
                         rowheight=25,
                         fieldbackground="white")
        estilo.map("Treeview",
                   background=[("selected", "#5500bb")])

        # Definir encabezados de la tabla
        recibo_tabla.heading("IDProducto", text="IDProducto")
        recibo_tabla.heading("Nombre", text="Nombre")
        recibo_tabla.heading("Cantidad", text="Cantidad")
        recibo_tabla.heading("PrecioUnit$", text="Precio Unit. ($)")
        recibo_tabla.heading("Precio$", text="Precio ($)")
        recibo_tabla.heading("PrecioBS", text="Precio (BS)")

        # Configurar el tamaño de las columnas
        recibo_tabla.column("IDProducto", width=30)
        recibo_tabla.column("Nombre", width=250)
        recibo_tabla.column("Cantidad", width=30, anchor="e")
        recibo_tabla.column("PrecioUnit$", width=100, anchor="e")
        recibo_tabla.column("Precio$", width=100, anchor="e")
        recibo_tabla.column("PrecioBS", width=100, anchor="e")

        # Agregar filas de datos
        for key, producto in data.items():
            recibo_tabla.insert("", "end", values=(
                producto['IDProducto'],
                producto['Nombre'],
                producto['Cantidad'],
                producto['Precio Unit. $'],
                producto['Precio'],
                producto['PrecioBS']
            ))

        # Empaquetar la tabla en la ventana
        recibo_tabla.pack(fill=tk.BOTH, padx=100, pady=0)

    # Añadir elementos de interfaz para las acciones
    total_frame = tk.Frame(frame)
    total_frame.pack(fill=tk.X)
    total_frame.grid_columnconfigure(0, weight=1)

    total_tabla = ttk.Treeview(total_frame, columns=(
        "Total"), show='headings', height=1)

    total_tabla.heading("Total", text="Total $")
    total_tabla.column("Total", anchor="e", width=100)

    total_tabla.insert("", "end", values=(f"{DatosRecibo[2]} $"))
    total_tabla.pack(fill=tk.X, padx=100, ipadx=10, pady=0)

    totalBS_frame = tk.Frame(frame)
    totalBS_frame.pack(fill=tk.X)
    totalBS_frame.grid_columnconfigure(0, weight=1)

    totalBS_tabla = ttk.Treeview(totalBS_frame, columns=(
        "TotalBS"), show='headings', height=2)

    totalBS_tabla.heading("TotalBS", text="Total BS")
    totalBS_tabla.column("TotalBS", anchor="e", width=100)

    totalBS_tabla.insert("", "end", values=(f"{DatosRecibo[3]} BS"))
    totalBS_tabla.pack(fill=tk.X, padx=100, ipadx=10, pady=0)

    # Botón "Imprimir"
    def imprimir_factura():
        factura_pdf.generar_factura_pdf(DatosRecibo, lista_detalles_dics)
        messagebox.showinfo(
            "Factura Generada", "El archivo PDF se ha generado y abierto con éxito.")

    # Colocar el botón al final
    boton_frame = tk.Frame(frame)
    boton_frame.pack(side=tk.BOTTOM, pady=20)

    imprimir_button = tk.Button(
        boton_frame, text="Imprimir", command=imprimir_factura, bg="blue", fg="white")
    imprimir_button.pack()

    mostrar_datos_recibo(lista_detalles_dics)
