import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
from modelos import movimientos_modelo, cierre_financiero_modelo


def modulo_movimientos(frame, ROL_USUARIO_ACTUAL):

    # Añadir elementos de interfaz para las acciones
    titulo_frame = tk.Frame(frame)
    titulo_frame.pack(fill=tk.X)
    titulo_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    titulo = tk.Label(titulo_frame, text="Modulo de Movimientos",
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

    cols = ("ID", "Tipo Movimiento", "Descripcion",
            "Cantidad $", "Cliente", "Fecha")

    movimientos_table = tk.ttk.Treeview(
        table_frame, columns=cols, show='headings')

    movimientos_table.heading(cols[0], text=cols[0])
    movimientos_table.column(cols[0], width=10, anchor="e", stretch=True)

    movimientos_table.heading(cols[1], text=cols[1])
    movimientos_table.column(cols[1], width=50, anchor="center", stretch=True)

    movimientos_table.heading(cols[2], text=cols[2])
    movimientos_table.column(cols[2], width=400, anchor="center", stretch=True)

    movimientos_table.heading(cols[3], text=cols[3])
    movimientos_table.column(cols[3], width=25, anchor="e", stretch=True)

    movimientos_table.heading(cols[4], text=cols[4])
    movimientos_table.column(cols[4], width=100, anchor="center", stretch=True)

    movimientos_table.heading(cols[5], text=cols[5])
    movimientos_table.column(cols[5], width=100, anchor="center", stretch=True)

    def refrescar_pantalla(pantalla, modulo, rol):
        for widget in pantalla.winfo_children():
            widget.destroy()
        modulo(pantalla, rol)

    def cargar_tabla():
        for i, row in enumerate(movimientos_modelo.mostrar_movimientos()):
            id = row[0]
            tipoMovimiento = row[1]
            descripcionMovimiento = row[2]
            cantidad = row[3]
            cliente = row[4]
            fecha = row[6]

            if i % 2 == 0:
                movimientos_table.insert("", tk.END, values=(
                    id, tipoMovimiento, descripcionMovimiento, cantidad, cliente, fecha), tags=("par",))
            else:
                movimientos_table.insert(
                    "", tk.END, values=(
                        id, tipoMovimiento, descripcionMovimiento, cantidad, cliente, fecha), tags=("impar",))

    cargar_tabla()

    def cierre_financiero():
        balance = balance_entry.get()
        listaRecibos = {}
        datosTabla = movimientos_modelo.mostrar_movimientos()

        for i in range(len(datosTabla)):
            row = {}
            for j, col in enumerate(cols):
                row[col] = movimientos_table.item(
                    movimientos_table.get_children()[i])["values"][j]
            listaRecibos[i + 1] = row

        cierre_financiero_modelo.crear_cierre_financiero(
            f"{listaRecibos}", balance)

        for movimientos_a_cerrar in movimientos_table.get_children():
            valores = movimientos_table.item(movimientos_a_cerrar, "values")
            valores_id = valores[0]

            movimiento_obtenido = movimientos_modelo.mostrar_movimiento(
                valores_id)

            IDMovimiento = int(movimiento_obtenido[0])

            movimientos_modelo.cierre_movimientos(IDMovimiento)

        refrescar_pantalla(frame, modulo_movimientos, ROL_USUARIO_ACTUAL)
        messagebox.showinfo("Informacion!", "Cierre Ejecutado")

    # Configurar los colores para las etiquetas
    # Color para filas pares
    movimientos_table.tag_configure("par", background="#B5D4F4")
    movimientos_table.tag_configure("impar", background="#CBDFF3")

    movimientos_table.pack(fill=tk.BOTH, expand=1)

    # Añadir elementos de interfaz para las acciones
    form_frame = tk.Frame(frame)
    form_frame.pack(fill=tk.X)

    balance_entry = tk.Entry(form_frame)
    balance_entry.pack(side=tk.RIGHT, padx=10)
    tk.Label(form_frame, text="Balance:").pack(side=tk.RIGHT, padx=5)

    balance_total = movimientos_modelo.sumar_movimientos()[0][0]

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

    sell_button = tk.Button(
        buttons_frame, text="Cierre Financiero",  bg="#28c3d9", command=cierre_financiero)
    sell_button.grid(row=1, column=3, padx=4, pady=10)
