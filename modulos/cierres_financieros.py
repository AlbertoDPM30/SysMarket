import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
from modelos import movimientos_modelo, cierre_financiero_modelo


def modulo_cierres_financieros(frame, ROL_USUARIO_ACTUAL):

    # Añadir elementos de interfaz para las acciones
    titulo_frame = tk.Frame(frame)
    titulo_frame.pack(fill=tk.X)
    titulo_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    titulo = tk.Label(titulo_frame, text="Modulo de Cierres Financieros",
                      font=("Helvetica", 16, "bold"))
    titulo.grid(row=0, column=0, pady=15)

    # Crear tabla
    table_frame = tk.Frame(frame)
    table_frame.pack(fill=tk.BOTH, expand=1)

    # Crear un estilo personalizado
    estilo = ttk.Style()
    estilo.theme_use("alt")
    estilo.configure("Treeview", font=("Verdana", 14), rowheight=30)
    estilo.configure("Treeview.Heading", font=("Verdana", 14, "bold"))
    estilo.configure("Treeview",
                     foreground="black",
                     rowheight=25,
                     fieldbackground="white")
    estilo.map("Treeview",
               background=[("selected", "#5500bb")])

    cols = ("ID", "Movimientos", "Total $", "Fecha")

    cierres_table = tk.ttk.Treeview(
        table_frame, columns=cols, show='headings')

    cierres_table.heading(cols[0], text=cols[0])
    cierres_table.column(cols[0], width=10, anchor="e", stretch=True)

    cierres_table.heading(cols[1], text=cols[1])
    cierres_table.column(cols[1], width=400, anchor="center", stretch=True)

    cierres_table.heading(cols[2], text=cols[2])
    cierres_table.column(cols[2], width=25, anchor="e", stretch=True)

    cierres_table.heading(cols[3], text=cols[3])
    cierres_table.column(cols[3], width=100, anchor="e", stretch=True)

    def cargar_tabla():
        for i, row in enumerate(cierre_financiero_modelo.mostrar_cierres_financieros()):
            id = row[0]
            movimientos = row[1]
            total = row[2]
            fecha = row[3]

            if i % 2 == 0:
                cierres_table.insert("", tk.END, values=(
                    id, movimientos, total, fecha), tags=("par",))
            else:
                cierres_table.insert(
                    "", tk.END, values=(
                        id, movimientos, total, fecha), tags=("impar",))

    cargar_tabla()

    # Configurar los colores para las etiquetas
    # Color para filas pares
    cierres_table.tag_configure("par", background="#B5D4F4")
    cierres_table.tag_configure("impar", background="#CBDFF3")

    cierres_table.pack(fill=tk.BOTH, expand=1)

    # Añadir elementos de interfaz para las acciones
    form_frame = tk.Frame(frame)
    form_frame.pack(fill=tk.X)

    balance_entry = tk.Entry(form_frame)
    balance_entry.pack(side=tk.RIGHT, padx=10)
    tk.Label(form_frame, text="Balance:").pack(side=tk.RIGHT, padx=5)

    balance_total = cierre_financiero_modelo.sumar_cierres_finacieros()[0][0]

    # Mostrar el resultado en el campo de entrada de solo lectura
    if balance_total is not None:
        balance_entry.config(state="normal")
        balance_entry.delete(0, tk.END)      # Limpiar entrada
        balance_entry.insert(0, f"{balance_total:.2f} $")
        balance_entry.config(state="readonly")
    else:
        balance_entry.config(state="normal")
        balance_entry.delete(0, tk.END)
        balance_entry.insert(0, "0.00 $")
        balance_entry.config(state="readonly")

    # Boton de cierre financiero
    buttons_frame = tk.Frame(frame)
    buttons_frame.pack(fill=tk.X)
    buttons_frame.grid_columnconfigure(0, weight=1)
