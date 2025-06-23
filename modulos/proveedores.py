import tkinter.ttk as ttk
import tkinter as tk
from modelos import proveedores_modelo


def modulo_proveedores(frame, ROL_USUARIO_ACTUAL):

    # Añadir elementos de interfaz para las acciones
    titulo_frame = tk.Frame(frame)
    titulo_frame.pack(fill=tk.X)
    titulo_frame.grid_columnconfigure(0, weight=1)

    # Agregar un texto al principio del marco
    titulo = tk.Label(titulo_frame, text="Modulo de Proveedores",
                      font=("Helvetica", 16, "bold"))
    titulo.grid(row=0, column=0, pady=15)

    # Añadir elementos de interfaz para las acciones
    form_frame = tk.Frame(frame)
    form_frame.pack(fill=tk.X)
    form_frame.grid_columnconfigure(0, weight=1)
    form_frame.grid_columnconfigure(1, weight=1)
    form_frame.grid_columnconfigure(2, weight=1)

    tk.Label(form_frame, text="Nombre:").grid(row=0, column=0, padx=10)
    NombreProveedor_entry = tk.Entry(form_frame, width=50)
    NombreProveedor_entry.grid(row=1, column=0, padx=10)

    tk.Label(form_frame, text="Dirección:").grid(row=0, column=1, padx=10)
    direccion_entry = tk.Entry(form_frame, width=100)
    direccion_entry.grid(row=1, column=1, padx=10)

    tk.Label(form_frame, text="Telefono:").grid(
        row=0, column=2, padx=10)
    telefono_entry = tk.Entry(form_frame, width=50)
    telefono_entry.grid(row=1, column=2, padx=10)

    IDProveedor_tag = tk.Label(form_frame, text="ID:")
    IDProveedor_entry = tk.Entry(form_frame, width=50)

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

    cols = ("ID", "Nombre", "Dirección", "Telefono", "Fecha Creacion")

    proveedores_table = tk.ttk.Treeview(
        table_frame, columns=cols, show='headings')

    proveedores_table.heading(cols[0], text=cols[0])
    proveedores_table.column(cols[0], width=10, anchor="e", stretch=True)

    proveedores_table.heading(cols[1], text=cols[1])
    proveedores_table.column(cols[1], width=100, anchor="center", stretch=True)

    proveedores_table.heading(cols[2], text=cols[2])
    proveedores_table.column(cols[2], width=400, anchor="center", stretch=True)

    proveedores_table.heading(cols[3], text=cols[3])
    proveedores_table.column(cols[3], width=25, anchor="e", stretch=True)

    proveedores_table.heading(cols[4], text=cols[4])
    proveedores_table.column(cols[4], width=50, anchor="center", stretch=True)

    def cargar_tabla():
        for i, row in enumerate(proveedores_modelo.mostrar_proveedores()):
            if i % 2 == 0:
                proveedores_table.insert("", tk.END, values=row, tags=("par",))
            else:
                proveedores_table.insert(
                    "", tk.END, values=row, tags=("impar",))

    def refrescar_tabla():
        for item in proveedores_table.get_children():  # Eliminar todas las filas existentes
            proveedores_table.delete(item)
        cargar_tabla()

    cargar_tabla()

    # Configurar los colores para las etiquetas
    # Color para filas pares
    proveedores_table.tag_configure("par", background="#B5D4F4")
    proveedores_table.tag_configure("impar", background="#CBDFF3")

    proveedores_table.pack(fill=tk.BOTH, expand=1)

    def limpiar_entradas():
        form_frame.grid_columnconfigure(3, weight=0)
        NombreProveedor_entry.delete(0, tk.END)
        direccion_entry.delete(0, tk.END)
        telefono_entry.delete(0, tk.END)
        IDProveedor_entry.delete(0, tk.END)
        IDProveedor_tag.grid_forget()
        IDProveedor_entry.grid_forget()
        IDProveedor_entry.config(state="normal")
        NombreProveedor_entry.focus_set()
        btn_editar.grid_forget()
        btn_eliminar.grid_forget()

    def agregar_proveedor():
        NombreProveedor = NombreProveedor_entry.get()
        descripcion = direccion_entry.get()
        telefono = telefono_entry.get()

        proveedores_modelo.crear_proveedor(
            NombreProveedor, descripcion, telefono)
        refrescar_tabla()
        limpiar_entradas()

    def editar_proveedor():
        IDProducto = IDProveedor_entry.get()
        NombreProveedor = NombreProveedor_entry.get()
        descripcion = direccion_entry.get()
        telefono = telefono_entry.get()

        proveedores_modelo.editar_proveedor(
            IDProducto, NombreProveedor, descripcion, telefono)
        refrescar_tabla()
        limpiar_entradas()

    def eliminar_proveedor():
        IDProducto = IDProveedor_entry.get()
        proveedores_modelo.eliminar_proveedor(IDProducto)
        refrescar_tabla()
        limpiar_entradas()

    # Función para mostrar las entradas cuando se selecciona un elemento
    def mostrar_entradas(event):
        seleccionado = proveedores_table.focus()
        if seleccionado:
            valores = proveedores_table.item(seleccionado, "values")
            limpiar_entradas()
            form_frame.grid_columnconfigure(3, weight=1)

            NombreProveedor_entry.insert(0, valores[1])
            direccion_entry.insert(0, valores[2])
            telefono_entry.insert(0, valores[3])

            btn_editar.grid(row=2, column=3, columnspan=1, padx=2, pady=10)
            btn_eliminar.grid(row=2, column=4, columnspan=1, padx=2, pady=10)

            IDProveedor_tag.grid(row=0, column=3, padx=10)
            IDProveedor_entry.grid(row=1, column=3, padx=10)
            IDProveedor_entry.insert(0, valores[0])
            IDProveedor_entry.config(state="readonly")

    # Vincular la selección de un elemento a la función
    proveedores_table.bind("<<TreeviewSelect>>", mostrar_entradas)

    add_button = tk.Button(
        form_frame, text="Agregar Proveedor +", bg="#26b135", command=agregar_proveedor)
    add_button.grid(row=2, column=0, columnspan=2, padx=4, pady=10)

    btn_limpiar = tk.Button(
        form_frame, text="Limpiar todo |x|", bg="#dadada", command=limpiar_entradas)
    btn_limpiar.grid(row=2, column=2, columnspan=1, padx=4, pady=10)

    btn_editar = tk.Button(
        form_frame, text="Editar Proveedor !", bg="#fbcf3a", command=editar_proveedor)

    btn_eliminar = tk.Button(
        form_frame, text="Eliminar Proveedor X", bg="#de3f1f", fg="#FFFFFF", command=eliminar_proveedor)
